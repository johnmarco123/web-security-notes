---
title: SQL injection
slug: sql-injection
group: server-side
status: in-progress
apprentice: 0/2
practitioner: 0/17
updated: 2026-08-28
summary: Untrusted input reaching a SQL query unparameterised — still everywhere, still critical.
---

## What it is

One paragraph, in your own words, no copy-paste. If you can't write it without looking it
up, you haven't learned it yet.

## Why it survives code review

Not the definition — the internet has that. Why does this keep reaching production? What
does the flawed mental model look like from the developer's side? This section is what
separates your notes from every other set of notes.

## Finding it in a live app

The signal that makes you stop and look closer: a parameter shape, an error string, a timing
difference, a response length delta, a header that shouldn't be there. Labs tell you where
the bug is. Real targets don't. Be specific enough to act on.

## Fixing it

The actual remediation at code level, and why the obvious fix is usually wrong — blocklists,
client-side checks, patching one endpoint instead of the authorisation layer.

This is your edge. Almost nobody writing web-security notes can write this section.

## Payloads worth keeping

```
```

<!-- private:start -->

## Lab log

`+` solved unaided · `~` needed a hint · `!` read the solution

| Lab | Mark | What the trick was / what tripped me up |
|---|---|---|
|  |  |  |

## Revisit before Practitioner tier

Everything marked `~` or `!` above. If this list is empty, you rushed.

<!-- private:end -->
