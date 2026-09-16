---
layout: note
title: Web Cache Deception
group: server-side
status: done
updated: 2026-08-28
summary: Cache a valuable resource as if it was a static file, which allows attacker to view victims file via cache
---


## What it is
Web Cache deception is when a attacker uses a specific link which hits a cache
which can exist at any amount of layers, whether thats a load balancer, etc. If
this cache just served a victim, and also serves the same response to the
attacker, they may be able to retrieve data that was for the victim only.

Some important things to look out for when we are finding a exploitable surface
for web cache deception: Look for GET, HEAD, or OPTIONS. as methods that
actually alter the servers state usually AREN'T cached

While testing, make sure the cache key that we decide on keeps changing,
otherwise cached responses will impact our results

## Extensions to use
Param miner extension: we use this, go to param miner ->
settings and add dynamic cachebuster, burp now will add
unique query strings to every request, so we don't have to
`^.^`

## Why it survives code review

This keeps reaching production as it is very hard to coordinate multiple
systems to all be on the same page. The core of this is that /profile;a.js may
get interpreted in two seperate ways between the load balancer and the actual
server response.

## Finding it in a live app

N/A

## Fixing it

The way to fix this typically is to have a whitelist for the cache which can
stop a whole variety of attacks

## Payloads worth keeping
google.com/whatever/foo.js
google.com/whatever/foo.exe
google.com/whatever/foo.ico
google.com/whatever/foo.css

In some cases, /profile;foo.css can get through via delimiter discrepancies.

## Delimiters
;
%00 which is an encoded null character

## Notes
to test you can first check the following:
www.google.com/whatever/foobareee
www.google.com/whatever/foobar;eee

we can then see if ; is treated as a delimiter or not based off responses

IMPORTANT - when iterating through delimiters ensure you shut off intruder
encoding! you can find it at the bottom of the payloads in the intruder tab

for /static/..%2fprofile
an origin server could see /profile, whilst the cache could not follow the ..
and still see static, and assume its OK and cache the profile

To test how the origin server normalizes the URL path, send a request to a
non-cacheable resource with a path traversal sequence and an arbitrary
directory at the start of the path. To choose a non-cacheable resource, look
for a non-idempotent method like POST. For example, modify /profile to
/aaa/..%2fprofile:
