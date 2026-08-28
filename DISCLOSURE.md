# Writeups — the public half

Everything in here is written to be published. `01-learning/portswigger/` is the private
half: raw notes, payloads, dead ends, "I got stuck for an hour on X". Never publish those.

## The rule

**Do not publish lab solutions.** Thousands already exist, PortSwigger publishes an official
solution for every lab, and a repo full of them tells a hiring manager that you can follow
instructions. It also buries the writeups that actually matter.

Publish the *class*, not the *answer*.

| Don't publish | Do publish |
|---|---|
| "How I solved lab-user-id-controlled-by-request-parameter" | "IDOR: why it survives code review, and how to hunt it" |
| A payload that beat one lab's filter | How that filter class works and what generally defeats it |
| A walkthrough with the answer at the end | Your methodology, including what you tried that failed |

## What goes where

- **`vuln-classes/`** — one per Academy topic, written after you finish that topic's labs.
  This is the bulk of your Phase 1 and 2 output. ~25 of these by the end of Phase 2.
- **`findings/`** — real disclosed bugs. Phase 2 onward. Far more valuable than everything
  else here combined. See the disclosure rules below.
- **`tools/`** — anything you build in `03-tooling/` that's worth explaining. Your developer
  background is the differentiator; a well-explained tool proves it better than a CV line.

## Disclosure rules for `findings/` — read before publishing any real bug

1. **Most programs forbid disclosure without written permission.** Check the program policy.
   Publishing without it can get you banned, and in a bad case is a legal problem.
2. Ask for permission explicitly after the bug is **fixed**, not when it's triaged.
3. Even with permission: no customer data, no screenshots containing real user information,
   no internal hostnames unless the program is fine with it.
4. If permission is refused, you can usually still write the *technique* up generically with
   the target anonymised. Ask first.
5. When in doubt, wait. A finding you publish too early is worth less than the program
   relationship you burn.

## Format

One markdown file per writeup, `kebab-case-title.md`. Use `_TEMPLATE.md`.
Keep them short — 600-1200 words. Nobody reads a 5000-word writeup.
