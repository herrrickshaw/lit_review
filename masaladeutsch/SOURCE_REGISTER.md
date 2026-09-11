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

### PPV&FR Authority registration data (Protection of Plant Varieties and Farmers' Rights Authority, MoA&FW)
India's plant-variety-rights registry. The homepage carries a live certificate counter
with a crop-category breakdown, **verified by direct fetch on 2026-08-27**: **10,802
certificates issued as of 31.07.2026** — Cereals 6,246, Vegetables 1,367, Fibre Crops 989,
Legumes 866, Oilseeds 577, Fruits 425, Spices 151, Sugar Crops 93, Trees/Forest 43,
Flowers 36, Cash crops 5, Medicinal & Aromatic plants 4.
- **Data**: Annual Report 2024-25 — free PDF, **no login, no payment**, 22.77 MB, at
  `plantauthority.gov.in/sites/default/files/annual-report-2024-25-english.pdf` (link
  verified on the report's landing page). Also free and public: the *Plant Variety
  Journal* (monthly, latest Vol. 20 No. 07, July 2026), the *Compendium of Varieties
  Registered under PPV&FR Act, 2001*, Gazette Notifications, and Public Notices
  2007-2025. Login is required only for PARV, the online **application** system — not
  for any of the published data. Gazette Notification G.S.R. 483(E) of 4 July 2025
  (PPVFR Amendment Regulations 2025) is the most recent rule change.
- **Finding**: the distribution is extraordinarily lopsided. Cereals alone hold **6,246
  of 10,802 certificates — 57.8% of every plant-variety right India has ever granted**.
  Against that, spices have 151 and medicinal & aromatic plants have 4. The blog has
  already published that spices are a **$4.45 billion export book across eight crops in
  eight states** (`indias-445-billion-spice-export-book-is`); that entire export book
  rests on 151 registered varieties. The juxtaposition is the piece, and both halves are
  primary-sourced — one from this registry, one from the blog's own prior work.
- **Blog fit**: opens the **confirmed zero-coverage seeds / plant-variety-rights /
  agricultural-IP area**. Dedup was run against `meta/manifest.json` (217 posts,
  snapshot 2026-08-27T04:20): a regex for seed/variety/germplasm/breed/PPVFR/patent/
  ICAR/hybrid/cotton/plant returned **2 hits, both false positives** —
  `the-cbg-incentive-stack-every-leg-of` and `india-will-finance-waste-to-energy`, where
  "plant" means an industrial facility. Coverage of this subject is genuinely zero.
  It extends the existing crop-economics beat, whose nearest published neighbours are
  `379-kilos-hectare-in-punjab-44-in` (input use mapped by crop and state) and
  `indias-445-billion-spice-export-book-is`.
- **Caveat**: four things need checking before publication. (1) The homepage counter is
  a **live figure with no vintage archive** — it must be screenshotted or cross-read
  against the Annual Report PDF, and dated in the piece, or it becomes unverifiable
  later. (2) A widely-repeated split — 19,888 applications filed, 9,210 certificates, of
  which **4,847 (52.6%) registered by farmers** rather than companies — appeared only in
  a search-result snippet and **was NOT verified against any page fetched today**. It is
  the more striking claim of the two and must be confirmed from the Annual Report PDF
  before it is used at all. (3) "Certificates issued" is not "varieties commercially
  sold" — registration is a legal act, not a market outcome, and the piece must not
  elide them. (4) The crop-category counts sum to 10,802 exactly, so the breakdown is
  complete, but the categories are the Authority's own and their boundaries are
  undefined on the homepage.
- **Grade: COMMISSIONABLE.**


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

### Minor Irrigation Census, 6th round (Ministry of Jal Shakti, DoWR-RD&GR) + AERR irrigation-recovery paper
Paired source: one census that counts who actually owns India's irrigation, one
peer-reviewed paper that measures what the public money bought. Neither is on the blog.
- **Data**: **free, no login, no payment — all verified by direct download 2026-08-28.**
  The census document portal `mowr.nic.in/irrigationcensus/` returns HTTP 200 and links
  direct PDFs under `Documents/MI-Census/Reports/`: `6-MI-Report-All-India-Vol-I.pdf`
  and `6-MI-Report-State-Wise-Vol-II.pdf` both fetch as real PDFs (ranged GET returned
  HTTP 206, `application/pdf`, valid PDF 1.6). Every earlier round is there too —
  `Files/5th-MICensusReport.pdf`, `4thmicensusreport.pdf`, `Third-MI-report.pdf`, the
  2nd in six parts — so a **six-census series from reference year 1986-87 to 2017-18**
  is obtainable, which is what makes a trend argument possible rather than a snapshot.
  The primary release is PIB PRID **1952480**, Ministry of Jal Shakti, **26 Aug 2023**,
  fetched in full 2026-08-28 (needs a browser user-agent; plain fetchers get 403 —
  consistent with this register's standing PIB note).
  The AERR paper is **Seema Bathla, Elumalai Kannan & Gautam Kumar Das, "Public
  investment in irrigation across the Indian states: Financial recovery and governance",
  *Agricultural Economics Research Review* 37(1), pp. 93-112, 2024**
  (`epubs.icar.org.in/index.php/AERR/article/view/154839`). ⚠️ Abstract is public but
  **the full-text PDF is NOT freely downloadable** — the article page exposes only
  BibTeX/RIS citation exports, no PDF galley link, and the issue page redirects to a
  login screen. Treat it as a **concept citation**, not a data source.
- **Finding**: the census numbers, verbatim from the release. India has **23.14 million
  minor irrigation schemes; 21.93 million (94.8%) are groundwater** and only 1.21 million
  (5.2%) surface water. **96.6% of all MI schemes are under private ownership** — 98.3%
  of groundwater schemes, 64.2% of surface water. Of schemes with a single source of
  finance (60.2% of the total), **79.5% are financed by the individual farmer's own
  savings**. 97.0% are 'in use'. 18.1% of individually-owned schemes are owned by women
  (collected for the first time in this round). Growth over the 5th census: +1.42 million
  schemes, groundwater +6.9%, surface water +1.2%.
  Set against that, AERR's abstract reports that across **20 states, 1981-82 to 2019-20**,
  "increasing public capital formation in irrigation has **barely corresponded** with the
  outcomes in terms of net irrigated area, potential utilised, and rate of financial
  recovery" — while agriculturally advanced states spend *more*, not less. The census
  explains why the two can both be true: the state is capitalising the 5% of schemes it
  owns, and the country irrigates itself off the other 95%, out of pocket.
- **Blog fit**: opens the **confirmed zero-coverage "irrigation investment and
  governance" area** (LITERATURE_SURVEY §3), and puts a second post in the "water"
  band, which the survey scored at 2 hits in 192 titles. Dedup run against
  `meta/manifest.json` (**219 posts, snapshot 2026-08-28T07:27**): a regex for
  water/irrigat/soil/groundwater/aquifer/canal/drip/watershed/borewell/tubewell/
  reservoir/rain returned **8 title hits, none about irrigation**. Nearest published post
  is `tamil-nadus-water-infrastructure-runs` (25 Aug 2026) — checked by reading the post
  body, not by title: it is **urban municipal** water finance (KfW SMIF-TN tranches, tank
  desilting) and contains **zero** occurrences of irrigation, groundwater, tubewell or
  dugwell. It is a strong cross-link rather than an overlap, because it makes the same
  shape of argument — the headline water number not matching the money underneath.
  Others in the 8: `the-water-bill-nobody-mentions-what` (Taiwan fabs),
  `price-is-wire-how-gcam-actually-links` (GCAM modelling),
  `guar-gum-indias-35-billion-export-peak` ("poor soil" in the title only).
- **Caveat**: 🔴 **vintage — a 7th census exists and is partly published.** The 6th
  census reference year is **2017-18** (released Aug 2023), so the headline figures are
  eight years stale on the ground. `7-MI-Report-State-Wise-Vol-II-Part-1.pdf` fetches
  (HTTP 206, valid PDF) but `7-MI-Report-All-India-Vol-I.pdf` returns **404**, and the
  7th MI Census is running jointly with the 2nd Census of Water Bodies, 1st Census of
  Major & Medium Irrigation Projects and 1st Census of Springs at
  `wrcensus.mowr.gov.in` — i.e. still in progress. Any piece must date the 6th-census
  figures explicitly and check the 7th before publication; the all-India 7th totals
  were **not** obtainable today and must not be guessed at.
  Second caveat: the **village-level microdata is not confirmed obtainable**. The
  data.gov.in catalog page is JS-rendered with no resource hrefs in the HTML, and the
  catalog-level API id (`35a18274-b04c-4db6-b732-b23ff68a359b`) returned
  `{"message":"Meta not found"}` against the public sample key — per-resource ids are
  needed and were not found today. Do not promise village or district granularity.
  Third: "schemes" are not "farmers" and not "hectares" — one owner can hold several,
  and the census counts structures, not irrigated area. State that rather than sliding
  between units.

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

- **data.gov.in "6th Minor Irrigation Census — Village Schedule, Ground Water / Surface
  Water Schemes"** — the obvious route to village-level microdata, but not obtainable as
  fetched 2026-08-28: the catalog page is JS-rendered with zero `/resource/` hrefs in the
  served HTML, and the catalog-level API id `35a18274-b04c-4db6-b732-b23ff68a359b`
  returned `{"message":"Meta not found"}` against the public sample key. Not a permanent
  dead end — per-resource ids would need harvesting from the rendered page first. Re-probe
  before promising any sub-state granularity. Logged 2026-08-28.
- **jalshakti-dowr.gov.in `/document/...` report pages** — the route PIB itself links for
  the 6th MI Census reports, but it is a Next.js SPA: HTTP 200, 7,256 bytes, and the only
  hrefs served are CSS/JS bundles and the favicon. Use `mowr.nic.in/irrigationcensus/`
  instead, which serves direct PDF paths. Logged 2026-08-28.
- **7th Minor Irrigation Census all-India totals** — not published yet.
  `7-MI-Report-State-Wise-Vol-II-Part-1.pdf` fetches, `7-MI-Report-All-India-Vol-I.pdf`
  returns 404, and the round is still running jointly with the 2nd Census of Water Bodies
  at `wrcensus.mowr.gov.in`. Do not cite a 7th-census national figure from any secondary
  source until the all-India volume appears. Logged 2026-08-28.

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

---

## Added 2026-08-26 (Wednesday theme: energy and gas)

The energy beat is the blog's second-heaviest: a manifest grep for
`gas|energy|ethanol|lpg|petrol|diesel|crude|electric|power|solar|coal|refin|pngrb|cgd|blend|pipeline|fuel`
matches **60 of 211 posts**, with ethanol alone accounting for roughly fifteen. Every
candidate today failed the third grading question — the blog has covered it — and the
day's one real result is a dedup finding, not a new source.

### 🔴 Corpus-survey Tier-1 item 2 ("ethanol feedstock balance against the E20 target") is CLOSED
Not a new source — a correction to this register's own standing backlog. The item, and
the matching COMMISSION_QUEUE entry "Does India have the feedstock for E20?", were both
logged 2026-08-22 against an AERR paper whose latest listed issue is Vol. 37 No. 1 (2024).
The blog then **answered the question itself the following day**:
`india-hit-e20-on-maize-and-rice-not`, published **2026-08-23**, 23,234 bytes, labels
Ethanol & Biofuels · Agriculture & Fertilisers · Energy & Fuels · India.
- The post names the AERR paper by its title ("does India have enough feedstock to meet
  its E20 targets by 2025?") and treats it as the question being answered, which is
  precisely the framing the queue item proposed.
- It runs on ESY 2025-26 allocation data, not the 2024 AERR vintage: ~1,048 crore litres
  allocated against 1,776 crore litres offered (a 59% allocation rate); grain 72.5% of
  allocation vs cane 27.5%; maize alone 45.7%, up from 6.2% in ESY 2022-23; surplus FCI
  rice 22.3%, i.e. more than direct sugarcane juice.
- **Consequence:** do not commission that item. Anything further on E20 feedstock must
  be a genuinely new angle, not the balance question. The only obvious remaining one is
  the *food-security* side the post states but does not develop — a fifth of the petrol
  blend coming out of the public foodgrain stock, against FCI's own stocking norms — and
  that would need the FCI stock series, not an ethanol series. Related published posts
  to dedup against first: `fci-grain-flow-procurement-storage`,
  `fci-storage-scenario-capacity-stock-and`, `7186-litre-why-maize-is-indias-priciest`,
  `sugar-at-5570-kilo-why-cane-acreage`.

### Weak — logged, not actioned (2026-08-26)
- **ESY 2025-26 ethanol allocation figures** (via press aggregation of DFPD/MoPNG; PIB
  factsheet "Ethanol Blending in India", `static.pib.gov.in/.../doc202675912001.pdf`,
  July 2026) — the underlying primary is real and free, but every headline figure is
  already in a post three days old (see above). WEAK on dedup, not on quality. The PDF
  itself did not text-extract on fetch (415 KB, compressed streams); the PIB HTML
  factsheet route `FactsheetDetails.aspx?id=150699` returned **403** to a plain fetcher —
  consistent with this register's standing note that PIB needs a browser user-agent.
- **ORF Middle East, "A $6 LNG Window: Mapping India's Short-Term Gas Demand Potential"**
  (Parul Bakshi, 9 Dec 2025) — fetched and read. Fails grading question 1: no downloadable
  dataset, table or appendix; the numbers are the author's own contribution to an OIES
  report, not a released official series. Fails question 3 as well — the gas-competitiveness
  thesis is already the published `thermal-parity-is-dead-what-85-oil-and`. Its one
  usable figure is a hedge, not a finding: demand "roughly 5–10 percent above the PNGRB
  Good-to-Go baseline", explicitly called "incremental rather than transformative".
  BACKGROUND at best.
- **OIES, "The Global Outlook for Gas Demand in a $6 World"** — could not be assessed:
  `oxfordenergy.org` returned **403** to the fetcher, so nothing about it was verified
  first-hand and nothing is claimed here. Modelled projections with no released dataset
  would be BACKGROUND even if fetched. Re-probe with a browser user-agent if the gas beat
  is revisited.
- **ORF, "A $6 LNG Window: Mapping India's Long-Term Gas Demand Potential"** — companion
  piece to the above, same author and same data profile. Not separately fetched; assumed
  nothing about it beyond that. Not registered.

### Weak / background — logged, not actioned (2026-08-27)
- **Lakshmi Prasanna, Subba Rao, Hari Prasad, Waris & Arun Kumar (2023), "Essentially
  derived variety concept in plant variety rights protection system: underlying economic
  theories, and issues in implementation", *Agricultural Economics Research Review*
  36(1): 77-86, `epubs.icar.org.in/index.php/AERR/article/view/143786`** — fetched and
  read. Open access, free PDF, and squarely in the Thursday beat, but it fails grading
  question 1: the abstract describes a review that "trace[s] theories underlying, and
  rationale behind [the] EDV concept by reviewing economic models of innovation" and
  "documented some challenges in implementation". No released dataset, no appendix, and
  the article page carries no quantified finding of any kind. **BACKGROUND** — the right
  citation to sit *inside* a piece built on the PPV&FR registry data above, explaining
  what an essentially derived variety is and why the boundary is contested, but not a
  piece on its own.


---

## Added 2026-08-29 (Saturday theme: trade, tariffs and industrial policy)

🔴 **File-loss note.** This file and `COMMISSION_QUEUE.md` were both missing from
`masaladeutsch-archive/docs/` at the start of today's run. Neither was ever committed to
git (`git log --all --diff-filter=AD` returns nothing for either path), so when something
reset the repo's working tree on 2026-08-28 (docs/ mtime 14:14) they were wiped as
untracked files, taking six days of Track B output with them. Both were restored from the
Track C mirror at `/Users/Shared/lit_review/masaladeutsch/` (synced 2026-08-28 07:48).
The restore is trustworthy: `LITERATURE_SURVEY.md`, which *is* tracked, is byte-identical
between the repo and the mirror, and the restored queue has 9 open items, matching the
count the 2026-08-28 log recorded. Content after 2026-08-28 07:48 — if any — is not
recoverable. **These two files need committing to git; the mirror is the only copy.**

### Defence Positive Indigenisation Lists — 5th and 6th PIL primaries (DDP, Ministry of Defence)

Follow-up to the 2026-08-22 entry above, which closed with "The 6th PIL needs its own
release verified." It is now verified, from its own release, and the trip turned up a
second primary that contradicts the figure the blog has already published.

- **Data**: two PIB releases, both fetched in full today. **PRID 2300723** (18 Aug 2026,
  11:15AM, Ministry of Defence) and **PRID 2033571** (16 Jul 2024, 12:29PM). Free, no
  login. 🔴 PIB 403s plain fetchers — a browser User-Agent is required, and
  `PressReleaseDetail.aspx` returns a shell with no body; use
  `PressReleasePage.aspx?PRID=<id>`, which returns the full text.

- **Finding 1 — the published post's declared floor can now be closed.** The post
  `5071-items-you-cannot-import-and-rs` (23 Aug 2026) states plainly that "a fifth list
  exists in the sequence but its item count is not established in the sources used here,
  so it is excluded rather than estimated — the 5,071 total is therefore a floor, not the
  full count." PRID 2033571 establishes it: the **5th PIL is 346 items, import-substitution
  value ₹1,048 crore**. The full six-list DPSU total is therefore **5,417**, not 5,071.
  This reconciles exactly against the other primary: PRID 2300723 states "5,012 items
  notified under the first five Positive Indigenisation Lists", and 4,666 + 346 = 5,012.
  Two independent PIB releases agree to the item.

- **Finding 2 🔴 — the ₹2,570 crore figure the blog published is contradicted by an
  *earlier* ministry release.** PRID 2033571 (July 2024) says of the same PIL 1–4 scope:
  "four PILs comprising 4,666 items were notified by the DDP for DPSUs, of which **2,972**,
  having import substitution value worth **Rs 3,400 crore**, have already been
  indigenised." The register entry above, and the published post, carry **2,736 items /
  ₹2,570 crore** for that same scope. A cumulative indigenisation count cannot fall from
  2,972 to 2,736, nor its value from ₹3,400 cr to ₹2,570 cr, between 2024 and 2026 — so
  the two are different vintages or different scopes, and the post's headline arithmetic
  (**₹94 lakh per item**) rests on the smaller pair. On the 2024 primary the same
  calculation gives **₹114 lakh per item** across a *larger* base. The direction of the
  post's argument survives; the specific number does not.

- **Finding 3 — the series the post explicitly set aside is quantified.** The post notes
  the Department of Military Affairs runs "a different series and are not counted above."
  PRID 2033571 gives it: "five positive indigenisation lists of **509 items** notified by
  the Department of Military Affairs (DMA)." Both series together = 5,417 + 509 = **5,926**.

- **Finding 4 — the PIL lists are a small slice of the actual programme.** PRID 2300723:
  more than **33,000** items offered on SRIJAN by DPSUs and SHQs up to June 2026, of which
  the 5,012 PIL items are a subset; more than **15,700** indigenised for an estimated
  import-substitution value of about **₹9,000 crore over the last five years**; and DPSU
  procurement orders on domestic vendors of about **₹10,000 crore** up to March 2026.
  ₹9,000 cr ÷ 15,700 ≈ **₹57 lakh an item** — the same shape as the post's finding (long
  list, small money) at four times the scale, but on a *different denominator*.

- **Blog fit**: this does not open a beat — it **materially updates a published post**,
  `5071-items-you-cannot-import-and-rs` (23 Aug 2026, labels Industrial Policy · Import
  Substitution · Manufacturing · India). Manifest dedup: snapshot 2026-08-29T06:04, 224
  posts, 15 title hits on the defence/indigenisation/import-substitution regex; that slug
  is the only one on the PILs, and it was read in full rather than judged by title.

- **Caveat**: 🔴 the SRIJAN "items offered" total went **down** — over 36,000 by June 2024
  (PRID 2033571) against more than 33,000 by June 2026 (PRID 2300723). A cumulative offer
  count cannot shrink, so the series has been re-based or de-duplicated at some point and
  neither release says so. Do not build a trend on it, and do not present the two as
  comparable. Same caution applies to "indigenised": 12,300 in three years (2024) vs
  15,700 in five years (2026) are different windows, not a delta. And "import substitution
  value" remains the ministry's own undefined term throughout.

- Grade: **COMMISSIONABLE** — as a correction-and-update piece, not a new subject.

### Weak / background — logged, not actioned (2026-08-29)

- **DGCI&S publication activity** (dgciskol.gov.in) — surfaced by the second Saturday
  query: Laspeyres trade indices for Apr–May 2026 on both 2012-13 and 2022-23 bases, a
  committee report on base-year revision for merchandise trade indices, and a quarterly
  merchandise-trade review for Oct–Dec 2025. Not fetched, so nothing is asserted about
  contents. Noted only because a **base-year revision** is the kind of thing that silently
  breaks a published index series, and the blog runs trade-data pieces off this portal;
  worth a proper look on a future Saturday. BACKGROUND, pending verification.

---

## Added 2026-08-31 (Monday theme: agricultural labour and rural incomes)

**Dedup finding that reframes the theme, recorded first because it changes the brief.**
`LITERATURE_SURVEY.md` §3 lists agricultural labour and rural incomes as a zero-coverage
area. That is now **stale**. The published post `a-17-rural-pay-rise-that-nobody-received`
(22 Aug 2026) was read in full today, and it does not merely touch the beat — it covers
the Labour Bureau's CPI-AL/CPI-RL base revision from 1986-87 to 2019=100 and the
undisclosed village-sample swap underneath the headline 17-18% wage jump; the
break-adjusted 4.3% versus the old-sample 6.23%; the fact that CPI-AL sets wages under
the central rural employment guarantee and anchors state minimum wages for agricultural
and rural labour; **MGNREGA's repeal** by the VB-G RAM G Act 2025 (assent 21 Dec 2025, in
force 1 Jul 2026), with a side-by-side of the two schemes' guaranteed days (100 -> 125)
and work-availability windows; early VB-G RAM G person-days (30 crore approved April 2026
-> 43 crore May); and PM-KISAN's landholding targeting as the reason it exerts no pressure
on the agricultural wage. **MGNREGA and rural wage indexation should be treated as a
covered subject from now on, not a gap.** Manifest dedup: snapshot 2026-08-31T07:39,
237 posts; regex `wage|labour|labor|employ|mgnrega|rural|migrant|income|job|worker` over
titles returns 4 hits, of which this is the only one on the beat.

Two sub-angles the post explicitly declines and leaves open: (a) VB-G RAM G's own
performance, which the post refuses on the ground that the scheme was "nine weeks old at
the time of writing" — still true, it is nine days older today, so hold it; (b) the
occupation-level anomalies in the Labour Bureau's own tables, for which the post notes
"no occupation-level explanation has been offered".

**Open-item check (step 1, which outranks new candidates).** The E20 feedstock item and
the Minor Irrigation item both carry AERR citations pinned to "latest listed issue is
Vol. 37 No. 1 (2024)". Re-checked today at `epubs.icar.org.in/index.php/AERR/issue/archive`:
the archive still ends at **Vol. 37 No. 1 (2024)**, twelve issues back to Vol. 31 No. 2
(2018). No newer issue, so neither item is unblocked and both caveats stand unchanged.

### NSS 77th Round — Situation Assessment of Agricultural Households (NSSO / MoSPI)

**Data**: PIB PRID 1753856, MoSPI, "NSS REPORT NO. 587: Situation Assessment of
Agricultural Households and Land and Livestock Holdings of Households in Rural India,
2019", posted 10 Sep 2021 — fetched in full 2026-08-31. 🔴 PIB 302-redirects plain
requests to `?PRID=<id>&reg=48&lang=2`; follow redirects (`curl -L`) **and** send a
browser user-agent, or you get a 174-byte "Object moved" stub. Reference year is the
agricultural year **July 2018 – June 2019**; fieldwork Jan–Dec 2019 in two visits.
Sample stated in the release: 5,950 FSUs allotted, 5,940 surveyed in visit 1, 58,035
households, of which 45,714 agricultural households (44,770 in visit 2). Free, no login.
Companion release for the comparison year: PIB PRID 2003180 (MoA&FW, 6 Feb 2024).

**Finding**: for the household India's farm-income policy is actually measured on,
**wages are the largest single source of income, not crops**. Table 6, paid-out-expenses
basis, average monthly income per agricultural household: wages **₹4,063**, net receipt
from crop production **₹3,798**, farming of animals ₹1,582, non-farm business ₹641,
leasing out land ₹134 — total **₹10,218**. On the fuller basis that also charges imputed
expenses, the gap roughly doubles: wages ₹4,063 (unchanged, since imputation hits farm
costs) against crop production **₹3,058** and animals **₹441**, total **₹8,337** — wages
are then **49%** of household income and crop production **37%**.

And the survey reaches that result on a population **defined to exclude the rural workers
most dependent on wages**. The release states in terms: "households which were entirely
agricultural labour households and households receiving income entirely from coastal
fishing, activity of rural artisans and agricultural services were not considered as
agricultural households and they were kept outside the scope of the survey." Qualifying
required more than ₹4,000 of agricultural produce value plus a member self-employed in
agriculture. Landless share within the surveyed population: 8.2%; average area owned
0.512 ha. Indebtedness: 50.2% of agricultural households, ₹74,121 average outstanding.

**Blog fit**: extends the beat `a-17-rural-pay-rise-that-nobody-received` opened, from
the opposite side. That post is about the index that sets what agricultural labourers are
paid; this is the official survey that measures farm household income and leaves pure
agricultural-labour households out of the frame entirely — while still finding that the
wage beats the crop inside the households it does count. Nearest published post by slug:
`a-17-rural-pay-rise-that-nobody-received`. Also adjacent to
`annadata-to-urjadata-farmer-income-case` (4 Aug 2026), which argues a farmer-income case
without this income decomposition. Dedup on bodies, not just titles: `grep -rliE
'situation assessment|77th round|NSS 587|agricultural household' posts/` returns two files
(`the-price-of-grain-msp-msv-and`, `tamil-nadus-water-infrastructure-runs`) and the phrase
"agricultural households" appears exactly **once** across the whole corpus — incidental,
not a treatment. The income composition is uncovered.

**Caveat**: 🔴 **vintage is the whole risk here.** Reference year 2018-19, published 2021,
and it is *still* the current official figure — PIB PRID 2003180 (MoA&FW, 6 Feb 2024) is a
Lok Sabha reply that gives the government's own latest answer as the 77th round, tabulating
only 2012-13 (70th round, NSS Report 576) at ₹6,426 and 2018-19 (77th round) at ₹10,218.
So the number is seven years stale by reference year and there is no newer round to cite —
that is a fact about the data, not a defect in the source, but every figure must be dated
in the piece and no "farmers today earn" phrasing is defensible. Second caveat: the two
expense bases are not interchangeable, and the ₹6,426 comparison figure's basis was not
established today — do not compute a 2012-13 → 2018-19 growth rate until both are
confirmed to be on the same basis. Third: "agricultural household" is a survey construct
with a ₹4,000 threshold, not a synonym for "farmer" — the piece must define it early.

### Weak / background — logged, not actioned (2026-08-31)

- **ICAR e-publications, *Agricultural Economics Research Review* archive
  (`epubs.icar.org.in/index.php/AERR/issue/archive`)** — re-fetched today only as the
  open-item vintage check described above. Still ends at Vol. 37 No. 1 (2024). Not a
  candidate in itself; logged so the next Monday/Friday run does not re-fetch it hoping
  for a new issue. Re-check no sooner than a month out.

---

## Added 2026-09-01 (Tuesday theme: insurance, reinsurance and financial plumbing)

Dedup baseline for this whole section, run 2026-09-01 against `meta/manifest.json`
(snapshot 2026-08-31, **238 posts**): a regex for `insur|reinsur|irdai|ifsca|gift.?city|
solvency|actuar` over the full manifest returns **exactly one post** —
`premium-now-claim-later-float-indias` ("Premium Now, Claim Later: The Float India's Car
Boom Is Building", 2026-08-22, labels incl. *Insurance & Reinsurance*), which is motor
float. `irdai`, `ifsca`, `gift city`, `solvency` and `actuar` return **zero**. The beat is
as empty as the survey said.

### IRDAI obligatory cession to GIC Re, held at 4% for FY 2025-26 (third consecutive year)

IRDAI's annual cession notification for the financial year 1 April 2025 – 31 March 2026,
as reported and quoted by Reinsurance News (fetched 2026-09-01, HTTP 200).

- **Data**: the notification text itself is quoted verbatim — "The percentage cession of
  the sum insured on each General Insurance Policy to be reinsured with the Indian
  Re-insurer(s) shall be 4% (four percent) in respect of insurance attaching during the
  financial year beginning from 1st April, 2025 to 31st March, 2026." The backing
  dataset is the **IRDAI Annual Report 2024-25** (free PDF, no login — a copy is served
  at `lifeinscouncil.org/component/IRDAI%20Annual%20Report%202024-25.pdf`; source it from
  `irdai.gov.in` before publication), which carries 74 registered insurers and reinsurers
  as at 31 March 2025 and industry AUM of ₹74.43 lakh crore. Minimum commission floors by
  line are also stated: 5% motor TP and oil & energy, 10% group health, 7.5% crop, 15% all
  other classes.
- **Finding**: every general insurance policy written in India carries a **compulsory 4%
  cession to a single state-owned reinsurer**, GIC Re — held at 4% for the third year
  running, down from 5% earlier. The interesting number is on the receiving side: GIC Re's
  obligatory business fell from **43% of total revenue to 39%** (April–October FY25), and
  was 30% in FY21. So the mandate is being *held constant* while the recipient's
  dependence on it moves — up sharply from FY21, then down again. A compulsory transfer
  whose share of the beneficiary's book is not stable is not the settled arrangement it is
  usually described as.
- **Blog fit**: opens the near-empty **Insurance & Reinsurance** beat from the
  wholesale/plumbing end rather than the retail end. Nearest published post is
  `premium-now-claim-later-float-indias` (motor float — the retail side of the same
  balance sheet). The structural sibling is `who-collects-indias-gst-and-who`: identical
  who-pays-vs-who-receives framing, applied to a mandated transfer instead of a tax.
- **Caveat**: the 4% and the quoted sentence reached this register **through a trade
  publication quoting the notification**, not from `irdai.gov.in` directly — pull the
  notification itself before publishing, and do not repeat the 5%-to-4% history until the
  year of that change is sourced (the article does not give it). The 43%→39% figure is a
  **part-year** number (April–October FY25) and must not be presented as a full-year
  share. Finally, "4% cession" is 4% of *sum insured on each policy*, not 4% of industry
  premium — do not convert one into the other without the Annual Report's own tables.
- Grade: **COMMISSIONABLE**. Logged 2026-09-01.

### General Insurance Council industry statistics (Flash Figures, Segmentwise Report, GIC Year Book 2024-25)

`gicouncil.in/statistics/industry-statistics/`, fetched 2026-09-01.

- **Data**: four published series — **Flash Figures**, **Segmentwise Report**, **Financial
  Highlights**, and **Yearbook Archives**, latest edition **GIC Year Book 2024-25**, served
  as a PDF at `/Year-Book/GIC_Yearbook_2024-25.pdf`. Free, no login, no paywall on the
  statistics pages. Segments covered: fire, marine, motor, health, aviation, liability,
  personal accident, crop, engineering, property, miscellaneous. This is the segment-level
  premium data the blog would need for any general-insurance piece, and it is the natural
  primary behind the existing motor-float post.
- **Finding (NOT yet primary-verified)**: the statistics page surfaces **₹94,247.6 crore in
  total health claims settled in 2024-25, with cashless-only admissions at 66.4% of
  volume**. Both fetches placed this figure inside a **news item on the page**, not in a
  data table — so it is trade-press-on-a-trade-body-site, which is not the same thing as
  the Council's own statistics.
- **Blog fit**: the dataset, not the figure, is what earns the entry — it is the missing
  primary under the whole *Insurance & Reinsurance* label, and it would let a future piece
  put the motor float of `premium-now-claim-later-float-indias` next to the other ten
  segments instead of standing alone.
- **Caveat**: periodicity and year-coverage of Flash Figures and the Segmentwise Report
  were **not** resolvable from the fetched pages — confirm both before building anything
  time-series on them. The health-claims figure above must be re-sourced from the Year Book
  PDF or dropped; do not publish it on the page-snippet's authority. Note also that the GI
  Council is an **industry body**, not the regulator — cross-read anything load-bearing
  against IRDAI.
- Grade: **BACKGROUND** (obtainable primary data confirmed; no verified finding yet).
  Logged 2026-09-01.

### Weak / not deep-read, one line each

- **GIFT City IIO premiums "quadruple to $648.7 million in FY26"** (Business Standard,
  4 June 2026) — the most striking number of the day and a confirmed zero-coverage area,
  but the **primary could not be located**: the Business Standard article 403s,
  `ifsca.gov.in/Publication` 404s, and the IFSCA Bulletin listing
  (`ReportPublication/index/wF6kttc1JR8=`) renders an **empty table**. IFSCA's own homepage
  publishes a differently-scoped counter — **"USD 334 Mn+ premium transacted by insurance
  entities (IIOs & IIIOs)" for Q4 2025-26** — which includes intermediary offices and so
  cannot be reconciled with the press figure without the underlying release. A quadrupling
  off a $162.10 mn base is also a small-base artefact as much as a finding. Re-try when the
  **IFSCA Annual Report 2025-26** appears; do not commission on press attribution alone.
- **NCAER, "Making the IFSC a Re-insurance Hub"** (hosted on ifsca.gov.in,
  `ncaer-report20042022032732.pdf`, dated 2022) — a commissioned advocacy report, four years
  stale, and its numbers are projections rather than released data. Background at best.

### seednet.gov.in — DA&FW Seed Net portal (candidate, NOT assessed)

- **Data**: unknown. Surfaced 2026-09-03 as a possible government primary for the
  Thursday seeds / plant-variety-rights / agricultural-IP beat — the three-generation
  breeder → foundation → certified seed production series, seed availability and indent,
  and state-wise figures are the sort of thing the portal is supposed to carry.
- **Status**: `https://seednet.gov.in/Material/Seed_Production.htm` returned **HTTP 503**
  on direct fetch, so **nothing on the page has been read and nothing is claimed about
  it**. Not graded. Retry on a future Thursday before deciding whether it is
  COMMISSIONABLE, BACKGROUND or WEAK.
- **Blog fit (provisional)**: would extend the same confirmed zero-coverage area the open
  PPV&FR queue item opens. Manifest dedup re-run 2026-09-03 for
  seed/variet/ppvfr/patent/breeder/germplasm/intellectual/hybrid across titles and slugs:
  **zero hits**, so the area is still genuinely uncovered.
- **Caveat**: Seed Replacement Rate is the figure most likely to be reachable and also
  the one most likely to be quoted loosely — search-result prose today gave "less than
  25%-30%" for open-pollinated food grains and oilseeds with no year and no source
  attached. Treat any SRR number as unusable until it is read off a dated departmental
  table. WEAK on evidence until fetched, logged 2026-09-03.

---

## Added 2026-09-04 (Friday theme: irrigation, water and soil)

**Dedup first.** The Friday theme's headline source is already here: the AERR paper
Bathla, Kannan & Das, "Public investment in irrigation across the Indian states",
AERR 37(1) 2024, was registered on the irrigation entry at line 158 and already carries
an open queue item (COMMISSION_QUEUE, the 6th Minor Irrigation Census piece). Today's
search returned it again; it is **not re-logged**. The soil half of the Friday theme was
untouched, so the search went there.

Manifest dedup re-run 2026-09-04 across all **255** post titles for
`irrigat|water|soil|groundwater|canal|drip|organic carbon|aquifer|monsoon|rainfall|watershed`:
**6 hits, none about soil or agricultural water**. All six are water *infrastructure
spending* pieces — `amruts-197-lakh-crore-urban-portfolio`,
`tamil-nadus-water-infrastructure-runs`, `indias-79-lakh-crore-rural-water`,
`the-water-bill-nobody-mentions-what` (semiconductor fabs),
`price-is-wire-how-gcam-actually-links` (a model, not a measurement), and
`guar-gum-indias-35-billion-export-peak`, where "poor soil" is agronomic colour in a
trade piece. Soil health as a measured quantity has **zero coverage**.

### Soil Health Card scheme — the national soil-test panel, and its April-2023 break — COMMISSIONABLE
- **Data**: the Soil Health Card portal, `soilhealth.dac.gov.in`, run by DA&FW with NIC.
  Verified live by direct fetch 2026-09-04: home and `/nutrient-dashboard` both return
  **HTTP 200**. It is a JavaScript single-page app, so the dashboard content is not
  visible to a plain fetch; the app's own bundle
  (`/assets/index-Ed_k0WPH.js`) names its data endpoint as an Apollo GraphQL client
  pointed at **`https://soilhealth4.dac.gov.in`**, which answers a bare GET with
  **HTTP 400** — i.e. the server is up and rejecting a malformed query, not refusing
  access. No login wall was encountered at the transport level. The card itself carries
  **12 parameters: N, P, K, S; Zn, Fe, Cu, Mn, Bo; pH, EC and OC (Organic Carbon)** —
  organic carbon is a scheme-standard field on every card, not an add-on.
- **Finding**: not the SOC level — the **regime break in how it is measured**. PIB
  release PRID 2104403, Ministry of Agriculture & Farmers Welfare, "Celebrating a Decade
  of Soil Health Cards", posted 18 Feb 2025 (fetched in full 2026-09-04), states that the
  portal was revamped and rolled out in **April 2023** with GIS integration, and that
  from then on the mobile app **restricts the sample-collection region** for the village
  operator, **auto-selects the latitude and longitude** of the sample, and generates a
  **QR code linking sample to result directly from geo-mapped labs, "without any manual
  intervention"**. It renders layers down to **cadastral boundary**. The plain reading is
  that samples before April 2023 were sited and keyed by hand and samples after it are
  machine-geolocated and machine-keyed — so any district organic-carbon series that
  straddles April 2023 is comparing two different collection regimes, and a "decline" or
  "improvement" across that seam may be an artefact of the seam. The same release gives
  the delivery scaffolding: **665 Village-Level Soil Testing Labs across 17 States** as of
  February 2025, and, as of 2024, **1,020 schools running the School Soil Health
  Programme with 1,000 school labs and 125,972 students enrolled**. The scheme was folded
  into RKVY as the "Soil Health & Fertility" component from **2022-23**.
- **Blog fit**: opens the **soil** half of the Friday zero-coverage area (irrigation is
  already opened by the Minor Irrigation Census queue item) and puts a fourth post in the
  water/land cluster. Nearest published post is `indias-79-lakh-crore-rural-water` — that
  is Jal Jeevan Mission *drinking-water* capital expenditure, a different ministry and a
  different quantity; the connection is thematic only and should be cross-linked as the
  blog cites its own reporting, never as confirmation.
- **Caveat**: 🔴 **The export path is the one thing not yet verified.** The endpoint is
  live and the dashboard is described by the government as being in the public domain,
  but no query has been run and no district-level organic-carbon table has been pulled.
  Nothing about SOC levels, trends, or district rankings may be written until a real
  query returns a real table. Second, the widely circulated "ICAR six-year study, 254,236
  soil samples, 620 districts, 29 states" figure surfaced today **only from coaching-site
  secondaries** (vajiramandravi, carpediemias, dhruvstarindustryinsights) and is **not
  verified**; do not repeat it on that authority — trace it to the IISS Bhopal source or
  drop it. Third, PIB PRID 2104403 gives no national count of cards issued or samples
  tested, so those numbers must come from the portal or a dated Lok Sabha answer, not
  from this release. Fourth, `pib.gov.in` returns **403 to a plain fetcher and 302 to a
  UA-less curl** — it needs a browser user-agent and `-L` to follow to the
  `&reg=&lang=` form of the URL.

### Weak / background — one line each (triaged, not deep-read)
- **Rattan Lal, "Soil Carbon in Agro-Ecosystems of India", Journal of the Indian Society
  of Soil Science 74(1), 2026** (`epubs.icar.org.in/index.php/JISSS/article/view/180202`,
  fetched 2026-09-04) — **BACKGROUND**. It is a review and a policy argument, not a
  measurement: the abstract carries exactly one number, a proposed payment-for-ecosystem-
  services rate of **US $50 per credit (~INR 4,600)**, and no SOC stock in Mg/ha or Pg,
  no sample, no district. It also names the **Bharat Soil Protection Policy (BSPP) being
  developed by ICAR** and calls for a Soil Health Act at district, state and national
  level — both useful as the policy frame around a piece built on portal data, neither
  able to carry one. Cite inside, do not commission.
- **AERR 37(1) 2024, Bathla, Kannan & Das, public irrigation investment and financial
  recovery** — already registered (line 158) with an open queue item. Re-surfaced by
  today's first search; not re-logged.
- **Frontiers in Sustainable Food Systems 2025, SOC fractions across land uses in
  temperate India** — single-region field study outside the Indian-journal estate, no
  national panel, nothing the blog could pull. **WEAK**.
- **Coaching-site summaries of the ICAR/IISS SOC study** (vajiramandravi, carpediemias,
  dhruvstarindustryinsights) — **WEAK by construction**: secondary prose with no
  citation to a dated ICAR document. Logged only so a future run does not mistake their
  agreement with each other for corroboration.

---

## Added 2026-09-07 (Monday theme: agricultural labour and rural incomes)

**Step 1 outranked the search today, and produced the day's whole result.** The Monday
theme is now well covered — the 2026-08-31 entry established that
`a-17-rural-pay-rise-that-nobody-received` (22 Aug 2026) treats CPI-AL/CPI-RL rebasing,
the village-sample swap, MGNREGA's repeal by the VB-G RAM G Act 2025 and PM-KISAN's
targeting, and that the beat should be treated as covered rather than as a gap. Manifest
dedup re-run today (snapshot 2026-09-05T22:16, **257 posts**, regex
`wage|labour|labor|mgnrega|nrega|rural|farm|employ|migrant|income|agricultur|harvest|crop`
over titles and slugs): 11 hits, of which exactly one — that post — is on the beat, and
one more, `annadata-to-urjadata-farmer-income-case`, is adjacent. Unchanged picture. So
the open-queue check took priority, and it paid.

### PPV&FR Authority registry — the blocked check is resolved, and it changes a number

**Status of the host.** `https://plantauthority.gov.in/` returned **HTTP 200, 171,508
bytes** on direct fetch today with a browser user-agent. On 2026-09-03 it returned 503 and
the Thursday run recorded the item as un-advanceable. It is up now, so the two outstanding
checks on the queued item "57.8% of India's plant-variety rights are cereals" were run.
(The deep link `/plant-varieties-registry-related-information` still fails outright —
curl exit 000, connection never completes — so the homepage is the working surface.)

**Data**: two ECharts series hardcoded in the homepage source, both headed with an
explicit vintage the site states itself: "**10885 Certificates issued as on 31.08.2026**"
and "10885 Certificates issued crop group-wise as on 31.08.2026". Free, no login, no
browser needed beyond a UA string. This is materially better than what the item was
resting on: the 2026-08-27 capture was described in the queue as a *live counter with no
vintage archive*, which is why check (1) told the writer to date-stamp it by hand. The
page now carries its own as-on date.

**Finding 1 — the crop split holds, on a newer vintage.** Crop-group series as on
31.08.2026, total 10,885: **Cereals 6,280**, Vegetables 1,386, Fibre 1,006, Legumes 872,
Oilseeds 577, Fruits 429, Sugar 93, Other 242. Cereals are **57.7%**, against the 57.8%
(6,246 of 10,802, as on 31.07.2026) captured on 2026-08-27. The queued headline survives.

The two captures also **cross-validate**, which is the reason to trust either. Month on
month: cereals +34, vegetables +19, fibre +17, legumes +6, fruits +4, oilseeds 0, sugar 0,
other +3 — summing to +83, exactly 10,885 − 10,802. And today's single "Other" bucket
(242) reconciles with the five small categories the 31.07 capture broke out separately
(Spices 151 + Trees 43 + Flowers 36 + Cash 5 + Medicinal & Aromatic 4 = 239, +3 in a
month). ⚠️ Note the consequence for the piece: **today's homepage no longer breaks out
spices**, so the "Spices get 151" half of the working title is only available from the
2026-08-27 capture or the Annual Report — do not expect to re-fetch it.

**Finding 2 — check (2) is resolved, and the unverified figure was wrong in the direction
that matters.** The registration-type series as on 31.08.2026, total 10,885: **Farmer
5,368**, Extant Notified 2,025, New 1,921, Extant VCK (varieties of common knowledge)
1,557, **EDV 14**. Farmers' varieties are therefore **49.3%** of all certificates ever
issued — **just under half, not over it**. The circulating snippet claim the queue item
flagged as unverified ("4,847 of 9,210 certificates (52.6%) went to farmers") is now
superseded by a dated primary, and a piece written on it would have asserted that most
Indian plant-variety certificates go to farmers when the Authority's own figure says they
do not. Both series sum independently to the same 10,885, which is the check that makes
them usable.

**Finding 3 — incidental, and the sharpest number on the page.** Essentially derived
varieties: **14 certificates, 0.13% of 10,885**, in a register that has been issuing since
2007 — while the homepage simultaneously carries a live notice, "General Guidelines
Regarding the Registration of EDV". EDV is the doctrine that decides whether a variety
bred from a protected variety needs the original breeder's authorisation, so it is the
mechanism that determines who captures the value of incremental breeding. Fourteen.

**Blog fit**: does not open a new area — it resolves checks on an item already queued
against the confirmed zero-coverage seeds / plant-variety-rights / agricultural-IP area.
Nearest published posts remain `indias-445-billion-spice-export-book-is` and
`379-kilos-hectare-in-punjab-44-in`, both to be cross-linked as earlier reporting in house
style, never as confirmation.

**Caveat**: 🔴 these are **chart literals embedded in homepage JavaScript**, not a
published table — genuinely primary, and internally consistent across two independent
series and two dates, but the Authority publishes no schema for them. The category names
come from hidden inputs on the same page (`Extant Notified`, `Extant VCK`, `Farmer`,
`New`, `EDV`) and are undefined there, so check (4) of the original item — state that the
categories are the Authority's own and undefined — now applies to the *registration-type*
split as well as the crop split. The Annual Report cross-read (check 1) is still worth
doing and is still the citable artefact; nothing here replaces it. Check (3) stands
unchanged: certificates issued ≠ varieties commercially sold. The host is intermittent —
up today, 503 four days ago — so anyone writing this should pull and keep a local copy
rather than plan to fetch at publication time.

### Weak/off-scope, one line each (triaged, not deep-read)

- **AERR, "Agricultural wages in India: trends and determinants"**
  (`epubs.icar.org.in/index.php/AERR/article/view/140527`) — WEAK by dedup, not by
  quality: farm-wage trends are the exact subject of `a-17-rural-pay-rise-that-nobody-received`,
  which runs on the Labour Bureau's own CPI-AL series and a base-revision break. A
  determinants paper does not contradict or materially update it.
- **Venkatesh P., "Recent Trends in Rural Employment and Wages in India: Has the Growth
  Benefitted the Agricultural Labours?", AERR Vol. 26 (2013)** — WEAK on vintage: a
  thirteen-year-old series on a beat where the live question is a 2026 base revision and a
  scheme repealed in December 2025.
- **Pattayat & Parida, "Drivers of Rural Non-farm Sector Employment in India, 1983–2019"
  (Sage, 2024)** and **NCAER, "Rural Non-farm Employment in India: Access, Incomes and
  Poverty Impact"** — WEAK by dedup: rural non-farm employment is **already queued** as
  "Rural India's fastest quarter off the farm" (COMMISSION_QUEUE, logged 2026-08-24) on
  the PLFS Quarterly Bulletin, which is a quarterly official series running to Apr–Jun
  2026. Neither an academic panel ending in 2019 nor an undated NCAER volume improves on
  that source, and the queue item is the piece.
- **IJAgS, "Trends in agriculture, non-farm sector and rural employment in India: An
  insight from state level analysis"** (`epubs.icar.org.in/index.php/IJAgS/article/view/48502`)
  — same dedup as above; not fetched beyond the search listing, and not counted as assessed.
- **AERR issue archive** — not re-checked today. It was confirmed on 2026-08-31 as still
  ending at Vol. 37 No. 1 (2024), and one week is not a plausible interval for a new issue
  of a journal whose archive has been static since 2024.

## Added 2026-09-08 (Tuesday theme: insurance, reinsurance and financial plumbing)

Second Tuesday pass on this theme (2026-09-01 took the domestic wholesale end — the IRDAI
obligatory cession and the GI Council statistics), so it was re-aimed at the leg 09-01
explicitly left untouched: **IFSCA / GIFT City**, which that entry's own dedup run
recorded as returning zero manifest hits. Dedup re-run today against
`meta/manifest.json` (snapshot 2026-09-07T19:53+05:30, **257 posts**): a regex for
`ifsca|gift.?city|reinsur|insur|bullion|fintech|offshore|banking.?unit` over the full
manifest returns **exactly one post**, `premium-now-claim-later-float-indias` ("Premium
Now, Claim Later: The Float India's Car Boom Is Building", 2026-08-22), matching only on
`insur`. `ifsca`, `gift city`, `bullion`, `offshore` and `banking unit` return **zero**,
unchanged from a week ago and now against 19 more posts.

### IFSCA Bulletin, Jan–Mar 2025 — GIFT IFSC's insurance leg is 94% reinsurance

`ifsca.gov.in/Document/ReportandPublication/ifsca-bulletin-jan-mar-202509052025055132.pdf`,
fetched 2026-09-08 (HTTP 200, 4.6 MB, text extracted with `pdftotext -layout`). Issued by
the Division of Economic Policy and Analysis, IFSCA; the front matter states the source is
"the periodic reports submitted by the regulated entities to IFSCA" and grants explicit
reproduction permission subject to acknowledgement.

- **Data**: a quarterly statistical bulletin with **26 numbered tables**, free, no login,
  no paywall, published on the regulator's own domain, and issued each quarter (Apr–Jun,
  Jul–Sep, Oct–Dec, Jan–Mar editions for 2024 and 2025 all resolve on `ifsca.gov.in`), so
  it is a genuine time series rather than a one-off report. The tables the blog would
  actually use: **Table 3** number of IBUs, **Table 4/5** assets and liabilities of IBUs,
  **Table 10** industry-wise credit exposure of IBUs, **Table 11** *country-wise* exposure
  of IBUs, **Table 12** IFSC exchange turnover, **Table 24** premium written by IFSC
  Insurance Offices (IIOs) and Intermediary Offices (IIIOs), **Table 25** line-of-business
  direct insurance, **Table 26** line-of-business reinsurance. Headline dashboard figures
  (as on/during Mar 2025): 865 total IFSCA registrations (including in-principle/
  provisional), banking assets USD 88.51 Bn, average monthly IFSC-exchange turnover USD
  92.15 Bn, 162 fund management entities with USD 15.74 Bn of commitments raised, 33
  aircraft lessors and 24 ship lessors, 31.99 tonnes of gold traded on IIBX worth USD 2.9
  Bn in the quarter, and 18 insurance offices plus 27 intermediary offices.
- **Finding**: GIFT IFSC is described everywhere as an offshore insurance hub. Its own
  quarterly tables say the direct-insurance business barely exists. Summing Table 25 across
  the four quarters of FY 2024-25 gives **USD 12.42 Mn of gross direct written premium**
  (2.43 + 2.42 + 3.96 + 3.61); summing Table 26 over the same four quarters gives **USD
  195.45 Mn of reinsurance premium** (44.54 + 48.00 + 44.76 + 58.15). Reinsurance is
  therefore **94.0% of the centre's insurance book**. The direct **life** line is USD
  **2.54 Mn for the entire year** (0.46 + 0.82 + 0.90 + 0.36) — under ₹25 crore, from a
  jurisdiction hosting 18 registered insurance offices. Set against USD 88.51 Bn of banking
  assets on the same dashboard page, the whole insurance leg is roughly a five-hundredth of
  the banking leg. The centre did not fail to attract insurance; it attracted one *kind* of
  insurance, the wholesale cession end, and almost none of the retail end it is marketed on.
- **Blog fit**: opens the **IFSCA / GIFT City** zero-coverage area and gives the near-empty
  *Insurance & Reinsurance* label its offshore half. Nearest published post is
  `premium-now-claim-later-float-indias` (motor float — domestic, retail, the opposite end
  of the same balance sheet). It also completes the pipe the 2026-09-01 entry opened: India
  *compels* 4% of every general policy into a domestic state reinsurer (GIC Re) while the
  offshore centre built to attract international reinsurance capacity writes USD 195 Mn a
  year. Structural sibling on the blog is `who-collects-indias-gst-and-who` — the same
  who-writes-vs-who-receives framing.
- **Caveat**: four things must be checked before publication. (1) Table 24's Jan–Mar 2025
  IIO figure of USD 61.70 Mn carries a printed footnote — "Reinsurance data of one IIO is
  under examination and hence not included" — so that one quarter is understated by an
  unknown amount; the 94% share should be recomputed once the audited figure lands, and
  quoted as *approximately* 94% until then. (2) All FY 2024-25 figures are marked
  **unaudited** on both tables. (3) Table 26 shows "Health + PA" collapsing from 26.48 to
  2.21 between Oct–Dec and Jan–Mar while a separate "Health Insurance" line appears at
  5.77 in the same quarter — that looks like a reclassification, not a collapse in
  business, and must be resolved against the following bulletin before either number is
  narrated. (4) Table 24 (offices) and Tables 25/26 (lines of business) are differently
  scoped — do not add or divide across them.
- Grade: **COMMISSIONABLE**. Logged 2026-09-08.

### Weak/off-scope, one line each (triaged, not deep-read)

- **IFSCA Annual Report 2024-25** (issued 2025-08-18; TeamLease RegTech and Cyril Amarchand
  Mangaldas both carry summaries) — almost certainly the right *annual* primary, but three
  searches failed to surface a direct PDF URL on `ifsca.gov.in`, and every accessible
  account of its contents was a law-firm or compliance-vendor summary rather than the
  document. Not registered on secondhand summaries. Worth one attempt at
  `ifsca.gov.in/ReportPublication/index/zcGvy-Iqfcg=` (the Annual Reports index, which does
  resolve) on a future Tuesday; the quarterly bulletins already carry the tables, so this is
  a completeness errand, not a blocker.
- **PwC India, "Banking in GIFT IFSC" (April 2024)** — a consultancy explainer, not a data
  source; its figures are restatements of IFSCA's own. Standing rule on vendor material
  applies. WEAK, and unnecessary now that the primary is in hand.
- **`giftcityadvisor.com` mirror of the Jul–Sep 2025 IFSCA bulletin** — a third-party copy of
  a document the regulator publishes itself. Never cite the mirror; note only that a
  **Jul–Sep 2025** edition exists, which means the series runs at least two quarters past
  the edition read today and a piece built on it can be brought to a current vintage.
- **`gicouncil.in` industry statistics** — surfaced again alongside today's query; **already
  registered 2026-09-01** with its own caveats. Listed only so the day's candidate count is
  honest, not re-triaged.

## Added 2026-09-09 (daily task, Wednesday: energy and gas)

The weekday brief warns that energy is heavily covered and to bias hard toward something
unrun. Dedup measured how heavily: a broad energy regex over the **257-post manifest**
(snapshot 2026-09-07) returns **93 hits** — more than a third of the blog. But the same
sweep found the coverage is almost entirely on the **molecule** side. Narrow regexes
returned: nuclear **0**, energy-efficiency/PAT/appliance-labelling **0**, domestic coal
supply (Coal India / e-auction / washery / linkage) **0**, transmission-and-grid **0** real
hits (one false positive on "SIP"), power-market/exchange **0** real (all forex false
positives). A precise electricity-distribution regex
(`discom|at&c|electricity|power utilit|rdss|distribution util|smart meter|kwh`) returns
exactly **one** post. So the blog has 93 energy pieces and essentially nothing on the
**electron** side: the grid, the discoms, the power market, nuclear. That asymmetry is the
day's real finding and it should shape future Wednesdays.

The one electricity post is `discom-debt-relief-token-charge` — an interactive *calculator*
(read directly, 4,673 chars), not a reported piece. It models a per-connection token charge
against discom debt, with defaults sourced to ICRA May 2025 (debt ₹7.4 lakh crore), IISD
2025 (subsidies ₹2.1 lakh crore), CEA/Manorama (8.7% CAGR) and PFC (~70% rural billing
efficiency), and its standing premise is **"₹64,000 cr added to debt every year"**. Today's
source bears directly on that premise, which makes this a materially-updating candidate
against a named slug rather than a new-beat land grab.

### PIB / Ministry of Power — two releases, six weeks apart, two different FY25 AT&C loss figures

Both fetched directly (`pib.gov.in` returns HTTP 403 to a plain fetch; a browser
User-Agent over curl returns HTTP 200 — the standing PIB access note holds).

- **Data**: two Press Information Bureau releases from the **same ministry**, free, no login.
  (1) **PRID 2200450**, *"Key Initiatives to Bring Down AT&C Losses of Power Distribution
  Utilities"*, **08 DEC 2025 5:02PM by PIB Delhi** — a written reply by the Minister of
  State for Power, Shri Shripad Yesso Naik, in the **Rajya Sabha**. (2) **PRID 2215761**,
  *"Power Distribution Utilities Record Positive PAT After Years of Losses; This Marks a New
  Chapter, Says Power Minister"*, **18 JAN 2026 10:34AM by PIB Delhi** — a press release
  quoting the Union Minister of Power, Shri Manohar Lal. The underlying annual series is
  PFC's *Report on Performance of Power Utilities*; neither release names its source.
- **Finding**: the two releases give **different AT&C loss figures for the same financial
  year**. The December parliamentary answer: AT&C losses "reduced from 21.91% in FY 21 to
  **16.16% in FY25**". The January press release: AT&C losses "reduced from 22.62% in FY
  2013-14 to **15.04% in FY 2024-25**". FY25 and FY 2024-25 are the same year, and the gap
  is **1.12 percentage points**. This is not cosmetic. RDSS — the flagship distribution
  scheme, ₹2.83 lakh crore sanctioned per the December release — targets a pan-India AT&C
  band of **12–15%**. At 15.04% the scheme lands just outside its own target; at 16.16% it
  misses by more than a point. The lower number appears in the celebratory press release;
  the higher one was given under parliamentary answer six weeks earlier. Alongside it, the
  January release reports the sector's first positive bottom line in years: **PAT of
  +₹2,701 crore in FY 2024-25**, against **−₹25,553 crore in FY 2023-24** and **−₹67,962
  crore in FY 2013-14** — a ₹28,254 crore swing in a single year — and an ACS–ARR gap
  narrowing from ₹0.78/kWh (FY 2013-14) to **₹0.06/kWh (FY 2024-25)**.
- **Blog fit**: opens the confirmed zero-coverage **electricity distribution** area, and
  materially updates `discom-debt-relief-token-charge`, whose entire model rests on discoms
  *adding* ₹64,000 crore of debt a year — a premise a sector-wide positive PAT puts in
  question, or at least dates. Nearest published neighbours are
  `thermal-parity-is-dead-what-85-oil-and` (power economics reached through fuel prices) and
  `rooftop-solar-is-working-household` (the consumer end of distribution). Structurally it
  is the same move as `fourteen-years-of-indian-wholesale` and the WPI-rebasing work: take
  an official number everyone repeats and ask which official number.
- **Caveat**: five, and the first is the one that could kill the piece. (1) **The two
  releases may not have the same denominator.** Neither states which utilities it counts —
  all distribution utilities, only RDSS participants, discoms-plus-power-departments, or
  state-only. The January PAT sentence says "DISCOMs and power departments" explicitly; the
  December AT&C sentence says only "distribution utilities at the national level". If the
  coverage differs, the 1.12-point gap is a scope difference, not a contradiction, and the
  piece must say so — resolve this against the PFC report's utility count before writing
  anything. (2) **FY25 figures are almost certainly provisional.** PFC's own FY 2023-24
  edition covered 63 of 72 distribution utilities with 52 of 59 submitting audited accounts
  (trade-press figure, see WEAK below); an FY25 number published in Dec 2025 / Jan 2026
  cannot be more audited than that, and provisional numbers get revised. (3) **AT&C loss is
  a ratio, and ratios move for accounting reasons.** The same January release lists the
  *Electricity Distribution (Accounts and Additional Disclosure) Rules, 2025* and new
  subsidy-accounting rules among its achievements — changes to how subsidy is booked move
  ACS–ARR and AT&C without a single unit of stolen power being recovered. (4) **₹0.06/kWh
  is suspiciously round and is a national average** that hides state dispersion; do not
  narrate it as "cost recovery achieved". (5) The FY21 and FY 2013-14 baselines are
  different in the two releases, so the *trends* are not directly comparable either — only
  the FY25 endpoint is a like-for-like clash.
- Grade: **COMMISSIONABLE**. Logged 2026-09-09.

### Weak/off-scope, one line each (triaged, not deep-read)

- **PFC, *Report on Performance of Power Utilities* (2023-24 and 2024-25 editions)** — the
  underlying annual series for every figure above, and the primary this piece really wants.
  **Currently unreachable.** `pfcindia.com` now fails TLS (its certificate covers only
  `*.pfcindia.co.in`), and `pfcindia.co.in` has migrated to a React SPA that returns the
  same 2,322-byte JavaScript shell — HTTP 200, `text/html` — for *every* legacy
  `ensite/DocumentRepository/...` PDF path indexed by search engines, including the
  2024-25 edition, with a browser User-Agent and Referer set. The Wagtail CMS at
  `cms.pfcindia.co.in` serves documents from `/media/documents/`, but the site's own API
  routes (`/api/v2/data_listing/`, `/api/v2/search-page/`) 404 from outside the app. Not
  registered on trade-press figures alone. **Next attempt should drive the SPA in a browser
  to capture the real `cms.pfcindia.co.in/media/documents/` URL**, which is the one durable
  path — this is a retrieval problem, not a source problem, and the document is free.
- **Power Line Magazine, "PFC releases latest report... for 2023-24" (02 June 2025)** —
  fetched, and the only accessible account of the FY24 edition: AT&C **rose** 15.11% →
  16.12% between FY23 and FY24, billing efficiency 86.98% → 86.91%, collection efficiency
  97.6% → 96.51%, 63 of 72 utilities covered. Useful as corroboration that the series was
  *worsening* the year before both PIB releases claim improvement — but it is trade press
  summarising a document, so **cite the PFC report or nothing**. WEAK as a citation,
  valuable as a pointer.
- **PFC/MoP, *13th Annual Integrated Rating & Ranking of Power Distribution Utilities***
  (indexed at two `pfcindia.co.in` paths, one dated 18 06 2025) — the per-discom grading
  companion to the report above and the natural source for a state-by-state map in the
  blog's usual style. Same broken repository, so unverified; note it for the same browser
  attempt.
- **Dataful / FACTLY structured discom tables** — a third-party re-publication of PFC's
  numbers in clean form. Convenient, but it is a mirror of a government series; the standing
  rule applies. Never cite in place of PFC.

---

## 2026-09-11 (daily task, Friday: irrigation, water and soil)

### Soil Health Card nutrient dashboard — the GraphQL endpoint answered, and it changes what the queued soil piece can claim

The 2026-09-04 entry registered `soilhealth4.dac.gov.in` as "up and awaiting a well-formed
query" — the endpoint returned HTTP 400 to a bare GET and nothing had been pulled. It has
now been queried successfully, which resolves the **blocking check** on the queued item
*"India tested its soil twice. The second time, a machine chose the spot."*

- **Data — obtainable, free, unauthenticated, and district-level.** `soilhealth.dac.gov.in`
  serves a 657-byte SPA shell; the operation names are in its bundle at
  `/assets/index-Ed_k0WPH.js`. The relevant one is **`GetNutrientDashboardForPortal`**,
  taking `state`, `district`, `block`, `village`, `cycle` and `scheme` — so granularity
  runs to **village**, not state-only, which was the risk the blocking check named. It
  answers over plain POST with a browser `User-Agent` plus `Origin`/`Referer` on
  `soilhealth.dac.gov.in`; **no login, no key, no cookie**. Schema introspection is
  disabled (a generic "Unable to connect to the server" error), so operation names must
  come from the bundle. `GetState` returns the 34 state/UT ids needed as inputs. Each row
  carries sample **counts** (not values) for twelve parameters — N, P, K, S, **OC**, pH,
  EC, Fe, Zn, Cu, B, Mn — bucketed High/Medium/Low for OC.
- **Finding — 9,204,404 organic-carbon samples in 2024-25 across 743 districts, and
  47.6% of them are Low.** Medium 28.4% (2,612,208), High 24.0% (2,211,638), Low 47.6%
  (4,380,558). 2023-24: 4,111,331 samples, **50.1% Low**. 2025-26 (in progress):
  11,367,996 samples, **51.9% Low**. Rows are stamped `lastProcessedAt` 2026-09-10, i.e.
  the series is live, not a static release.
- **Finding that matters more — the public dashboard does not span the seam at all.**
  Cycles **2020-21 and 2022-23 return zero rows**; the first cycle with any data is
  **2023-24**. The queued item's argument was that the April-2023 portal rebuild put a
  methodological seam through India's only national soil panel. The stronger and simpler
  version is now available: **the public data begins at the seam.** Any district- or
  national-level organic-carbon *trend* that crosses April 2023 cannot be sourced from
  this portal, because the portal holds nothing before it. That reframes the piece from
  "compare two regimes carefully" to "the comparison everyone is making cannot be made
  from the government's own dashboard".
- **Integrity check, done rather than assumed.** Calling the query with no `state`
  returns a national aggregate in a different row shape (37 rows for 2024-25 against 861
  when summed state-by-state). The **OC totals reconcile exactly — 9,204,404 either way**,
  so the no-state call is a genuine aggregate and not a partial slice. 32 of 34 states
  returned 2024-25 rows; **Delhi and Dadra & Nagar Haveli and Daman & Diu returned none**.
- **Blog fit.** Opens the **soil / soil-organic-carbon** zero-coverage area (survey §3,
  0 posts). Nearest published post is `indias-79-lakh-crore-rural-water` — drinking water
  under a different ministry, so adjacent, not overlapping. Cite it as earlier reporting
  in house style, never as confirmation.
- **Caveats.** (1) These are **counts of samples in a bucket, not measured carbon values**
  — never write "organic carbon fell to X%"; the honest sentence is "X% of samples tested
  Low". (2) The High/Medium/Low thresholds are not published on the endpoint; find them
  before characterising what "Low" means agronomically. (3) Sample counts are not area and
  not farms — sampling density varies by state, so a state with more Low samples may
  simply have tested more. Never rank states on these counts without a denominator.
  (4) 2025-26 is an **incomplete cycle**; do not compare its percentage to a closed year
  without saying so. (5) Rows are per district **per scheme** (861 rows over 743
  districts), so a naive district count double-counts — group before counting.
  (6) Undocumented endpoint behind a public dashboard: keep a dated local copy of every
  figure used, as with the PPV&FR chart literals.
