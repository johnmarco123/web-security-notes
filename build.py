#!/usr/bin/env python3
"""
Build the notes site.

    python3 build.py            # -> site/
    python3 build.py --private  # keep private sections (local review only)

One .md per topic in this directory. Everything between <!-- private:start --> and
<!-- private:end --> is stripped unless --private is passed, so a single file is both
your working notes and the published page. Never maintain two copies.

Stdlib only. Run it in WSL.
"""
import argparse
import html
import re
import shutil
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "site"
PRIVATE = re.compile(r"<!--\s*private:start\s*-->.*?<!--\s*private:end\s*-->", re.S)

GROUPS = [("server-side", "Server-side"), ("client-side", "Client-side"), ("advanced", "Advanced")]
STATUS_ORDER = {"done": 0, "in-progress": 1, "not-started": 2}


# ── parsing ──────────────────────────────────────────────────────────
def parse(path):
    """Split a note into (frontmatter dict, body). Frontmatter is simple key: value."""
    raw = path.read_text(encoding="utf-8")
    meta, body = {}, raw
    if raw.startswith("---"):
        end = raw.find("\n---", 3)
        if end != -1:
            for line in raw[3:end].strip().splitlines():
                if ":" in line and not line.lstrip().startswith("#"):
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip()
            body = raw[end + 4:]
    meta.setdefault("title", path.stem.replace("-", " ").title())
    meta.setdefault("slug", path.stem)
    meta.setdefault("group", "advanced")
    meta.setdefault("status", "in-progress")
    meta.setdefault("summary", "")
    return meta, body


def frac(s):
    """'12/17' -> (12, 17). Anything unparseable -> (0, 0)."""
    m = re.match(r"\s*(\d+)\s*/\s*(\d+)\s*$", s or "")
    return (int(m.group(1)), int(m.group(2))) if m else (0, 0)


# ── a small markdown subset ──────────────────────────────────────────
def inline(t):
    t = html.escape(t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", t)
    return t


def md(text):
    out, lines, i = [], text.split("\n"), 0
    list_open = table_open = False

    def close_list():
        nonlocal list_open
        if list_open:
            out.append("</ul>")
            list_open = False

    def close_table():
        nonlocal table_open
        if table_open:
            out.append("</tbody></table></div>")
            table_open = False

    while i < len(lines):
        ln = lines[i]

        if ln.strip().startswith("```"):
            close_list(); close_table()
            lang = ln.strip()[3:].strip()
            i += 1
            buf = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i]); i += 1
            i += 1
            cls = f' class="lang-{html.escape(lang)}"' if lang else ""
            out.append(f"<pre><code{cls}>{html.escape(chr(10).join(buf))}</code></pre>")
            continue

        h = re.match(r"^(#{1,4})\s+(.*)$", ln)
        if h:
            close_list(); close_table()
            lvl = len(h.group(1)) + 1          # page <h1> is the title
            out.append(f"<h{lvl}>{inline(h.group(2))}</h{lvl}>")
            i += 1
            continue

        if re.match(r"^\s*[-*]\s+", ln):
            close_table()
            if not list_open:
                out.append("<ul>"); list_open = True
            item = re.sub(r"^\s*[-*]\s+", "", ln)
            item = re.sub(r"^\[ \]\s*", "", item)
            item = re.sub(r"^\[x\]\s*", "", item, flags=re.I)
            out.append(f"<li>{inline(item)}</li>")
            i += 1
            continue

        if ln.strip().startswith("|") and ln.strip().endswith("|"):
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if not table_open and re.match(r"^\s*\|[\s:|-]+\|\s*$", nxt):
                close_list()
                out.append('<div class="tw"><table><thead><tr>'
                           + "".join(f"<th>{inline(c)}</th>" for c in cells)
                           + "</tr></thead><tbody>")
                table_open = True
                i += 2
                continue
            if table_open:
                if all(not c for c in cells):        # skip blank rows
                    i += 1
                    continue
                out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in cells) + "</tr>")
                i += 1
                continue

        if not ln.strip():
            close_list(); close_table()
            i += 1
            continue

        if ln.strip().startswith(">"):
            close_list(); close_table()
            out.append(f"<blockquote>{inline(ln.strip().lstrip('>').strip())}</blockquote>")
            i += 1
            continue

        if ln.strip() == "---":
            close_list(); close_table()
            out.append("<hr>")
            i += 1
            continue

        close_list(); close_table()
        para = [ln]
        while i + 1 < len(lines) and lines[i + 1].strip() and not re.match(
                r"^\s*([-*#>|]|```)", lines[i + 1]):
            i += 1
            para.append(lines[i])
        out.append(f"<p>{inline(' '.join(x.strip() for x in para))}</p>")
        i += 1

    close_list(); close_table()
    return "\n".join(out)


# ── page shell ───────────────────────────────────────────────────────
CSS = """
:root{--bg:#f2f3f7;--surface:#fff;--surface2:#f8f9fc;--ink:#14161f;--ink2:#454b60;
--muted:#767d94;--line:#e0e3ec;--line2:#cdd2e0;--accent:#d2600a;--accent-soft:#fdf0e4;
--done:#1a8f6c;--done-soft:#e5f4ef;--warn:#b8830c;--warn-soft:#fbf2df}
@media(prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#0e1017;--surface:#161923;
--surface2:#1b1f2b;--ink:#e9ebf3;--ink2:#b0b6c9;--muted:#7f8699;--line:#242835;--line2:#333949;
--accent:#ff8f43;--accent-soft:#2a1c0f;--done:#3cbb93;--done-soft:#122a23;--warn:#e0a93a;
--warn-soft:#2a2213}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.65 "IBM Plex Sans",
system-ui,-apple-system,Segoe UI,sans-serif;-webkit-font-smoothing:antialiased}
a{color:var(--accent)}
.wrap{max-width:760px;margin:0 auto;padding:32px 20px 80px}
.wrap.wide{max-width:1000px}
header.top{border-bottom:1px solid var(--line);background:var(--surface)}
header.top .in{max-width:1000px;margin:0 auto;padding:14px 20px;display:flex;
align-items:baseline;gap:12px}
header.top b{font-family:Archivo,system-ui,sans-serif;font-weight:800;letter-spacing:-.03em;
font-size:17px}
header.top span{font-size:12px;color:var(--muted);margin-left:auto;font-variant-numeric:tabular-nums}
h1{font-family:Archivo,system-ui,sans-serif;font-weight:800;letter-spacing:-.03em;
font-size:clamp(28px,5vw,38px);line-height:1.12;margin:0 0 6px;text-wrap:balance}
h2{font-family:Archivo,system-ui,sans-serif;font-weight:700;letter-spacing:-.02em;
font-size:21px;margin:38px 0 10px;text-wrap:balance}
h3{font-family:Archivo,system-ui,sans-serif;font-weight:700;font-size:17px;margin:26px 0 8px}
p{margin:0 0 14px;max-width:66ch}
ul{margin:0 0 16px;padding-left:22px}li{margin:4px 0}
code{font-family:"IBM Plex Mono",ui-monospace,Menlo,monospace;font-size:.88em;
background:var(--surface2);border:1px solid var(--line);border-radius:3px;padding:1px 4px}
pre{background:var(--surface2);border:1px solid var(--line);border-radius:6px;
padding:14px 16px;overflow-x:auto;margin:0 0 16px}
pre code{background:none;border:0;padding:0;font-size:13px;line-height:1.55}
blockquote{margin:0 0 16px;padding:2px 0 2px 16px;border-left:3px solid var(--line2);
color:var(--ink2)}
hr{border:0;border-top:1px solid var(--line);margin:30px 0}
.tw{overflow-x:auto;margin:0 0 16px}
table{border-collapse:collapse;width:100%;font-size:14px}
th{text-align:left;font-family:"IBM Plex Mono",monospace;font-size:10px;letter-spacing:.12em;
text-transform:uppercase;color:var(--muted);padding:0 10px 7px 0}
td{border-top:1px solid var(--line);padding:8px 10px 8px 0;vertical-align:top}
.lede{color:var(--ink2);font-size:18px;margin-bottom:26px;max-width:60ch}
.meta{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:0 0 30px}
.pill{font-family:"IBM Plex Mono",monospace;font-size:10.5px;font-weight:600;
letter-spacing:.1em;text-transform:uppercase;padding:3px 8px;border-radius:3px;
background:var(--surface2);border:1px solid var(--line2);color:var(--muted)}
.pill.done{background:var(--done-soft);border-color:var(--done);color:var(--done)}
.pill.in-progress{background:var(--warn-soft);border-color:var(--warn);color:var(--warn)}
.grp{margin:0 0 34px}
.grp>.lbl{font-family:"IBM Plex Mono",monospace;font-size:10.5px;letter-spacing:.14em;
text-transform:uppercase;color:var(--muted);font-weight:600;display:block;margin-bottom:12px}
.cards{display:grid;gap:10px;grid-template-columns:repeat(auto-fill,minmax(300px,1fr))}
.card{display:block;background:var(--surface);border:1px solid var(--line);border-radius:6px;
padding:14px 16px;text-decoration:none;color:inherit}
.card:hover{border-color:var(--accent)}
.card .t{font-family:Archivo,system-ui,sans-serif;font-weight:700;font-size:15.5px;
margin-bottom:3px;display:flex;justify-content:space-between;gap:10px;align-items:baseline}
.card .s{font-size:13.5px;color:var(--muted);line-height:1.5}
.card .n{font-family:"IBM Plex Mono",monospace;font-size:11px;color:var(--muted);flex:none}
.card.not-started{opacity:.55}
.bar{height:6px;background:var(--surface2);border:1px solid var(--line);border-radius:99px;
overflow:hidden;margin:22px 0 34px}
.bar i{display:block;height:100%;background:var(--accent)}
.back{font-size:13.5px;color:var(--muted);text-decoration:none;display:inline-block;
margin-bottom:22px}
.back:hover{color:var(--accent)}
footer{border-top:1px solid var(--line);margin-top:50px;padding-top:18px;font-size:12.5px;
color:var(--muted)}
"""

SHELL = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@700;800&family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<style>{css}</style>
</head><body>
<header class="top"><div class="in"><b>Web Security Notes</b><span>{sub}</span></div></header>
{body}
</body></html>
"""


def build(keep_private=False):
    notes = sorted(p for p in HERE.glob("*.md") if not p.name.startswith("_"))
    if not notes:
        print("No notes yet. Copy _TEMPLATE.md to <topic>.md and write one.")
        return 1

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    pages, done_labs, total_labs = [], 0, 0
    for path in notes:
        meta, body = parse(path)
        if not keep_private:
            body = PRIVATE.sub("", body)

        a_d, a_t = frac(meta.get("apprentice"))
        p_d, p_t = frac(meta.get("practitioner"))
        done_labs += a_d + p_d
        total_labs += a_t + p_t

        counts = []
        if a_t:
            counts.append(f"apprentice {a_d}/{a_t}")
        if p_t:
            counts.append(f"practitioner {p_d}/{p_t}")

        inner = (
            f'<div class="wrap">'
            f'<a class="back" href="index.html">&larr; all topics</a>'
            f'<h1>{html.escape(meta["title"])}</h1>'
            + (f'<p class="lede">{html.escape(meta["summary"])}</p>' if meta["summary"] else "")
            + '<div class="meta">'
            + f'<span class="pill {meta["status"]}">{meta["status"].replace("-", " ")}</span>'
            + "".join(f'<span class="pill">{c}</span>' for c in counts)
            + "</div>"
            + md(body)
            + f'<footer>Updated {html.escape(meta.get("updated", ""))}</footer>'
            + "</div>"
        )
        (OUT / f'{meta["slug"]}.html').write_text(
            SHELL.format(title=html.escape(meta["title"]) + " — Web Security Notes",
                         css=CSS, sub="", body=inner),
            encoding="utf-8")
        pages.append((meta, a_d + p_d, a_t + p_t))

    # index
    done_topics = sum(1 for m, _, _ in pages if m["status"] == "done")
    pct = round(done_labs / total_labs * 100) if total_labs else 0
    sections = ""
    for key, label in GROUPS:
        grp = [x for x in pages if x[0]["group"] == key]
        if not grp:
            continue
        grp.sort(key=lambda x: (STATUS_ORDER.get(x[0]["status"], 3), x[0]["title"]))
        cards = ""
        for meta, d, t in grp:
            n = f"{d}/{t}" if t else ""
            cards += (
                f'<a class="card {meta["status"]}" href="{meta["slug"]}.html">'
                f'<div class="t"><span>{html.escape(meta["title"])}</span>'
                f'<span class="n">{n}</span></div>'
                f'<div class="s">{html.escape(meta["summary"])}</div></a>'
            )
        sections += (f'<div class="grp"><span class="lbl">{label} &mdash; {len(grp)}</span>'
                     f'<div class="cards">{cards}</div></div>')

    idx = (
        f'<div class="wrap wide">'
        f"<h1>Web security notes</h1>"
        f'<p class="lede">Working notes from the PortSwigger Web Security Academy — what each '
        f"vulnerability class is, why it survives code review, how to find it in a live "
        f"application, and how to fix it in code.</p>"
        f'<div class="bar"><i style="width:{pct}%"></i></div>'
        f"{sections}"
        f'<footer>{done_topics} of {len(pages)} topics complete &middot; '
        f"{done_labs} of {total_labs} labs &middot; built {date.today().isoformat()}</footer>"
        f"</div>"
    )
    (OUT / "index.html").write_text(
        SHELL.format(title="Web Security Notes", css=CSS,
                     sub=f"{done_labs}/{total_labs} labs", body=idx),
        encoding="utf-8")

    assets = HERE / "assets"
    if assets.is_dir():
        shutil.copytree(assets, OUT / "assets", dirs_exist_ok=True)

    print(f"Built {len(pages)} pages -> {OUT}")
    if keep_private:
        print("WARNING: private sections INCLUDED. Do not publish this build.")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--private", action="store_true",
                    help="keep private sections (local review only, never publish)")
    sys.exit(build(ap.parse_args().private))
