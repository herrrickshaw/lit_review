# Literature Register

Running log of papers reviewed for market-pipeline technique extraction. One entry
per paper. Seeded 2026-08-22 from a 12-paper session sweep (5 agents, per-technique
file:line verification against the repo). Extended daily by the
`literature-review-daily` scheduled task — read-only, no repo edits, no backtests
run from this task; candidate backtests go to `BACKTEST_QUEUE.md` instead.

**Grading convention**: EVIDENCE-GRADE strong = risk-adjusted metric (Sharpe/return),
costs modelled or addressed, disclosed universe/period. weak = price-level MAPE/RMSE,
no costs, small/undisclosed universe, or self-contradicting result.

**Dedup rule**: check arXiv ID against every entry below before triaging a candidate.

---

## Strong evidence, high relevance

### 2605.19337 — Agentic Trading: When LLM Agents Meet Financial Markets
Audit of 77 LLM-trading studies; reproducibility checklist (only 2/19 primary
studies time-consistent, 0 reached R3). **Hub paper for citation-following.**
- Doing-right: survivorship reported not dropped, multiple-testing correction
  (deflated_sharpe.py), immutable forward log (signal_tracker.py) — repo reaches R3.
- Gap: no embargo/CPCV anywhere in the repo (`grep -rniE 'embargo|cpcv'` = 0 hits).
- Action taken: none yet. Queued: 21-day outcome embargo on signal_tracker.py.

### 2607.15414 — AI Trading: Evaluating LLMs for Technical Market Analysis
5-LLM eval; failure modes incl. sideways-regime degradation.
- Gap: `market_regime.py` computes 'chop' but scanner only demotes on 'bear'.
- Action queued: extend regime demotion to chop+HIGH-vol (build_mailer.py:434 already
  flags it as a warning; not yet a hard gate).

### 2602.00196 — Generative AI for Stock Selection (Rasekhschaffe)
AI-generated features decorrelated from traditional ones (corr 0.06-0.14), combine well.
- Gap: all 10 repo factors derive from ONE weekly close panel (factor_learning.py:37).
- Action queued: promote sentiment_pipeline.py (collected, unused as factor) or PEAD
  data into FACTORS.

### 1809.09441 — Temporal Relational Ranking for Stock Prediction (RSR)
Ranking beats regression/classification on same backbone (Table 5) — well evidenced.
Its relational-graph claim is weaker (Table 6: graph CUTS NASDAQ IRR 0.68->0.23).
- Gap: no learning-to-rank formulation anywhere in repo; scores are independent
  per-stock thresholds (Piotroski >=7, Darvas 0-7).
- Action queued: replace build_mailer.py:227 fixed pio>=7 gate with a within-market,
  within-week cross-sectional percentile cut.

### 2607.19005 — Observable Matrix Dynamics of Stocks (Halperin)
Spectral/correlation-matrix regime + effective-dimension method, S&P 500 crises.
- Gap: market_regime.py:76 is EMA-vs-index + vol percentile only — cannot distinguish
  a correlated crash from a dispersion unwind.
- Action queued: participation ratio of (a) the nightly correlation matrix
  (market_correlation_scan.py already builds it, discards it after writing files),
  and (b) the 10-factor correlation matrix — direct measurement of the redundancy gap.

### 2603.19286 — Generalized Stock Price Prediction w/ News Fusion
Proves relevance filtering must key on full company name, not ticker (US ticker
runs LOSE to a no-news baseline: MAE 0.2653 vs 0.1030).
- Doing-right: sentiment_pipeline.py:399-408 already reached this independently
  (ticker-matching demoted to guarded fallback).
- Gap: the per-ticker match is a hard GATE (drops non-matching articles, truncates
  [:15]) rather than a relevance SCORE; aggregation weights by provider, not relevance.
- Coverage caveat: free news exists for IN/US only.

### 2506.16746 — SSPT: Pre-training Time Series Models with Stock Data Customization
3 label-free pretext tasks (code/sector/moving-average classification) — needs no
data the repo doesn't already have (stock codes, sectors, prices).
- Feasibility check done: torch 2.13.0 installed, warehouse (7,955 US symbols,
  2016-2026) exceeds the paper's largest dataset. Repo taxonomy is 11-12 sectors vs
  paper's 112-129 (weaker pretext signal) — mitigable via `industry` column.
- Verdict: task-design idea transfers even without training the transformer;
  same free-label insight cashes in via Lasso.

---

## Weak evidence or narrow scope — logged, not actioned

- **1902.08684** (candlestick Word2Vec) — only paper of its batch that models costs
  and reports significance tests, but its own held-out result LOSES to buy-and-hold
  (Table 3/5). Repo already has both halves (Darvas boxes + KMeans clustering) at
  better quality. Verdict: not worth a build.
- **2305.14382** (Informer, 1-5min intraday) — does not transfer; repo has no
  intraday trading and its one real intraday module (intraday_monitor.py) is unwired.
- **2506.04658** (DRL: DDQN/PPO) — order-placing/shorting agent; doesn't map to a
  signal-only long-only pipeline. Non-transferable mechanism, transferable idea only
  (abstention-rate as a headline metric — see below).
- **1809.09441 companion papers** (GNN rolling-window, KG+LLM, Node Transformer+BERT)
  — see paper-G-relational.md; KG+LLM paper has NO quantitative evaluation at all,
  cite for schema only, never for evidence.
- **2509.12286** (Quantum GAN) — self-refuting: its own table shows QGAN RMSE 251.89
  vs classical GAN 84.27. Discard.
- **2505.05325** (LSTM+VADER) — MAPE 2.72 on 4 correlated tech stocks, no date range,
  no costs. Metric rewards lagging. Discard.
- **1909.12227** (autoencoder+CNN+LSTM) — no costs, no backtest, universe undisclosed.
  One durable line (predict rate-of-change not price level) — repo already does this.

---

- **2601.06090** (Nordic correlation regime shifts, Girnyk) — passes on rigor
  (two decades, eigenvalue-ratio crisis indicator, cleaned correlation matrix,
  min-variance overlay) but the universe is 3 *indices* (OMXS30/OMXC20/OMXH25),
  not a stock cross-section, and costs are unmentioned. The mechanism it uses
  (λ₁/λ₂ crisis indicator) is already captured by 2604.17251's spectral-gap
  feature — nothing additional to queue. Logged, not deep-read.
- **2601.08571** (Regime Discovery, EMD/Hilbert-Huang + variable-length Markov
  chains) — descriptive only: no Sharpe/return/IR, no MAPE/RMSE, no date range
  disclosed, no costs. Regime taxonomy (Normal/High/Extreme) adds nothing over
  `market_regime.py`'s existing bull/chop/bear × LOW/MID/HIGH. Discard.
- **2507.14325** (multiscale RMT eigenvalue distribution) — physics-side
  distributional modelling of the spectrum, no trading evaluation of any kind.
  Off-scope for technique extraction. Discard.

## Rejected adoptions (build-vs-borrow verdicts)

### arXiv:2412.20138 / github.com/TauricResearch/TradingAgents
**REJECT adoption.** Default fundamentals path is a live snapshot ignoring backtest
date (`y_finance.py:274-282`, stamped `datetime.now()`) — any historical run is
unfalsifiable. No transaction costs in its backtest (3 stocks, 62 trading days,
single seed). ~$1-5 per ticker-date in LLM API cost; replicating 20 daily finalists
across 5 markets ≈ $1,200/month to replace a mailer that costs zero. Borrowable idea
only: outcome-feedback loop, which score_signals.py already ~80% implements
deterministically (no LLM needed).

---

## Session log

- 2026-08-23 (daily): 8 candidates triaged (3 via citation-following from
  2605.19337, 5 via the Saturday correlation-spectrum query). 3 deep-read
  (2604.17251, 2608.09641, 2607.04958), 3 logged weak/narrow, 2 found but left
  untriaged for budget (2212.05504, 2511.21515). 3 queue items added (9-11).
- 2026-08-22: 12 papers processed (5 agents + 1 solo), ~95 techniques extracted,
  register seeded. Entry-bar look-ahead bug found (backtest_screeners.py,
  factorial_screener_test.py) and fixed; measured on 10.5y NSE (20,905 signals)
  and 5.1y US (14,646 signals) offline panels — bias real, short-horizon,
  ~-0.15 to -0.22pp (India) / -0.09 to -0.15pp (US), washes out by T+3mo.
- 2026-08-22/23: full historical stock-pick performance measured (23,900 merged
  entries, 4 sources incl. real Gmail draft/sent brief content — the send
  tool doesn't exist, only create_draft, so real briefs were recoverable as
  drafts). Overall median vs benchmark -2.74%, win rate 53%. Caught and fixed
  a benchmark-computation bug mid-analysis (panel-median fallback produced a
  fabricated +46.77% "vs bench" for India; replaced with a real NIFTYBEES+NIFTY50
  splice). Discovered signal_tracker.py --record has been silent 31+ days,
  wired into no cron/launchd job. Five scheduled tasks now running: brief-log
  audit, signal-tracker resume, Gmail brief parser, literature review, weekly
  performance monitor — all Mon-Sat/weekly, all read-only against the live
  pipeline except their own designated output files.
- 2026-08-23: BACKTEST_QUEUE items #1 and #3 executed (not just queued).
  Factor redundancy: participation ratio 4.92/10 (IN), 4.53/10 (US) — confirms
  the qualitative "factors are redundant" finding with a real number.
  Correlation-spectrum regime signal: validated against the independent,
  out-of-sample-to-this-repo COVID crash — 5 lowest-PR windows in 10.5y of
  NSE data are all Mar-May 2020, PC1 absorption 50-53% vs 14-15% calm.
  Logged only, not gated, per the "measure before wiring" discipline.

---

## Added 2026-08-23 (daily task)

### 2604.17251 — ORCA: Online Regime Correlation Analyzer (Kriuk & Kriuk, 2026-04-19)
Spectral graph theory + RMT + Random Forest to predict 10-day rallies/crashes.
24 exchange-traded instruments, 15y US daily (2009–2024), 127 spectral + 79
price features. **EVIDENCE-GRADE: strong** — Sharpe 1.13 / CAGR 15.6% vs 3.7%
buy-and-hold, max DD −7.5%, crisis-detection AUC 0.741, and it models costs
(5bps per unit of position change + 50bps/yr leverage) *inside* the grid-search
objective, not just the final table. 8-fold expanding walk-forward, 3y train /
6mo test, **10-trading-day anti-leakage gap** matched to the prediction horizon.
**CORRECTION 2026-08-23** (4-agent CPCV/embargo research round, primary source
re-fetched and confirmed): ORCA does NOT ablate this gap — it reports ONE
walk-forward result with the 10d gap already baked in, not a with/without
comparison. The gap-methodology description above is accurate; do not read it
as "ORCA showed the gap's effect empirically" — it didn't test that.
- Doing-right: repo already models cost in its walk-forward
  (`walk_forward_backtest.py:156`, 0.2% round-trip STT+brokerage).
- Gap 1 (spectral): the repo computes correlation matrices
  (`market_correlation_scan.py:168`, `:311`) but never decomposes them — the
  matrix is consumed only as thresholded graph edges (`:171-178`) / MST (`:312-313`)
  and then written to CSV. `grep -rniE 'eigen|effective_rank|absorption_ratio|marchenko'`
  over `code/python_files/` (excluding vendored `.venv`) returns exactly one hit,
  a *comment* at `market_correlation_scan.py:306`. This paper supplies the missing
  formulas: absorption ratio AR_k = Σ₁..ₖλᵢ/Σλᵢ (k∈{1,3,5}), eigenvalue entropy
  H = −Σλ̃ᵢlnλ̃ᵢ, effective rank ER = exp(H), spectral gap λ₁/λ₂, condition number
  λ₁/λₙ, Marchenko–Pastur excess λ₁−(1+√(n/T))², first-eigenvector HHI.
- Gap 2 (embargo): `walk_forward_backtest.py:173-181` splits 60/20/20 strictly
  chronologically with **zero gap** — `test_start` is the next trading day after
  train. Repo horizons run to 8 forward windows, so the overlap is real.
- Action queued: items 9 and 10 below.

### 2608.09641 — Lower Spectrum of Financial Correlation Matrices (Grassi, Pastorino, Uberti, 2026-08-10)
Argues the *smallest* eigenvalues carry the diversification-collapse signal, not
just the largest. Defines m⁻ = count of eigenvalues below the lower
Marchenko–Pastur bound (1−√(n/w))². Datasets: 10 S&P sector indices 1990–2020;
377 S&P constituents and 199 Nikkei 225 constituents, both 2005–2020.
Rolling window w=1000.
- **EVIDENCE-GRADE: medium.** Real disclosed universes and long periods, and the
  predictive test is risk-conditional (1% VaR and next-day return dispersion rise
  with m⁻) — but it is a risk-forecasting result, not a traded strategy, and no
  transaction costs appear. Graded medium, not strong, on that basis; it is
  nonetheless directly usable because the repo wants a *regime gate*, not a trade.
- Gap: same as above — no eigendecomposition exists to compute m⁻ from. It is one
  extra line on a matrix `market_correlation_scan.py` already builds and discards.
- Note: m⁻ is the mirror of ORCA's effective rank; computing both from one
  decomposition costs nothing extra, so they should be queued as a single change.
- Action queued: folded into item 9.

### 2607.04958 — Look-Ahead-Freedom as Temporal Non-Interference (Fonseca, 2026-07-06)
Found by citation-following from the hub paper 2605.19337. Reframes look-ahead
bias as temporal non-interference over a time-indexed information lattice.
Central practical construct: a **pipeline calculus separating a datum's
availability time from its reference time**. Proves the general problem
undecidable (Π⁰₁-hard) where availability depends on data values, but gives a
sound, linear-time-decidable type-and-effect system on the value-independent
fragment — which explicitly covers windowing, resampling, joins, point-in-time
and vintage reads. Their checker caught every planted leak that differential and
tiling detectors missed.
- **EVIDENCE-GRADE: n/a (not an empirical trading paper)** — graded instead on
  whether the mechanism transfers. It does, in reduced form.
- Doing-right: the repo independently hit this distinction — `pe_bands.py:82-93`
  uses an FYE+90d availability proxy rather than the reference date, which is
  exactly the availability-vs-reference split this paper formalises.
- Gap: that discipline is per-site folklore, not checkable. `grep -rniE
  'embargo|purge|cpcv'` over `code/python_files/` still returns 0 non-vendored
  hits, and no module annotates its columns with an as-of semantics.
- Not adopted wholesale: implementing the type system is out of scope for a
  one-person Mac pipeline. The transferable part is the annotation discipline.
- Action queued: item 11.

---

## CPCV / embargo — dedicated research round (2026-08-23)

User-requested deep dive on the one gap flagged as "purely theoretical, not yet
actioned" (item 6/10). 4 parallel agents: foundational algorithm, critiques/
failure-modes, empirical effect-sizes, implementation reality. Full synthesis
and the concrete action are in BACKTEST_QUEUE.md item 6 — this section is the
source ledger.

**Foundational** (AFML Ch.7 §7.4.1 p.105 / §7.4.2 p.107 / Ch.12, via
mlfinlab docs+source, reasonabledeviations.com, Towards AI): purging drops
training rows whose LABEL window overlaps a test label window. Embargo has no
single canonical formula — mlfinlab defaults to % of dataset; "embargo ≥
horizon" is a theoretically-argued convention, not a proven law. CPCV's real
contribution is a Sharpe *distribution* over C(N,k) paths for overfitting
detection, not leakage prevention (purge+embargo alone does that). Cost:
C(20,10) ≈ 184,756 splits.

**Critiques** (eslazarev/purged-cross-validation README — fetched and
confirmed; Arian/Norouzi M./Seco 2024 Knowledge-Based Systems — abstract-level
only, SSRN/ScienceDirect blocked 403): purge/embargo ≠ protection against
selection bias across strategy configurations — that needs deflated Sharpe,
which `deflated_sharpe.py` already implements here. No verified minimum-
sample-size threshold in the literature; reasoned (not sourced) inference that
CPCV's ~100+-path stability requirement is in tension with India's shorter
history (~2,500 trading days).

**Empirical** (eslazarev repo's own ablations — fetched; ORCA 2604.17251
primary source — fetched and confirmed, see correction above; Arian et al. —
abstract only): no clean equity-Sharpe before/after number exists in the
accessible literature. Real inflation numbers on synthetic/crypto/non-financial
targets: naive shuffled CV reports R²=0.83–0.99 on literally unpredictable
data; purged/walk-forward CV correctly collapses this below baseline. No
literature-validated embargo-to-horizon scaling formula found (ORCA uses 1×
horizon with no ablation; one weak secondary source claims 2×, unconfirmed
against AFML directly).

**Implementation** (GitHub/PyPI, fetched and independently re-verified this
session): mlfinlab is dead for reuse — closed-source, delisted from PyPI,
confirmed. `sklearn.model_selection.TimeSeriesSplit(gap=...)` is real
(confirmed against the installed sklearn 1.9.0 — `gap=0` default) but only a
fixed-index-count gap, not label-horizon-aware purging. Two alternative
libraries found and rejected: `timeseriescv` (stale since 2022-02, usable as
reference code only) and `purgedcv` (released the same day as this research,
zero track record). `walk_forward_backtest.py` independently confirmed to run
under Python 3.11 (not 3.9), so no version blocker either way. Recommendation:
hand-build, ~40–80 lines for purge+embargo, ~150–250 for full CPCV.

**Convergent verdict, reached independently by all four agents**: build a
minimal purge+embargo function now (embargo = 252 trading days, the repo's
longest evaluated horizon); pair it with the deflated Sharpe ratio already in
`deflated_sharpe.py`; do not build full CPCV as a first move — its documented
value is overfitting-distribution analysis, not leakage prevention, and its
combinatorial cost is unjustified before the simpler fix lands.

---

## Evidenced-screener backtest round (2026-08-23)

3-agent literature search (quality/value, momentum/technical, low-vol/size)
ranked candidates by evidence quality; all cited **McLean & Pontiff (2016,
JoF)** independently — 97 published predictors lose 26% return out-of-sample,
58% post-publication. Four candidates were built, tested, and backtested for
real: momentum 12-1 (Jegadeesh & Titman 1993), 52-week-high proximity (George
& Hwang 2004, both IN+US, OHLCV only), gross profitability (Novy-Marx 2013)
and accruals (Sloan 1996, both US-only — India's `total_assets` is 0%
populated in every fundamentals table checked, unreconstructable, a genuine
data gap not fillable from local sources).

**Two real bugs found and fixed during the build**, both worth remembering
for any future forward-return scorer in this repo:
1. A near-zero `assets_est` (units/reporting error in the source filing, e.g.
   OGS FY2013 computing gp_assets_pct = 8.13e10%) let data errors dominate a
   top-decile ranking — fixed with a disclosed plausibility filter (|value|
   <= 300%), not a silent drop.
2. **The "score as of today" convention itself is a confound**, not just a
   convenience: CETX (and 774 of 2,167 gross-profitability signals) had a
   next-available price bar YEARS after the signal date (a real gap in the
   price panel's per-symbol coverage), silently producing an arbitrarily
   delayed "entry" that bears no resemblance to the signal. A 30-calendar-day
   staleness guard fixed this. Even after the fix, "hold until today" gives
   each signal a wildly different holding period (recent signals held weeks,
   2016-era signals held a decade), which by itself produced implausible
   -94%/-117% "vs bench" medians — not from a bug, but from comparing an
   uneven-hold raw return against a benchmark that simply compounded over
   whatever window happened to elapse. **Fixed-horizon scoring (1mo/3mo/6mo/
   1yr from each signal's own entry) is the correct design and the one that
   should be reused for any future paper-motivated backtest in this repo** —
   `run_factor_backtests_fixed.py` is the reusable pattern.

**Final result, all four screens, real benchmarks (NIFTYBEES+NIFTY50 splice
IN, SPY US), entry-bar-correct, staleness- and split-guarded:**

| screen | market | n (1yr) | 1yr vs bench |
|---|---|---:|---:|
| Momentum 12-1 | IN | 3,541 | -14.11% |
| Momentum 12-1 | US | 17,606 | -15.08% |
| 52-week-high | IN | 4,387 | -2.50% |
| 52-week-high | US | 16,216 | -12.56% |
| Gross profitability | US | 1,214 | -14.29% |
| Accruals | US | 2,436 | -32.48% |

**Every screen underperforms the benchmark, and the gap widens at longer
horizons** — a consistent pattern, not noise. This is exactly what McLean &
Pontiff's decay finding predicts: none of these well-published, heavily-
publicized anomalies shows a live edge in this dataset today. 52-week-high in
India is the closest to neutral (~0% at 1mo-6mo, only drifting negative at
1yr) but still never positive. Combined with the debt-turnaround screen's
earlier -14.71% result, five separate paper-motivated screens have now been
tested with this repo's rigor and NONE has shown a real edge — a real,
disciplined finding in itself, not a failed exercise.

---

## Existing-screener + screener.in round (2026-08-23, same day continued)

Applied the SAME fixed-horizon methodology retroactively to this repo's OWN
production screeners, using their real detection code directly
(`backtest_screeners.detect_darvas_signals()`/`detect_golden_cross_signals()`,
unmodified, already entry-bar-fixed) plus 3 screens sourced from
https://www.screener.in/screens/ (user-provided URL, fetched 2026-08-23; 24
public screens found, several matching what was already covered): RSI
Oversold (<30) and a simple single-leg Debt Reduction (vs. the earlier 3-leg
debt-turnaround trajectory). New reusable module:
`run_existing_screeners_fixed.py` + Piotroski F-Score built fresh from
`public.global_fundamentals` (9-point, US-only, same total_assets gap as
gross_profitability/accruals; a missing input EXCLUDES that point from both
numerator and denominator rather than scoring it as failed — tested).

**Result, 1yr vs benchmark, real signals not extrapolated:**

| screen | market | n (1yr) | 1yr vs bench |
|---|---|---:|---:|
| **Darvas box breakout** | **IN** | **17,963** | **+1.41%** |
| Darvas box breakout | US | 16,267 | -1.87% |
| Golden Cross | IN/US | n/a | inconclusive — only 566 raw signals total, too rare for a mature 1yr sample within the 3y scan window |
| Piotroski F-Score >=7 | US | 1,211 | -9.12% |
| RSI Oversold (<30) | IN | 2,335 | -15.00% |
| RSI Oversold (<30) | US | 13,134 | -18.39% |
| Debt reduction (simple) | US | 5,862 | -9.35% |

**Darvas in India is the one real, sizeable edge found across the entire
2026-08-23 research round** — improving monotonically with horizon (-0.40%
at 1mo -> +1.41% at 1yr, win rate 54%->60%), on this repo's own production
detection logic, at genuine scale (17,963-20,505 signals per horizon). It
independently corroborates this repo's own pre-existing, separately-derived
finding at `code/python_files/CLAUDE.md`: "India | momentum/trend | trend +
sector-relative value, +5.3%/6M" -- a real cross-check, not circular, since
that finding predates tonight's work and used different methodology. Darvas
in the US shows no edge, consistent with the same doc's "US | mixed/light"
characterisation.

RSI Oversold's negative 1yr number should not be read as discrediting the
signal's actual (short-horizon, mean-reversion) thesis: India is near-neutral
at 3mo (+0.03% vs bench) and only degrades by 1yr -- holding a "buy the dip"
signal for a full year contradicts its own logic. If revisited, test it at
1-4 week horizons specifically, not 1yr.

**Combined tally, all screens tested 2026-08-23 with identical rigor: 13
market/screen combinations, 1 real positive edge (Darvas, India), 1
inconclusive (Golden Cross, small n), 11 negative.** The negative results are
not a failed session -- they are exactly what a disciplined test should
produce when most tested ideas are heavily-published, decay-prone anomalies
(McLean & Pontiff). The one positive result surviving this level of scrutiny,
and cross-checking against an independently-derived prior finding, is the
kind of signal worth acting on BECAUSE eleven other plausible ideas were
tested with equal rigor and did not survive.

---

## Regional/regime literature survey — buy/hold/sell rule variation (2026-08-23)

Sourced by a dedicated research agent to ground `backtest_zone_rules.py` and
`strategy_regime_survival.py`'s per-market, per-regime design against the
academic literature, following the mom126 bug fix + India significance
re-test the same day. Full source-by-source detail with credibility grading
kept in this session's transcript; key findings and grades below.

**Regional variation — why momentum/reversal strength differs by market:**
- Rouwenhorst (1998, JoF) — momentum present in 12 developed markets, not US-only. *Very high credibility.*
- Griffin, Ji & Martin (2003, JoF, 40 countries) — momentum profits don't co-move across countries; not a single global risk factor. *Very high.*
- Chui, Titman & Wei (2010, JoF, 41 markets) — momentum magnitude tracks Hofstede individualism (overconfidence proxy); explains why momentum is weak in Korea/Japan (low-individualism). *High, causal claim contested.*
- Hameed & Kusnadi (2002, J. Financial Research) — unrestricted momentum fails in 6 Asian markets incl. Korea. *High — direct Korea corroboration.*
- Balvers & Wu (2006, J. Empirical Finance) — [already in repo] momentum+mean-reversion coexist, OPTIMAL WEIGHT DIFFERS BY COUNTRY. *Very high — closest thing to a direct endorsement of this repo's whole per-market design.*
- India: JBF (2023), 3,956 BSE stocks 2000-2021 — momentum AND reversal both real, liquidity-conditional (momentum in liquid names, reversal in illiquid). *High.* Explains why this repo's India trend rule tests marginal (t<1.5): a uniform EMA rule averages two opposite-signed liquidity regimes.
- Korea: Investment Analysts Journal (2024) + Emerging Markets Finance & Trade (2022) — individual-stock momentum REVERSES in Korea, explained by a "salience"/behavioral effect; foreign investors trade momentum, retail investors are contrarians. *Moderate-high — strongest literature match to any of this repo's own findings (Korea mom126 t=-2.13).*
- Japan: Asness (2011, JPM/AQR) — momentum Sharpe ~0.03 in Japan vs 0.22-0.48 elsewhere, argued to be within noise given momentum/value's negative correlation. *High but self-interested (AQR); later work on residual/industry-neutral momentum finds Japan momentum DOES work with better specification — treat "just noise" skeptically.*

**Regime-dependence — bull vs bear:**
- Cooper, Gutierrez & Hameed (2004, JoF) — US momentum profit is +0.93%/mo after up-markets, **-0.37%/mo after down-markets**; sign LITERALLY FLIPS by regime. *Very high — landmark result, directly explains why this repo's uniform trend rule "dies in bear markets everywhere."*
- Daniel & Moskowitz (2016, JFE) — "momentum crashes" cluster specifically at the bear-to-rebound TRANSITION (not throughout the bear), via short-leg option-like beta. *Very high.* Actionable: check whether this repo's regime-labeled data shows worst trend-following losses concentrated at that specific transition point, not spread through the bear regime.
- Asness et al. (2013, JoF) — value/momentum negatively correlated everywhere, linked to opposite-signed funding-liquidity exposure — mechanistically ties momentum failure to the same liquidity contractions that mark bear regimes. *Very high.*
- McLean & Pontiff (2016, JoF) — [already in repo] ~26-58% return decay post-discovery/publication. Caveat for ALL of this repo's backtested effect sizes, weighted least for Korea (mean-reversion) and India (liquidity-conditional momentum) since those anomalies are less likely to have been arbitraged by crowded global momentum capital than plain US/EU/JP momentum.

**Practitioner (lower weight, directional only):** Research Affiliates and AQR both run momentum+mean-reversion combined systematically, treating them as complementary horizons rather than competing rules — consistent with, not independent confirmation of, Balvers & Wu.

**Corroboration table — literature vs. this repo's own findings:**
| This repo's finding | Verdict |
|---|---|
| Korea: significantly negative momentum | STRONGLY CORROBORATED — best-supported match in the whole survey |
| US/JP/EU: regime-conditional (bull-momentum/bear-revert) | CORROBORATED as a general pattern (Cooper-Gutierrez-Hameed, Daniel-Moskowitz) |
| India: trend favored but not significant | PARTIALLY CORROBORATED — likely a liquidity-conditional specification issue, not "no edge"; a %ADV split is a concrete next refinement |
| India + Europe are the ONLY markets whose single rule survives both regimes | **NO literature match found — flag as a genuinely novel, unconfirmed result of this repo's own backtest, not literature-backed** |

**Uses**: the India-liquidity-split idea and the bear-regime-transition-timing check are both queued as candidate refinements, not yet built — see `BACKTEST_QUEUE.md` convention if picked up.

---

## Added 2026-08-24 (daily task, citation-following from hub 2605.19337)

### 2606.08285 — Beyond Agent Architecture: Execution Assumptions and Reproducibility in LLM-Based Trading Systems (Yao & Zheng, 2026-06-06)
Cites the hub paper (2605.19337); extends its reproducibility audit to a coded
evidence matrix over 30 LLM-trading studies specifically on execution realism:
point-in-time controls, temporal splits, execution timing, turnover treatment,
transaction costs, artifact release. Demonstrates via a 10-equity worked example
that undisclosed friction/timing choices materially compress active-strategy
results.
- Doing-right (all verified by grep, not assumed): transaction costs are modelled
  and disclosed — `walk_forward_backtest.py:156` (`TRANSACTION_COST = 0.002`,
  "0.2% round-trip (STT + brokerage)") and `backtest_screeners.py:176-177`
  (same rate, cited to JIER 2024). Point-in-time discipline is pervasive, not a
  single site — `backtest_ccc.py:134` (`pit_panel`), `backtest_liquidity_forward.py:78`
  ("PRECEDING-only frame => strictly point-in-time"), `backtest_piotroski_plus.py:40,106`,
  `backtest_pe_anomalies.py:157` (`pit_eps_panel`). Turnover is tracked as a tiering
  input (`adaptive_liquidity.py:236` `retier(..., turnover_col=...)`) and eviction
  rules bound rebalance frequency (>5-session eviction per the watchlist mailer).
- Gap: none material found. This repo is a signal-only EOD mailer (no execution
  layer), so "execution timing" (fill assumptions, latency) in the paper's sense
  doesn't apply — there is no order execution to misreport.
- Action queued: none. Logged as a doing-right confirmation from a second,
  independent audit (different authors, narrower lens than the hub paper),
  corroborating rather than adding to the hub's checklist.

### Weak/off-scope, one line each (triaged, not deep-read)
- **2607.19453** (Binance spot extrema audit, Jadouli) — real costs (31bps),
  real negative result (10-pair selector -6.72%/19 cycles, NO_TRADE conclusion),
  genuinely rigorous by this register's own bar — but crypto spot intraday timing
  models, and this pipeline trades neither crypto nor intraday. No transferable
  mechanism; logged for completeness of the citation-following sweep only.
- **2407.17645** (Hopfield Networks for Asset Allocation) — surfaced by an
  embargo/CPCV arXiv search (uses CPCV for validation) but abstract discloses no
  universe, date range, or cost treatment, and the mechanism (training a Hopfield
  network) needs an ML-training path this repo doesn't have. Not deep-read.

---

## Added 2026-08-25 (daily task, Tuesday gap query: factor redundancy / spanning tests)

Citation-following from hub 2605.19337 returned **no new candidates today** — the
Semantic Scholar citation list is unchanged at 3 papers (2607.19453, 2607.04958,
2606.08285), all three already in this register. The whole day's yield came from
the weekday gap query.

### 2601.10279 — Selecting and Testing Asset Pricing Models: A Stepwise Approach (Feng, Lan, Wang & Zhang, 2026-01-15)
Accepted at *Management Science*. Sequentially adds/removes factors from a baseline
(e.g. CAPM) to find the model spanning the joint efficient frontier of test assets
*and* all candidate factors, then tests performance on selected **and unselected**
factors — the unselected half is the part most selection procedures skip. Uses
asset-pricing duality (minimising unexplained pricing error ≡ maximising Sharpe) to
argue selection consistency. Standard factor models fail their test; the derived
8-factor model passes and holds up out-of-sample.
- **EVIDENCE-GRADE: medium.** Sharpe-based (not MAPE/RMSE), peer-reviewed at a top
  journal, and it reports out-of-sample results — but the abs page discloses neither
  the date range nor any transaction-cost treatment, so it does not clear the bar for
  "strong" as this register defines it. Graded on mechanism transfer, which is direct:
  the repo has a factor set and no formal test of whether its members are redundant.
- Gap (verified, not assumed): `grep -rniE 'spanning.test|stepwise|orthogonaliz|residualiz|variance_inflation' --include='*.py' code/python_files/ research/` returns
  **zero hits**. The repo's only factor-selection mechanism is L1 shrinkage —
  `factor_learning.py:88` (`LassoCV(cv=5, n_alphas=40, max_iter=5000)`), whose kept-set
  is read off `lcv.coef_` at `:89-90`. Lasso zeroing a coefficient is *not* a spanning
  test: it answers "does this factor improve the fitted combination" under one penalty
  path, not "is this factor's return spanned by the others", and it gives no t-stat.
- Complements, does not duplicate, queue item 1 (DONE): that item **counted** redundancy
  (participation ratio 4.92 of 10 IN / 4.53 of 10 US). A spanning test **names** which
  specific factors are the redundant ones and attaches a significance level.
- Action queued: item 12.

### 2111.05072 — The Evolving Causal Structure of Equity Risk Factors (D'Acunto, Bajardi, Bonchi & De Francisci Morales, 2021-11-09)
Causal structure learning over **11 US equity risk factors, 29 years, daily**. Two
findings that bear directly on this repo's own measured result: (a) the causal network
among factors **sparsifies over the long run**, and (b) that trend **reverses under
financial stress** — the network densifies, driven by the market factor, until
"exposure to different factors boils down to exposure to the market risk factor."
Argues causal structure beats plain correlation specifically during downturns.
- **EVIDENCE-GRADE: medium.** Long disclosed period, disclosed factor count, daily
  frequency, and the headline claim is tested for statistical significance — but it is
  a structural/descriptive study with no traded strategy, no Sharpe, and no costs.
  Usable here for exactly the reason 2608.09641 was: the repo wants a *regime
  descriptor*, not a trade.
- Gap (verified): the repo's factor-redundancy measurement is **static**.
  `research/factor_redundancy.py:65` takes one `df.corr()` over the entire pooled panel
  (263K/261K obs) and eigendecomposes that single matrix at `:42-52`. There is no
  rolling variant — `grep -rniE 'rolling' --include='*.py' research/` hits only
  `correlation_regime_spectrum.py:9`, which is the **stock** correlation matrix
  (150-symbol NSE universe, rolling 60d), not the factor matrix.
- Why this matters concretely: if the paper's densification result holds here, the
  "4.92 of 10" headline from queue item 1 is an *average over two structurally
  different regimes*, and the true calm-period figure is higher while the stress-period
  figure is materially lower — i.e. the factor set collapses toward one factor exactly
  when the mailer most needs diversification. That is a falsifiable prediction about
  data already on disk, testable with machinery that already exists.
- Cheap: the rolling-window code in `correlation_regime_spectrum.py` and the spectral
  stats in `factor_redundancy.py:42` already exist; this points the former at the
  latter's matrix. No new data, no new fetch, no training.
- Action queued: item 13.

### Incidental finding (not from a paper — found while grep-verifying the above)
`factor_learning.py:88` runs `LassoCV(cv=5, ...)` on the train split (`:84-85`,
60/40 chronological). `cv=5` is plain 5-fold KFold: sklearn will fit the penalty path
on folds that sit *after* the fold being scored, so α is tuned with future information
even though the outer 60/40 train/test boundary is chronologically clean. This is a
third concrete site for the purge+embargo function already specified in queue item 6,
and it was not previously named there. Queued as item 14.

### Weak/off-scope, one line each (triaged, not deep-read)
- **2606.19550** (Shin, "Which Portfolios? The Construction Dependence of Factor Model
  Performance") — real finding (model rankings flip with weighting/rebalancing choice;
  FF3 most stable under daily constant-weighting), but it evaluates FF3/FF5/FF6/q5 on
  characteristic-unsorted random CRSP portfolios, and this repo uses none of those
  models; no cost treatment disclosed. No transferable mechanism for a screener.
- **2606.23596** (Shin, "Anatomy of the Market: A Body-Tail Test of Factor Models") —
  same author, same limitation: an internal-consistency diagnostic for q5/FF3 (q5 shows
  offsetting body/tail leg alphas at daily frequency). Diagnoses academic factor models
  the repo does not run. Discard.
- **2603.29751** (Common Risk Factors in Decentralized AI Subnets) — surfaced by the
  spanning-test query and does report spanning alphas, but the universe is crypto AI
  subnets. Off-scope universe entirely.
- **2603.16365** (FactorEngine, LLM-based factor mining) — needs a per-query LLM API
  spend path; this register already rejected that cost profile once on
  arXiv:2412.20138 (TradingAgents, ~$1,200/mo to replace a zero-cost mailer). Discard.
- **2604.26747** (Constrained LLM Agents in Cryptocurrency Markets) — crypto, LLM-cost.
  Discard on both counts.
- **2405.07294** (Factor Strength Estimation in Vector and Matrix Time Series) —
  econometric estimation theory, no trading evaluation of any kind. Off-scope.
