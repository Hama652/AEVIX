# Security Policy

AEVIX treats infrastructure security as a long-term engineering concern.

## Reporting Issues

Report suspected security issues privately through the team channel that will be defined for this repository before any production deployment. Do not publish exploit details in public issues.

## Scope

This repository currently contains foundation code only. Security concerns that matter most at this stage are:

- unsafe configuration loading
- accidental path traversal or filesystem writes
- logging leakage of sensitive values
- dependency or supply-chain drift

## Response Goals

- acknowledge reports promptly
- reproduce the issue with a minimal case
- patch the problem at the root cause
- add regression coverage where practical
