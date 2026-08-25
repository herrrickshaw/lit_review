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

## Done

(none yet)
