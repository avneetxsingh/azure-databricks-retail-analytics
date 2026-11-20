# Contributing

Improvements to correctness, reproducibility, documentation, and the retail analytics workflow are welcome.

## Workflow

1. Open an issue for substantial behavior or architecture changes.
2. Create a focused branch from an up-to-date `main`.
3. Make the change and update relevant documentation.
4. Run `python tools/validate_repository.py` from the repository root.
5. Validate behavior changes in an isolated development environment where possible.
6. Open a pull request explaining the problem, resulting behavior, checks, and limitations.

## Guidelines

- Never commit credentials, signed URLs, or private customer records.
- Clear notebook outputs and execution counts.
- Keep input and output paths easy to identify and explain overwrite behavior.
- Preserve the distinction between CSV directories and Delta tables.
- Test meaningful behavior changes with representative valid/invalid inputs.
- Reconcile metrics before and after joins and document changed definitions.
- Describe implemented capabilities accurately; label planned/unverified integrations.
- Include provenance and sharing terms for any dataset contribution.

Contributions must be yours to submit and compatible with the MIT license. External data and dependencies retain their own terms. No contributor license agreement is currently required.

For vulnerabilities or credential exposure, use [SECURITY.md](SECURITY.md), not a public issue containing sensitive details.
