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


- [ ] India built an offshore insurance hub. It writes USD 12 million of direct cover a year.
      Source: IFSCA Bulletin, Jan-Mar 2025 (International Financial Services Centres
      Authority, Division of Economic Policy and Analysis) — free PDF on the regulator's
      own domain, no login, explicit reproduction permission with acknowledgement:
      ifsca.gov.in/Document/ReportandPublication/ifsca-bulletin-jan-mar-202509052025055132.pdf
      (fetched 2026-09-08, HTTP 200, 4.6 MB; text extracts cleanly with `pdftotext
      -layout`). Tables used: Table 25 (line-of-business direct insurance) and Table 26
      (line-of-business reinsurance), both quarterly across FY 2024-25; Table 24 (offices
      and premium by IIO/IIIO). Quarterly series, so a current-vintage edition exists — a
      Jul-Sep 2025 bulletin is known to be out.
      Argument: GIFT IFSC is sold as an offshore insurance and reinsurance hub, and by its
      own quarterly tables it is only the second of those. Across the four quarters of
      FY 2024-25 it wrote USD 12.42 Mn of gross direct premium against USD 195.45 Mn of
      reinsurance — 94% of the book is cession business. Direct life for the entire year
      was USD 2.54 Mn, under Rs 25 crore, from a jurisdiction hosting 18 registered
      insurance offices; the whole insurance leg is about a five-hundredth of the USD
      88.51 Bn of banking assets on the same dashboard page. The centre did not fail to
      attract insurance. It attracted the wholesale end and almost none of the retail end
      it is marketed on — which is the same shape as the domestic story in the queued
      4%-cession piece, seen from the offshore side: India compels 4% of every general
      policy into a state reinsurer at home while the centre built to import international
      reinsurance capacity writes USD 195 Mn a year.
      Checks needed: (1) Table 24's Jan-Mar 2025 IIO figure carries a printed footnote —
      "Reinsurance data of one IIO is under examination and hence not included" — so that
      quarter is understated by an unknown amount; quote the share as ~94% and recompute
      when the audited figure lands; (2) every FY 2024-25 figure on both tables is marked
      unaudited — say so in the piece; (3) 🔴 Table 26 shows "Health + PA" falling 26.48 ->
      2.21 between Oct-Dec and Jan-Mar while a separate "Health Insurance" line appears at
      5.77 the same quarter — resolve this against the next bulletin before narrating
      either number, it looks like a reclassification and not a collapse; (4) Table 24
      counts offices, Tables 25/26 count lines of business — do not add or divide across
      them; (5) pull the following quarter's bulletin before publishing so the piece is not
      a year stale.
      Logged: 2026-09-08 from the IFSCA Bulletin register entry
      Opens: the IFSCA / GIFT City zero-coverage area, and the offshore half of the
      near-empty *Insurance & Reinsurance* label. Pairs with the queued 4%-cession item as
      two ends of one pipe; if both are written, write the domestic one first.
      Manifest dedup run 2026-09-08 (257 posts, snapshot 2026-09-07): a regex for
      `ifsca|gift.?city|reinsur|insur|bullion|fintech|offshore|banking.?unit` returns
      exactly one post, `premium-now-claim-later-float-indias` (motor float, domestic
      retail), matching on `insur` alone. `ifsca`, `gift city`, `bullion`, `offshore` and
      `banking unit` return zero.


- [ ] The Ministry of Power published two different AT&C loss figures for the same year
      Source: two PIB releases, both fetched directly 2026-09-09 (pib.gov.in returns 403 to
      a plain fetch; a browser User-Agent over curl returns 200). PRID 2200450, "Key
      Initiatives to Bring Down AT&C Losses of Power Distribution Utilities", 08 DEC 2025
      5:02PM, a written reply by the Minister of State for Power in the Rajya Sabha:
      AT&C losses "reduced from 21.91% in FY 21 to 16.16% in FY25". PRID 2215761, "Power
      Distribution Utilities Record Positive PAT After Years of Losses", 18 JAN 2026
      10:34AM, quoting the Union Minister of Power: AT&C losses "reduced from 22.62% in FY
      2013-14 to 15.04% in FY 2024-25". Same year, same ministry, 1.12 points apart, six
      weeks apart. Supporting figures from the January release: PAT +Rs 2,701 crore in FY
      2024-25 against -Rs 25,553 crore in FY 2023-24 and -Rs 67,962 crore in FY 2013-14;
      ACS-ARR gap Rs 0.78/kWh (FY 2013-14) to Rs 0.06/kWh (FY 2024-25). Underlying annual
      series is PFC's Report on Performance of Power Utilities, which neither release
      names and which is CURRENTLY UNREACHABLE — see the register's WEAK note; getting it
      is the first job.
      Argument: RDSS, the flagship distribution scheme with Rs 2.83 lakh crore sanctioned,
      targets a pan-India AT&C band of 12-15%. Whether it hit that target depends on which
      of its own ministry's two numbers you read: 15.04% lands just outside the band,
      16.16% misses by more than a point. The lower figure is the one in the celebratory
      press release; the higher one was given to Parliament six weeks earlier. The piece is
      not "the government is lying" — it is that a scheme graded on a ratio published two
      ways cannot be graded, and the blog can show exactly where the two series part.
      Checks needed: (1) THE PIECE DIES IF THE DENOMINATORS DIFFER — neither release states
      which utilities it counts (the January PAT line says "DISCOMs and power departments",
      the December AT&C line says only "distribution utilities at the national level"). If
      the coverage differs, this is a scope difference and not a contradiction; resolve it
      against the PFC report's utility count BEFORE writing a word, and if it resolves that
      way, write the scope-difference piece instead, which is still a piece. (2) FY25
      figures are provisional — PFC's FY 2023-24 edition covered 63 of 72 utilities with 52
      of 59 audited, so an FY25 number published in Dec 2025 cannot be firmer; say so.
      (3) AT&C is a ratio and the same January release credits the Electricity Distribution
      (Accounts and Additional Disclosure) Rules, 2025 and new subsidy-accounting rules —
      changes to how subsidy is booked move the ratio without recovering a stolen unit.
      (4) Do not narrate Rs 0.06/kWh as cost recovery achieved: it is a national average and
      suspiciously round. (5) The two releases use different baselines (FY21 vs FY 2013-14),
      so only the FY25 endpoint is a like-for-like clash — do not compare the trends.
      Cross-link to discom-debt-relief-token-charge in house style (cite the earlier post as
      reporting, never as confirmation): that calculator's standing premise is Rs 64,000
      crore of new discom debt every year, and a sector-wide positive PAT dates it — worth
      saying plainly, since it is the blog's own number.
      Logged: 2026-09-09 from the PIB AT&C register entry
      Opens: the electricity-distribution / grid area — 93 of 257 posts are energy, but a
      precise regex (discom|at&c|electricity|power utilit|rdss|smart meter|kwh) returns
      exactly ONE, and that one is a calculator. The blog covers the molecule side of
      energy exhaustively and the electron side almost not at all.

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

- **2026-09-03 — the PPV&FR item's outstanding checks could NOT be advanced today; both
  primaries were down.** The Thursday daily run tried to resolve check (2) on the open
  "57.8% of India's plant-variety rights are cereals" item — the unverified
  "4,847 of 9,210 certificates (52.6%) went to farmers" split that came only from a
  search snippet. `https://plantauthority.gov.in/` and
  `https://plantauthority.gov.in/plant-varieties-registry-related-information` both
  returned **HTTP 503** on direct fetch. The split therefore remains **unverified** and
  the standing instruction stands: confirm it from the Annual Report PDF or drop it
  entirely — do not repeat it on snippet authority.
  Operational consequence for whoever writes this piece: the homepage certificate counter
  is a **live counter on an intermittently unavailable NIC host**, with no vintage
  archive. Do not plan the piece around fetching it at publication time. Pull the figures
  once, date-stamp them in the text, and hold the Annual Report PDF locally as the
  citable artefact. The 2026-08-27 direct-fetch figures in the item above remain the
  best record we have precisely because they were captured when the host was up.


- [ ] India tested its soil twice. The second time, a machine chose the spot.
      Source: Soil Health Card portal, `soilhealth.dac.gov.in` (DA&FW / NIC) — the
      Nutrient Dashboard, whose data comes from the app's own Apollo GraphQL endpoint
      `https://soilhealth4.dac.gov.in` (verified live 2026-09-04: portal and dashboard
      HTTP 200, endpoint answers a bare GET with HTTP 400, i.e. up and awaiting a
      well-formed query). The card carries 12 parameters including **OC (Organic
      Carbon)**. Primary narrative source: **PIB PRID 2104403, Ministry of Agriculture &
      Farmers Welfare, "Celebrating a Decade of Soil Health Cards", 18 February 2025**
      (fetched in full 2026-09-04). Policy frame: Rattan Lal, "Soil Carbon in
      Agro-Ecosystems of India", JISSS 74(1) 2026, open access on epubs.icar.org.in.
      Argument: the Soil Health Card scheme has been measuring organic carbon on every
      card since 2015, but in **April 2023** the portal was rebuilt — the mobile app now
      restricts the operator's sample-collection region, auto-captures latitude and
      longitude, and QR-links each sample to a geo-mapped lab "without any manual
      intervention", with map layers down to cadastral boundary. Samples before that were
      sited and keyed by hand. So India's only national soil panel has a seam running
      through it, and any district organic-carbon trend that crosses April 2023 is
      comparing two different collection regimes before it is comparing two soils — which
      is a problem for the ICAR-study headlines about declining SOC that are currently
      circulating without anyone naming the seam.
      Checks needed: (1) 🔴 **BLOCKING — pull an actual district-level organic-carbon
      table from the dashboard before writing a word about levels or trends.** The
      endpoint is live but no query has been run; if the public dashboard turns out to be
      state-level only, or auth-walled, the piece becomes a shorter methods note and the
      argument must be rebuilt around the PIB release alone. (2) 🔴 Do **not** use the
      "254,236 samples, 620 districts, 29 states" ICAR figure — it came only from coaching
      sites today and is unverified; trace it to IISS Bhopal or drop it. (3) PIB PRID
      2104403 gives no national cards-issued or samples-tested count — get those from the
      portal or a dated Lok Sabha answer, never from the release. (4) pib.gov.in needs a
      browser user-agent and `-L`; a plain fetch gets 403 and a UA-less curl gets 302.
      (5) The April-2023 seam is a **plain reading of the release's own description of the
      change**, not a claim the government makes about comparability — write it as the
      former and say so. (6) Cross-link `indias-79-lakh-crore-rural-water` in house style
      (that is drinking water under a different ministry — cite as earlier reporting,
      never as confirmation).
      Logged: 2026-09-04 from the Soil Health Card register entry
      Opens: the **soil** half of the Friday zero-coverage area (irrigation is already
      opened by the Minor Irrigation Census item). Manifest dedup 2026-09-04: 255 posts,
      6 title hits on water/soil terms, none about soil or agricultural water.

- **2026-09-07 — the PPV&FR item's two outstanding checks are RESOLVED. One of them
  changes a number the piece would otherwise have got wrong.** `plantauthority.gov.in`
  was up today (HTTP 200, 171,508 bytes, browser UA) after the 503 recorded on
  2026-09-03, and both charts were fetched directly.
  **Check (1) — vintage — is satisfied and no longer needs hand-dating.** The homepage
  now states its own as-on date in both chart headings: "10885 Certificates issued as on
  **31.08.2026**". Crop groups on that date: Cereals **6,280** · Vegetables 1,386 ·
  Fibre 1,006 · Legumes 872 · Oilseeds 577 · Fruits 429 · Sugar 93 · Other 242.
  Cereals **57.7%** — the queued headline survives on the newer vintage (it was 57.8%,
  6,246 of 10,802, as on 31.07.2026). The two captures reconcile exactly: the month's
  +83 certificates distribute as cereals +34, vegetables +19, fibre +17, legumes +6,
  fruits +4, other +3, and today's single "Other" (242) matches the five small
  categories broken out on 31.07 (Spices 151 + Trees 43 + Flowers 36 + Cash 5 +
  Medicinal & Aromatic 4 = 239). ⚠️ **But today's homepage no longer breaks out spices**,
  so "Spices get 151" in the working title is now only available from the 2026-08-27
  capture or the Annual Report — do not plan to re-fetch it.
  **Check (2) — the farmer split — is resolved, and the unverified figure was wrong in
  the direction that matters.** Registration-type series as on 31.08.2026: **Farmer
  5,368** · Extant Notified 2,025 · New 1,921 · Extant VCK 1,557 · EDV 14, summing
  independently to the same 10,885. Farmers' varieties are **49.3% — just under half.**
  The circulating "4,847 of 9,210 (52.6%) went to farmers" snippet is superseded; had it
  been used, the piece would have claimed a majority that the Authority's own figure does
  not support. **Use 5,368 of 10,885 as on 31.08.2026, and say "just under half".**
  **New material worth putting in the piece:** essentially derived varieties account for
  **14 certificates, 0.13%**, in a register issuing since 2007 — while the same homepage
  carries a live notice, "General Guidelines Regarding the Registration of EDV". EDV is
  the doctrine deciding whether a variety bred from a protected variety needs the original
  breeder's authorisation, i.e. who captures the value of incremental breeding. This pairs
  with the AERR 36(1):77-86 (2023) concept citation already on the item.
  **Checks that still stand:** (3) certificates issued ≠ varieties commercially sold;
  (4) the categories are the Authority's own and undefined on the page — and this now
  applies to the registration-type split too, whose labels come from hidden inputs on the
  same page. The Annual Report 2024-25 PDF remains the citable artefact and the
  cross-read is still worth doing. 🔴 The figures above are **chart literals embedded in
  homepage JavaScript**, not a published table: primary and internally consistent across
  two series and two dates, but pull and keep a local copy — the host is intermittent
  (200 today, 503 four days ago).
  Logged: 2026-09-07 from the PPV&FR registry register entry.

- **2026-10-07: "India built an offshore insurance hub…" is PUBLISHED. Stop treating it as
  Open.** It went out 2026-09-18 as `india-built-offshore-insurance-hub-it`, but the
  `- [ ]` entry above was never ticked (append-only file).
  **New update item, not a new article:** refresh that post against the IFSCA Bulletin, Q1
  FY 2026–27 (see SOURCE_REGISTER, 2026-10-07).
  - FY26 direct GWP is USD 40.72 Mn, not 12.42, so the headline number is stale.
  - Reinsurance share is 93.7% (was 94.0%), so the argument survives.
  - Direct life is 19.43 Mn for FY26 and 13.25 Mn in Q1 FY27 alone.
  - Suggested form: a dated update box under the headline. Do not rewrite the post.
  - Checks: (1) unaudited, so say so; (2) do not annualise Q1 FY27's USD 400.30 Mn
    reinsurance, which is driven by Life and Trade Credit treaties; (3) never add IIIO
    transacted premium (481.36) to IIO written premium; (4) re-read the post's own checks
    1 and 3. The Jan–Mar 2025 "one IIO under examination" understatement is now superseded
    by FY26 data.

- **2026-10-09: "57.8% of India's plant-variety rights are cereals. Spices get 151." is
  PUBLISHED. Stop treating it as Open.** It went out 2026-09-17 as
  `577-of-indias-plant-variety`; the `- [ ]` entry above was never ticked (append-only file).
  **Update item, not a new article:** the Authority's homepage now reads "10981 Certificates
  issued as on 30.09.2026" (SOURCE_REGISTER, 2026-10-09).
  - Cereals 6,324 of 10,981 = **57.6%** (post: 57.7%). Spices **still 151**. Headline holds.
  - 🔴 The registration-type pie and the year-wise chart on the same page are still the
    31.08.2026 series (sum 10,885). Keep the farmer share at 49.3% **as on 31.08.2026**; do
    not divide 5,368 by 10,981.
  - Suggested form: a dated update box under the headline, two sentences. Do not rewrite.
  - Checks: (1) pull and keep a local copy of the page the day you write; (2) say the crop
    and type series carry different as-on dates; (3) the two "Plantation crop" boxes (7 and
    5) cannot be assigned to Cash vs Medicinal & Aromatic from the page — leave them lumped.

- [ ] Half of India's plant-variety certificates were issued in the last three years.
      Source: PPV&FR Authority homepage, year-wise "Certificates Issued" chart (literal in
      page JavaScript), as on 31.08.2026: 2023 1,259 · 2024 2,017 · 2025 2,073 against a
      2009–2022 run that never exceeded 833 (2014) and fell to 265 in 2022. 2023–2025 =
      5,349 of 10,885 = 49.1%. See SOURCE_REGISTER 2026-10-09, Finding 3.
      Argument: the register that the 2026-09-17 piece described as cereal-heavy and
      spice-light has also, very recently, changed speed — and whether that is new breeding
      or an administrative backlog being cleared decides what the piece can claim.
      Checks needed: (1) applications-filed series from the PPV&FR Annual Report (2023-24
      PDF is on the site; 2024-25 cited by the published post) — if filings did not jump,
      this is clearance, not activity; (2) which registration type drove 2023–25 (farmer vs
      new vs extant) — monthly Plant Variety Journal or the `/list-certificates?name=`
      pages; (3) explain the 2022 trough (265); (4) re-fetch the chart on writing day and
      date-stamp it — the series lags the headline counter by a month on 2026-10-09;
      (5) the 2026-10-01 register already saw a snippet claiming "half in the last two
      years" on a 9,210 base — cite the primary, not the snippet.
      Logged: 2026-10-09 from the PPV&FR homepage register entry.
      Extends: `577-of-indias-plant-variety` (2026-09-17). Area no longer zero-coverage;
      manifest dedup 2026-10-09: 346 posts, 4 under Seeds & Plant Genetics, none on issuance
      volume.

### 2026-10-26 batch: ministry documents published Sep–Oct 2026

Found through the ministry-by-ministry document index (95,995 documents across 85 union
ministry and department sites, `/Users/Shared/india_ministry_sites_2026-10-26/`), filtered to
substantive documents dated September–October 2026 on the blog's beats. Each primary document
below was downloaded and read (scanned ones by OCR); local copies are in that folder's
`article_sources/`. Manifest dedup 2026-10-26: 420 posts, none on any of the ten; none in this
queue or SOURCE_REGISTER.

- [ ] India is ordering captive coal plants to run flat out.
      Source: Ministry of Power, directions under Section 11 of the Electricity Act, 2003 to
      generating companies owning captive plants, 25 Sep 2026
      (https://powermin.gov.in/static/uploads/2026/09/1c9e465d38785fe239f2aef55220d076.pdf):
      captive coal plants of 50 MW and above to "operate and generate power to the maximum
      extent of their available capacity" and offer surplus through the power exchanges; plant
      list in the annexure. Same day: Section 11 directions to the CGPL (Mundra) imported-coal
      plant extended to 31 Dec 2026, after earlier validity to 30 Jun and 30 Sep 2026
      (https://powermin.gov.in/static/uploads/2026/09/5eab55faac0030c9fe0950ea40c5547e.pdf).
      Argument: two emergency must-run orders in one day, the third extension for Mundra, show
      the ministry treating autumn 2026 as a supply squeeze, and captives are now being drafted
      as merchant capacity.
      Checks needed: (1) count the annexure (plants, MW) from the PDF; (2) peak demand and
      shortage data (Grid India daily reports) for Sep–Oct 2026; (3) exchange prices before and
      after 25 Sep (IEX/PXIL); (4) whether earlier Section 11 captive orders exist and how they
      ended; (5) Coal Ministry October notes say plant stocks are "stable above 18 MT", so
      reconcile shortage with stock.
      Logged: 2026-10-26 from the ministry document index (powermin).
      Extends: `the-ministry-of-power-published-two` (2026-09-19).

- [ ] India now has two coal exchanges waiting for a licence.
      Source: Coal Controller Organisation notices inviting stakeholder suggestions under rule
      8(1) of the Coal Exchange Rules, 2026 (notified 4 Jun 2026; registration portal live
      15 Jul 2026) on applications from Indian Coal Exchange Ltd (CIN U66190DL2026PLC467125,
      incorporated 01/06/2026; notice dated 1 Oct 2026,
      https://coal.nic.in/sites/default/files/2026-10/15-10-2026a-wn.pdf) and from MCXCEIL
      (second notice, same listing on coal.nic.in). Context: draft Colliery Control (Amendment)
      Rules, 2026 consultation (https://coal.nic.in/sites/default/files/2026-10/16-10-2026a-wn.pdf).
      Argument: exchange trading would be the first price-discovery market for Indian coal,
      replacing an allocation-and-notified-price system, and both applicants appeared within
      weeks of the portal opening.
      Checks needed: (1) owners and promoters of each applicant (MCA filings; MCXCEIL is
      presumably MCX-linked, confirm); (2) what the Rules allow to be traded and by whom;
      (3) the 30-day comment window dates; (4) don't call either a licensed exchange until
      registration is granted.
      Logged: 2026-10-26 from the ministry document index (coal).
      Extends: `india-has-auctioned-141-commercial-coal` (2026-10-09).

- [ ] The phone PLI's replacement pays 2.75% and wants the battery made in India.
      Source: MeitY, Scheme Guidelines, Mobile Phone Manufacturing Scheme, Target Segment-1
      (gazette CG-DL-E-21082026-275648, 21 Aug 2026; guidelines posted 6 Oct 2026),
      https://www.meity.gov.in/static/uploads/2026/10/0e56b4295930f4a180b399d440ae3690.pdf
      (scanned; read by OCR). Para 9: incentive on eligible sales up to the FY24–FY26 average
      minus baseline at 2.75% (FY27, FY28), 2.5% (FY29, FY30), 2.25% (FY31); additional rates
      for domestic sourcing of display module 0.30%, camera module 0.30%, enclosure 0.50%,
      batteries incl. cells 0.20% (USB cables also listed).
      Argument: the successor to the smartphone PLI is cheaper per rupee of sales and moves the
      reward from assembly volume to local components, so the question is whether 0.2–0.5% is
      enough to pull display, camera and cell making into India.
      Checks needed: (1) re-read para 9.1(ii) rates for sales above the 9.1(i) band (OCR
      garbled them); (2) total outlay and tenure from the gazette notification;
      (3) compare with the old PLI's 4–6% rates and actual disbursals; (4) TradeStat imports of
      the named sub-assemblies (display, camera module, cells).
      Logged: 2026-10-26 from the ministry document index (meity).
      Extends: `nine-ministries-one-list-every-company` (2026-08-30).

- [ ] From June, rooftop solar needs Indian cells. Here is who makes them.
      Source: MNRE, ALMM List-II (solar PV cells), 12th revision dated 08.10.2026,
      https://mnre.gov.in/static/uploads/2026/10/d1f27eb73e8b4201c6fb42266f109bdc.pdf
      (text PDF; manufacturer, plant, capacity tables); MNRE OM 283/53/2026-GRID SOLAR,
      18 Jul 2026, https://mnre.gov.in/static/uploads/2026/10/ff10a64fa507f3e79029ecabb73c053d.pdf
      (scanned; OCR): no blanket extension of List-II; net-metering and open-access projects
      commissioned on or after 18 Jun 2026 must use List-II cells, with a limited window to
      commission without them until 31 Dec 2026.
      Argument: the domestic-cell mandate has now started for rooftop and open access, and the
      enlisted cell capacity, not module capacity, is the number that decides whether projects
      can be built on time.
      Checks needed: (1) sum enlisted cell capacity (GW) and count manufacturers from the 12th
      revision; (2) compare with module List-I capacity and annual installations; (3) how the
      window's conditions are worded (which projects qualify); (4) earlier revisions for a
      growth series.
      Logged: 2026-10-26 from the ministry document index (mnre).
      Extends: `the-solar-panel-recycling-opportunity` (2026-09-11),
      `indias-battery-storage-boom-is` (2026-09-11).

- [ ] Power lines now pay more for land than pipelines do.
      Source: Ministry of Power, Guidelines for payment of compensation for Right of Way for
      transmission lines, F.No. 3/4/2016-Trans-Part(4), 6 Oct 2026,
      https://powermin.gov.in/static/uploads/2026/10/0e00977da34887886bdbb05757ec76d9.pdf
      (scanned; OCR). Compensation based on circle rate unless market rate is higher; market
      rate = average of three valuations, with the highest and lowest normalised to ±20% of the
      median (worked illustration gives ₹51.67 lakh); tower-base area compensated at 200% of
      market value (base = area inside the four legs plus 1 m on each side).
      Argument: wires have moved to a market-rate, multi-valuer formula with a 2x tower-base
      premium, so the comparison with the Right-of-User rules for gas pipelines is the story.
      Checks needed: (1) corridor (line-span) compensation percentage from the full text;
      (2) earlier versions (14.06.2024, 21.03.2025, 15.12.2025 letters) for what changed;
      (3) PNG Pipelines (Acquisition of RoU) Act rates for the comparison; (4) whether states
      must adopt it (it is addressed to Chief Secretaries).
      Logged: 2026-10-26 from the ministry document index (powermin).
      Extends: `right-of-user-what-indias-pipeline` (2026-09-05),
      `green-energy-corridor-iii-is-15-times` (2026-10-09).

- [ ] India is renaming its shrimp regulator and giving it every fish pond.
      Source: Department of Fisheries, draft Coastal Aquaculture Authority (Amendment) Bill,
      2026, posted for comments 29 Sep 2026,
      https://dof.gov.in/static/uploads/2026/10/97be78526647bdf21d0f6e20d8cdf6a7.pdf: renames
      the Coastal Aquaculture Authority Act, 2005 the "Aquaculture Authority of India Act, 2026"
      and applies it to "all forms of aquaculture and allied activities in inland, coastal and
      marine areas".
      Argument: a regulator built for coastal shrimp farms would take in inland aquaculture,
      most of India's fish farming by area, so registration, inputs and antibiotic rules written
      for export shrimp would reach inland farms.
      Checks needed: (1) the bill's registration, penalty and inputs clauses in full; (2) inland
      vs coastal aquaculture production and area (Handbook of Fisheries Statistics); (3) the
      comment deadline; (4) state fisheries acts it would overlap.
      Logged: 2026-10-26 from the ministry document index (dof).
      Extends: `indias-shrimp-exports-did-not-collapse` (2026-08-23).

- [ ] To sell meat and milk abroad, India is fencing off FMD-free farms.
      Source: Department of Animal Husbandry and Dairying, Guidelines for establishment of Foot
      & Mouth Disease (FMD) Free Compartments in India, 13 Oct 2026,
      https://www.dahd.gov.in/static/uploads/2026/10/5944939d829dc13828f756bf105513f4.pdf:
      compartments "with vaccination", under the WOAH Terrestrial Animal Health Code; aims
      include improving international trade of animal products; national FMD programme
      WOAH-endorsed since 2015, mass vaccination since 2019.
      Argument: compartmentalisation lets individual farm clusters prove disease freedom
      without the whole country being FMD-free, which is the route into markets closed to
      Indian dairy and meat.
      Checks needed: (1) which markets accept FMD-free-with-vaccination compartments and for
      which products; (2) how a compartment is certified, by whom, and the cost; (3) buffalo
      meat and dairy export destinations (APEDA / TradeStat); (4) any compartment already
      applied for.
      Logged: 2026-10-26 from the ministry document index (dahd).
      Extends: `indias-animal-protein-export-complex` (2026-08-05),
      `the-milk-india-doesnt-drink-cheese-and` (2026-08-19),
      `india-imports-whey-protein-its-cheese` (2026-10-22).

- [ ] NITI's data-centre checklist starts with the grid, then the water.
      Source: NITI Aayog, Data Centre Evaluation Framework to Help States Plan for Sustainable
      Growth, Oct 2026,
      https://www.niti.gov.in/sites/default/files/2026-10/Data-Centre-Evaluation-Framework-to-Help-States-Plan-for-Sustainable-Growth.pdf:
      at site selection, developer, DISCOM and STU to jointly validate a "Power Readiness and
      Ramp-up Plan" (total campus demand, sanctioned MW, year-wise energisation, substation and
      transmission); treat large data centres as grid-interactive loads capable of demand
      response; cites Virginia, Dublin, Amsterdam, Johor and Bangkok as cases where capacity
      outran grid, water and land.
      Argument: the central planning body is telling states to price grid and water capacity
      into data-centre incentives before signing them, the opposite of the current subsidy race.
      Checks needed: (1) the framework's water (WUE) and PUE thresholds, if any; (2) which state
      data-centre policies already require any of this; (3) announced DC capacity by state
      (MW); (4) keep it as a framework for states, not a mandate.
      Logged: 2026-10-26 from the ministry document index (niti).
      Extends: `028-unit-diesel-math-behind-indias-data` (2026-08-20).

- [ ] What a kilometre of metro should cost, according to the ministry that pays for it.
      Source: MoHUA, Report on Benchmarking for Cost Estimation of Metro Rail Projects, and
      Appraisal Guidelines for Metro Rail Project Proposals, both 30 Sep 2026,
      https://mohua.gov.in/static/uploads/2026/10/9973d066e44c1e52dff6fed68392e011.pdf: per
      route-km and per-station norms, e.g. utility shifting (civil and E&M combined) up to
      ₹6 crore per route-km, multimodal station provision ₹3 crore per station.
      Argument: published benchmark costs give a yardstick for every sanctioned metro DPR, so
      the piece can show which approved projects sit above or below the ministry's own norms.
      Checks needed: (1) full benchmark table (elevated vs underground, per km); (2) price base
      year of the benchmarks; (3) sanctioned costs and lengths of recent approvals (Cabinet
      press releases); (4) do not compare across price years without indexing.
      Logged: 2026-10-26 from the ministry document index (mohua).
      Extends: `indias-reported-central-project-overrun` (2026-10-09).

- [ ] Round III of coal gasification opens its bids. (Hold until results.)
      Source: Ministry of Coal (CCT Section), Financial Incentive Scheme for Coal/Lignite
      Gasification (₹8,500 crore), Round III, Categories II and III, notice of 13 Oct 2026
      (https://coal.nic.in/sites/default/files/2026-10/13-10-2026a-wn.pdf): technical bids,
      invited by notification of 13 Aug 2026, opened 14 Oct 2026 via MSTC.
      Argument: who bids in Round III, and for which products, tests the coal-to-chemicals
      rankings the blog published in August against real investment decisions.
      Checks needed: (1) the 13 Aug 2026 bid notification (categories, caps); (2) Round I and II
      awardees; (3) wait for the technical/financial evaluation results; (4) map any awardee
      products onto the August post's import-price ranking.
      Logged: 2026-10-26 from the ministry document index (coal).
      Extends: `indias-coal-to-chemicals-menu-ranked-by` (2026-08-27).

- **2026-10-26 (later): corrections to three entries in the 2026-10-26 batch, found while drafting.**
  Drafts of four entries now exist as unpublished Blogger drafts (`out/new-posts-2026-10-26/`,
  ids in `blogger_drafts.json`): captive coal, phone scheme, ALMM List-II, transmission RoW.
  - Phone scheme: the headline rates are **5% (FY27, FY28), 4.5% (FY29, FY30), 4% (FY31)** under
    para 9.1(ii); the 2.75%→2.25% schedule applies only to the 9.1(i) band. Domestic-sourcing
    top-ups total 1.5% (USB cables 0.20% too) and need ≥25% localisation. Read from page 7 of 18.
  - ALMM List-II: the mandate applies to net-metering/open-access projects commissioned on or after
    **1 June 2026**, not 18 June (OCR misread the superscript "st"). Read from the OM's page image.
  - CGPL (Mundra): 31 Dec 2026 is the **second** extension of the Section 11 order (30 Jun → 30 Sep
    → 31 Dec), not the third.

- **2026-10-26: four entries of the 2026-10-26 batch are PUBLISHED. Stop treating them as Open.**
  - Captive coal must-run → `india-ordered-112-captive-coal-plants`
  - Phone scheme → `the-phone-plis-successor-pays-up-to-5`
  - ALMM List-II cells → `indias-approved-solar-cell-makers-can`
  - Transmission RoW → `a-hectare-under-power-line-now-pays`
  Still open from that batch: coal exchanges, aquaculture authority bill, FMD-free compartments,
  NITI data-centre framework, metro cost benchmarks, coal gasification Round III (hold for results).

- [ ] India's first revived urea plant has lost ₹7,954 crore to the technology it bought
      Source: Standing Committee on Chemicals and Fertilisers, report on fertiliser logistics and
      forced bundling, presented 6 Aug 2026, read via the PRS summary (prsindia.org, fetched
      2026-10-29). Primary PDF on eparlib.sansad.in: fetch_source.sh returned no content today, so
      retry, or pull it from the sansad.in committee-reports page. Supporting: RFCL's filed annual
      accounts (MCA) for FY22–FY25; DoF plant-wise production; the 15th Report (self-sufficiency,
      1 Dec 2025) for the 27-of-33-plants-over-25-years context.
      Argument: the five-plant FCIL/HFCL revival the blog has followed since the Parliament-questions
      piece is now producing checkable numbers, and the first one is a loss. RFCL, running since
      2021, carries an estimated ₹7,954 crore revenue loss to November 2025 from recurring
      technology failure, while DAP capacity utilisation nationally fell from 87.5% to 67.8% in
      three years. The committee's remedy, performance guarantees and warranty obligations in
      future technology transfers, is an admission that the revival contracts had none.
      Checks needed: (1) 🔴 fetch the report and quote the RFCL paragraph; establish whether ₹7,954
      crore is foregone revenue at nameplate or an accounting loss, and against which capacity;
      (2) RFCL's own filed accounts for the loss and utilisation, never the committee's estimate
      alone; (3) 67.8% is ten months of 2025-26, say so; (4) name the technology licensor from
      RFCL's own disclosures, not press; (5) keep forced bundling out of this piece, since
      `nano-urea-works-as-supplement-and-fails` already covers the FCO amendment; (6) house style:
      cite `thirty-one-years-of-asking-parliament`, `nature-versus-nurture-indias-fertiliser`
      (whose plant table calls RFCL "Operational" without qualification) and
      `the-reactor-nobody-names-how-coal` as the blog's own earlier reporting, never as
      confirmation; (7) rule 8 applies: the piece needs a "What would fix this" section.
      Logged: 2026-10-29 from the Standing Committee logistics-report register entry
      Extends: the fertiliser beat's plant-performance gap. Two published posts ask DoF to publish
      plant-wise utilisation; this report is the first official answer. Posts dedup 2026-10-29:
      `Ramagundam` in 3 posts (tables and a pipeline map); the loss figure and DAP utilisation in
      none.
