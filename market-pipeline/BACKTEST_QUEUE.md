# Backtest Queue

Concrete, paper-motivated changes ready to test — populated by literature review,
consumed by hand (this file is never executed automatically). Each item traces to
a LITERATURE_REGISTER.md entry. Move an item to DONE with a one-line result link
when it's been run; do not delete history.

## Queued, priority order

1. ~~**Factor redundancy measurement**~~ — **DONE 2026-08-23**, see `research/factor_redundancy.py`
   / `factor_redundancy.md`. Participation ratio **4.92 of 10** (IN) / **4.53 of 10** (US) —
   the 10-factor set carries roughly HALF the information a truly independent set would.
   Worst pairs: golden_cross×breakout (r=+0.66/+0.65), plus the documented AND-combinations
   (lowvol×qual_mom r=+0.55–0.61, lowvol×def_revert r=+0.56). 263K/261K obs each.

2. **Ranking reformulation** — cross-sectional percentile cut replacing the fixed
   `pio >= 7` gate at `build_mailer.py:227`, keeping existing sort/top-15 truncation.
   Motivated by: 1809.09441 (RSR). Test via `factor_learning.py:62 ls_book_ir`.

3. ~~**Regime gate via correlation spectrum**~~ — **MEASURED 2026-08-23** (not yet
   gated — log-first per item 9's own instruction), see `research/correlation_regime_spectrum.py`
   / `.csv`. 150-symbol NSE universe, rolling 60d windows, 10.5y. Participation ratio
   ranges 3.5–24.1 (mean 12.3); the 5 LOWEST-PR windows in the entire 10.5-year sample
   are all March–May 2020 (COVID). Independent sanity check passed: mean PR during
   Feb–May 2020 = 6.0 vs Jun–Dec 2019 calm period = 9.4, PC1 absorbs 50–53% of variance
   at the crash's worst point vs 14–15% in the calmest windows. The metric carries real
   information the current gate (EMA-vs-index + vol percentile) does not have. Next step
   if pursued: decide a threshold and backtest it as an actual gate, not just log it.

4. **Wire execution_cost_model.py in** — currently imported by nothing
   (`grep -rl execution_cost_model` returns only its own file). Almgren-Chriss
   square-root impact + 15% ADV cap already implemented. Every paper reviewed this
   week shares the same flaw the repo could actually fix. Motivated by: nearly
   every paper in the register (gross-of-cost is the single most repeated
   evidence-grade problem found).

5. **Fundamental screens on `public.global_fundamentals`** — 111,411 US rows to
   1987, 14 markets, `filed` column available for real point-in-time discipline
   (not the FYE+90d proxy currently used in `pe_bands.py:82-93`). Deferred from
   2026-08-22 session for scope. Larger effort — schema/PIT-discipline work first.

6. **Purge+embargo function — NOT full CPCV** on `signal_tracker.py` and the gap
   in item 10. **RESEARCHED 2026-08-23** by 4 parallel agents (theory, critique,
   empirical, implementation) — see LITERATURE_REGISTER.md "CPCV/embargo" section
   for full sourcing. All four independently converged on the same conclusion:
   - **Purging rule** (AFML Ch.7 §7.4.1, p.105): drop any training row whose
     LABEL window overlaps a test row's label window — not just overlapping
     timestamps, overlapping *label formation periods*.
   - **Embargo length**: no single literature formula. mlfinlab's reference
     default is a % of the dataset (horizon-agnostic); ORCA (2604.17251) uses
     embargo = horizon (10d gap for a 10d target) but does NOT ablate it — one
     number reported, gap already baked in, not a before/after comparison
     (corrects the earlier register entry, which implied an ablation existed).
     Given the repo's own longest horizon is 252 trading days, **embargo = 252
     trading days is the conservative, source-justified choice** — apply the
     rule "≥ longest evaluated horizon", not the previously-guessed 21 days.
   - **CPCV's real value-add is a Sharpe *distribution* across C(N,k) combinatorial
     paths for detecting backtest overfitting** — NOT leakage prevention, which
     purge+embargo alone already solves. Cost grows fast (C(20,10)≈184,756 splits).
   - **CPCV is necessary-but-not-sufficient anyway**: it cannot catch selection
     bias across strategy configurations — that needs the deflated Sharpe ratio,
     which `deflated_sharpe.py` ALREADY implements here. Pairing purge+embargo
     with disciplined DSR bookkeeping (deflate by every configuration actually
     tried) is the better-justified addition than building full CPCV machinery.
   - mlfinlab (the reference implementation) is DEAD for reuse — closed-source,
     pulled from PyPI. `sklearn.model_selection.TimeSeriesSplit(gap=...)` is real
     (confirmed on the installed sklearn 1.9.0) but only a fixed-index-count gap,
     not label-horizon-aware purging — usable as a low-level primitive only.
     Hand-build: ~40-80 lines for purge+embargo, ~150-250 for full CPCV.
   **ACTION: hand-build a ~40-80 line purge+embargo function (embargo=252d),
   wire it into `signal_tracker.py`'s outcome-counting and item 10's
   walk-forward gap. Do not build full CPCV as a first move.**
   Motivated by: 2605.19337 §13.1.2 (original prompt), AFML Ch.7/12, 2604.17251,
   Arian/Norouzi M./Seco 2024 (Knowledge-Based Systems), eslazarev/purged-cross-validation.

7. **chop+HIGH-vol regime gate** — currently a warning string in the brief
   (`build_mailer.py:434`), not a hard demotion. Motivated by: 2607.15414.

8. **Sentiment relevance scoring, not gating** — turn the hard ticker-match gate
   in `sentiment_pipeline.py:443-452` into a relevance score multiplied into the
   existing provider-weighted mean (`:519-526`). Motivated by: 2603.19286.
   Coverage caveat: IN/US only.

9. **Spectral descriptors from the nightly correlation matrix** — sharpens and
   supersedes item 3 by giving it exact formulas. `market_correlation_scan.py`
   already builds the matrix (`:168` full-universe, `:311` MST path) and discards
   it after writing CSVs. One `np.linalg.eigvalsh` on that same matrix yields, in
   a few lines: absorption ratio AR_k (k∈{1,3,5}), eigenvalue entropy H, effective
   rank ER=exp(H), spectral gap λ₁/λ₂, condition number λ₁/λₙ, Marchenko–Pastur
   excess λ₁−(1+√(n/T))², and m⁻ = count of eigenvalues below (1−√(n/T))².
   Log them as a daily time series first; only then consider gating on them.
   Motivated by: 2604.17251 (upper spectrum), 2608.09641 (m⁻, lower spectrum),
   2607.19005. Cheap — no new data, no new fetch.

10. **Anti-leakage gap in the walk-forward split** — `walk_forward_backtest.py:173-181`
    splits 60/20/20 strictly chronologically with a zero-day gap: `test_start` is
    the next trading day after train ends, while forward returns are measured over
    8 horizons. Insert a gap equal to the longest evaluated horizon between each
    boundary and re-run to measure how much of the reported edge was overlap.
    Motivated by: 2604.17251 (10-day gap matched to a 10-day horizon). Complements
    item 6 (which covers the forward log, not the backtester).

11. **Availability-time vs reference-time column annotation** — audit every
    fundamentals read for whether it keys on when a datum was *available* or when
    it *refers to*. `pe_bands.py:82-93` already uses an FYE+90d availability proxy;
    the point-in-time `filed` column in item 5 is the real fix for that one site.
    The queued work is the cheap part: enumerate the sites and label them, so the
    discipline is checkable rather than folklore. Motivated by: 2607.04958.
    Explicitly NOT adopting the paper's type-and-effect system — out of scope.

12. **Factor spanning test on the 10-factor set** — regress each of the 10 `FACTORS`
    (`factor_learning.py:37`) on the other nine and report the intercept α with its
    t-stat; a factor whose α is insignificant is spanned by the rest and is a drop
    candidate. Reuse the exact feature matrix `research/factor_redundancy.py` already
    builds (`:64-65`) — no new data. Sharpens item 1: that item *counted* redundancy
    (PR 4.92/10 IN, 4.53/10 US), this one *names* which factors are redundant and
    attaches significance. Note the repo currently has no spanning test at all
    (`grep -rniE 'spanning.test|stepwise|orthogonaliz|residualiz|variance_inflation'
    --include='*.py'` = 0 hits); `LassoCV` at `factor_learning.py:88` is L1 shrinkage,
    not a spanning test — it yields no t-stat and answers a different question.
    Motivated by: 2601.10279 (Feng/Lan/Wang/Zhang, Management Science).

13. **Rolling factor redundancy — is 4.92/10 stable or a two-regime average?**
    `research/factor_redundancy.py:65` computes ONE `df.corr()` over the whole pooled
    panel, so item 1's headline is a full-sample point estimate with no time variation.
    2111.05072 finds the causal network among 11 US risk factors sparsifies long-term
    but **densifies under stress**, collapsing toward pure market exposure. Concrete
    test: apply the rolling-window loop already written in
    `research/correlation_regime_spectrum.py` (currently pointed at the 150-symbol NSE
    *stock* matrix) to the 10-factor matrix instead, and plot participation ratio over
    time. Falsifiable prediction to check: PR dips sharply in Mar–May 2020, the same
    windows item 3 already flagged as the 5 lowest-PR stock-correlation windows in
    10.5y. If it holds, the factor set is least diversified exactly when it matters
    most. Cheap — both halves of the code already exist, no new data or fetch.
    Motivated by: 2111.05072 (D'Acunto et al.), complements items 1, 3 and 9.

14. **Third purge+embargo site: `LassoCV(cv=5)` at `factor_learning.py:88`** — the
    outer 60/40 train/test split (`:84-85`) is chronologically clean, but the inner
    penalty-path CV is plain 5-fold KFold, so α is tuned on folds that sit *after* the
    fold being scored. Swap for a purged/embargoed splitter (or at minimum
    `TimeSeriesSplit`) once item 6's function exists. Not a new investigation — this is
    a previously-unnamed third site for the function item 6 already specifies
    (alongside `signal_tracker.py` and item 10's walk-forward gap). Found incidentally
    while grep-verifying item 12 on 2026-08-25.

15. **Limit-locked / untradable-bar guard beyond KR** — `_flag_stale_halted_days()` at
    `factorial_screener_test_KR.py:119` exists only in the KR screener
    (`grep -rln '_flag_stale_halted_days' --include='*.py'` → one file), yet India is
    the market with statutory daily price bands (±5/10/20%). 2507.07107 measures what
    this costs on a limit-band market: computing factors over closes nobody could
    transact at inflates IC by **18%** and cuts realized Sharpe by **0.44**. Concrete
    test, cheap and data-free: from the existing IN OHLCV panel, flag bars where
    (a) `Volume == 0`, or (b) `High == Low` (limit-locked, zero intraday range), or
    (c) `|Close/prev_Close - 1|` sits within ~0.3% of 5/10/20%. Count the flagged share
    per market, then re-run one settled screener backtest twice — once as-is, once with
    flagged bars excluded from signal formation — and report the IC and Sharpe delta.
    Falsifiable prediction: if Du's mechanism transfers, IN shows the largest degradation
    and US/EU (no daily bands) show ~none, which would also tell us whether the
    India-only edge in the validated-edge registry is partly this artefact. Secondary,
    one-line fix regardless of outcome: `backtest_liquidity_forward.py:74` filters
    `Volume >= 0` where `cost_vs_edge.py:130`, `backtest_piotroski_plus.py:77` and
    `daily_breakout_combo_us.py:82` all use `Volume > 0` — make it consistent.
    Motivated by: 2507.07107 (Du). Independent of items 1/3/9/12 (factor redundancy)
    and of items 6/10/14 (purge+embargo) — this is a data-hygiene item, not a
    validation-protocol one.

16. **Is momentum's net-of-cost failure a premium problem or a churn problem?** —
    Baldi-Lanfranchi (2024) shows TCU momentum (full rebalance to target every period)
    earns 0.64%/mo gross, pays 63bps/mo in costs, and nets 0.01%/mo — while the *same*
    signal traded at an optimized partial intensity pays 30bps/mo and nets 22x more,
    lifting annualized net Sharpe by 0.19. This repo measured momentum 12-1 at -14.11%
    vs bench (IN, n=3,541) and -15.08% (US, n=17,606) on 2026-08-23 and filed it as "no
    edge". That test used the full-rebalance form. Concrete, cheap test that does NOT
    require building a portfolio-construction layer: re-run the existing momentum 12-1
    backtest with a **hold-through rule** — once a name is in the top decile, keep it
    until it falls below a wider exit band (e.g. top 30%) instead of re-forming the
    basket from scratch each period — and report gross return, realized turnover, and
    net return for the standard form vs each of 2-3 band widths. Falsifiable prediction:
    if the paper's mechanism transfers, gross return falls modestly while turnover (and
    hence the cost drag at the repo's 0.2% round-trip, `backtest_screeners.py:176`) falls
    much faster, so the net gap to benchmark narrows. If net barely moves, momentum's
    failure here is a genuinely absent premium and the question is settled — which is a
    useful result either way. Explicitly OUT of scope: implementing TCA factors properly
    (needs a weight vector and an optimizer over trading intensity; this repo is
    signal-only with no execution layer). Related: the watchlist mailer's >5-session
    eviction rule is the repo's existing frequency heuristic and is the natural second
    place to apply the same measurement.
    Motivated by: Baldi-Lanfranchi (2024), Transaction-cost-aware Factors.

17. **Full-sample winsorization thresholds in the factorial-screener OLS** —
    2604.07880 quantifies what full-sample filtering thresholds do to a factor zoo: the
    6-month bond momentum premium of 0.30%/mo is *entirely* an artifact of ex-post
    winsorization, and across 432 specifications only 26 (6.0%) survive BH-FDR
    correction. This repo already gets it right in the two places that matter most —
    entry is the next bar, not the signal bar (`backtest_screeners.py:293`), which
    structurally prevents the correlated errors-in-variables half; and `rloo_rescore.py:291`
    `winsorize_xs()` clips within each day's own cross-section (`axis=1` at `:309-310`).
    But three sites still compute clip bounds from the whole pooled sample:
    `factorial_screener_analysis.py:97-107` (live at `:111`, feeding the OLS),
    `train_ppo_factor_weights.py:132-133`, and `factor_zscore_panel.py:45-46` (which
    explicitly adopts the same convention). Concrete test: re-fit
    `fit_factorial()` twice — once as-is, once with the clip bounds computed
    **within each formation year's own cross-section** (the `rloo_rescore.py:291` pattern,
    which already exists and is tested) — and report the coefficient, HC3 standard error
    and BH-adjusted p-value for every screener x horizon under both. Falsifiable
    prediction: if the effect is real, coefficients move within noise; if any screener's
    significance depends on pooled-sample bounds, that screener's effect is partly an
    artifact and should be re-graded. NOTE — do not overstate this: the repo's
    winsorization is **symmetric** (1/99 both tails), while the paper's fatal case is
    **asymmetric** filtering. The hazard being tested is the full-sample threshold alone,
    which is the milder member of the same family. Cheap: no new data, no fetch, one
    changed function and a re-fit. Secondary: `train_ppo_factor_weights.py:132` sits
    upstream of an RL training run, so a pooled bound there leaks across the
    chronological split made just below it at `:141`.
    Motivated by: 2604.07880 (Dickerson, Robotti & Rossetti). Independent of items
    6/10/14 (purge+embargo) and 15 (untradable bars) — this is a threshold-provenance
    item, adjacent to 15's data-hygiene family.

18. **Raw sample covariance in both optimisers — no eigenvalue treatment** —
    `portfolio_builder.py:217` computes `cov = R.cov().values * TRADING_DAYS` and feeds it
    unfiltered into `port_var = lambda w: w @ cov @ w` at `:222`; `mutual_fund_theorem.py:107`
    does the identical thing. The repo's only shrinkage is on *expected returns*
    (`_expected_returns()`, `portfolio_builder.py:190-200`, James-Stein toward the
    cross-sectional mean) — Sigma is never touched. `mutual_fund_theorem.py:156` already
    prints "without shrinkage (Ledoit-Wolf) or hard position constraints" as a warning when
    half-sample turnover exceeds 0.5, so this is a self-diagnosed gap that was never closed.
    Concrete test: re-run `optimise()` three ways on the same panel — raw `R.cov()` as-is,
    `sklearn.covariance.LedoitWolf` linear shrinkage, and a frozen-eigenvalue estimator
    (spectrum estimated once on the earliest third of the sample and held fixed for the
    rest, the paper's "Average Oracle") — and report, for each, out-of-sample realized
    volatility, max drawdown, Sharpe **and turnover**. Falsifiable prediction: if the
    warning at `:156` is right, raw-sample min-variance weights should show materially
    higher out-of-sample realized volatility and turnover than either shrunk version; if
    they do not, the warning is over-cautious and should be re-worded. 🔴 Turnover is not
    optional in this comparison — 2507.01918's own neural estimator wins on variance
    (Sharpe 1.011 vs QIS 0.942) while running 112% turnover per 5 days against QIS's 44%,
    which is how a lower-variance estimator loses money net of cost. Cheap: no new data,
    no fetch, no training; sklearn is already a dependency and the frozen-eigenvalue
    variant is ~15 lines of numpy. Note the standing caution from 2605.30464 (logged
    2026-08-28), whose headline negative result was that plain Ledoit-Wolf shrinkage beat
    every distributional method it tested — consistent with, not duplicative of, this item.
    Motivated by: 2507.01918 (Bongiorno, Manolakis & Mantegna). Independent of item 9
    (spectral descriptors as a *regime signal*) — this is Sigma-as-optimiser-input, a
    different use of the same matrix.

19. **Minimum Track Record Length — is the existing DSR gate resting on enough history?** —
    `deflated_sharpe.py:52` computes the deflated Sharpe and `:81` gates it at
    `survives = d >= 0.95`, writing `✅ real` / `⚠️ fragile` verdicts into
    `reports/deflated_sharpe.md` (`:104-107`). But `T` at `:77` is just `best["n"]`,
    formation weeks, passed straight into the DSR and never itself checked. DSR answers
    "did the winner beat the best-of-N benchmark"; it does not answer "is this sample long
    enough for that comparison to be stable." MTRL (Bailey & López de Prado) is the
    companion statistic and is about ten lines of the arithmetic already sitting in this
    file: `MTRL = 1 + [1 - skew*SR + (kurt-1)/4 * SR^2] * (Z_alpha / SR)^2`, i.e. the same
    bracket already computed as `denom**2` at `deflated_sharpe.py:57`. Concrete test:
    compute MTRL per market x regime, put it next to the `T_weeks` column already written
    to `reports/deflated_sharpe.csv` (`:82`), and flag every row whose DSR passed on fewer
    observations than its own MTRL requires. Falsifiable prediction: bear-regime rows have
    materially fewer formation weeks than bull rows, so if any bear cell currently carries
    `✅ real` while T_weeks < MTRL, that label is unearned and the report's verdict column
    is overstating its own evidence. Cheap: no new data, no fetch, no refit — one function
    and one extra column. Motivated by: 2608.23808 (Santoni, Jouanne & Scullin), whose
    MTRL gate is one of the three the repo lacks entirely.

20. **`overfitting_report()` is labelled PBO but computes Sharpe decay — replace it with
    real CSCV, or fix the citation** — `walk_forward_backtest.py:1086` cites "Bailey et al.
    (2014) — 'Probability of Backtest Overfitting'" on a function (`:1082`) that computes
    `decay = (train - val)/abs(train)*100` from per-split mean Sharpe (`:1094-1096`) and
    buckets it at hardcoded 50%/20% thresholds (`:1111-1116`). PBO is a different
    statistic: split the trial matrix into S even blocks, and over the C(S, S/2)
    train/test partitions record the out-of-sample rank of whichever configuration was
    best in-sample; PBO is the fraction of partitions where that rank falls below the
    median. The repo already has the required input — the market x regime x factor
    info-ratio matrix in `reports/profitability_optimizer.csv`, the same file
    `deflated_sharpe.py:65` reads. At S=8 that is C(8,4)=70 partitions, ~30 lines with
    `itertools.combinations`, no new data. Concrete test: compute real PBO on that matrix
    and compare its verdict against the existing `Overfit_Risk` HIGH/MEDIUM/LOW labels —
    if they disagree, the current thresholds are miscalibrated and the strategy matrix at
    `:1120` is selecting on a decay number that does not mean what its docstring claims.
    While in this function, also add **fold-level profitability** (share of splits with
    positive return) beside the mean-Sharpe columns — 2512.12924 reports 41% (14 of 34
    folds) next to its aggregate Sharpe 0.33, and the pair is far more informative than
    either alone. 🔴 Minimum acceptable outcome even if CSCV is not built: detach the
    Bailey citation from a function that does not implement it. Cheap: no new data, no
    fetch. Motivated by: 2608.23808 (Santoni, Jouanne & Scullin) for the gate, 2512.12924
    (Deep, Deep & Lamptey) for the fold-level metric. Independent of item 6 (purge+embargo,
    which is about leakage into the split); this is about grading what comes out of it.

## Done

(none yet)
