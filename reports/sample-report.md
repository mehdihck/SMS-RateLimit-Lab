# Authorized OTP Rate-Limit Assessment — Report Template

> Keep this report private until disclosure is approved by the system owner.

## Assessment metadata

- Assessor: MEHDIHCK
- Target: `[approved target identifier — do not publish sensitive details]`
- Authorization reference: `[ticket / written approval reference]`
- Test window: `[date and time, timezone]`
- Scope: `[approved endpoints and limits]`

## Executive summary

`[Describe the observed behavior. Do not claim a vulnerability unless supported by evidence.]`

## Methodology

- Controlled request volume within the written scope.
- Recorded response status codes and timestamps.
- Compared server-side rate-limit behavior under approved test conditions.
- No third-party identities or unauthorized recipients were used.

## Evidence

| Test case | Expected behavior | Observed behavior | Evidence reference |
|---|---|---|---|
| Baseline quota | `[expected]` | `[observed]` | `[private evidence ID]` |
| Limit exceeded | HTTP 429 or equivalent | `[observed]` | `[private evidence ID]` |
| Identity/header handling | Only trusted proxy metadata is honored | `[observed]` | `[private evidence ID]` |

## Impact

`[Explain realistic impact, affected users, and prerequisites.]`

## Recommendations

- Enforce quotas server-side using trusted identity signals.
- Honor forwarding headers only from explicitly trusted reverse proxies.
- Apply per-account, per-destination, and per-source controls as appropriate.
- Add cooldowns, abuse monitoring, and alerting.
- Avoid revealing whether an account or phone number exists.

## Disclosure

`[Record owner notification, remediation status, and permission to publish.]`
