# Notes

One markdown file per topic. Each file is **both** your working notes and the published
page — there is no second copy to keep in sync.

## How it works

Anything between `<!-- private:start -->` and `<!-- private:end -->` is stripped when the
site is built. That's where the lab log and your "got stuck for an hour" material lives.
Everything else is public.

```bash
python3 build.py              # -> site/   (private stripped — this is what you publish)
python3 build.py --private    # -> site/   (everything, for your own review only)
```

Run it in WSL. Stdlib only, no dependencies.

## Writing a note

```bash
cp _TEMPLATE.md access-control.md
```

Fill in the frontmatter (`title`, `slug`, `group`, `status`, lab counts, `summary`), then
write. The `summary` line is the card text on the index, so make it a real sentence.

Update `apprentice:` and `practitioner:` counts as you go — the index bar and the footer
totals are computed from them.

## The four sections that matter

1. **What it is** — in your own words. If you can't write it without looking, you haven't
   learned it.
2. **Why it survives code review** — the developer's flawed mental model. This is what makes
   the notes yours rather than a restatement of the Academy.
3. **Finding it in a live app** — the signal. Labs tell you where the bug is; real targets
   don't.
4. **Fixing it** — code-level remediation. Almost nobody writing web-security notes can write
   this section. You can. It's the whole reason an appsec team would hire you.

## Publishing

`site/` is gitignored — it's build output, regenerated on demand. Commit the markdown.
Before publishing anything about a real target, read `DISCLOSURE.md`.
