# Repo literature register (portfolio review, Track D)

Papers, tools, standards and datasets reviewed against the CODE of the herrrickshaw repos outside
market-pipeline's trading-strategy scope. Written by Track D of the `literature-review-daily` task.
Baseline: the 2026-10-24 code-grounded portfolio review (`baseline/*.result.json`: per repo what the code
does, README claims the code does not back, method snippets, prior art already found, verdict
open / prior-art / adjacent / crowded). Published view: https://claude.ai/artifact/Sn14uD5uJYpndfT6GWy9mT
(a point-in-time snapshot; this register is the live record).

Do not re-log anything already listed under a repo's `prior_art` in the baseline.

## Entry format

### <exact title> — <arXiv id / DOI / URL> — cluster <letter> — logged YYYY-MM-DD
- **Source:** authors, venue, year.
- **Repos:** which repos it bears on.
- **Repo already does:** what the code does on this point, cited `repo:path:line` from a real grep/read (or UNVERIFIED).
- **Gap:** what the source does that the repo does not (or "none").
- **Verdict effect:** confirms / changes the repo's baseline verdict (e.g. open -> prior-art), with one line why.
- **Action queued:** the REPO_ACTIONS.md line added, or "none".

## Entries

### Risks and Limits of Automatic Consolidation of Statutes — doi 10.18653/v1/2025.nllp-1.29 — cluster F — logged 2026-10-29
- **Source:** Max Prior, Adrian Hof, Niklas Wais, Matthias Grabmair (TU Munich), Natural Legal Language Processing Workshop 2025 (ACL), pp. 396–407, Nov 2025. PDF fetched in full via fetch_source.sh.
- **Repos:** gazette-translated-indexed.
- **What it shows:** 908 amendment–law pairs from 140 Bundesgesetzblatt PDFs across four German codes (BGB 177, StGB 162, HGB 254, EStG 315), aligned with daily snapshots of gesetze-im-internet 2019–2025. GPT-4.1-mini applies amendments to produce consolidated text. Exact match 50.33% single-step (30.16% EStG to 75.93% StGB) and 20.51% multi-step (chains average 2.79 amendments), while BLEU/ROUGE/BERTScore sit at 0.93–0.99 regardless. Expert review of 100 imperfect outputs: 51% of errors minimal-to-moderate, 78% trivially correctable, yet legally material divergences persist. Ground-truth versions were themselves hard to pin down for some codes at some dates.
- **Repo already does:** links instruments and never rewrites them. `db/schema.sql` `cross_reference.relation_type` is `amends | supersedes | corrigendum | rescinds | repeals | cites` between two `gazette_notification` rows. `grep 'consolidat' '*.py'` hits only two comments describing drafting shapes (`extract/steel_patterns.py:13`, `extract/mohua_patterns.py:15`). There is no consolidation step and no synthesised text.
- **Gap:** none the repo should close. The paper is evidence that consolidation-by-LLM is where the errors live, which supports the repo's link-only design. What it offers is a benchmark shape the repo lacks: amendment–target pairs with an exact-match metric and a per-code breakdown, built from gazette PDFs. The repo's 52 test files assert on quoted notification text but publish no aggregate precision/recall of the template matchers over the hand-verified seed rows.
- **Verdict effect:** confirms `open`. No equivalent for Indian gazette notifications exists; the German work is text synthesis, not notification lineage.
- **Action queued:** REPO_ACTIONS 2026-10-29 (matcher precision/recall report).

### An Ontology-Driven Graph RAG for Legal Norms: A Structural, Temporal, and Deterministic Approach (SAT-Graph RAG) — arXiv:2505.00039 — cluster F — logged 2026-10-29
- **Source:** Hudson de Martim (Federal Senate of Brazil), arXiv, v1 29 Apr 2025, v5 11 Sep 2025. Abs page fetched. Case study on the Brazilian Constitution; no quantitative evaluation and no code link on the abs page.
- **Repos:** gazette-translated-indexed.
- **What it shows:** an LRMoo-style split of abstract legal Works from versioned Expressions; temporal states as aggregations that reuse unchanged components' versions; legislative events (amendments) reified as Action nodes so causality, point-in-time retrieval and provenance become queryable. Method only, no benchmark.
- **Repo already does:** a two-type graph (notification, cross_reference) with `publish_date` on the notification only (`db/schema.sql`). `grep 'effective' '*.py'` returns one hit, a curl `%{url_effective}` flag at `ingest/egazette_search.py:161`; `grep 'commence' '*.py'` returns 0 hits. `subject_thread.status` is `active | superseded` with no date. The graph can say *that* B supersedes A but not *from when*, and cannot answer "which notification governed on date D".
- **Gap:** no temporal validity on edges or nodes (commencement or w.e.f. date, cessation date). Indian notifications state this in fixed drafting phrases ("shall come into force on …", "with effect from …") that the repo's anchor-plus-window matchers (`extract/common_templates.py:115-128`, per the baseline snippet) are built to catch.
- **Verdict effect:** confirms `open`. This is prior art for the *schema*, not for the Indian dataset. The nearest open-source analogue found in today's open-ground check is luatdo (below), Vietnam only.
- **Action queued:** REPO_ACTIONS 2026-10-29 (effective_date on cross_reference).

## Weak / not relevant

- **luatdo (github.com/tamnd/luatdo, MIT, Go, 5 stars, 31 commits)**. Cluster F, open-ground check for gazette-translated-indexed, logged 2026-10-29. README fetched. Builds a versioned legal knowledge graph for **Vietnam** from two Hugging Face corpora (306 effective laws; about 171k vbpl.vn documents, about 128k after parsing): Component vs TextVersion nodes dated from effect, ten amendment event kinds including suspend and resume, half-open validity intervals, about one million citation and amendment edges resolved deterministically without an LLM, nine post-build invariants, and one end-to-end check at 94.4% agreement with a published consolidation. It is the closest thing found to what the gazette repo does, for a different country and with the temporal layer the gazette repo lacks. Verdict stays `open` (no India equivalent). Logged here rather than as an entry because it is a tool with no paper and its claims are its own README.
- **gazetter (pkg.go.dev/github.com/arjunmadan/gazetter, MIT, last published Mar 2023)**. Cluster F, logged 2026-10-29, search snippet only. A Go CLI that downloads eGazette PDFs by article-id range and year. A download tool: no index, no graph. Not prior art.
- **LeSICiN (AAAI-22, Zenodo 6053791) and Hier-SPCNet (arXiv 2209.12474)**. Cluster F, logged 2026-10-29, snippets only. Case–statute citation networks over Indian court judgments for statute identification, not notification lineage. Hier-SPCNet drops citations to amended Acts when no year is given, which is the inverse of the gazette repo's problem. Not fetched.

- **S&P Global Market Intelligence, "Point-in-Time relevance for APAC markets" (Joseph & Fruin, Oct 2019, spglobal.com PDF)**. Cluster A/B, logged 2026-10-24. Seen only through a search summary, not fetched. It is vendor research on period-end-to-report lags and restatements in Asia, and its message is that a fixed lag cannot mimic PIT. Fetch the PDF before anything is claimed: it is the one source found that could give measured JP/KR/IN reporting lags. Baseline `prior_art` was not checked today.
- **tradevodata, "Your backtest saw the future: lookahead bias in fundamental data measured across 313,562 rows" (dev.to blog)**. Cluster A/B, logged 2026-10-24. A vendor blog on US SEC data only (mean lag 43 days, max 61, per the search summary). It does not cover non-US markets. Not fetched. WEAK.
