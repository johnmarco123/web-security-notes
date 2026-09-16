---
layout: note
title: Server-side vulnerabilities
group: server-side
status: in-progress
updated: 2026-09-15
summary: Server side vulnerabilities can be many things, such as path traversal, access control, broken authentication and many more
---

## What it is
There is plenty of server side vulnerabilities, those including but not limited to:
* Path traversal
 This can be utilized when getting files, a get request for a file -> this can
 be sent to repeater, and try to traverse paths this way. This is one of many
 ways, and can be more in depth then this simple example
* Access Control
    Few ways that access control can be messed up.
    1. It can have 0 access control and be exposed somewhere in the app
    2. a cookie could have a flag that is a bool stating whether or not the
       user is an admin
    3. a UUID could be used in a parameter, and although UUID may not be
       guessable, maybe they have a publicly available resource that exposes
       their UUID
    4. There is vertical, and horizontal priviledge escalation. Sometimes you
       can be moving horizontally, and target an admin user, and ultimately get
       vertical priviledge escalation
* Authentication
    1. Authentication is like a login page for example, do you have
       AUTHENTICATION to log in to account A. This can be done via brute force
    2. Maybe even though 2fa is shown, it doesn't do anything! most likely this
       wont happen in a real scenario though, but its worth checking
* Server-side request forgery
    1. Server side request forgery is a way to trick the server to grab
       resources from external / internal places AS the server
* File upload vulnerabilities
    1. If they dont care for extensions such as PHP extension, you can simply
       upload a php file and it may run. More often then not though they have
       filters you may be able to weasle around
* OS command injection
* SQL injection

## Why it survives code review
It is tedious, and also very complex to ensure a server is entirely secure, and
it is easy to forget about things

## Fixing it
Each independent server side vulnerability needs attention across nearly all
parts of the system.

## Payloads worth keeping

## Notes
