# Security

This is an instructional project. Cloud identity, data permissions, secret scopes, and runtime security must be configured for the environment where it runs.

## Credentials

- Keep SAS tokens, account keys, passwords, private keys, and Databricks tokens outside Git and notebook outputs.
- Use secret references or appropriate identity-based authentication.
- Do not print signed URLs or include them in screenshots or issue reports.
- Limit credentials to required permissions and duration.
- Inspect ADF parameters, exported dashboard queries, infrastructure files, and images before publication.

If a credential is exposed, revoke or rotate it through the owning service. Removing a value from the latest file does not revoke it or erase Git/workspace history. Original notebook copies may also retain old values.

## Private reports

Use **Security → Report a vulnerability** on this repository. Do not submit active credentials or customer information in a public issue.

Include the affected file, impact, and reproduction steps using placeholders. Do not include a usable token. This personal project has no guaranteed response-time SLA.

The offline checker only detects selected credential patterns and outputs. It is not a full security audit and does not inspect cloud permissions or all historical commits.
