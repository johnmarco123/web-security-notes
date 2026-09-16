---
layout: note
title: API testing
group: server-side
status: in-progress
updated: 2026-08-28
summary: 
---

## What it is
Api's can typically have misconfigured permissions for files, authentication
for resources, etc. This is a big span of different bugs that can be found

## Why it survives code review
API's can be quite large, and tough to review every potential vulnerability

## Fixing it
Targetted API hardening of each endpoint, pruning unused endpoints IF POSSIBLE
For specifically server side parameter polution, you wanna use an allowlist to
define characters that don't need encoding and make sure all other user inputs
are encoded before its used in a serverside request

## Payloads worth keeping
