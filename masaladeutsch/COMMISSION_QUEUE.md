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

- [ ] 57.8% of India's plant-variety rights are cereals. Spices get 151.
      Source: PPV&FR Authority registry — homepage certificate counter with crop-category
      breakdown, 10,802 certificates as of 31.07.2026 (verified by direct fetch
      2026-08-27: Cereals 6,246 · Vegetables 1,367 · Fibre 989 · Legumes 866 · Oilseeds
      577 · Fruits 425 · Spices 151 · Sugar 93 · Trees 43 · Flowers 36 · Cash crops 5 ·
      Medicinal & Aromatic 4). Annual Report 2024-25 free PDF, no login, 22.77 MB,
      plantauthority.gov.in/sites/default/files/annual-report-2024-25-english.pdf.
      Supporting: Plant Variety Journal (monthly, free), Compendium of Registered
      Varieties. Concept citation: AERR 36(1):77-86 (2023) on essentially derived
      varieties, open access.
      Argument: India's plant-breeders'-rights system has granted 10,802 certificates and
      more than half of them — 6,246 — are cereals, while the eight-crop, $4.45 billion
      spice export book the blog has already mapped rests on 151 registered varieties and
      the entire medicinal-and-aromatic-plants category has four. Legal protection has
      followed the crops the public breeding system already worked on, not the crops
      India actually earns from.
      Checks needed: (1) the homepage counter is live with no vintage archive — date it
      in the piece and cross-read it against the Annual Report PDF before publishing;
      (2) the widely-repeated "4,847 of 9,210 certificates (52.6%) went to farmers, not
      companies" split came ONLY from a search snippet and is NOT yet verified — confirm
      from the Annual Report PDF or drop it entirely, do not repeat it on snippet
      authority; (3) do not equate "certificates issued" with "varieties commercially
      sold"; (4) the crop categories are the Authority's own and undefined on the
      homepage — state that. Cross-link to indias-445-billion-spice-export-book-is and
      379-kilos-hectare-in-punjab-44-in in the blog's own house style (cite the earlier
      post as reporting, never as confirmation).
      Logged: 2026-08-27 from the PPV&FR Authority registration-data register entry
      Opens: the confirmed zero-coverage seeds / plant-variety-rights / agricultural-IP
      area (manifest dedup: 217 posts, 2 regex hits, both false positives on "plant" =
      industrial facility).


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


- [ ] India irrigates itself. 96.6% of its irrigation is privately owned, and 79.5% of it
      was paid for out of farmers' own savings.
      Source: 6th Minor Irrigation Census, Ministry of Jal Shakti (DoWR-RD&GR), reference
      year **2017-18**, released 26 Aug 2023. Primary release PIB PRID 1952480 (fetched in
      full 2026-08-28; needs a browser user-agent, plain fetchers get 403). Reports as free
      direct PDFs, verified by ranged GET 2026-08-28 (HTTP 206, valid PDF, no login):
      `mowr.nic.in/irrigationcensus/Documents/MI-Census/Reports/6-MI-Report-All-India-Vol-I.pdf`
      and `...6-MI-Report-State-Wise-Vol-II.pdf`. Earlier rounds at
      `mowr.nic.in/irrigationcensus/Files/` (5th, 4th, 3rd, 2nd) give a six-census series
      back to reference year 1986-87. Concept citation (abstract only, PDF NOT free):
      Bathla, Kannan & Das, "Public investment in irrigation across the Indian states:
      Financial recovery and governance", AERR 37(1):93-112, 2024.
      Argument: India has 23.14 million minor irrigation schemes and 21.93 million of them
      — 94.8% — are groundwater, not canals. 96.6% of all schemes are privately owned
      (98.3% of groundwater ones), and of the schemes with a single source of finance,
      79.5% were funded by the individual farmer's own savings. Meanwhile the peer-reviewed
      measurement of the public half, across 20 states and four decades, is that rising
      public capital formation in irrigation "has barely corresponded" with net irrigated
      area, potential utilised, or financial recovery. The country's irrigation is
      overwhelmingly a private, self-financed, groundwater system that the public
      irrigation budget neither built nor recovers from — which is the opposite of how
      irrigation policy is usually discussed.
      Checks needed: (1) 🔴 VINTAGE — the 6th census reference year is 2017-18 and a **7th
      census is partly published**: `7-MI-Report-State-Wise-Vol-II-Part-1.pdf` fetches but
      `7-MI-Report-All-India-Vol-I.pdf` 404s, and the round is still running with the 2nd
      Census of Water Bodies at `wrcensus.mowr.gov.in`. Date every figure to 2017-18 and
      re-check for the 7th all-India volume before publishing; do NOT take a 7th-census
      national number from a secondary source. (2) Units — the census counts *schemes*, not
      farmers and not hectares; one owner can hold several. Never slide between the three.
      (3) The 79.5% own-savings figure applies only to the 60.2% of schemes with a *single*
      source of finance — quote it with that denominator attached, not as "79.5% of all
      schemes". (4) Village/district microdata is NOT confirmed obtainable (data.gov.in
      catalog is JS-rendered, catalog-level API id returns "Meta not found") — do not
      promise sub-state granularity until re-probed. (5) The AERR full text is paywalled;
      use the abstract's own wording or find the ResearchGate copy, and do not attribute
      numbers to it that the abstract does not state. (6) Groundwater ownership being
      private is not the same as groundwater being unsubsidised — power subsidy is the
      obvious rejoinder and the piece should meet it rather than ignore it.
      Cross-link in house style (cite as reporting, never as confirmation):
      `tamil-nadus-water-infrastructure-runs` — same shape of argument, headline water
      number not matching the money underneath — and `379-kilos-hectare-in-punjab-44-in`.
      Logged: 2026-08-28 from the Minor Irrigation Census + AERR register entry
      Opens: the confirmed zero-coverage irrigation-investment-and-governance area, and
      only the 4th substantive water post in 219 (manifest dedup 2026-08-28: 8 title hits,
      none on irrigation; nearest post read in full and contains zero irrigation mentions).


- [ ] The fifth list was 346 items. Three numbers in the defence indigenisation post need correcting.
      Source: PIB PRID 2033571 (16 Jul 2024, MoD) and PIB PRID 2300723 (18 Aug 2026, MoD),
      both fetched in full 2026-08-29. Note PIB 403s plain fetchers — browser UA required,
      and use `PressReleasePage.aspx?PRID=<id>`, not `PressReleaseDetail.aspx`, which
      returns a body-less shell.
      Argument: the published post `5071-items-you-cannot-import-and-rs` said its 5,071
      total was "a floor, not the full count" because the 5th PIL's size was not
      established. It was 346 items (₹1,048 crore), making the six-list DPSU total 5,417 —
      confirmed independently by the 2026 release's own "5,012 items notified under the
      first five" (4,666 + 346). The same 2024 release also states that of the 4,666 items
      in PILs 1-4, 2,972 worth ₹3,400 crore were already indigenised — larger on both
      counts than the 2,736 / ₹2,570 crore the post published for that scope two years
      later, which a cumulative count cannot do. And the DMA series the post set aside is
      509 items across five lists. The post's thesis (long list, small money) holds; three
      of its numbers do not.
      Checks needed: (1) establish which vintage/scope the ₹2,570 crore pair actually
      belongs to before printing either pair — do not simply swap in the 2024 figures, and
      do not present ₹94 lakh and ₹114 lakh an item as a trend; (2) 🔴 the SRIJAN "items
      offered" total falls from over 36,000 (June 2024) to more than 33,000 (June 2026),
      which is impossible for a cumulative count — the series was re-based or de-duplicated
      and neither release admits it; treat as a data-quality caveat, never as a decline;
      (3) "12,300 indigenised in three years" and "15,700 in five years" are different
      windows, not a delta; (4) "import substitution value" is the ministry's own undefined
      term in every release — state that; (5) the 33,000-item SRIJAN pool and the 5,012-item
      PIL pool are different denominators, so ₹9,000 cr ÷ 15,700 (₹57 lakh/item) is not
      comparable with the PIL-only per-item figure. House style: cite the earlier post as
      the blog's own reporting, never as confirmation.
      Logged: 2026-08-29 from the 5th/6th PIL primaries register entry
      Updates: the published post `5071-items-you-cannot-import-and-rs` (23 Aug 2026).
      Supersedes the open item "4,666 items on the defence indigenisation lists, ₹2,570
      crore of substitution" logged 2026-08-22 — that item's headline figures are the ones
      now in question, and its "verify the 6th PIL against its own release" check is done.

- [ ] The wage beats the crop, in the survey that leaves the wage-earners out
      Source: NSS 77th Round Situation Assessment of Agricultural Households, NSSO/MoSPI
      — PIB PRID 1753856 (10 Sep 2021), fetched in full 2026-08-31. 🔴 PIB 302-redirects
      to `?PRID=<id>&reg=48&lang=2`; you need `curl -L` **and** a browser user-agent or
      you get a 174-byte "Object moved" stub. Vintage companion: PIB PRID 2003180
      (MoA&FW, 6 Feb 2024), the Lok Sabha reply confirming the 77th round is still the
      government's own latest figure. Underlying reports: NSS Report No. 587 (2018-19)
      and No. 576 (2012-13); microdata catalogued at microdata.gov.in (NOT probed today —
      do not promise unit-level cuts until it is).
      Argument: India's official measure of farm household income finds that wages are
      the largest single source — ₹4,063 a month against ₹3,798 from crop production on
      the paid-out basis, and ₹4,063 against ₹3,058 once imputed costs are charged, where
      wages are 49% of the ₹8,337 total and crops 37%. It reaches that result on a
      population the survey defines to *exclude* the households most dependent on wages:
      "households which were entirely agricultural labour households ... were kept
      outside the scope of the survey." The measure that anchors farm-income policy is
      therefore built on a sample tilted toward cultivation, and the wage still wins.
      Pairs with the published wage-index piece as its mirror image: that post is about
      the index setting what agricultural labourers are paid; this is the income survey
      that does not count them.
      Checks needed: (1) 🔴 VINTAGE — reference year is July 2018-June 2019 and there is
      no newer round; date every figure and never write "farmers today earn". (2) The two
      expense bases (paid-out only vs paid-out plus imputed) are different measures —
      never mix them in one sentence, and do NOT compute a 2012-13 → 2018-19 growth rate
      from ₹6,426 → ₹10,218 until the ₹6,426 figure's basis is confirmed from NSS Report
      576 itself, which was not checked. (3) "Agricultural household" is a survey
      construct — more than ₹4,000 of produce value plus a member self-employed in
      agriculture — not a synonym for "farmer"; define it in the first third of the piece.
      (4) The exclusion clause also removes coastal fishing, rural artisan and
      agricultural-services households; quote it whole rather than presenting it as an
      agricultural-labour exclusion alone. (5) Wages here are wage/salary income from any
      employment, farm or not — do not read ₹4,063 as farm wages. (6) The 8.2% landless
      figure is landlessness *within the surveyed population*, so it is not India's rural
      landlessness rate; attach the denominator.
      House style: cite `a-17-rural-pay-rise-that-nobody-received` as the blog's own
      earlier reporting, never as confirmation; `annadata-to-urjadata-farmer-income-case`
      is the other natural cross-link.
      Logged: 2026-08-31 from the NSS 77th Round register entry
      Opens: farm-household income *composition* — uncovered on bodies as well as titles
      (manifest 2026-08-31, 237 posts; the phrase "agricultural households" appears once
      in the entire corpus, incidentally). Note the survey's separate finding that 50.2%
      of agricultural households are indebted, ₹74,121 average outstanding, which is a
      second piece, not this one.

- [ ] The 4% every Indian insurance policy pays to one state reinsurer
      Source: IRDAI's annual obligatory-cession notification for FY 1 Apr 2025 – 31 Mar
      2026, quoted verbatim in Reinsurance News (fetched 2026-09-01) — "The percentage
      cession of the sum insured on each General Insurance Policy to be reinsured with the
      Indian Re-insurer(s) shall be 4% (four percent)...". Backing data: IRDAI Annual
      Report 2024-25 (free PDF, no login — 74 registered insurers/reinsurers as at
      31.03.2025, industry AUM ₹74.43 lakh crore). Segment data for the general-insurance
      side: General Insurance Council statistics (Flash Figures, Segmentwise Report, GIC
      Year Book 2024-25 PDF, all free, no login) — see the separate BACKGROUND entry.
      Argument: every general insurance policy written in India carries a compulsory 4%
      cession of sum insured to a single state-owned reinsurer, GIC Re — held at 4% for
      three consecutive years, down from 5%, with statutory minimums running to 15% on
      most classes. But the recipient's dependence on the mandate has moved sharply while
      the rate sat still: obligatory business was 30% of GIC Re's revenue in FY21, 43% the
      year before last, and 39% across April–October FY25. A compulsory transfer is
      usually reported as a fixed arrangement; the rate is fixed and the thing it does is
      not.
      Checks needed: (1) 🔴 pull the notification from irdai.gov.in itself — this reached
      the register through a trade publication quoting it, and the register's rule is that
      press attribution is not primary; (2) do NOT repeat the 5%→4% history until the year
      of that change is sourced, the article does not give it; (3) 43%→39% is an
      April–October part-year figure — never present it as a full-year share; (4) 4%
      cession is 4% of *sum insured per policy*, not 4% of industry premium — do not
      convert without the Annual Report's own tables; (5) source GIC Re's revenue split
      from GIC Re's own disclosures, not from the same article.
      Logged: 2026-09-01 from the IRDAI obligatory-cession register entry
      Opens: the wholesale/plumbing end of the near-empty *Insurance & Reinsurance* beat.
      Manifest dedup run 2026-09-01 (238 posts): `insur|reinsur|irdai|ifsca|gift.?city|
      solvency|actuar` returns exactly ONE post, `premium-now-claim-later-float-indias`
      (motor float — the retail side of the same balance sheet, and the natural
      cross-link). `irdai`, `ifsca`, `gift city`, `solvency`, `actuar`: zero hits each.
      Structural sibling: `who-collects-indias-gst-and-who`, same who-pays-vs-who-receives
      framing applied to a mandated transfer instead of a tax. Cite both as reporting,
      never as confirmation.


## Done

- [x] What a farm labourer earns, and why it stopped tracking output
      Published 2026-08-22 as "A 17% Rural Pay Rise That Nobody Received".

---

## Notes appended by the daily task

*(This file is append-only, so a superseded item is annotated here rather than edited or
moved above. Read this section before picking anything from Open.)*

- **2026-08-26 — "Does India have the feedstock for E20?" is superseded. Do not commission.**
  The blog answered it in `india-hit-e20-on-maize-and-rice-not`, published 2026-08-23 —
  after that queue item was logged on 2026-08-22. The post cites the same AERR paper by
  title and answers it on ESY 2025-26 data (grain 72.5% of allocation, cane 27.5%, maize
  45.7%, FCI rice 22.3%, ~1,048 of 1,776 crore litres allocated), which is a newer vintage
  than the AERR Vol. 37 No. 1 (2024) source the item was resting on. The residual angle,
  if one is wanted, is the food-security side the post states but does not develop — a
  fifth of the petrol blend drawn from the public foodgrain stock, tested against FCI's
  own stocking norms — and that needs the FCI stock series, not an ethanol series. Dedup
  first against `fci-grain-flow-procurement-storage` and
  `fci-storage-scenario-capacity-stock-and`.
  Logged from the 2026-08-26 register entry.
