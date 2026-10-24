# learning-agents — Security

How this project handles authentication and access. Follows [`docs/security.md`](https://github.com/robece/dev-practices/blob/main/infrastructure/docs/security.md) of dev-practices. Facts only, checkable in the code or in production; no secrets, tokens or key material.

## Summary

| | |
|---|---|
| Exposure | public: the repository is public and the slides are published with GitHub Pages at `robece.github.io/learning-agents`; the demos run locally |
| People | none: public page, no sign-in |
| Programs | none |
| Exceptions | everything committed is public |

## Actors and credentials

| Actor | Credential | Checked by | Reaches |
|---|---|---|---|
| Anyone on the internet | none | nobody | the slides, the demo prompts, the repository contents |
| The owner running a demo | his own Claude Code sign-in, kept outside the repository | Claude Code | the demo folders on his machine |

## Edge and identity provider

This project has no Traefik route and does not use authentik.

## Secrets

None: the repository is public, so it must hold no credential, no private path and no personal data.

## Exceptions and known gaps

1. The repository is public by design, the only public one among these projects; a commit of anything private would be visible at once.
2. The demos paste prompts into Claude Code; what the agent does on the machine is governed by Claude Code's own permissions.
