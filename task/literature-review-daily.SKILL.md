---
name: literature-review-daily
description: "Mon-Sat 07:30 IST: three review tracks plus a sync. A) trading-strategy literature for market-pipeline, triaged and graded into the literature register. B) commissioning sources for the masaladeutsch blog, graded into its source register. D) papers, tools and datasets for the other herrrickshaw repos (energy/process, battery/health, trade policy, civic records, dev tooling, finance toolkits), checked against what each repo's code actually does. C) mirror the review files into the private lit_review repo and push. Read-only in every source repo apart from the named append targets; no backtests run, no blog post published; the Track C mirror is the task's only git write."
---

Three independent daily reviews, run in order A, B, D, then the C sync. **Track A** extends the market-pipeline literature review (trading techniques). **Track B** finds commissioning material for the masaladeutsch blog (article sources). **Track D** (added 2026-10-24) keeps the code-grounded portfolio review of the other herrrickshaw repos current. They share nothing but this file: different repos, different registers, different grading bars.

This is a small, bounded, DAILY task — not a repeat of a full research sweep. You have no memory of prior runs; everything you need is in the files below.

**Run Track A first.** If it consumed an unusual amount of effort, do Track B at reduced budget (triage 2, deep-read 0) or skip it with one line in the log saying so. A skipped Track B is fine; a Track A that never finished is not. The same rule applies to Track D after Tracks A and B: reduce it (triage 2, deep-read 0) or skip it with one line rather than letting the run sprawl.

## Track A — where things live
- **Register (read this first)**: `/Users/umashankar/market-pipeline/research/LITERATURE_REGISTER.md` — every paper already reviewed, graded, with its doing-right/gap verdict. Check every candidate's arXiv ID against this file before triaging it — do not re-review a paper already logged.
- **Backtest queue**: `/Users/umashankar/market-pipeline/research/BACKTEST_QUEUE.md` — concrete paper-motivated actions, consumed by hand later. Append to it; never execute anything from it.
- **Per-day log**: write today's run to `/Users/umashankar/market-pipeline/research/literature_runs/YYYY-MM-DD.md` (use today's actual date).
- **The pipeline** (for grep-verifying "does the repo already do this"): `/Users/umashankar/market-pipeline` (code in `code/python_files/`). It is a personal daily EOD multi-market equity screener (India/US/Europe/Japan/Korea) emitting an email brief. No orders placed, no intraday trading, one person on a Mac, no GPU cluster.

## Track A — 🔴 hard constraints
- **Read-only.** Do not edit any file in `/Users/umashankar/market-pipeline` except appending to `research/LITERATURE_REGISTER.md`, `research/BACKTEST_QUEUE.md`, and writing today's file under `research/literature_runs/`. Do not run any pipeline script, any backtest, or any git write command **in this repo**. Do not touch `/tmp/daily_pipeline.lock`. (The one place git writes are allowed is the mirror repo in Track C — never here.)
- **Budget cap.** Triage at most 8 new candidate papers today. Deep-read (extract techniques, grade evidence) at most 3 that pass triage. This must stay cheap enough to run unattended every day — do not try to repeat the full 12-paper sweep from 2026-08-22.
- **Grade before reading deeply.** For every candidate, spend ~30 seconds first: what evaluation metric does it use (Sharpe/return/IR vs bare price-level MAPE/RMSE), how many instruments, what date range, are transaction costs modelled or addressed. A paper whose headline metric is price-level MAPE/RMSE with no cost discussion and a small undisclosed universe should be logged as EVIDENCE-GRADE: weak in one line and NOT deep-read. Past examples of this pattern already in the register: a Quantum-GAN paper whose own table contradicts its abstract, an LSTM+VADER paper on 4 correlated tech stocks. Do not spend deep-read budget on papers shaped like these.
- **No fabrication.** Every claim about a paper must come from content you actually fetched (WebFetch the arXiv abs/html page). Every "the repo already does this" claim must come from a real `grep`/`Read` you ran yourself, cited as file:line — never assumed from the register's prior summaries, which may have drifted.

## Track A — what to search, in this order

1. **Citation-following** from the register's highest-graded hub paper, arXiv:2605.19337 ("Agentic Trading: When LLM Agents Meet Financial Markets" — an audit of 77 studies' reproducibility). Try `https://api.semanticscholar.org/graph/v1/paper/arXiv:2605.19337/citations?fields=title,externalIds,abstract,year` via WebFetch (free, no auth) to find papers citing it. Papers citing a rigor-focused audit tend to skew rigor-focused themselves.

2. **One gap-derived query**, rotating by day of the week so you don't repeat the same search every run — pick using today's weekday:
   - Monday: "combinatorial purged cross-validation finance backtest embargo"
   - Tuesday: "effective number of factors equity factor redundancy spanning test"
   - Wednesday: "learning to rank cross-sectional equity returns"
   - Thursday: "transaction cost aware factor evaluation net of cost backtest"
   - Friday: "point-in-time fundamentals database survivorship bias equity"
   - Saturday: "correlation matrix eigenvalue market regime effective dimension"

   **Alternate-week topics (added 2026-10-17)** — on odd ISO weeks use these instead of the list above, same weekday mapping:
   - Monday: "overnight intraday return decomposition cross-market momentum"
   - Tuesday: "liquidity-adjusted Piotroski F-score small-cap emerging markets"
   - Wednesday: "regime-switching hidden Markov model equity allocation out-of-sample"
   - Thursday: "post-earnings announcement drift emerging markets point-in-time"
   - Friday: "backtest overfitting deflated Sharpe ratio multiple testing"
   - Saturday: "LLM agent financial report extraction hallucination evaluation"

   Use WebSearch if available, else construct an arXiv search URL like `https://arxiv.org/list/q-fin.TR/recent` or `https://arxiv.org/abs/<id>` for anything you already have an ID for. If WebSearch is not available as a tool, use WebFetch on `https://arxiv.org/list/q-fin.TR/recent` and `https://arxiv.org/list/q-fin.PM/recent` and skim titles/abstracts for relevance to the day's query theme instead.

3. Stop searching once you have ~8 candidates or have made 3 genuine search attempts, whichever comes first — this is a bounded daily task, not an exhaustive sweep.

## Track A — for each paper that passes triage (deep-read, max 3)

Fetch the abs page, get exact title/authors/date/abstract, extract 2-5 concrete techniques. For each: does the repo already do this (verify by grep/read, cite file:line, or mark UNVERIFIED), is it a gap, and if it's a gap and genuinely actionable at this pipeline's scale (no GPU training, no paid data), append one line to `research/BACKTEST_QUEUE.md` describing the concrete change.

Append one new section to `research/LITERATURE_REGISTER.md` per paper that passes triage, in the same format as existing entries (see the file for the exact style — one heading per paper, "Doing-right:" / "Gap:" / "Action queued:" bullets). For papers that fail triage, add ONE line each to the "Weak evidence" section, not a full write-up.

## Track A — output

Write `research/literature_runs/<today>.md` with: candidates found, triage verdicts (pass/fail, one line why), full write-ups for the ones deep-read, and what (if anything) got queued to BACKTEST_QUEUE.md. Keep it under ~500 words — this is a daily log entry, not a report. If truly nothing relevant turned up today, say so in one line and stop; do not pad or force a paper into the register that doesn't belong there.

---

# Track B — commissioning sources for the masaladeutsch blog

Different repo, different purpose. Track A asks *is this technique worth implementing*.
Track B asks *can this carry an article*. A paper can pass one and fail the other.

## Track B — where things live

- **Register (read first)**: `/Users/umashankar/masaladeutsch-archive/docs/SOURCE_REGISTER.md`
  — every source already assessed, with its COMMISSIONABLE / BACKGROUND / WEAK grade.
- **Commission queue**: `/Users/umashankar/masaladeutsch-archive/docs/COMMISSION_QUEUE.md`
  — article ideas with a named dataset attached. Append only; never write the article.
- **Corpus survey**: `/Users/umashankar/masaladeutsch-archive/docs/LITERATURE_SURVEY.md`
  — the 2026-08-22 profile of what the blog covers and the confirmed zero-coverage areas.
  Read its section 3 before searching; it is the map of what is missing.
- **Published corpus**: `/Users/umashankar/masaladeutsch-archive/meta/manifest.json`
  — every published post, with title, slug, date and labels. This is the dedup source of truth.
- **Per-day log**: append your Track B findings to the same daily file Track A writes,
  under a `## Track B` heading. Do not create a second log file.

## Track B — hard constraints

- **Read-only, and nothing is published.** You may append to `docs/SOURCE_REGISTER.md` and
  `docs/COMMISSION_QUEUE.md` only. Never edit a file in `posts/`, never call
  `tools/blogger_api.py`, never run `tools/snapshot.py`, never git-commit or push **in
  this repo**. (Track C's mirror is the only git write in this whole task.)
  Track B produces reading material for a human, not drafts.
- **Budget cap.** Triage at most **5** candidates. Deep-read at most **2**. This runs every
  day; it must stay cheap.
- **Dedup before anything else.** Check each candidate against the register, the survey's
  commissioning list, and the manifest titles. The blog has ~192 posts and a heavy trade and
  logistics beat — assume a trade-flow paper is probably already covered and check rather
  than assuming it is not.
- **Vendor market-sizing is WEAK by default.** Mordor, Grand View, IMARC and similar publish
  modelled figures with undisclosed scope; one overstated an India figure by 6.5×. Log them
  as WEAK in one line. Never queue an article whose central number is a vendor estimate.
- **No fabrication.** Every claim about a source must come from a page you actually fetched.
  Every "the blog already covered this" claim must come from a real grep of the manifest,
  cited by slug — never from memory of the register.

## Track B — what to search, in this order

1. **The open commissioning list.** Read `COMMISSION_QUEUE.md`. If any open item now has a
   newer or better source than the one recorded, note it — that is worth more than a new
   candidate, because it unblocks a piece already judged worth writing.

2. **One gap-derived query, rotating by weekday.** These are drawn from the survey's
   confirmed zero-coverage areas and from beats where new official data lands regularly:

   - **Monday — agricultural labour and rural incomes.** AERR and EPW on farm wages,
     MGNREGA, rural non-farm employment. Zero-coverage area; the wages piece opened it.
   - **Tuesday — insurance, reinsurance and financial plumbing.** IRDAI returns and
     handbooks, GI Council segment data, IFSCA GIFT City approvals, RBI bulletins.
     Newest beat on the blog; the register is nearly empty here.
   - **Wednesday — energy and gas.** OIES, IEA, ACER, PPAC, PNGRB, Eurostat `nrg_*`.
     Heavy existing coverage, so bias hard toward something the blog has not run.
   - **Thursday — seeds, plant variety rights and agricultural IP.** PPVFR authority,
     AERR on essentially derived varieties, ICAR. Confirmed zero coverage.
   - **Friday — irrigation, water and soil.** JISSS on soil organic carbon, AERR on public
     irrigation investment and cost recovery. Water has two mentions in 192 posts.
   - **Saturday — trade, tariffs and industrial policy.** DGCI&S, MoSPI, WTO, PIB.
     The blog's single heaviest beat (63 posts), so the dedup bar is highest here: only log
     something that contradicts or materially updates an existing post.

**Added beats (2026-10-17), used on even ISO weeks in place of the weekday list above:**
   - Monday — biofuels, SAF and ethanol: DGCI&S/PPAC/MNRE/ICAO/CORSIA releases, GOBARdhan, CBG.
   - Tuesday — carbon markets and compliance: EU ETS, CCTS India, CBAM, BEE notifications.
   - Wednesday — critical minerals, batteries and PLI outcomes: MoM, USGS, PIB.
   - Thursday — fertiliser, coal-to-urea and chemicals import substitution: DoF, FAI, DGCI&S.
   - Friday — city gas, CGD and refinery economics: PNGRB, PPAC, CHT.
   - Saturday — Gulf/DACH/India trade corridors: UAE FCSC, Destatis, Swiss FOCBS, CEPA/TEPA.
   Same dedup bar, budget caps and WEAK-by-default rule for vendor estimates apply.

3. **The estate, when a query needs a home.** ICAR `epubs.icar.org.in` hosts 67 open-access
   journals, of which fifteen map onto subjects the blog has never mentioned; AERR is the
   closest in method to how the blog argues. Non-ICAR: EPW, NITI working papers, Indian
   Journal of Agricultural Economics, OIES. Government primaries: PIB, MoSPI, IRDAI, DGCI&S,
   Agmarknet, PNGRB.

Stop at ~5 candidates or 3 genuine search attempts, whichever comes first.

## Track B — grading

For each candidate, answer three questions in about thirty seconds:

1. **Is there obtainable primary data?** A named dataset, portal, return or appendix the
   blog could pull itself. If the only numbers are the authors' own model output with no
   released data, it is BACKGROUND at best.
2. **Is there a finding worth reporting?** Something quantified that a reader would not
   already assume. A paper confirming the obvious is BACKGROUND.
3. **Has the blog covered it?** Grep the manifest. If yes, it is WEAK unless it contradicts
   or materially updates the published piece — in which case say which post, by slug.

COMMISSIONABLE requires yes, yes, no. Anything else is BACKGROUND or WEAK.

## Track B — for each source that passes (deep-read, max 2)

Fetch the actual page. Record exact title, authors, publication and date. Then append one
entry to `SOURCE_REGISTER.md` in the existing format, with:

- **Data**: the specific dataset or table, and whether it is downloadable without payment
  or login.
- **Finding**: the quantified claim, with the figure.
- **Blog fit**: which existing beat it extends or which zero-coverage area it opens, and
  the slug of the nearest published post.
- **Caveat**: the thing that would need checking before publication — vintage, scope,
  sample, or a figure that looks too round.

If it is COMMISSIONABLE, also append one entry to `COMMISSION_QUEUE.md` in that file's
format: working title, source, the argument in one sentence, and the checks needed.

Sources that fail triage get one line each in the register's WEAK section. No write-up.

## Track B — output

Append a `## Track B` section to today's Track A log file. Under ~250 words: candidates
found, one-line verdict each, the write-ups for anything deep-read, and what was queued.

If nothing relevant turned up, write one line saying so and stop. Do not pad, and do not
promote a marginal source to fill the day — the register is more useful sparse and honest
than full and padded. An empty day is a legitimate result and should be recorded as one.

---

# Track D — literature for the rest of the repo portfolio

Added 2026-10-24 after a code-grounded review of all 118 `herrrickshaw` GitHub repos. Track A covers
market-pipeline's trading strategies only; Track D covers everything else that review found: energy and
process design, batteries and health, India trade and industrial policy, civic records, dev tooling, and
the corporate-finance toolkits. It asks a third question: **does this source change what we know about a
repo** — new prior art that overturns an "open" verdict, a method the repo should adopt, or a dataset or
standard its code gets wrong.

## Track D — where things live

- **Baseline (read the day's cluster first):** `/Users/Shared/lit_review/portfolio/baseline/<CLUSTER>.result.json`.
  For each repo: `does` (what the code actually does), `claims_vs_code` (README claims the code does not back),
  `snippets` (the method's real lines), `prior_art` (already found — do not re-log), `verdict`
  (open / prior-art / adjacent / crowded / n/a). `baseline/code_audit.json` has LOC, tests and CI per repo.
- **Register:** `/Users/Shared/lit_review/portfolio/REPO_LITERATURE_REGISTER.md` — entry format at its top.
  Check every candidate against it and the baseline `prior_art` before triage.
- **Action queue:** `/Users/Shared/lit_review/portfolio/REPO_ACTIONS.md` — append only; never executed by this task.
- **Per-day log:** append a `## Track D` section to the same `research/literature_runs/<today>.md` file
  Track A writes. Do not create another log file.
- **Repos:** `github.com/herrrickshaw/<repo>`. Read code with `gh api repos/herrrickshaw/<repo>/contents/<path>`
  (add `-H "Accept: application/vnd.github.raw"`) or a `git clone --depth 1 --filter=blob:none` into a NEW
  empty directory under the scratchpad (never under `$HOME`), read with grep/Read, and delete it at the end.

## Track D — hard constraints

- **Read-only in every herrrickshaw repo.** No commits, pushes, branches, issues, PRs or comments. The only
  writes are the two `portfolio/` files above and today's log section. `portfolio/` is versioned by Track C.
- **Budget cap.** Triage at most **5** candidates; deep-read at most **2**. Same 30-second pre-grade as Track A:
  what does the source actually show, on what data, and is it reproducible (code/data released)?
- **No fabrication.** Every claim about a source comes from a page you fetched. Every "the repo does / does not
  do X" comes from a grep or read you ran today, cited `repo:path:line` — not from the baseline, which is a
  2026-10-24 snapshot and may be stale. If the code changed since the baseline, say so.
- **Privacy.** Private repos may be read but quote at most 3 lines from them. Never quote data rows from
  `india-govt-yellow-pages` (named officials' contacts), and never open `personal-profile` or `working-files`.
- **Vendor market-size estimates are WEAK by default** (same rule as Track B).
- **Do not re-queue fixed items.** `REPO_ACTIONS.md` lists what was already fixed on 2026-10-24.

## Track D — what to search

1. **Open-ground check (one triage slot, when the day's cluster has one).** The baseline marks these repos
   `open` (no direct equivalent found on 2026-10-24): saf-monitoring-system, cng-cgd-retail-outlet-mapping,
   discom-debt-and-revenue-models (C); prenatal-care-toolkit (D); iem-tracker (E); gazette-translated-indexed,
   CBSE_paper_patterns (F). Search once for a new tool or paper doing the same thing. If one exists, that is
   the most valuable finding of the day: log it with `Verdict effect: open -> prior-art`.

2. **One rotating query for the day's cluster.** Even ISO weeks use the first query, odd ISO weeks the second.

   | Day | Cluster (baseline file) | Even week | Odd week |
   |---|---|---|---|
   | Mon | C energy, process & fuels (`C_energy_process_fuels`) | "techno-economic analysis open-source process model validation lignocellulosic ethanol biogas" | "CORSIA SAF life-cycle emissions ILUC default values update" |
   | Tue | D battery, health & ML (`D_battery_health_ml`) | "battery state of charge estimation extended Kalman filter real-cell open dataset benchmark" | "echocardiography valvular heart disease deep learning public dataset validation" |
   | Wed | E trade, industry & policy (`E_trade_industry_policy`) | "revealed comparative advantage import penetration India HS6 trade data" | "production linked incentive scheme evaluation firm-level India" |
   | Thu | F civic records & govt text (`F_civic_govt_text`) | "statute amendment citation graph legal document versioning NLP" | "exam question classification Bloom taxonomy recurrence NLP" |
   | Fri | G dev tooling, RAG & publishing (`G_devtools_rag_content`) | "hybrid retrieval BM25 dense reciprocal rank fusion domain-specific RAG evaluation" | "data provenance tamper-evident lineage hash chain reproducible pipelines" |
   | Sat | A/B finance toolkits & data (`A_market_data_screeners`, `B_quant_research_finance`) | "put-call-futures parity arbitrage emerging market transaction costs" | "point-in-time fundamentals filing date look-ahead bias non-US equities" |

   Saturday is for the toolkits and data engineering (parity mechanics, DCF/valuation methods, point-in-time
   data), **not** trading-strategy alpha papers, which stay in Track A. Use WebSearch, or arXiv/Semantic Scholar
   via WebFetch if WebSearch is unavailable.

3. Stop at ~5 candidates or 3 genuine search attempts, whichever comes first.

## Track D — for each source that passes triage (deep-read, max 2)

Fetch the source; record exact title, authors, venue, date and id. Find the repo(s) it bears on in the day's
baseline file, then check the CURRENT code (grep/read, cite file:line) for the specific point. Append one entry
to `REPO_LITERATURE_REGISTER.md` under `## Entries` in the format at the top of that file. If the gap is concrete
and doable without paid data or a GPU, append one line to `REPO_ACTIONS.md` under `## Open`. Sources that fail
triage get one line each under `## Weak / not relevant`.

## Track D — output

Append `## Track D` to today's log: the cluster and query used, candidates with a one-line verdict each, the
write-ups, any verdict changes, and what was queued. Under ~250 words. An empty day is a legitimate result:
one line saying so, nothing padded.

---

# Track C — sync the mirror repo

Runs **last**, after Tracks A, B and D have finished writing. Purely mechanical: no research,
no judgement, no budget. Its only job is to version today's review output somewhere
independent of the two repos it was written into.

## Where

`/Users/Shared/lit_review` — a standalone git repo, **private** on GitHub as
`herrrickshaw/lit_review`, `main` tracking `origin/main`. It lives outside `$HOME` on
purpose: `/Users/umashankar` is itself a git repo (`global-market-research-platform`),
and a nested repo there risks being swept into that repo's commits.

It is a **mirror**. The source of truth stays where Tracks A and B wrote it:

| mirror path | source of truth |
|---|---|
| `market-pipeline/LITERATURE_REGISTER.md` | `~/market-pipeline/research/LITERATURE_REGISTER.md` |
| `market-pipeline/BACKTEST_QUEUE.md` | `~/market-pipeline/research/BACKTEST_QUEUE.md` |
| `market-pipeline/literature_runs/` | `~/market-pipeline/research/literature_runs/` |
| `masaladeutsch/SOURCE_REGISTER.md` | `~/masaladeutsch-archive/docs/SOURCE_REGISTER.md` |
| `masaladeutsch/COMMISSION_QUEUE.md` | `~/masaladeutsch-archive/docs/COMMISSION_QUEUE.md` |
| `masaladeutsch/LITERATURE_SURVEY.md` | `~/masaladeutsch-archive/docs/LITERATURE_SURVEY.md` |
| `task/literature-review-daily.SKILL.md` | `~/.claude/scheduled-tasks/literature-review-daily/SKILL.md` (this file) |
| `portfolio/` | **itself** — Track D writes here directly; this is the one directory whose source of truth is the mirror repo. Never overwrite it from anywhere else. |

Copy source → mirror, never the reverse. If the two ever disagree, the source repo wins.

The `task/` copy exists because `~/.claude/` is gitignored in the `$HOME` repo
(`.gitignore:49: /.claude/`) — deliberately, and that repo is **public**. So this file
has no version history anywhere else. Mirroring it here is the only record of how the
task's instructions changed over time. Copy it in step 1 along with the rest; never
force-add it into the `$HOME` repo.

## 🔴 Hard constraints

- **This is the ONLY git write in the entire task.** Tracks A and B remain forbidden from
  committing or pushing in `market-pipeline` and `masaladeutsch-archive`. Every git
  command here must be scoped with `git -C /Users/Shared/lit_review`. Never run a bare
  `git` command from a working directory inside either source repo.
- **Never change the repo's visibility.** It is private deliberately — the register
  describes a live trading pipeline by `file:line`, names its factor set, and records
  which screens do and do not carry an edge. Making it public is a human decision. Do not
  run `gh repo edit`, and do not create a second repo.
- **Secret-scan before pushing.** If the grep below hits anything, **stop, do not push**,
  and say so in today's log. Do not try to scrub and push anyway.
- **Never force-push, never rewrite history, never `git reset --hard`.**
- **Failure here must not fail the run.** Tracks A and B have already written their real
  output to the source repos by this point; the mirror is a convenience. If any step
  below fails — no network, auth expired, push rejected — record one line in today's log
  saying what failed and finish normally. Do not retry in a loop.

## Steps

1. Copy the seven source paths in the table above (everything except `portfolio/`, which is already in place), source → mirror (`literature_runs/` copies the
   whole directory, so back-dated files that were added by hand get picked up too).

2. Check whether anything actually changed:
   ```
   git -C /Users/Shared/lit_review status --porcelain
   ```
   **If the output is empty, stop here.** Nothing to do — do not create an empty commit.
   A quiet day is a legitimate result; note it in one line in today's log.

3. Secret-scan the working tree before staging anything:
   ```
   grep -rniE --exclude-dir=task 'api[_-]?key|secret|password|passwd|token|bearer|BEGIN [A-Z ]*PRIVATE KEY|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{20,}|xox[baprs]-|AIza[0-9A-Za-z_-]{35}' --include='*.md' /Users/Shared/lit_review
   ```
   **`--exclude-dir=task` is required, not optional.** `task/` holds a copy of this very
   file, which contains the pattern above verbatim — without the exclusion the scan
   always matches itself and the push would be blocked every single day. `task/` is a
   hand-edited spec, not generated output, so excluding it loses nothing.

   Any hit outside `task/` → stop, do not push, log it. (Registers quote papers and
   government releases; a false positive on a word like "token" in prose is possible, so
   read the hit before concluding — but when genuinely unsure, do not push.)

4. Stage, commit with today's real date, and push:
   ```
   git -C /Users/Shared/lit_review add -A
   git -C /Users/Shared/lit_review commit -q -m "Sync literature review — YYYY-MM-DD"
   git -C /Users/Shared/lit_review push
   ```
   Extend the commit subject with a few words on what the day produced when there is
   something worth naming (e.g. `Sync literature review — 2026-08-25 (queued items 12-14;
   opened crop-insurance beat)`). An empty day still gets a plain dated subject, provided
   step 2 found a real change.

5. Add one line to today's log under a `## Track C` heading: what was synced, the commit
   short SHA, or what failed. One line — this is bookkeeping, not a report.
