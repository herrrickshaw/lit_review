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

## Weak / not relevant

- **S&P Global Market Intelligence, "Point-in-Time relevance for APAC markets" (Joseph & Fruin, Oct 2019, spglobal.com PDF)**. Cluster A/B, logged 2026-10-24. Seen only through a search summary, not fetched. It is vendor research on period-end-to-report lags and restatements in Asia, and its message is that a fixed lag cannot mimic PIT. Fetch the PDF before anything is claimed: it is the one source found that could give measured JP/KR/IN reporting lags. Baseline `prior_art` was not checked today.
- **tradevodata, "Your backtest saw the future: lookahead bias in fundamental data measured across 313,562 rows" (dev.to blog)**. Cluster A/B, logged 2026-10-24. A vendor blog on US SEC data only (mean lag 43 days, max 61, per the search summary). It does not cover non-US markets. Not fetched. WEAK.
