# Incident catalogue (seed list)

Ground truth for evaluation. Incidents are positives the detector should catch. Planned changes (mergers, migrations) are hard negatives: real routing changes that must not be reported as incidents. These rows seed the incidents and known-events tables in Week 8. Times are UTC.

| Date | Type | Networks | What happened | Window (UTC) | Source |
| --- | --- | --- | --- | --- | --- |
| 2026-08-20 | Planned change | Cox AS22773, Charter | Charter completed its acquisition of Cox | — | [Light Reading](https://lightreading.com/cable-technology/charter-wraps-cox-and-liberty-broadband-transactions) |
| 2026-02 (early) | Planned change | Lumen → AT&T | AT&T completed its purchase of Lumen's consumer fibre business | — | [Total Telecom](https://totaltele.com/att-completes-acquisition-of-lumen-mass-markets-fiber-biz/) |
| 2024-11-15 | Planned change | Sunrise AS6730, Liberty Global AS6830 | Sunrise spun off from Liberty Global and listed on SIX | — | [SIX](https://www.six-group.com/en/newsroom/news/the-swiss-stock-exchange/2024/sunrise-listing.html) |
| 2023-11 | Planned change | Lumen EMEA → Colt AS8220 | Colt completed its purchase of Lumen's EMEA business | — | [Colt](https://www.colt.net/resources/colt-lumen-emea/) |
| 2020-08-30 | Incident (outage) | CenturyLink/Level(3) AS3356 | A bad Flowspec rule caused a global outage; about 3.5% drop in global traffic | 10:03–14:30 | [Cloudflare](https://blog.cloudflare.com/analysis-of-todays-centurylink-level-3-outage/) |
| 2019-06-24 | Incident (route leak) | Verizon AS701 | Verizon propagated a route leak from a customer's BGP optimizer | 10:34–12:39 | [Cloudflare](https://blog.cloudflare.com/the-deep-dive-into-how-verizon-and-a-bgp-optimizer-knocked-large-parts-of-the-internet-offline-monday) |

Pending: TIM's sale of Sparkle (AS6762) to MEF and Retelit, signed April 2025 ([Corriere Comunicazioni](https://www.corrierecomunicazioni.it/?p=342276)). Add the closing date once it's announced.

## Where to find more

- [Kentik: a brief history of the internet's biggest BGP incidents](https://www.kentik.com/blog/a-brief-history-of-the-internets-biggest-bgp-incidents/)
- Cloudflare Radar route-leak and hijack events, RIPE Labs articles and NANOG threads
