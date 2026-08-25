# Commission Queue — masaladeutsch

Concrete article ideas with a named primary source attached. Appended to by track B of
the `literature-review-daily` scheduled task; consumed by hand when picking what to
write next. Nothing here is written automatically.

Each entry must name **where the data comes from** and **what the piece would argue**.
An idea without an obtainable dataset belongs in the register as BACKGROUND, not here.

Format:

```text
- (working title)
      Source: (dataset / paper / portal, with the exact table or series if known)
      Argument: (the finding, in one sentence — what a reader would not already assume)
      Checks needed: (what must be verified before writing)
      Logged: YYYY-MM-DD from (register entry)
```

---

## Open

- [ ] 4,666 items on the defence indigenisation lists, ₹2,570 crore of substitution
      Source: DDP Positive Indigenisation Lists 1–4 (2,851 + 107 + 780 + 928 items);
      DPSU-wise indigenised lists published as PDFs on srijandefence.gov.in (verified
      downloadable, HTTP 200, 1.9 MB); PIB releases PRID 1924426 and the ~18 Aug 2026
      6th-PIL notification.
      Argument: 2,736 of 4,666 listed items are recorded as indigenised, but the claimed
      import-substitution value totals only ₹2,570 crore — about ₹94 lakh an item. The
      list is long and the money is small, which is the opposite of how the count is
      usually reported.
      Checks needed: source total defence imports for the same period before stating any
      share; verify the 6th PIL against its own release; the ministry defines
      "import substitution value" itself and the definition needs stating in the piece.
      Logged: 2026-08-22 from the defence PIL register entry

- [ ] Rebuilding the $189 billion substitution list from public trade data
      Source: DGCI&S TradeStat (already used by the blog for the 827-code chemical work);
      the official 1,272-product list is NOT published — press only (Business Standard
      16 Jul 2026, Policy Circle).
      Argument: filter every HSN line above $50 mn of annual imports from public data and
      see whether it lands near the government's 1,272 products and $189 bn. The blog has
      the method already; nobody has published the reconstruction.
      Checks needed: do not state 1,272 or $189 bn as established fact — attribute to
      press reporting. The "not made in India or in inadequate quantity" half of the
      official filter is not reproducible from trade data alone, and the piece must say so.
      Logged: 2026-08-22 from the 1,272-product register entry

- [ ] Does India have the feedstock for E20?
      Source: AERR, "Does India have enough feedstock to meet its E20 targets by 2025?";
      cross-check against the blog's existing maize-acreage and sugarcane-diversion posts.
      Argument: the target is set in blending percentage but bounded by a feedstock
      balance nobody publishes as a balance.
      Checks needed: AERR's latest listed issue is Vol. 37 No. 1 (2024) — anything
      time-sensitive needs a newer source before publication.
      Logged: 2026-08-22 from the corpus survey (Tier 1, item 2)

- [ ] Nano-urea: does it substitute for anything?
      Source: IJAgS nano-nitrogen dosing trials; IFFCO deployment figures.
      Argument: test the marketing claim against the trial literature, following the
      blog's existing 4:2:1 and FOM/LFOM pieces.
      Checks needed: separate IFFCO's own trial data from independent trials.
      Logged: 2026-08-22 from the corpus survey (Tier 1, item 3)

- [ ] Does a tomato price in Kolar reach Delhi?
      Source: AERR on tomato market integration and e-NAM performance in Odisha;
      Agmarknet daily mandi prices (fully reproducible).
      Argument: the blog has mapped CPI by state; this is the transmission mechanism
      underneath it.
      Checks needed: Agmarknet series continuity across the period chosen.
      Logged: 2026-08-22 from the corpus survey (Tier 1, item 4)

- [ ] Rural India's fastest quarter off the farm
      Source: PLFS Quarterly Bulletin, NSO/MoSPI — Jan-Mar 2026 and Apr-Jun 2026
      releases, both fetched directly (free PDFs, mospi.gov.in/uploads/).
      Argument: rural agriculture's employment share fell for two straight quarters,
      58.5% -> 55.8% -> 52.9% (Oct-Dec 2025 through Apr-Jun 2026) — a 5.6-point drop in
      six months, confirmed against the primary bulletins, not press reports. The
      secondary sector absorbed most of the shift (20.9%->22.6%->24.4%) and regular wage
      employment rose for a third straight quarter (14.8%->15.5%->16.1%) as
      self-employment fell — faster movement than the "decades-long" framing rural-urban
      transition pieces usually assume, and sharper still for rural women (agriculture's
      share of female rural employment: 75.5%->73.5%->70.7%). Pairs with the published
      farm-wages piece as its structural counterpart.
      Checks needed: the rural quarterly series is only 5 points old (methodology
      revamped Jan 2025) so hedge any "trend" language as early-series, not established;
      check whether the secondary-sector rise is broad-based or concentrated in a few
      states before generalising (state-level breakdowns are in the same bulletins).
      Logged: 2026-08-24 from the PLFS Quarterly Bulletin register entry; Apr-Jun 2026
      figure verified same day against the primary bulletin.

- [ ] India's largest crop insurer pays out ₹1.83 lakh crore. Farmers funded about 2% of it.
      Source: PIB Explainer ID 155010, "Empowering Annadatas: Pradhan Mantri Fasal Bima
      Yojana", Ministry of Agriculture & Farmers Welfare, 11 Aug 2025 — fetched 2026-08-25
      (needs a browser user-agent; plain fetchers get 403). Scheme rules in the compendium
      PDF at pmfby.gov.in/compendium/.
      Argument: the scheme is reported as insurance and headlined by its payout — 78.41 crore
      applications, ₹1.83 lakh crore in claims since 2016 — but the release never states what
      farmers paid in. By PMFBY's own capped rates the farmer funds 1.5–5% of actuarial
      premium and Centre+states fund 95–98.5% on a 50:50 split (90:10 in NE/Himalayan states),
      so nearly every rupee disbursed is public money routed through insurers. Same
      who-pays-vs-who-receives structure as the published GST piece
      (`who-collects-indias-gst-and-who`), applied to the agriculture beat.
      Checks needed: the release is 11 Aug 2025, so re-base every "since inception" total
      before writing. Do NOT promise state-level numbers — the gross-premium series is not
      confirmed obtainable (pmfby.gov.in is a SPA: /adminStatistics/dashboard, /reportsummary
      and /statistics all return the same 6,842-byte shell, /api/v1/dashboard/statistics 404s,
      data.gov.in catalog query failed). Distinguish "applications insured" from "farmers
      insured" — one farmer files across seasons and plots. Several states have waived the
      farmer share entirely, which pushes the farmer-funded fraction below the capped rate;
      say so rather than quoting 2% as universal. Avoid the vendor/aggregator figures
      (Indiastat is paywalled; agrijob.in's ₹1.92 lakh crore contradicts the primary).
      Logged: 2026-08-25 from the PMFBY register entry

## Done

- [x] What a farm labourer earns, and why it stopped tracking output
      Published 2026-08-22 as "A 17% Rural Pay Rise That Nobody Received".
