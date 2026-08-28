# Notes

One markdown file per topic. GitHub Pages builds the site with Jekyll on push — there is
no local build step and nothing to run.

## Adding a topic

```bash
cp _TEMPLATE.md access-control.md
```

Fill in the frontmatter, write the four sections, commit, push. That's it.

```yaml
---
layout: note
title: Access control
group: server-side       # server-side | client-side | advanced
status: in-progress      # not-started | in-progress | done
labs_done: 4
labs_total: 22
updated: 2026-09-14
summary: One sentence. This is the card text on the index.
---
```

`labs_done` / `labs_total` drive the progress bar and the totals in the header and footer,
so keep them current. `status` sets the pill colour and dims not-started cards.

## The four sections that matter

1. **What it is** — in your own words. If you can't write it without looking, you haven't
   learned it.
2. **Why it survives code review** — the developer's flawed mental model. This is what makes
   the notes yours rather than a restatement of the Academy.
3. **Finding it in a live app** — the signal. Labs tell you where the bug is; real targets
   don't.
4. **Fixing it** — code-level remediation. Almost nobody writing web-security notes can write
   this section. You can, and it's the reason an appsec team would hire you.

## Turning on GitHub Pages

Repo → Settings → Pages → Source: **Deploy from a branch** → `main` / root.
First build takes a minute or two. If it fails, the error shows in the Actions tab.

## Images

Drop them in `assets/` and reference as `![alt](assets/name.png)`.

## Before publishing anything about a real target

Read `DISCLOSURE.md`. Most programs forbid disclosure without written permission.
`../hunting/` deliberately sits outside this repo — target names and recon output must
never end up in a public repo.
