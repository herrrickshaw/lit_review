# Repo actions queue (Track D)

Concrete, source-motivated changes to herrrickshaw repos. Appended by the daily task; never executed by it.
A human picks items up, does them in the repo, and ticks them here.

Format: `- [ ] YYYY-MM-DD · <repo> · <concrete change> · source: <id or URL> · register: <entry title>`

## Already done before Track D started (2026-10-24, for reference; do not re-queue)
- [x] 2026-10-24 · global-market-research-platform, stock-screener-platform · put-call parity futures leg on the hedging side · PR #22 / #2
- [x] 2026-10-24 · financial-analysis-toolkit(-public) · DCF loss carryforward accumulates · PR #2 / #1
- [x] 2026-10-24 · saf-monitoring-system · D7566 Annex A8 = ATJ-SKA · PR #1
- [x] 2026-10-24 · prenatal-care-toolkit · PCPNDT 2-year retention treated as a minimum · PR #2
- [x] 2026-10-24 · financial-analysis-toolkit · 63 CFI templates given engines, 149 given verified sources · PR #3

## Open
- [ ] 2026-10-29 · gazette-translated-indexed · add `effective_date` (and a nullable `ceases_date`) to `cross_reference` and `gazette_notification` in `db/schema.sql`, with a shared template in `extract/common_templates.py` for "shall come into force on" / "with effect from" / "w.e.f."; half-open intervals; a `verify/` query for "notifications in force on <date> for <instrument>" · source: arXiv:2505.00039 (schema), luatdo README (interval convention) · register: SAT-Graph RAG entry
- [ ] 2026-10-29 · gazette-translated-indexed · publish a matcher precision/recall report: run the candidate extractors (`extract/cross_ref.py` per the 2026-10-24 baseline; path not re-checked today) over every seeded notification and score candidates against the hand-verified `db/seed_*.sql` rows, per ministry, exact-match on (target, relation_type); put the table in the README and run it in CI · source: doi 10.18653/v1/2025.nllp-1.29 (benchmark shape) · register: Risks and Limits of Automatic Consolidation entry
- [ ] 2026-10-30 · ship2shore_rag · make the shore path's sparse leg real BM25 instead of `ts_rank` at `retrieval/retriever.py:47` (either re-score the `fetch_k` full-text candidates in-process with `rank_bm25` before the RRF, or install ParadeDB `pg_search` and use its BM25 operator, or make the FTS5 SQLite path the default); and add an opt-in contextual-chunk prefix (source title, section heading and a one-line chunk summary prepended before embedding and indexing) · report Recall@5 and MRR on `eval/queries.yaml` (17 queries) before and after each change and keep whichever helps, since a badly tuned hybrid can lose to dense alone · source: arXiv:2604.01733 · register: From BM25 to Corrective RAG entry
