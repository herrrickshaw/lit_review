# Source Register — masaladeutsch

Running log of papers, datasets and official releases assessed as **commissioning
material for the blog**. One entry per source. Extended by track B of the
`literature-review-daily` scheduled task.

This is deliberately *not* the market-pipeline literature register. That one grades
papers on whether a technique is worth implementing in a screener. This one grades
sources on whether they can carry an article: primary data the blog can pull itself,
a finding worth reporting, and a subject the blog has not already covered.

**Grading convention**

- **COMMISSIONABLE** — names a primary dataset the blog can obtain (government portal,
  journal appendix, official return), and carries at least one quantified finding that
  is either counterintuitive or not already common knowledge in Indian coverage.
- **BACKGROUND** — sound and relevant, but no independently obtainable data. Useful for
  context or a citation inside a piece built on something else. Not a piece on its own.
- **WEAK** — modelled or vendor-sourced numbers with undisclosed method, a scope too
  narrow to generalise, or a finding the blog already published. One line, no write-up.

Vendor market-sizing reports are **WEAK by default**. A standing correction applies:
one such report overstated an India figure by 6.5×. If a vendor number is the only
source for a claim, the claim does not go in an article.

**Dedup rule** — before logging a candidate, check it against:
1. this file,
2. `docs/LITERATURE_SURVEY.md` (the 2026-08-22 corpus survey and its commissioning list),
3. `meta/manifest.json` (every published post title).

---

## Commissionable

### Defence Positive Indigenisation Lists (DDP, Ministry of Defence)
Four PILs notified for DPSUs covering Line Replacement Units, sub-systems, spares and
components: 1st 2,851 items, 2nd 107, 3rd 780, 4th 928 — **4,666 items** total (arithmetic
checked against the release, sums exactly). A 6th PIL of 405 items was notified around
18 August 2026 per PIB listings; not yet verified against its own release.
- **Data**: DPSU-wise item lists are published as PDFs on the Srijan portal
  (`srijandefence.gov.in`). Verified downloadable — the 12 May 2023 notification returns
  HTTP 200, 1.9 MB, `application/pdf`. No login, no payment.
- **Finding**: 2,736 of the 4,666 items are recorded as indigenised (58.6%), but the
  claimed import-substitution value totals only **₹2,570 crore** (₹1,756 cr + ₹814 cr) —
  roughly $295 mn, averaging **₹94 lakh per item**. A very large item count against a very
  small rupee value.
- **Blog fit**: defence indigenisation is effectively zero-coverage. The only defence post
  is `jai-kisan-jai-javan-fci-based-military` (military rations, FCI-based), and "Positive Indigenisation List"
  appears in the corpus only inside `quarterly-reportage-4034-scheme` as a logged scheme
  announcement, never analysed. The method is the one the blog already uses on chemicals in
  `top-15-chemicals-for-import` and `chemical-import-substitution-hsn-8-registry` — a code-by-code
  substitution list checked against trade data.
- **Caveat**: "import substitution value" is the ministry's own definition and is not
  reconciled here against actual defence import lines. The count-versus-value gap is the
  story, but the denominator (total defence imports over the same period) must be sourced
  before any share is stated. The 6th PIL needs its own release verified.
- Grade: **COMMISSIONABLE**. Logged 2026-08-22 (Saturday rotation).

### The 1,272-product, $189 billion import-substitution list (centre-state / DPIIT)
A centre-state exercise reported to have identified 1,272 products worth nearly $189 bn of
annual imports, each above a $50 mn annual import threshold and either not made in India or
made in inadequate quantity; sectors named are chemicals, electronics, machinery and
speciality steel.
- **Data**: the list itself is **not published**. Traced through Business Standard (16 July
  2026, HTTP 403 to automated fetch) and Policy Circle; no PIB release found for it — a PIB
  search returned only defence PILs and the DPIIT year-end review. The obtainable data is
  the *substitute* for it: DGCI&S TradeStat, which the blog already uses, can be filtered to
  every HSN line above $50 mn independently.
- **Finding**: the reproducible question is whether a public-data reconstruction of the
  ">$50 mn, inadequately made in India" filter lands anywhere near 1,272 products and
  $189 bn. Policy Circle also reports mobile-phone assembly at 18–20% domestic value
  addition, which is the standing critique of counting import substitution by output value.
- **Blog fit**: extends `chemical-import-substitution-hsn-8-registry` and
  `chemical-import-substitution-full-hsn-8_01082878313` from chemicals to all sectors,
  and `half-of-indias-import-bill-is`. The blog has 40 trade-adjacent posts, so
  this only earns a piece as a *check on an official claim*, not as a report of it.
- **Caveat**: no primary document located. Do not state 1,272 or $189 bn as established —
  attribute to press reporting, or derive the blog's own figure and compare.
- Grade: **COMMISSIONABLE** (as a reconstruction, not a write-up of the list).

### PLFS Quarterly Bulletin, January–March 2026 and April–June 2026 (NSO, MoSPI)
Official quarterly labour-force releases — Jan-Mar 2026 published 11 May 2026 (fourth in
the series), Apr-Jun 2026 published 10 August 2026 (fifth). The survey was revamped from
Jan 2025 to cover rural areas quarterly, not just urban. Both fetched and read directly
(not via secondary reporting).
- **Data**: `mospi.gov.in/uploads/PressRelease/Press_note%20_Jan_March_2026%20PLFS_QB.pdf`
  and `mospi.gov.in/uploads/latestReleases/latest_release_1786356517178_3a125c52-4680-4258-9dc5-aebea9b8f3f0_Press_note_Apr-Jun_2026_PLFS_QB.pdf`
  — both free PDFs, no login. Apr-Jun 2026 sample: 5,59,673 persons surveyed nationally
  (3,18,792 rural). A new quarterly bulletin is released roughly 5-6 weeks after each
  quarter ends, so this is a recurring, obtainable series, not a one-off.
- **Finding**: rural agriculture's share of employment fell for two straight quarters —
  58.5% (Oct–Dec 2025) → 55.8% (Jan–Mar 2026) → **52.9%** (Apr–Jun 2026, confirmed against
  the primary bulletin, p.8) — a 5.6-point drop in six months, while the rural secondary
  sector rose 20.9%→22.6%→24.4% and tertiary 20.6%→21.7%→22.7% over the same two
  quarters. Rural regular wage/salaried employment rose for a third straight quarter
  (14.8%→15.5%→16.1%) as self-employment fell (63.2%→62.5%→61.4%, p.7). The shift is
  sharper for rural women: agriculture's share of rural female employment fell
  75.5%→73.5%→70.7% across the same three quarters (p.8 chart). Readers who think of
  "rural India moving off farms" as a decades-long trend would not expect a two-quarter
  move this size.
- **Blog fit**: zero coverage — `PLFS`, `labour force`, `non-farm` return no manifest
  hits. Extends `A 17% Rural Pay Rise That Nobody Received` (farm wages, published
  2026-08-22): that piece covered what farm labour earns, this covers how many rural
  workers are still doing farm labour at all, and the two would read as a pair.
- **Caveat**: the rural quarterly series only has 5 data points (Apr–Jun 2025 through
  Apr–Jun 2026, methodology revamped Jan 2025) — real, but too short to call an
  established multi-year "trend" without hedging as early data from a young series.
- Grade: **COMMISSIONABLE**. Logged 2026-08-24 (Monday rotation); Apr-Jun 2026 figure
  verified against the primary bulletin same day, superseding the press-sourced estimate.

---

## Background only

### DPIIT Year End Review — PLI aggregate outcomes (PIB, Ministry of Commerce & Industry)
Official aggregates: ₹1.46 lakh crore investment, ₹12.5 lakh crore production, ₹4 lakh crore
exports, 9.5 lakh jobs, 1,300+ manufacturing units across 14 sectors and 27 states/UTs.
- **Data**: PIB release, fetched and readable (PRID 2086347, HTTP 200).
- **Blog fit**: the blog already has five PLI posts including
  `pli-medical-devices-coverage-and-gaps` and two priority-sector PLI-coverage pieces. These are headline
  aggregates without sector splits, so they are citation material inside a future piece
  rather than a piece themselves.
- Grade: **BACKGROUND**. Logged 2026-08-22.

### PMFBY premium-sharing structure and cumulative claims (PIB Explainer 155010, Ministry of Agriculture & Farmers Welfare)
"Empowering Annadatas: Pradhan Mantri Fasal Bima Yojana", PIB Explainer ID 155010,
posted **11 August 2025** (a year old — see Caveat). Fetched directly 2026-08-25 (the
`PressNoteDetails.aspx` URL 403s to plain fetchers; it returns HTTP 200 with a normal
browser user-agent).
- **Data**: the release itself carries the hard numbers, free and no login — **78.41 crore
  applications insured** and **₹1.83 lakh crore claims paid** since the 2016 launch;
  enrolment **3.17 crore (2022–23) → 4.19 crore (2024–25)**, +32%; non-loanee applications
  **20 lakh (2014–15) → 522 lakh (2024–25)**. It also states the full premium-sharing
  *rule*: the farmer pays a capped **2% (kharif food/oilseed), 1.5% (rabi food/oilseed),
  5% (annual commercial/horticultural)** of actuarial premium, and **"the remaining part
  (95% to 98.5%)... is borne jointly by the Central and State Governments on 50:50 basis"**,
  except North-Eastern (from Kharif 2020) and Himalayan states (from Kharif 2023) at 90:10.
  The release links a compendium PDF on `pmfby.gov.in/compendium/` for scheme rules.
- **Obtainability caveat (verified, not assumed)**: the state-wise/season-wise *gross
  premium* series is **not** confirmed pullable. `pmfby.gov.in` is a single-page app —
  `/adminStatistics/dashboard`, `/reportsummary` and `/statistics` all return the identical
  6,842-byte shell, `/api/v1/dashboard/statistics` 404s, and a `data.gov.in` catalog query
  for "fasal bima" failed to return. The argument below is buildable from the rule plus the
  cumulative totals *without* that series; anything state-level needs the portal cracked first.
- **Finding**: the release headlines ₹1.83 lakh crore paid *to* farmers but never states what
  farmers paid *in*. By the scheme's own capped rates, farmers fund only 1.5–5% of actuarial
  premium — so the overwhelming majority of every rupee disbursed is taxpayer-funded, split
  50:50 between Centre and states (90:10 in the hill states). The scheme is reported as
  insurance; structurally it is closer to a subsidy routed through insurers.
- **Blog fit**: opens the **crop-insurance** intersection of the blog's heaviest beat
  (agriculture) and its newest, near-empty one. Manifest grep confirms **zero** posts matching
  `pmfby|crop insur|fasal|reinsur|gic re` across all 210 posts, and only one insurance post at
  all — `premium-now-claim-later-float-indias` ("Premium Now, Claim Later: The Float India's
  Car Boom Is Building", 2026-08-22, labels incl. *Insurance & Reinsurance*), which is motor,
  not crop. The natural structural sibling is `who-collects-indias-gst-and-who` — same
  who-pays-vs-who-receives framing.
- **Caveat**: the release is **11 Aug 2025**, so "since inception" totals are ~15 months
  stale and must be re-based before publication. It is also an explainer with a promotional
  register (it opens with a single named farmer's testimonial) — use it for the *rule* and the
  *totals*, not for interpretation. The 90:10 hill-state split materially changes any national
  average and must not be flattened. Finally, "applications insured" is not "farmers insured" —
  one farmer files across seasons and plots, so 78.41 crore applications ≠ 78.41 crore people.


---

## Weak — logged, not actioned

- India's simple average tariff rising 12% (FY2011) to 14.3% (FY2021) — sourced only to a
  commercial tariff-aggregator site, and the blog already runs heavy tariff coverage across
  40 trade-adjacent posts. Needs a WTO Tariff Profiles primary before it is usable. WEAK,
  logged 2026-08-22.
- PMFBY figures via **Indiastat** — real state/season-wise gross premium, paid claims and
  claim-ratio tables exist there, but it is a paid subscription aggregator, not a primary
  source. Use only to locate a series, never to cite one. WEAK, logged 2026-08-25.
- PMFBY claims summaries on **agrijob.in** ("₹1.92 lakh crore claims paid", state-wise premium
  lists) — SEO content farm restating PIB without attribution, and its total already disagrees
  with the primary release's ₹1.83 lakh crore. Do not cite. WEAK, logged 2026-08-25.
- **IBEF** PMFBY scheme page — IBEF is a Department of Commerce promotional body; useful only
  as a pointer to primaries it cites. BACKGROUND at best, not a source. Logged 2026-08-25.
- **pmfby.gov.in dashboard** — the obvious primary, but unusable as fetched today: SPA shell on
  every route, no working JSON endpoint found. Not a dead end permanently, just not obtainable
  without cracking the app's XHR calls. Re-probe before commissioning anything state-level.
  Logged 2026-08-25.

---

## Seeded from the 2026-08-22 corpus survey

The survey in `docs/LITERATURE_SURVEY.md` established the corpus profile and a 14-item
commissioning list. Its Tier-1 items are the standing backlog and do **not** need
re-deriving each day:

1. Farm labour wages against food inflation — **published 2026-08-22**, so this one is
   closed; the AERR wages paper is now cited in a live piece.
2. Ethanol feedstock balance against the E20 target (AERR).
3. Nano-urea against the trial literature (IJAgS).
4. Mandi market integration and e-NAM (AERR, Agmarknet).

Items 5–14 of that list remain open. A daily run should prefer a genuinely new source
over restating one of these.
