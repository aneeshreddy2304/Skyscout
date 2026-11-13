# Security setup and required owner actions

This security branch removes account-specific integration values from the current
source and replaces them with process-environment configuration. It does not load
`.env` automatically. Supply the variables through the operating system, deployment
platform, or a secret manager.

## Current configuration contract

| Variable | Purpose |
| --- | --- |
| `SHEETY_PRICES_ENDPOINT` | Destination-sheet API endpoint |
| `TEQUILA_API_KEY` | Flight-search provider credential |
| `TWILIO_SID` | Twilio account identifier |
| `TWILIO_AUTH_TOKEN` | Twilio authentication secret |
| `TWILIO_VIRTUAL_NUMBER` | Twilio sender number |
| `TWILIO_VERIFIED_NUMBER` | Verified SMS recipient |

The affected integrations now fail closed when required configuration is absent.
Do not commit populated `.env` files.

## Historical exposure that still requires owner action

Values matching the following categories existed on the public default branch and
remain available in Git history even after this PR is merged:

- A Tequila flight-search API key.
- A Twilio authentication token and account-specific messaging configuration.
- An account-specific Sheety endpoint.

Complete these actions in the provider dashboards:

1. Revoke the exposed Tequila key and issue a replacement with the minimum needed scope.
2. Rotate the Twilio authentication token, review recent account/message activity, and
   verify that only intended sender and recipient numbers remain configured.
3. Replace or disable the exposed Sheety project endpoint and review its access controls.
4. Store replacement values only in deployment secrets or local process configuration.
5. Review GitHub secret-scanning alerts and provider audit logs for unauthorized use.

## History cleanup is separate

This branch does **not** rewrite public Git history. If the owner decides to remove old
blobs later, coordinate a repository-wide history rewrite, force-push, collaborator
re-clone, fork review, and GitHub cached-object cleanup. Rotation must happen first;
history cleanup is not a substitute for revocation.

SMS can incur charges. Use stub providers or a dedicated test account when validating
the workflow.
