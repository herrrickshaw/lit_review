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

## Added 2026-08-26 (daily task, Wednesday gap query: learning-to-rank cross-sectional equity returns)

Citation-following from hub 2605.19337 again returned **no new candidates** — Semantic
Scholar still lists the same 3 citing papers (2607.19453, 2607.04958, 2606.08285), all
already registered. Third consecutive quiet day on that edge. Whole yield from the
weekday gap query. 1809.09441 (RSR) already covers the deep-learning-ranker branch of
this literature, so triage biased toward the *evaluation* and *data-hygiene* branches.

### 2507.07107 — Machine Learning Enhanced Multi-Factor Quantitative Trading: A Cross-Sectional Portfolio Optimization Approach with Bias Correction (Yimin Du, v1 2025-06-02, v2 2026-05-09)
Chinese A-share rolling-window factor pipeline. The paper's real contribution is not
the model — it is a named data-contamination mechanism. A-shares have price limits;
on a limit-locked day the printed close is a price **nobody could transact at**.
Standard pipelines compute factors over those closes and only filter for tradability
afterwards. Du calls this *upstream contamination* and quantifies it: it inflates the
information coefficient by **18%** while cutting realized Sharpe by **0.44**. The fix
is a "mask-first" design that threads the tradability constraint through every
operation rather than applying it at the end. Reports annualized Sharpe 2.05 synthetic
/ 1.63 real (deflated 0.978), 3,000-stock synthetic universe, 2022–2024 real backtest.
- **EVIDENCE-GRADE: medium.** Headline is Sharpe, not MAPE/RMSE, and it reports a
  *deflated* Sharpe — a rare and honest touch. Marked down because the real panel is
  proprietary A-share (unreproducible), the window is a short 2022–2024, and explicit
  transaction costs are not disclosed on the abs page. Graded mostly on mechanism
  transfer, which is direct: India runs ±5/10/20% circuit bands, so the exact hazard
  exists in this repo's largest market.
- Doing-right (verified): the repo is **already mask-first on liquidity**.
  `liquidity.py:5` states the design intent outright ("expensive strategy logic only
  runs on TRADABLE names"), the gate is `liquid_symbols()` at `liquidity.py:548`, and
  it is applied *before* scoring at `screener_kit.py:92-93` and
  `run_existing_screeners_fixed.py:66`. Turnover itself excludes untraded days —
  `liquidity.py:139` (`ok = ret.notna() & (dvol > 0) & dvol.notna()`), with the
  reasoning spelled out at `:128`. This is precisely the discipline Du argues for,
  arrived at independently.
- Doing-right (verified): the KR screener already implements the *stale-print* half.
  `factorial_screener_test_KR.py:119` `_flag_stale_halted_days()` exists because of a
  concrete find — `:128` records `Volume==0` stretches on `000300.KS` in a 200-symbol
  smoke test — and `:134` gives the exact rationale ("nobody could trade a Volume=0
  print").
- **Gap (verified, not assumed): that guard is KR-only.**
  `grep -rln '_flag_stale_halted_days' --include='*.py'` returns exactly one file,
  `factorial_screener_test_KR.py`. No India, US, EU or JP screener has an equivalent,
  and India is the one market with statutory daily price bands. Zero-volume handling is
  also inconsistent rather than absent: `cost_vs_edge.py:130`,
  `backtest_piotroski_plus.py:77` and `daily_breakout_combo_us.py:82` all filter
  `Volume > 0`, but `backtest_liquidity_forward.py:74` uses `Volume >= 0` and so admits
  untradable prints into a forward-return study.
- **Gap: no limit-locked-bar detection anywhere.** `grep -rniE 'circuit|price_limit'`
  over `--include='*.py'` returns only a portfolio drawdown kill-switch
  (`risk_management.py:5`), an unrelated retry helper (`iter_utils.py:48`), and prose in
  `quick_reference.py`. Nothing inspects a bar's range against a band.
- Action queued: item 15.

### 2605.00501 — LambdaRankIC: Directly Optimizing Rank IC for Financial Prediction (Yan Lin, Yihong Su, Yi Yang, 2026-05-01)
Argues the standard mismatch: models are *judged* on Rank IC (Spearman corr of
prediction with realized return) but *trained* on regression or NDCG-style losses that
do not align with it. Derives a closed-form lambda gradient for the pairwise rank swaps
so Rank IC can be optimized directly inside the LambdaRank framework, proves it
optimizes an upper bound on Rank IC, and ships it as a **custom XGBoost objective** —
i.e. CPU, no GPU. Out-of-sample it wins on Rank IC, ICIR, monthly return and Sharpe;
in simulation it beats regression and NDCG baselines specifically under low
signal-to-noise and heavy-tailed noise.
- **EVIDENCE-GRADE: medium.** Evaluated on finance metrics including Sharpe, not on
  MAPE/RMSE, and the low-SNR/heavy-tail simulation is the right stress test for equity
  returns. Marked down hard because the abs page discloses **neither the universe nor
  the date range** for the "real market data" experiments, and transaction costs are
  not mentioned at all.
- Doing-right (verified): the repo already evaluates by rank IC, and does it *better*
  than the paper's own summary statistic. `backtest_ccc.py:258` builds a per-month
  Spearman IC series; the comment at `:255-257` gives the reason for preferring
  full-cross-section IC over a quintile spread ("a quintile spread throws away the
  middle 60%"). `pead_liquidity_study.py:222,226` computes and reports rank IC with a
  t-stat. Crucially, `backtest_ccc.py:288-300` reports mean IC **with a
  non-overlap-corrected t-stat, independent-sample count and hit rate** — strictly
  more informative than the paper's ICIR, since ICIR ≈ t/√n and hides both n and the
  overlap correction. No action needed here; the register should not log this as a gap.
- **Gap, but NOT actionable at this scale.** The training half has no target: the repo
  has no learned cross-sectional ranker to re-fit — its scores are rule-based
  (Piotroski/Darvas/Coffee-Can composites), and the one learned component,
  `factor_learning.py:88`, is a `LassoCV` regression on factor returns, not a
  stock-level ranker. Adopting LambdaRankIC would mean *building* an ML ranker first,
  which is a different project from a rule-based EOD screener. Logged for the record;
  nothing queued.
- Action queued: none.

### Weak/off-scope, one line each (triaged, not deep-read)
- **2604.20204** (Li & Zhang, "ACT: Anti-Crosstalk Learning for Cross-Sectional Stock
  Ranking") — graph deep learning with a temporal-decomposition encoder on CSI300/CSI500;
  headline is a bare "up to 74.25% improvement" with no cost modelling and no disclosed
  date range, and it needs GPU training the pipeline does not have. Off-scope on compute
  and universe both; 1809.09441 already occupies this branch of the register.
- **2510.14156** (Kwiatkowski & Chudziak, "On Evaluating Loss Functions for Stock
  Ranking") — legitimate benchmark of pointwise/pairwise/listwise losses on S&P 500, and
  it is judged on ranking rather than MAPE/RMSE, but every finding is a *training-loss*
  choice and this repo trains no neural ranker. No transferable mechanism; abs page also
  discloses no date range and no cost treatment.
- **2503.09647** (Leveraging LLMs for Top-Down Sector Allocation) — surfaced by the
  ranking query but is an LLM-agent sector-allocation paper; per-query LLM spend profile
  this register has already rejected twice (2412.20138, 2603.16365). Discard.
- **"Building Cross-Sectional Systematic Strategies by Learning to Rank"** (Poh et al.,
  *Journal of Financial Data Science*, pm-research.com) — paywalled, no free preprint
  reachable from the search result, so it could not be verified against the
  no-fabrication rule. Not registered; note it as a possible re-check if an open version
  appears.

## Added 2026-08-27 (daily task, Thursday gap query: transaction-cost-aware factor evaluation)

Citation-following from hub 2605.19337 returned **no new candidates** for the fourth
consecutive day — Semantic Scholar still lists exactly 3 citing papers (2607.19453,
2607.04958, 2606.08285), all already registered. Entire day's yield from the weekday
gap query. Note for future runs: this edge has been dry since 2026-08-24; consider
demoting it to a weekly check rather than a daily one.

### Baldi-Lanfranchi (2024) — Transaction-cost-aware Factors (EPFL / Swiss Finance Institute, 17 May 2024)
Not on arXiv; fetched as PDF from afajof.org (AFA submission copy). Standard factors
are transaction-cost-*unaware* (TCU): they rebalance fully to the target weights each
period regardless of cost. TCA factors instead rebalance only *partially* toward the
target at an optimized trading intensity τ — a weighted average of last period's
allocation and the target factor. Trading intensity is factor-specific, driven by
characteristic persistence, characteristic/cost correlation, and risk-premium decay rate.
- **EVIDENCE-GRADE: medium-strong.** Headline metric is the net squared Sharpe ratio
  (Barillas–Shanken Sh² criterion), costs are the entire subject rather than an
  afterthought, and results are reported both in-sample and out-of-sample with
  factor-level spanning regressions. Marked down from strong because the pages fetched
  disclose neither the sample period nor the asset universe — that is a limit of what
  was read, not a claim the paper omits them.
- Numbers, verbatim from the fetched pages: net Sh² improves 28%–150% (abstract says
  "up to a factor of 2.5") switching TCU→TCA within a model. All 11 TCA factors produce
  positive net alphas on their TCU counterparts, 6 significant; TCU factors leave
  negative or insignificant intercepts on the TCA versions. Momentum is the worked case:
  gross premium 0.64%/mo (highest of the set), TCU trading costs 63bps/mo, net premium
  0.01%/mo — i.e. costs eat essentially all of it. TCA momentum incurs 30bps/mo,
  raising net return **22-fold** and annualized net Sharpe by 0.19. The Barillas–Shanken
  six-factor model has the highest gross Sh² (2.25) but its Sh² **drops 80% after costs**,
  ranking second-worst; TCA construction nearly doubles its net Sh².
- **Directly relevant to this repo's own result.** The 2026-08-23 round measured
  momentum 12-1 at **-14.11% vs bench (IN, n=3,541)** and **-15.08% (US, n=17,606)** and
  logged it as "no live edge." This paper is the specific claim that a chunk of
  momentum's net-of-cost failure is a *construction* artifact rather than an absent
  premium — TCU momentum is exactly the full-rebalance form the repo tested.
- Doing-right (verified): the repo does deduct costs rather than report gross —
  `walk_forward_backtest.py:156` (`TRANSACTION_COST = 0.002`, "0.2% round-trip
  (STT + brokerage)") and `backtest_screeners.py:176` (`TRANSACTION_COST_PCT = 0.002`),
  with net returns computed at `backtest_screeners.py:266`. Per-market round-trip bps
  are modelled separately at `confusion_matrix_eval.py:33`. So the repo is on the *net*
  side of the paper's four-way split, not the gross side it criticises.
- **Gap (verified): no trading-intensity or partial-rebalancing concept exists.**
  `grep -rniE 'trading_intensity|partial.rebal|rebalance_intensity|turnover_penalt|turnover.aware|cost.aware' --include='*.py'`
  over `code/python_files/` returns **zero non-vendored hits** (the only matches are
  inside `.venv/.../torch/fx/experimental/`). The repo's sole cost-mitigation mechanism
  is a *rebalancing-frequency* heuristic — the watchlist mailer's >5-session eviction /
  >15-session purge — which is precisely the alternative footnote 1 of this paper argues
  is dominated by intensity optimization, on the grounds that frequency reduction throws
  away higher-frequency characteristic changes while intensity optimization keeps the
  full information set and only damps the speed of adjustment.
- **Scope honesty: mostly NOT actionable as written.** TCA factors require a portfolio
  weight vector and an optimizer over τ. This repo is a signal-only, long-only EOD
  screener with no portfolio-construction or execution layer, so "implement TCA factors"
  is out of scope. What *is* in scope is the reduced form — measuring how much of the
  momentum screen's gross-to-net gap is churn rather than absent premium.
- Action queued: item 16 (scoped to the reduced form, not the full method).

### 2604.07880 — The Corporate Bond Factor Replication Crisis (Dickerson, Robotti & Rossetti, 2026-04-09)
Applies a bias-correction framework to a 108-signal "factor zoo" across nine thematic
clusters, Aug 2002 – Dec 2024 (269 months). Two named inflation sources: (i) a
**correlated errors-in-variables bias** — the same noisy transaction price enters both
the sorting signal and the return denominator, creating mechanical correlation; and
(ii) **asymmetric ex-post return filtering** — winsorization/filtering thresholds
computed from the *full sample* rather than from data available at portfolio formation.
- **EVIDENCE-GRADE: strong on method, medium on transfer.** Long disclosed period,
  disclosed universe, and — rare — a Benjamini-Hochberg FDR correction across all
  specifications rather than per-factor t-stats. Of 432 specifications, 119 had
  nominally significant premia (t>1.96); after correction only **26 (6.0%)** survive.
  Open-source artifacts released (Open Bond Asset Pricing, error-corrected TRACE).
  Downgraded on transfer only because the universe is corporate bonds — but both
  mechanisms are properties of *noisy prices*, not of bonds, so they carry to illiquid
  equities, which is where this repo's one validated edge lives.
- Quantified magnitudes: short-term reversal's premium falls from **−0.99% to −0.09%
  monthly** (>90% of the documented effect is bias). Value factors carry 36–45bps of
  bias, spread-based factors 15–18bps/month. The 6-month momentum premium of 0.30%/mo
  is **entirely** attributable to asymmetric ex-post winsorization — zero without it.
- **Doing-right #1, and it is the structural defence against mechanism (i):**
  `backtest_screeners.py:293` sets `entry_idx = signal_idx + 1` — entry is the close of
  the bar *after* the signal, with the signal-bar close preserved separately as
  `signal_price` (`:312-313`). The rationale is spelled out at `:275-285` (the 2026-08-22
  look-ahead fix). Because the sorting signal and the return denominator are drawn from
  **different bars**, the mechanical price-noise correlation the paper describes cannot
  form in this repo's screener backtests. This is a genuinely stronger position than the
  bond literature the paper indicts, and it was reached for a different stated reason
  (fill obtainability), which makes it a real independent convergence rather than luck.
- **Doing-right #2, against mechanism (ii):** `rloo_rescore.py:291` `winsorize_xs()`
  clips to **each day's own cross-section** — `np.nanpercentile(..., axis=1, keepdims=True)`
  at `:309-310` — and the docstring at `:301-303` records that it is applied identically
  to picks and peers so it "cannot move the advantage in a chosen direction." That is
  the point-in-time, symmetric form the paper says the bond literature failed to use.
- **Gap (verified): full-sample winsorization thresholds survive in three other places.**
  `factorial_screener_analysis.py:97-107` `winsorize()` takes `s.quantile(0.01), s.quantile(0.99)`
  over the **entire pooled series**, and it is still live at `:111`
  (`y = winsorize(df[horizon])`) feeding the OLS at the heart of the factorial screener
  analysis. Its own docstring at `:13-17` records that the primary split defence moved
  upstream into `factorial_screener_test.py` (exclusion, not winsorization), leaving this
  as "a light secondary guard" — but light or not, the thresholds are computed from data
  the formation date would not have had. Same pattern at
  `train_ppo_factor_weights.py:132-133` (`out["ret"].quantile([0.01, 0.99])` pooled, then
  `.clip()`), and `factor_zscore_panel.py:45-46` states outright that it adopts the
  "same convention as factorial_screener_analysis.py's winsorize()".
- **Precision caveat, stated so it is not overread later:** the repo's winsorization is
  *symmetric* (1st and 99th percentile both clipped), whereas the paper's fatal case is
  *asymmetric* filtering. The repo therefore has the milder member of the same family.
  The transferable hazard is the **full-sample threshold**, not the asymmetry, and the
  queued test should be read as measuring that and nothing more.
- Action queued: item 17.

### Weak/off-scope, one line each (triaged, not deep-read)
- **2602.00080** (Sheppert, "The GT-Score") — composite objective blending performance,
  significance, consistency and downside risk; but the headline metric is a
  "generalization ratio" (validation return / training return) on only **50 S&P 500
  names**, cost treatment undisclosed, and `deflated_sharpe.py` already gives this repo
  the multiple-testing half properly. Not deep-read.
- **2507.17211** (EFS: Evolutionary Factor Searching with LLMs) — does apply 0.1%/0.2%
  cost settings, but carries the per-query LLM spend profile this register has now
  rejected four times (2412.20138, 2603.16365, 2604.26747, 2503.09647). Discard.
- **2606.00060** (ML Bitcoin trading under transaction costs) — genuinely cost-aware and
  walk-forward, but crypto; same off-scope universe verdict as 2607.19453. Discard.
- **2603.21672** (Mislearning of Factor Risk Premia under Structural Breaks) — misspecified
  Bayesian learning framework; theoretical, no traded strategy and no cost treatment.
  Off-scope for technique extraction.
- **2601.10279** (Feng, Lan, Wang & Zhang) — resurfaced by today's query; **already
  registered 2026-08-25**, dedup hit, not re-triaged.

## Added 2026-08-28 (daily task, Friday gap query: point-in-time fundamentals / survivorship bias)

Citation-following from hub 2605.19337 returned **no new candidates for the fifth
consecutive day** — Semantic Scholar still lists exactly 3 citing papers (2607.19453,
2607.04958, 2606.08285), all already registered. **Acting on yesterday's note: this
edge should now be checked weekly (Mondays), not daily.** It has been dry since
2026-08-24 and costs a fetch every run for nothing.

**No paper was deep-read today and nothing was queued.** Three genuine search attempts
returned six candidates, every one of which fails triage — five of them because the
Friday query's 2026 literature on "point-in-time" has been almost entirely captured by
the LLM-benchmarking community, which is off-scope here for a reason worth recording
once (below) so future Friday runs stop re-triaging the same branch.

### Structural finding: the LLM look-ahead branch has zero surface area in this repo
The register has now rejected LLM-centric papers six times (2412.20138, 2603.16365,
2604.26747, 2503.09647, 2507.17211, and today's batch), but always on the **cost**
profile. Today's query surfaced a different sub-literature — *parametric* look-ahead
bias, i.e. an LLM trained after the fact already knowing how the period turned out
(2605.24564, 2601.13770). That hazard is not about cost at all, so it deserved a real
check rather than the standing cost rejection.
- **Verified, not assumed: there is no LLM anywhere in the signal path.** The only
  natural-language component is `sentiment_pipeline.py`, and it scores with VADER plus
  a hand-edited finance lexicon — `:66-67` instantiates `SentimentIntensityAnalyzer`,
  `:68-79` patches the lexicon, `:134` documents the scoring contract ("VADER with
  finance lexicon boost"). A fixed lexicon has no training corpus and therefore no
  future knowledge to leak. `grep -niE 'openai|anthropic|claude|gpt-|llm|llama'` over
  that file returns zero hits.
- The two learned components are fit on this repo's own panels (`factor_learning.py:88`
  LassoCV, `train_ppo_factor_weights.py`), so their leakage risk is the ordinary
  temporal-split kind already tracked as queue items 6/10/14 — not the parametric kind.
- **Verdict: not a gap, and not merely "too expensive" — structurally inapplicable.**
  Future runs should skip this branch on sight unless an LLM enters the signal path.

### Doing-right confirmation: survivorship (the other half of the Friday query)
Checked directly rather than trusted from the hub entry's one-line summary. The repo
does not merely disclose survivorship, it **bounds** it:
- `band_sip_backtest.py:20` — "DELISTING IS MODELLED, NOT DROPPED, AND IT DECIDES THE
  ANSWER", with 31.9% of the relevant names affected, and `:186` reports the SIP
  outcome under **both survivorship bounds** rather than picking one.
- `price_band_migration.py:23` — "SURVIVORSHIP IS REPORTED, NOT SILENTLY DROPPED."
- `backtest_liquidity_forward.py:172-175` — delisting-aware exit: a stock with no bar
  at t+63 exits at its last real close and is flagged `delisted_in_window`, rather than
  being inner-joined out of existence (`:43-45` gives the rationale).
- `sweep_piotroski_plus.py:40-45` — states the *residual* limitation honestly
  (screener.in serves listed companies only, so that particular route is an upper bound).
Nothing to queue: this is a stronger position than the papers surfaced today assume of
a personal pipeline.

### Weak/off-scope, one line each (triaged, not deep-read)
- **2601.13770** (Benhenda, "Look-Ahead-Bench: a Standardized Benchmark of Look-ahead
  Bias in Point-in-Time LLMs for Finance", 2026-01-20) — best-matched paper to today's
  query and it does release code (github.com/benstaf/lookaheadbench), but the abs page
  discloses neither universe nor date range, no cost treatment, and the hazard it
  measures cannot exist here per the VADER verification above. Not deep-read.
- **2605.24564** (Li, Wang & Ma, "Summoning the Oracle to Slay It", 2026-05-23) —
  proposes FinCAD, an inference-time Context-Aware Decoding fix for parametric
  look-ahead. Judged on returns/Sharpe/Spearman rather than MAPE, which is to its
  credit, but the universe is **five mega-cap equities**, costs are unmentioned, and
  the mechanism requires an LLM to decode from. Same inapplicability verdict.
- **2606.29771** (Qu & Chen, "CLQT", v1 2026-06-29 / v2 2026-08-02) — genuinely
  cost-aware (transaction *and* financing costs are a named pillar) and its diagnostic
  claim is real: the capability leader is not the Sharpe leader, because "the market
  path dominates a period's return." But it benchmarks **LLM portfolio-management
  agents**, and its transferable point — evaluate across distinct regimes rather than
  on one path — is already this repo's practice (`build_regimes.py`,
  `regime_tag_panel.py`, `strategy_regime_survival.py`, and the vs-benchmark reporting
  in the 2026-08-23 round). PDF fetch returned unparseable binary, so the universe,
  date range and cost figures could not be verified; graded on the abs page alone and
  **not** written up as though the full text had been read.
- **2605.30464** (Noguer i Alonso, "Distributional Portfolio Optimization", 2026-05-28)
  — surfaced for its point-in-time reconstitution record, but the abs page carries no
  detail on it, the backtest is K=25 DJIA, costs are unmentioned, and its own headline
  is a **negative** result (equal-weight, no-view Black-Litterman and Ledoit-Wolf
  shrinkage all beat every distributional method on Sharpe). Portfolio-construction
  scope this signal-only pipeline does not have. Discard.
- **2605.31201** (Point-in-Time Financial RAG with Frozen LLMs) — LLM retrieval
  architecture; same structural inapplicability, plus per-query spend. Discard.
- **2604.09060** ("Taming the Black Swan", momentum-gated hierarchical optimisation) —
  surfaced by the first query but off today's theme entirely; left untriaged for budget,
  not assessed. Noted here only so it is not counted as reviewed.

---

## Added 2026-08-29 (daily task, Saturday gap query: correlation-matrix eigenvalues / regime / effective dimension)

Note on dedup: the Saturday theme was already mined hard on 2026-08-23 (2604.17251 ORCA,
2608.09641 lower spectrum) with three weak entries (2601.06090, 2601.08571, 2507.14325).
Today's search returned those four again plus three genuinely new IDs. Only one passed.

### 2507.01918 — End-to-End Large Portfolio Optimization for Variance Minimization with Neural Networks through Covariance Cleaning (Bongiorno, Manolakis & Mantegna, v1 2025-07-02, v2 fetched)

Passed triage on evidence hygiene, which is the best in today's batch: out-of-sample
Jan-2000–Dec-2024, up to 1,000 US equities, headline metrics are Sharpe / realized
volatility / max drawdown (not MAPE), and the execution layer explicitly models market
orders at the auctions, empirical slippage, exchange fees and leverage financing.

**Doing-right:** the paper reports turnover next to variance — its own NN runs ~112%
turnover per 5 days at 2.9x gross leverage against QIS's 44% — i.e. it publishes the
number that would kill it net of cost rather than burying it. That is the standard this
repo's own estimator comparisons should meet.

**Gap (verified):** the repo builds its covariance matrices from the raw sample
estimator with no eigenvalue treatment at all. `portfolio_builder.py:217` is
`cov = R.cov().values * TRADING_DAYS`, fed straight into `port_var = lambda w: w @ cov @ w`
at `:222`; `mutual_fund_theorem.py:107` is the same line. Shrinkage in this repo is
applied only to *expected returns* — `_expected_returns()` at `portfolio_builder.py:190-200`
is James-Stein toward the cross-sectional mean — never to Σ. `mutual_fund_theorem.py:156`
already prints a warning naming the exact missing piece ("without shrinkage (Ledoit-Wolf)
or hard position constraints") when half-sample turnover exceeds 0.5, so the gap is one
the repo has already diagnosed on itself and not yet closed.

**Not adoptable:** the neural estimator itself. 240 independently trained BiLSTMs
(10 runs x 24 years, 100 epochs x 500 steps), and its edge over QIS is Sharpe 1.011 vs
0.942 frictionless — bought with 2.5x the turnover. No GPU here, and a long-only EOD
screener cannot pay that churn. The transferable content is the paper's *baseline table*,
not its model.

**Action queued:** item 18 — swap raw `R.cov()` for Ledoit-Wolf/QIS shrinkage at the two
sites above and measure, with turnover reported alongside realized volatility. The paper's
own "Average Oracle" baseline (eigenvalues estimated once on 1990–2000, frozen across the
whole 2000–2024 test window) reaches Sharpe 0.907 against QIS's 0.942 — within 4% at zero
re-estimation cost, which is the shape of thing this pipeline can actually run.

### Weak/off-scope, one line each (triaged, not deep-read)

- **2608.26990** (DSA: Evidence-Aware LLM-Agent Orchestration for Multi-Market Stock
  Research, Zhu & Shi, 2026-08-27; surfaced by citation-following from hub 2605.19337) —
  architecturally the closest thing yet published to this repo (six regional market paths,
  fifteen bundled strategy skills), but the authors state plainly that their 1,457 passing
  contract tests establish "implementation conformance for the tested software contracts,
  not superior report quality, forecasting accuracy, or investment returns." No returns,
  no Sharpe, no date range, no costs. Zero evidence content by this register's bar; of
  interest as a design comparison only, never as a citation. Not deep-read.
- **2608.26128** (Gómez Morales, "Analysis of the Principal Components of Correlation
  Matrices of S&P 500 Financial Data from an Econophysics Perspective", 2026-06-23) —
  430 S&P 500 names, k-Means over the largest eigenvalue and dominant-eigenvector entries,
  transition matrices and inverse participation ratios. Self-described as "descriptive
  rather than predictive": no trading evaluation, no costs, no returns. Every mechanism it
  offers is already covered by 2604.17251's spectral descriptors and queue item 9. Discard.
- **1102.1339** ("Correlation of financial markets in times of crisis", 2011) — surfaced by
  the same query; pre-dates all three spectral papers already logged and adds no mechanism
  they lack. Not fetched, so nothing is asserted about its contents beyond the title;
  logged here only so it is not re-surfaced as unreviewed.

## Added 2026-08-31 (daily task, Monday gap query: CPCV / purging / embargo)

Dedup note: this theme already had a dedicated four-agent round on 2026-08-23 (see
"CPCV / embargo — dedicated research round"), so the query was re-aimed at the adjacent
question that round left open — *how do you grade a backtest after the purging is done*.
Citation-following from hub 2605.19337 returned exactly four citing papers
(2608.26990, 2607.19453, 2607.04958, 2606.08285), **all four already in the register**;
it produced no new candidates today. Both arXiv APIs (Semantic Scholar, export.arxiv.org)
returned HTTP 429 for the whole session, so search fell back to WebSearch + direct abs
fetches.

### 2608.23808 — Equity Strategy Backtesting: Luck or Edge? The MinervaScore as a Statistical Robustness Grade (Santoni, Jouanne & Scullin, v1 2026-08-24, v2 2026-08-26, q-fin.ST)

Passed triage on the strength of what it does with its own negative result. The paper
proposes a composite post-selection grade over five gates — Deflated Sharpe Ratio,
Probability of Backtest Overfitting, Superior Predictive Ability, Minimum Track Record
Length, and a regime-stability diagnostic — calibrated on 359,062 production backtest
records, and then reports that on pre-registered unseen real-market data the score
**showed no significant forward relationship** (Spearman rho_s = 0.013, one-sided
permutation p = 0.40). It also states that its improvement over a corrected DSR-alone
baseline is "modest".

**Doing-right:** it pre-registers the real-market test, publishes the null, and refuses
the obvious overclaim — the authors present the score "as an auditable validation and
reporting layer, rather than as evidence of demonstrated real-market predictability."
The AUROC 0.989 headline is explicitly confined to synthetic data with known ground truth.
That separation of synthetic-discrimination from real-market-prediction is the exact
discipline the weak entries in this register fail.

**Gap (verified, and the reason this entry exists):** of the five gates, this repo
implements one, mislabels a second, and has none of the other three.
- DSR — **real.** `deflated_sharpe.py:42` (`expected_max_sr`, López de Prado E[max SR])
  and `:52` (`dsr`, with skew/kurtosis denominator). Driven at `:61-93` over
  `reports/profitability_optimizer.csv` per market x regime, gate at DSR >= 0.95.
- PBO — **cited but not implemented.** `walk_forward_backtest.py:1086` carries the
  citation "Source: Bailey et al. (2014) — 'Probability of Backtest Overfitting.'", but
  the function it documents, `overfitting_report()` at `:1082`, computes
  `decay = (train - val)/abs(train)*100` from mean Sharpe per split (`:1094-1096`) and
  buckets it with hardcoded thresholds — HIGH >50%, MEDIUM >20% (`:1111-1116`). That is a
  Sharpe-decay heuristic. PBO is the CSCV quantity: the fraction of train/test partitions
  in which the in-sample-best configuration ranks below the out-of-sample median. The two
  are not the same statistic and the citation should not be attached to this function.
- SPA (Hansen), MTRL, regime-stability gate — **absent.** Grep over `*.py` for
  `superior predictive ability|minimum track record|min_trl|track_record|hansen` returns
  no implementation; the only `PBO`/`SPA` string hits are `cite_check.py:58` (an acronym
  allowlist) and `smallcap_screener.py:259` (an unrelated single-page-app error string).

**Second verified weakness, found while checking the above:** the trial count fed to the
DSR is the narrow one. `deflated_sharpe.py:70` builds `trials_sr` from only the rows of
`profitability_optimizer.csv` matching that market x regime — the generated report at
`:100` describes it as "best of 10 factors" — while `T` at `:77` is `best["n"]`, formation
weeks. Neither number accounts for configuration choices made elsewhere in the pipeline,
and nothing anywhere checks that `T` is large enough for the estimate to mean anything.
MinervaScore's opening sentence is precisely this failure: standard summaries "do not
record how many candidates were tried... or whether the available history is long enough
to support the result."

**Not adoptable:** the composite score itself. It is calibrated on 359k proprietary
backtest records this repo does not have, its component weights are fitted to that
population, and its own real-market test came back null — adopting the 0-100 display
would import a number with no demonstrated forward content. The transferable content is
the **gate list**, not the aggregation.

**Action queued:** items 19 (MTRL as a gate on the existing DSR verdicts) and 20 (replace
the mislabelled Sharpe-decay heuristic with real CSCV PBO, and fix the citation either way).

### 2512.12924 — Interpretable Hypothesis-Driven Trading: A Rigorous Walk-Forward Validation Framework for Market Microstructure Signals (Gagan Deep, Akash Deep & William Lamptey, 2025-12-15, q-fin.TR)

Passed triage as a **negative result worth keeping**, not as a technique source. 100 US
equities, 2015-2024 (2,475 days), walk-forward W=252 / H=63 / step=63 giving K=34 folds,
explicit cost model (`$1` fixed commission + 5 bps slippage, execution at next day's open).
Result: 140 trades, 0.55% annualized return, Sharpe 0.33, max drawdown -2.76%, beta 0.058,
aggregate p = 0.34, and 14 of 34 folds profitable.

**Doing-right:** publishes the null in the abstract, declines to dress it up, and states
that it reports all tests "without adjusting for multiple comparisons to maintain
transparency about statistical limitations" rather than quietly omitting the adjustment.
It also reports **fold-level profitability (41%)** next to aggregate Sharpe — a per-period
hit rate that survives a lucky single fold, which aggregate Sharpe does not.

**Relevance (verified):** four of the five hypothesis families it tests map directly onto
signals this repo already computes in `strategy_regime_survival.py:137-142` — `revert`
(mean reversion), `breakout`, `mom_st`/`mom126` (flow momentum), `trend`. The paper's
conclusion is that these patterns, derived from **daily OHLCV**, lack the information
arrival to pay: "daily OHLCV-based microstructure signals require elevated information
arrival and trading activity." This repo is a daily EOD OHLCV pipeline. The read-across is
direct, and the honest use of the paper is as a prior against expanding the
microstructure-signal family, not as a recipe.

**Its own weaknesses, stated plainly:** it computes no deflated Sharpe (it cites Bailey &
López de Prado in the literature review and then reports a raw Sharpe), applies no
multiple-testing correction across 5 hypothesis types x 100 securities, and its
walk-forward has **no purge or embargo gap** between the 252-day train and 63-day test
windows — the same omission already tracked here as queue item 6. So it is a useful null,
not a methodological exemplar.

**Action queued:** none. The actionable content is a do-not-build prior plus the
fold-level-profitability reporting habit, which is folded into item 20 rather than queued
separately.

### Weak/off-scope, one line each (triaged, not deep-read)

- **2511.12490** (Mainak Singha, "Discovery of a 13-Sharpe OOS Factor: Drift Regimes
  Unlock Hidden Cross-Sectional Predictability", 2025-11-16) — EVIDENCE-GRADE: weak, and a
  near-perfect specimen of the disease 2608.23808 describes. Claims out-of-sample Sharpe
  "above 13" and 158.6% annualized at 12.0% volatility on S&P 500 names 2004-2024, with
  R-squared below 3% to standard risk factors. The abs page **does not disclose how many
  signal variants were searched** before this combination (value + short-term reversal,
  activated only when a stock shows >60% positive days in a trailing 63-day window) was
  selected — and a regime gate defined by a threshold on a trailing window is exactly the
  kind of parameter that gets tuned. The 1,000 randomization trials it does report test
  the sampling distribution of the chosen rule, not the selection process that produced it.
  A Sharpe of 13 on daily US equities is not a finding, it is a diagnostic. Not deep-read;
  logged here as the worked example for items 19-20.
- **2606.09025** (Zheli Xiong, "Continuous Cash-Overlay Filters for a Static
  Growth-Defensive Risk Sleeve", 2026-06-08, rev 2026-06-14) — 2 allocations (a risky ETF
  sleeve vs cash) over 2017-2026, headline 18.83% CAGR vs 16.62% buy-and-hold with max
  drawdown cut from -33.59% to -18.05%. No transaction-cost model stated. A single-sleeve
  tactical overlay on a 9-year window that contains one crash; the walk-forward label in
  the title does not offset a 2-asset universe. Off-scope for a cross-sectional screener.
- **2607.06117** (Zheli Xiong, "Relief-Gated Relative Rotation for QQQ-DIA Allocation",
  2026-07-07) — same author, same shape: **2 ETFs**, Sharpe 0.94 (2018 start) / 0.87
  (2022 start), and to its credit it does model 10 bps one-way cost — which is how you can
  see that it runs **354-506% annualized turnover**. Two instruments and a five-fold churn
  rate is not a result this pipeline can use. Off-scope.

---

## Added 2026-09-01 (daily task, Tuesday gap query: factor redundancy / spanning tests)

Citation-following from hub 2605.19337 returned the same four citing papers as the last
two runs (2608.26990, 2607.19453, 2607.04958, 2606.08285), **all already in the
register** — the hub's citation graph is exhausted for now. The Tuesday query was last
run 2026-08-25 (2601.10279, 2111.05072), so it was re-aimed from *which factor model
wins a spanning test* to *are my factors redundant through terms a correlation matrix
cannot see*. Five new candidates, two deep-read.

### 2503.23501 — Higher-Order Asset Pricing Factors via Forward Selection Fama-MacBeth Regression (Borri, Chetverikov, Liu & Tsyvinski, v1 2025-03-30, v2 2026-03-24)

EVIDENCE-GRADE: strong. 555 months (1973-10 to 2019-12), 484 characteristic-managed
portfolios, plus 148 zoo factors from Jensen, Kelly & Pedersen (2023) as the comparison
set. Metric is cross-sectional R-squared reported **both in- and out-of-sample**, not a
price-level error. No transaction-cost model, but it is an asset-pricing test rather than
a strategy backtest, so cost is not the load-bearing omission it would be for a signal.

Method: from 6 base factors (FF5 + momentum) build 57 candidates — 6 squares, 6 cubes,
15 pairwise products f_i·f_j, 30 mixed f_i·f_j². Forward-select by whichever candidate
most raises the Fama-MacBeth second-stage cross-sectional R², stopping when the next
addition buys less than 1 percentage point. Seven terms are selected (2 squares,
5 interactions). In-sample R² rises 31.2% → 58.7%; out-of-sample 8.9% → 14.8%. Only
**7 of 148 zoo factors stay significant at 5%** once the higher-order terms are in.

- Doing-right: nothing here yet — this is a clean gap.
- Gap (verified): the repo's redundancy diagnosis is **linear-only, on both sides**.
  `research/factor_redundancy.py:15-16` takes a *Pearson* correlation of the 10-factor
  matrix and eigendecomposes it, reporting participation ratio 4.92/10 (IN) and 4.53/10
  (US). The model that consumes those factors is equally linear: `factor_learning.py:43`
  `build_xy()` stacks the 10 raw `FACTORS` (`:37`) and nothing else, and `:88` fits
  `LassoCV` on that matrix. So a pair that is linearly near-orthogonal but related
  through a square or a product is invisible to the measurement *and* unavailable to the
  model — the same blind spot twice. `grep -rniE 'fama_macbeth|FamaMacBeth'` over the
  repo returns **zero implementations**; the only hit is a citation string in
  `paper_claim_audit.py:26`.
- Why it matters here specifically: the repo's 10 factors all come off ONE weekly close
  panel (`factor_learning.py:43` → `factor_library(close)`), which is exactly the
  condition under which the paper's result bites — a small base set whose apparent
  variety is higher-order structure, not new information. A PR of 4.92 measured
  linearly is an *upper* bound on independence, not a lower one.
- Action queued: item 21.

### 2602.20856 — Stochastic Discount Factors with Cross-Asset Spillovers (Avramov & He, 2026-02-24)

EVIDENCE-GRADE: mixed — excellent disclosure, unusable headline. Monthly CRSP
NYSE/AMEX/NASDAQ, 1963-01 to 2023-12, out-of-sample from 1973-02 on rolling 10-year
(120-month) windows, 138 firm-level signals across 13 themes from Jensen et al. (2023),
tested on 138 spread and 544 bivariate-sorted portfolios. Period, universe and window
are all stated — better than most of what this register sees.

Then the headline: annualised out-of-sample Sharpe **2.21** (spread) and **3.32**
(bivariate) versus 0.60 for self-predictive benchmarks, moderating to 1.58/2.21
post-2000. These are **gross**. The paper implements zero-cost leverage-two long-short
books rebalanced monthly and reports no turnover figure and no cost deduction anywhere.
A 3.32 Sharpe on monthly-rebalanced 544-portfolio long-short with costs unmeasured is
not a number this pipeline can borrow; the *method* is still worth taking.

Method worth taking: the estimation is not a neural net. It recasts max-Sharpe as a
managed-portfolio problem and solves it as a **ridge-penalised Britten-Jones (1999)
regression** — regress a vector of ones on the managed-portfolio return matrix, with λ
chosen by cross-validation — giving closed-form tangency weights.

- Gap (verified): the repo has no tangency/max-Sharpe factor combination at all.
  `grep -rniE 'ridge|tangency|britten'` finds ridge used only as a per-stock price
  ML engine (`full_us_market_scan.py:83`), and `fund_implementability.py:18` explicitly
  disclaims the tangency question. Factor weights come from `LassoCV`
  (`factor_learning.py:88`, an IR-agnostic MSE fit) and from PPO
  (`train_ppo_factor_weights.py`), with **no closed-form baseline between them**.
- Doing-right: the repo's own cost discipline is ahead of this paper's — queue item 16
  already treats net-of-cost churn as the question, which is precisely what a 3.32 gross
  Sharpe hides.
- Action queued: item 22 (the baseline, not the Sharpe claim).

### Weak/off-scope, one line each (triaged, not deep-read)

- **2604.04430** (Dickerson, Julliard & Mueller, "The Co-Pricing Factor Zoo",
  2026-04-06) — genuinely strong (Bayesian Model Averaging over "18 quadrillion models",
  out-of-sample Sharpe 1.5-1.8), but it prices **corporate bonds** jointly with stocks
  and needs Treasury term-structure controls and a BMA apparatus this pipeline has
  neither the data nor the reason to build. Same lead author as 2604.07880, already in
  the register. Off-scope, not weak.
- **2404.08129** (Borri, Chetverikov, Liu & Tsyvinski, "One Factor to Bind the
  Cross-Section of Returns", 2024-04-11) — the same team's precursor to 2503.23501: a
  non-linear single-factor model r_it = h(f_t·λ_i) + ε_it estimated by sieve, justified
  via Kolmogorov-Arnold. Only **171 assets** across mixed asset classes, and a
  nonparametric link function is a heavier lift than the forward-selection procedure for
  the same underlying insight. Logged as background to item 21; the successor is the
  actionable one.
- **2004.02670** (Arvanitis, Scaillet & Topaloglou, "Spanning analysis of stock market
  anomalies under Prospect Stochastic Dominance", 2020-04-06) — a subsampling +
  linear-programming test for whether anomalies expand the opportunity set *for
  prospect-theory investors*. The abs page discloses no universe, period or metric, and
  the prospect-utility framing does not map onto a screener that ranks on returns.
  Off-scope.

## Added 2026-09-03 (daily task, Thursday gap query: transaction-cost-aware factor evaluation)

Citation-following from hub 2605.19337 returned the **same four citing papers for the
fourth consecutive run** (2608.26990, 2607.19453, 2607.04958, 2606.08285), all already
in the register — the hub's citation graph remains exhausted. The Thursday query was
last run 2026-08-27 (Baldi-Lanfranchi, 2604.07880), so it was re-aimed from *do factor
premia survive their own trading costs* to *how do you report the cost sensitivity
itself* — i.e. breakeven cost as a first-class evaluation metric rather than a fixed
assumed charge. Six new candidates, one deep-read.

### 2603.01820 — Deep Learning for Financial Time Series: A Large-Scale Benchmark of Risk-Adjusted Performance (Saly-Kaufmann, Wood, Peter-Calliess & Zohren, 2026-03-02)

EVIDENCE-GRADE: strong on protocol, off-scope on models. Daily futures across five
asset classes (bonds, commodities, energy, FX, equity indices), 2010–2025, rolling
windows, fully out-of-sample. Headline metric is the **Sharpe ratio**, not a price-level
error — the benchmark is explicitly a position-sizing task, and the paper's own summary
notes that the models that top standard time-series benchmarks are *not* the ones that
top this one. The architectures themselves (xLSTM, PatchTST, VSN+LSTM, state-space
models) are out of scope here: they need GPU training of 50 independent runs per model,
which this pipeline neither has nor wants. The **evaluation apparatus** is the
transferable part.

Doing-right:
- **HAC t-statistics on Sharpe differences.** The paper tests significance with
  "heteroskedasticity and autocorrelation consistent t-statistics", Newey–West style.
  The repo already has exactly this: `newey_west_t()` at
  `code/python_files/rloo_rescore.py:385` ("t-stat of mean(x) with HAC (Bartlett)
  errors"), applied to per-date cohort series at `rloo_rescore.py:444-452` and
  documented in the emitted report at `rloo_rescore.py:514`. Not a gap.
- **Costs charged, not ignored.** Per-market cost assumptions exist at
  `confusion_matrix_eval.py:34` (`COST_BPS = {"IN": 40, "US": 15, "KR": 30, "JP": 25,
  "EU": 30, "CN": 35}`), deducted at `confusion_matrix_eval.py:80` and reported as a
  gross→net precision pair at `confusion_matrix_eval.py:132`. `sector_rotation.py:60`
  and `custom_indices.py:68` carry their own constants. Not a gap.
- **Seed robustness.** The paper re-runs at reduced budget (25 seeds, top 5) against its
  primary spec (50 runs, top 10 by validation loss) and checks rank stability. UNVERIFIED
  as a repo gap and deliberately not queued — the screener has no stochastic training
  loop for seeds to perturb, so the check has nothing to bite on.

Gap:
- **Breakeven cost is computed in one place, and it is not the product.** The paper
  defines it as "the maximum constant friction that specific asset's strategy can endure
  before its cumulative PnL is driven to zero", reported per asset in bps. The repo has
  a breakeven column only in `etf_builder.py:273` (header) / `:288` (the formula
  `be = edge / (tno * ppy) * 10_000 + COST_BPS`), and that variant answers a different
  and stricter question — the cost at which the scheme's *edge over the benchmark*
  vanishes, not at which its PnL vanishes. `quick_reference.py:18,293` is static
  documentation text, not a computation. `grep -rniE 'break[ _-]?even'` across
  `code/python_files/` finds nothing else. So the daily multi-market screen — the thing
  that actually emits the email — charges a fixed assumed cost per market and never
  inverts the question.

Action queued: item 23.

### Weak/off-scope, one line each (triaged, not deep-read)

- **2603.14288** (Huang & Fan, "Beyond Prompting: An Autonomous Framework for Systematic
  Factor Investing via Agentic AI", v1 2026-03-15, v2 2026-04-06) — claims an annualized
  Sharpe of **3.11** and a **59.53% return** from long-short portfolios on
  LLM-self-generated signals, while the abs page discloses no universe size, no sample
  period and no transaction-cost treatment. A self-directed signal-search loop grading
  its own output on US equities is a data-snooping engine; the abstract's answer to that
  is an assertion of "strict empirical discipline" with no reported turnover. This is the
  implausible-headline pattern the triage rule exists to catch. Weak.
- **2511.17462** (Engel, Chen, Polak & Boier, "Scaling Conditional Autoencoders for
  Portfolio Optimization via Uncertainty-Aware Factor Selection", 2025-11-21) — the idea
  is good (rank latent factors by forecast uncertainty, keep the top-k most predictable)
  and the metrics are risk-adjusted (Sharpe, Sortino, Omega), but it requires training a
  high-dimensional conditional autoencoder on a firm-characteristic panel plus Chronos /
  XGBoost-RAPIDS quantile models, and the abstract reports no universe, no period and no
  cost model. Off-scope at this pipeline's scale, not weak on method.
- **2510.19271** (Barunik, Janasek & Sarkany, "Managing Portfolios Across the Return
  Distribution", v1 2025-10-22, v2 2026-06-23) — dynamic allocation targeting a chosen
  region of the payoff distribution; the downside-targeted policy is reported as giving
  both the best left-tail protection and the highest Sharpe. No cost treatment, universe
  or period on the abs page, and the repo's screener ranks candidates rather than running
  a dynamic allocation policy, so there is nothing here to attach it to. Off-scope.
- **2603.15652** and **2512.12420** — surfaced by the Thursday search and **not triaged**;
  the day's triage budget went to the four above. Neither has been fetched, so nothing is
  claimed about either. Left for a future Thursday.

---

## Added 2026-09-04 (daily task, Friday gap query: point-in-time fundamentals / survivorship bias)

Citation-following from hub 2605.19337 returned the same four citing papers for the
**fifth consecutive run** (2608.26990, 2607.19453, 2607.04958, 2606.08285), all already
in the register. Two web searches returned five new IDs; one passed triage and was
deep-read.

### 2608.27734 — What survives honest evaluation? Leakage-safe, search-aware assessment of LLM-driven trading strategy discovery (Eray Gençay, v1 2026-08-27, q-fin.ST)

**Why this one is not covered by the standing LLM rejection.** The 2026-08-28 structural
finding rejects LLM papers because no LLM sits in this repo's *signal path*. This paper's
contribution is not a signal — it is the **evaluation harness placed around a search**,
and this repo does run a search: `profitability_optimizer.csv` picks the best of 10
factors per market×regime, and a dozen `sweep_*` / `backtest_*` scripts have each tried
their own configurations. The LLM is only what generates candidates in the paper; the
grading machinery is agnostic to what produced them. Triaged on that basis, not on the
LLM framing.

Passes triage on every count: headline metric is **Sharpe with Deflated Sharpe and PBO**
(not MAPE/RMSE), universe is **453 US equities plus 39 multi-asset ETFs** (ETFs
2005–2026), design window 2017–2021 / evaluation 2022–2025 for E1–E4 and 2007–2016 /
2017–2025 for E5–E6b, and costs are modelled explicitly: **1bp commission, 2bp spread,
square-root market impact against trailing 21-day dollar volume, and 50bp annualised
borrow on short notional**.

Headline result, and it is a negative one honestly reported: **zero LLM-discovered
strategies survived**. In E3 (100-candidate search, N=102 trials) the agent's best posted
a design Sharpe of 1.69 that collapsed to an evaluation Sharpe of **0.18**, DSR 0.86 —
below the 0.95 certification threshold. The passive benchmarks certify instead:
equal-weight buy-and-hold **DSR 0.97**, SPY **DSR 0.94**. This is worth recording because
it converts this register's six prior LLM rejections — all made on *cost* grounds — into
a *statistical* one made by someone who actually ran the experiment.

- **Doing-right:** point-in-time liquidity. The paper re-selects its tradeable set
  point-in-time and the repo does the equivalent: `backtest_liquidity_forward.py:40`
  states the discipline ("Liquidity, DMA50 and DMA200 at date t use bars <= t only.
  Enforced by SQL"), `:64` sets `LIQ_WINDOW = 60`, `:83` computes the rolling turnover
  window, and `:172-175` exits a delisted name at its last real close rather than
  inner-joining it out. The paper's own survivorship handling is *weaker* than this —
  it fixes the constituent list to current names and argues the resulting bias only
  makes its null conservative.
- **Doing-right:** the cost model. The paper's square-root-impact-plus-participation-cap
  design already exists here — `execution_cost_model.py:8` describes exactly a
  "square-root market-impact model and a participation-rate (%ADV) cap", and
  `build_business_valuation_report.py:285` reports it in use with a 15%-ADV cap. The flat
  per-market constants at `confusion_matrix_eval.py:34` are the weaker path and are
  already queue item 23. Borrow cost on short notional is a real gap but a known one —
  `project_retrospective.py:122` already flags the un-netted short leg — so nothing new
  is queued for it.
- **Doing-right (already queued, not re-queued):** PBO. The paper runs CSCV over 16
  blocks. `walk_forward_backtest.py:1086` cites Bailey's PBO on a function (`:1082`) that
  computes train→val Sharpe decay, which is a different statistic. That mismatch is
  already **queue item 20** and is not duplicated here.
- **Gap — the trial count N is scoped to one sweep, not to the search.** This is the new
  finding. `deflated_sharpe.py:42-49` implements E[max SR] correctly and `:52-58` the DSR,
  but `:71-74` builds `trial_srs` from a single `market × regime` slice of
  `profitability_optimizer.csv`, so `n_trials` written at `:82` is 10 — the factors in
  that one comparison. The paper's N comes from a **persistent ledger of every evaluation
  the search ever performed** (N=102 in E3, against 100 candidates). Every additional
  configuration this repo has tried against the same markets — `sweep_piotroski_plus.py`,
  `backtest_zone_rules.py`, `backtest_pe_anomalies.py`, `backtest_tier_anomalies.py` —
  is a trial that should raise the bar the winner has to clear, and currently does not.
  Since E[max SR] grows with N, the present DSR figures are an **upper bound on
  significance**, not a neutral estimate.
- **Considered and declined:** making look-ahead inexpressible. The paper's neatest idea
  is architectural — a feature registry whose leaky family is excluded from the
  agent-selectable set, with the tool schema and server-side validation deriving from the
  same flag, so invalid constructs never reach evaluation rather than being discouraged.
  That is a control for an agent tool-server with an untrusted caller. Here the caller is
  one person and the discipline is per-script and documented (`backtest_liquidity_forward.py:40`).
  Not queued: the machinery costs more than the failure mode it removes at this scale.
- **Action queued:** item 24 (widen the DSR trial count to a persistent cross-sweep ledger).

### Weak/off-scope, one line each (triaged, not deep-read)
- **2604.09060** (Chakraborty & Singh, "Taming the Black Swan", v1 2026-04-10 / v2
  2026-05-18, cs.CE) — carried forward from 2026-08-28 where it was left explicitly
  untriaged; **now triaged and closed**. AEGIS is Sortino-optimised portfolio
  *allocation* (volatility-adjusted momentum filter + minimax correlation + SLSQP) over a
  2006–2025 walk-forward, but the abs page discloses no universe size, no cost treatment
  and no code or data release, and portfolio construction is scope this signal-only
  pipeline does not have. Discard; future Friday runs need not carry it again.
- **2604.18500** (QRAFTI: An Agentic Framework for Empirical Research in Quantitative
  Finance) — its only on-theme content is preprocessing (delisting returns, share-class
  aggregation, universe screens) sitting downstream of an LLM agent harness. Structurally
  inapplicable per the 2026-08-28 finding. Not deep-read.
- **2602.14233** ("Evaluating LLMs in Finance Requires Explicit Bias Consideration") —
  about bias in grading LLMs, with no signal-path surface here. Discard.
- **2601.07687** (Physics-Informed Singular-Value Learning for Cross-Covariances
  Forecasting) — belongs to the Saturday covariance-cleaning branch already mined on
  2026-08-29 via 2507.01918, not the Friday theme. **Not fetched and not assessed**;
  noted only so it is not counted as reviewed.

---

## Added 2026-09-07 (daily task, Monday gap query: CPCV / purging / embargo)

Dedup note: this is the third Monday pass on the purging/embargo theme (2026-08-23 round,
2026-08-31 grading-after-purging angle), so the query was re-aimed a third time — at
*which* leakage conventions actually cost you anything, rather than at how to purge or how
to grade. Citation-following from hub 2605.19337 returned exactly the same four citing
papers for the **sixth consecutive run** (2608.26990, 2607.19453, 2607.04958, 2606.08285),
all already registered. That branch is dry and should be considered exhausted until the
hub accrues new citations; future Monday runs can skip straight to the web query.

### 2605.23959 — When Alpha Disappears: A One-Switch Benchmark for Decision-Time Leakage in Financial Backtests (Fan Zhang, Zhen Li, Sijia Peng & Yu Chen, 2026-05-12, q-fin.RM)

Passed triage on data shape as much as on rigour: two **daily-OHLCV equity panels** —
S&P 500 constituents, 2010–2024, 439 retained tickers, and CSI 300, 186 tickers — six
model families, yearly tests 2016–2024, proportional costs at 0/5/10 bps with 5 bps as the
headline. That is this repo's exact data regime, which is rare in the leakage literature.

The design is the contribution: rather than declaring a backtest "leaky" or "clean", it
holds the data panel, walk-forward split, model family, horizon, portfolio rule and cost
convention fixed and **toggles one evaluation convention at a time** against a clean
`t+1`-open reference (features from information available by the close of day t, execution
at the t+1 open, labels as open-to-open returns). What comes out is a *ranking of how much
each convention inflates Sharpe*, which is far more useful than a binary verdict.

**The measured result — leakage is highly selective:**

| Convention | Effect | Magnitude |
|---|---|---|
| `TEMP_CENTER` — centered rather than trailing rolling statistics, so a day-t feature can depend on t+3 | **large** | ~+19 to +27 Sharpe (Ridge h=5: +19.43 US, +21.70 China) |
| `EXEC_OPEN` — signal built from the full day-t bar (post-open high/low/close/volume) but executed at the day-t **open** | **large** | ~+5 to +26 Sharpe (Ridge h=5: +21.65 US, +26.16 China) |
| `STRUCT_GRAPH` — symmetric 252-day correlation graphs centered on monthly anchors | weak | mean ~+0.10 Sharpe |
| `NORM_GLOBAL` — normalisation fitted on the full sample instead of the training split | weak | ~+0.07–0.09 Sharpe |
| `EXEC_CLOSE` — close-of-day signal paired with same-day close execution | weak | ~+0.06 Sharpe (US panel) |

**Doing-right:** it states plainly that the benchmark "is diagnostic rather than a claim of
tradable alpha", and the clean-reference Sharpes it reports are modest and believable
(Ridge h=5: 0.68 US, 0.84 China) — a paper that publishes a 0.68 baseline and then shows
its own violations manufacturing a 20-Sharpe strategy is demonstrating the failure mode
rather than selling a result.

**Verified against this repo (greps run today, not carried from prior entries):**

- **`TEMP_CENTER` — clean, confirmed.** `grep -rn "center *= *True" --include='*.py'` over
  `code/python_files/` returns hits **only** inside `.venv/` (networkx, torch, sklearn,
  patsy, polars library source). No pipeline code constructs a centered rolling statistic.
  This is the single largest inflation channel the paper measures and the repo does not
  touch it.
- **`EXEC_OPEN` — structurally impossible here, confirmed.** `grep -n '"Open"'` over
  `backtest_screeners.py`, `walk_forward_backtest.py`, `rloo_rescore.py` and
  `backtest_zone_rules.py` returns **zero hits**. The backtest paths read `Close`,
  `High`, `Low` and `Volume` and never reference the open at all, so the +5 to +26 Sharpe
  channel has no surface area. Worth recording explicitly: an "Open-aware execution model"
  would look like an upgrade and is in fact the entry point to the worst bug in the paper.
- **`NORM_GLOBAL` — clean in the signal path, confirmed.** `StandardScaler().fit_transform`
  on a full sample appears at `cluster_extra_markets.py:61`, `valuation_clustering.py:52`,
  `sector_analysis.py:216` and `pattern_discovery.py:251` — all four are descriptive
  clustering / PCA reporting, not return-generating. In the one place it would matter,
  `ml_signal_engine.py`, `StandardScaler` is **imported at :76 and never instantiated**
  (`grep -n "StandardScaler\|scaler\|\.fit(" ml_signal_engine.py` shows only the import,
  a comment at `:218`, and three bare `model.fit(...)` calls at `:319`, `:441`, `:518`).
  That engine retrains on a rolling `TRAIN_WINDOW = 252` (`:98`) and its one normalised
  feature, `close_norm`, is documented at `:135` as "Z-score normalized close vs 20-day
  window" — trailing, not global.
- **`EXEC_CLOSE` — this is what the repo does, and the paper prices it.** The convention is
  documented in the docstring at `backtest_screeners.py:270` ("Entry = signal bar close.
  Exit = close at T+N") and stamped at `:402` (`"entry_price": curr_close`, where
  `curr_close = closes[i]` at `:385`) and `:439` (`float(closes.iloc[i])`), with the same
  shape in `walk_forward_backtest.py:1362`. The signal and the fill are the **same bar's
  close**. Under the paper's measurement that is the mildest of the five violations,
  ~+0.06 Sharpe on the US panel — but it is one-directional and it is optimistic.

**Gap (the one that survives):** the repo's whole backtest estate assumes it can trade the
close it has just observed. Nothing in the codebase has ever measured what a one-bar delay
costs, and the volume-confirmation branch at `backtest_screeners.py:397` makes the
assumption slightly sharper than it looks — it compares `vols[i]`, the completed day-t
volume, against the trailing 20-day mean, so the decision genuinely needs the full bar,
which is exactly the information set the paper pairs with a t+1 fill rather than a t fill.

**Not adoptable:** the benchmark harness itself. Reproducing a one-switch panel means six
model families × two panels × five toggles × nine yearly tests, and this repo trains no
cross-sectional model that would sit in it. The transferable content is the **ranking**,
which converts "we should probably worry about leakage" into a priced list.

**Action queued:** item 25 (one-bar execution delay as a reported variant, not a
replacement).

### Weak/off-scope, one line each (triaged, not deep-read)

- **2603.13252** (Ursina Sanderink, "When Alpha Breaks: Two-Level Uncertainty for Safe
  Deployment of Cross-Sectional Stock Rankers", 2026-02-24, cs.AI) — EVIDENCE-GRADE: weak,
  and a near miss. Its validation design is the best thing about it and is genuinely on
  today's theme: 109 chronological walk-forward folds, Feb 2016–Feb 2025, a **90-trading-day
  embargo** between training and prediction, and overlapping labels purged — stricter than
  anything in this repo. But the headline metric is **AUROC** (~0.72 overall, ~0.75 in the
  2024 holdout), the abs page discloses **no universe size**, and **no transaction cost
  treatment** appears anywhere, so the paper never converts its ranking quality into
  anything a screener can bank. A DEUP-based epistemic tail-risk cap that the authors
  themselves downgrade to "a tail-risk guard rather than a continuous sizing denominator"
  is not worth deep-read budget against those disclosure gaps. Logged rather than
  discarded: if a v2 adds a universe and a cost model, the 90-day embargo design is worth
  revisiting.
- **2609.00731** (Pan, Ding & Giesecke, "Agentic Empirical Asset Pricing: Methodological
  Foundations", 2026-09-01, cs.AI) — LLM agents doing autonomous factor discovery on two US
  equity panels; no cost treatment stated and no date range on the abs page. Its one
  transferable observation — "no single metric ranks the systems consistently", hence
  multi-axis evaluation — is already the operating assumption behind queue items 19, 20 and
  24. Structurally inapplicable per the standing 2026-08-28 finding that this repo has no
  LLM agent surface. Not deep-read.
- **2602.00080** (GT-Score) — surfaced again by today's search (4-year train / 2-year
  validation / 30-day embargo). **Already in the register**; not re-triaged, listed only so
  the day's candidate count is honest.
- **q-fin.ST recent listing** (2609.04420, 2609.02660, 2608.29692, 2608.29669, 2608.29025,
  2608.30446) — skimmed as a block; none concerns backtest validation, leakage or
  evaluation methodology. Rare-event onset forecasting, forex trade durations, two
  language-model-representation covariance papers, Bitcoin option deep hedging, and neural
  correlation-matrix shrinkage. No candidates.

## Added 2026-09-08 (daily task, Tuesday gap query: factor redundancy / spanning tests)

Third Tuesday pass on this theme (2026-08-25 asked *which factor model wins a spanning
test*, 2026-09-01 asked *are my factors redundant through terms a correlation matrix
cannot see*), so it was re-aimed again — at **whether the repo's existing redundancy
verdict is inferentially valid at all**, rather than at finding more factors.
Citation-following from hub 2605.19337 returned a **new** citing paper for the first time
in seven runs (2609.04917, alongside the same four already-registered ones), so that
branch is no longer dry, only slow. Four new candidates, two deep-read.

### 2601.06499 — Cross-Market Alpha: Testing Short-Term Trading Factors in the U.S. Market via Double-Selection LASSO (Jin Du, Alexander Walter & Maxim Ulrich, v1 2026-01-10, v2 2026-05-21)

EVIDENCE-GRADE: moderate-to-strong on design, weak on costs. S&P 500 large caps,
2002–2022, monthly rebalancing — a real, disclosed, twenty-year universe. A library of
191 short-term price-volume and microstructure signals (built for the retail-heavy
Chinese A-share market) is tested against a control set of **151 fundamental factors**;
17 survive as non-redundant risk premia. The abs page does not state a transaction-cost
treatment, which for *short-term* signals is the disclosure that matters most, so the
17-signal headline should be read as gross. The transferable content is the method, not
the count.

**Doing-right:** the repo already runs L1 selection over its factor set —
`factor_learning.py:88` fits `LassoCV(cv=5, n_alphas=40)` on the train split of the 10
signals at `factor_learning.py:37-38` (`trend, revert, mom126, mom_st, golden_cross,
breakout, lowvol, mom252, qual_mom, def_revert`), per market, walk-forward, and grades
the survivors on an out-of-sample information ratio (`ls_book_ir`, `:62`) rather than on
in-sample fit. Sparse selection *plus* an OOS grade is more than most of this literature
does.

**Gap:** the repo converts that selection into an inference claim it cannot support.
`factor_learning.py:145` states, in the generated report, "Lasso zeroing a factor = that
factor adds nothing once the others are in (built-in selection — a principled cure for
the multiple-testing fragility the Deflated-Sharpe flagged)". Single-stage LASSO does not
license that reading: the penalty biases coefficients toward zero, selection is unstable
across resamples, and post-selection coefficients have no valid standard errors. This is
precisely the problem double-selection (Belloni–Chernozhukov–Hansen) exists to fix — run
LASSO twice, once of the outcome on the controls and once of the signal-of-interest on
the controls, take the **union** of selected controls, then refit unpenalised and read
off a coefficient with valid inference. `grep -rniE
'double.?selection|post.?selection|debias|desparsif|belloni|chernozhukov'` over the whole
repo returns nothing on this (the two `trading_financials.py:60,78` hits are an unrelated
trade-filter step named DEBIAS). So the *strongest* factual claim the learned-factor
report makes is the one part of it with no test behind it.

**Distinct from queue item 21**, which attacks the same report from the non-linearity
side (a Pearson participation ratio and a linear model share a blind spot). This is the
inference side: even restricted to the linear terms both already see, "zeroed ⇒ adds
nothing" is unwarranted. The two are complementary and neither subsumes the other.

**Action queued:** item 26.

### 2609.04917 — Artificial Intelligence in Equity and Crypto Markets: Progress, Profitability Evidence, and the Limits of Automated Investing (Linsen Zhu & Mengqing Cai, 2026-09-04)

EVIDENCE-GRADE: not applicable — a critical review of public research through
2026-08-31, no original panel. Registered for its framing, not its numbers. Its organising
device is an **"alpha-translation chain"**: information → stable signal → feasible
positions → executable orders → risk-adjusted net returns after costs. A method is graded
by the *furthest link it demonstrates*, not by its headline metric. Its verdict is that
progress is "real but mainly upstream", and that no general AI architecture in the public
record delivers persistent, cross-regime, capacity-aware net alpha.

**Doing-right:** this repo sits unusually far down that chain for a one-person estate.
`cost_vs_edge.py` exists precisely to ask whether the small-cap Piotroski edge survives
costs, and grounds its answer in Krauss, Krüger & Beerstecher (2015) — the same finding
that set the ₹1 crore/day liquidity floor. Capacity is treated as a first-class question,
not a footnote. Under the review's own grading the pipeline reaches the last link on at
least one strategy, which is more than the reviewed AI literature manages.

**Gap:** none actionable, and this is deliberately not queued. The review's remaining
criticisms — temporal contamination, survivorship, capacity — already map onto queue items
23, 24 and 25 and onto the standing 2026-08-28 finding that this repo has no LLM-agent
surface for its AI-specific critiques to attach to. Logged as a citable external prior for
the *next* time an AI-flavoured method is proposed here: the burden of proof is the last
link in the chain, and the public record has not met it.

### Weak/off-scope, one line each (triaged, not deep-read)

- **2212.12845** (Wan, Li, Lu & Song, "Mining the Factor Zoo: Estimation of Latent Factor
  Models with Sufficient Proxies", 2022-12-25, stat.ME) — penalised reduced-rank
  regression for latent factor estimation with an increasing number of proxies, plus a
  heavy-tailed-robust variant. The abs page discloses **no universe, no date range, no
  evaluation metric and no cost treatment**; the claimed contribution is a convergence
  rate. Latent factors are also the wrong object here — this repo's 10 signals are named,
  interpretable and individually tradable, and replacing them with statistical factors
  would destroy the property that makes the mailer explainable. Off-scope.
- **1907.01670** (Zeng, Xia & Zhang, "Double Cross Validation for the Number of Factors in
  Approximate Factor Models", 2019-07-02) — surfaced by the query's "effective number of
  factors" clause and rejected on it. Pure econometric theory: consistency of a
  cross-validate-over-observations-then-over-variables rule as both dimensions grow, with
  no equity application. The repo's analogous quantity is already measured
  (`research/factor_redundancy.py` participation ratio, 4.92/10 IN and 4.53/10 US, per
  queue item 21), and a consistency proof for a different estimator does not change what
  to do about it. Not deep-read.
- **Citation-following, already registered** — 2608.26990, 2607.19453, 2607.04958,
  2606.08285 returned again (seventh consecutive run); listed only so the day's candidate
  count is honest. 2609.04917 was the one genuinely new hit and was deep-read above.
