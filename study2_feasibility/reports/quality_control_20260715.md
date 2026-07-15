# Study 2 Feasibility Audit Quality Control

- Live ClickHouse connection: successful.
- Access mode: read-only aggregate and metadata queries.
- Summary metrics: 21.
- Requested/derived dictionary fields: 24.
- Live schema fields: 146 across 13 tables/views.
- Anonymized example rows: 42 across 8 requested case types.
- Anonymous researcher IDs: all 12-character SHA-256 prefixes.
- Institution names: replaced with within-case pseudonyms.
- Researcher names and raw researcher IDs in delivered examples: none.
- Database password in delivered files: none.
- AP rule: `准教授`, `associate professor`, or `associate prof` in combined career text; assistant-professor views not used.
- Overlap and multiple-institution counts: explicitly labelled year-level upper-bound diagnostics.
- Empirical promotion model estimated: no.

Result: **PASS**.
