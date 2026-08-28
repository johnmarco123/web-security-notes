# Apprentice labs — 61 of them

Pulled from portswigger.net/web-security/all-labs on 2026-08-28.
Milestone: "Every Apprentice lab done" (Phase 1). Tick as you go; log the time in the tracker.

The Academy has **273 labs total** — 61 Apprentice, 173 Practitioner, 39 Expert.
So this list is 22% of the Academy and roughly the first 3 weeks of Phase 1.

## Suggested order
1. **SQL injection** and **XSS** first — they build Burp muscle memory and they're satisfying.
2. Then **Access control** (9 labs) and **Business logic** (4). These feel dull and are the
   single most valuable block here: they're the classes that pay on real programs because
   a scanner cannot find them.
3. Then everything else, in any order.
4. **Authentication**, **Information disclosure**, and **File upload** are the other three
   that map directly onto real-world findings.

Do not skip a topic because it has only one Apprentice lab — that one lab is the doorway to
the Practitioner set in Phase 1's second half.

---

## SQL injection  (2)

- [ ] [SQL injection vulnerability in WHERE clause allowing retrieval of hidden data](https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data)
- [ ] [SQL injection vulnerability allowing login bypass](https://portswigger.net/web-security/sql-injection/lab-login-bypass)

## Cross-site scripting  (9)

- [ ] [Reflected XSS into HTML context with nothing encoded](https://portswigger.net/web-security/cross-site-scripting/reflected/lab-html-context-nothing-encoded)
- [ ] [Stored XSS into HTML context with nothing encoded](https://portswigger.net/web-security/cross-site-scripting/stored/lab-html-context-nothing-encoded)
- [ ] [DOM XSS in document.write sink using source location.search](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink)
- [ ] [DOM XSS in innerHTML sink using source location.search](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-innerhtml-sink)
- [ ] [DOM XSS in jQuery anchor href attribute sink using location.search source](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-jquery-href-attribute-sink)
- [ ] [DOM XSS in jQuery selector sink using a hashchange event](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-jquery-selector-hash-change-event)
- [ ] [Reflected XSS into attribute with angle brackets HTML-encoded](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-attribute-angle-brackets-html-encoded)
- [ ] [Stored XSS into anchor href attribute with double quotes HTML-encoded](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-href-attribute-double-quotes-html-encoded)
- [ ] [Reflected XSS into a JavaScript string with angle brackets HTML encoded](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-string-angle-brackets-html-encoded)

## Cross-site request forgery (CSRF)  (1)

- [ ] [CSRF vulnerability with no defenses](https://portswigger.net/web-security/csrf/lab-no-defenses)

## Clickjacking  (3)

- [ ] [Basic clickjacking with CSRF token protection](https://portswigger.net/web-security/clickjacking/lab-basic-csrf-protected)
- [ ] [Clickjacking with form input data prefilled from a URL parameter](https://portswigger.net/web-security/clickjacking/lab-prefilled-form-input)
- [ ] [Clickjacking with a frame buster script](https://portswigger.net/web-security/clickjacking/lab-frame-buster-script)

## Cross-origin resource sharing (CORS)  (2)

- [ ] [CORS vulnerability with basic origin reflection](https://portswigger.net/web-security/cors/lab-basic-origin-reflection-attack)
- [ ] [CORS vulnerability with trusted null origin](https://portswigger.net/web-security/cors/lab-null-origin-whitelisted-attack)

## XML external entity (XXE) injection  (2)

- [ ] [Exploiting XXE using external entities to retrieve files](https://portswigger.net/web-security/xxe/lab-exploiting-xxe-to-retrieve-files)
- [ ] [Exploiting XXE to perform SSRF attacks](https://portswigger.net/web-security/xxe/lab-exploiting-xxe-to-perform-ssrf)

## Server-side request forgery (SSRF)  (2)

- [ ] [Basic SSRF against the local server](https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-localhost)
- [ ] [Basic SSRF against another back-end system](https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-backend-system)

## OS command injection  (1)

- [ ] [OS command injection, simple case](https://portswigger.net/web-security/os-command-injection/lab-simple)

## Path traversal  (1)

- [ ] [File path traversal, simple case](https://portswigger.net/web-security/file-path-traversal/lab-simple)

## Access control vulnerabilities  (9)

- [ ] [Unprotected admin functionality](https://portswigger.net/web-security/access-control/lab-unprotected-admin-functionality)
- [ ] [Unprotected admin functionality with unpredictable URL](https://portswigger.net/web-security/access-control/lab-unprotected-admin-functionality-with-unpredictable-url)
- [ ] [User role controlled by request parameter](https://portswigger.net/web-security/access-control/lab-user-role-controlled-by-request-parameter)
- [ ] [User role can be modified in user profile](https://portswigger.net/web-security/access-control/lab-user-role-can-be-modified-in-user-profile)
- [ ] [User ID controlled by request parameter](https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter)
- [ ] [User ID controlled by request parameter, with unpredictable user IDs](https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-unpredictable-user-ids)
- [ ] [User ID controlled by request parameter with data leakage in redirect](https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-data-leakage-in-redirect)
- [ ] [User ID controlled by request parameter with password disclosure](https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-password-disclosure)
- [ ] [Insecure direct object references](https://portswigger.net/web-security/access-control/lab-insecure-direct-object-references)

## Authentication  (3)

- [ ] [Username enumeration via different responses](https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-different-responses)
- [ ] [2FA simple bypass](https://portswigger.net/web-security/authentication/multi-factor/lab-2fa-simple-bypass)
- [ ] [Password reset broken logic](https://portswigger.net/web-security/authentication/other-mechanisms/lab-password-reset-broken-logic)

## WebSockets  (1)

- [ ] [Manipulating WebSocket messages to exploit vulnerabilities](https://portswigger.net/web-security/websockets/lab-manipulating-messages-to-exploit-vulnerabilities)

## Insecure deserialization  (1)

- [ ] [Modifying serialized objects](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-modifying-serialized-objects)

## Information disclosure  (4)

- [ ] [Information disclosure in error messages](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-in-error-messages)
- [ ] [Information disclosure on debug page](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-on-debug-page)
- [ ] [Source code disclosure via backup files](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-via-backup-files)
- [ ] [Authentication bypass via information disclosure](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-authentication-bypass)

## Business logic vulnerabilities  (4)

- [ ] [Excessive trust in client-side controls](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-excessive-trust-in-client-side-controls)
- [ ] [High-level logic vulnerability](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-high-level)
- [ ] [Inconsistent security controls](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-inconsistent-security-controls)
- [ ] [Flawed enforcement of business rules](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-flawed-enforcement-of-business-rules)

## HTTP Host header attacks  (2)

- [ ] [Basic password reset poisoning](https://portswigger.net/web-security/host-header/exploiting/password-reset-poisoning/lab-host-header-basic-password-reset-poisoning)
- [ ] [Host header authentication bypass](https://portswigger.net/web-security/host-header/exploiting/lab-host-header-authentication-bypass)

## OAuth authentication  (1)

- [ ] [Authentication bypass via OAuth implicit flow](https://portswigger.net/web-security/oauth/lab-oauth-authentication-bypass-via-oauth-implicit-flow)

## File upload vulnerabilities  (2)

- [ ] [Remote code execution via web shell upload](https://portswigger.net/web-security/file-upload/lab-file-upload-remote-code-execution-via-web-shell-upload)
- [ ] [Web shell upload via Content-Type restriction bypass](https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-content-type-restriction-bypass)

## JWT  (2)

- [ ] [JWT authentication bypass via unverified signature](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-unverified-signature)
- [ ] [JWT authentication bypass via flawed signature verification](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-flawed-signature-verification)

## GraphQL API vulnerabilities  (1)

- [ ] [Accessing private GraphQL posts](https://portswigger.net/web-security/graphql/lab-graphql-reading-private-posts)

## Race conditions  (1)

- [ ] [Limit overrun race conditions](https://portswigger.net/web-security/race-conditions/lab-race-conditions-limit-overrun)

## NoSQL injection  (2)

- [ ] [Detecting NoSQL injection](https://portswigger.net/web-security/nosql-injection/lab-nosql-injection-detection)
- [ ] [Exploiting NoSQL operator injection to bypass authentication](https://portswigger.net/web-security/nosql-injection/lab-nosql-injection-bypass-authentication)

## API testing  (1)

- [ ] [Exploiting an API endpoint using documentation](https://portswigger.net/web-security/api-testing/lab-exploiting-api-endpoint-using-documentation)

## Web LLM attacks  (3)

- [ ] [Exploiting LLM APIs with excessive agency](https://portswigger.net/web-security/llm-attacks/lab-exploiting-llm-apis-with-excessive-agency)
- [ ] [Exploiting AI agents to perform destructive actions](https://portswigger.net/web-security/llm-attacks/ai-powered-scanner-vulnerabilities/lab-indirect-prompt-injection-via-ai-powered-scan)
- [ ] [Exploiting AI agents to exfiltrate sensitive information](https://portswigger.net/web-security/llm-attacks/ai-powered-scanner-vulnerabilities/lab-sensitive-information-exfiltration)

## Web cache deception  (1)

- [ ] [Exploiting path mapping for web cache deception](https://portswigger.net/web-security/web-cache-deception/lab-wcd-exploiting-path-mapping)
