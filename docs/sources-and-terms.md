# Data sources and terms

Every external source, what we use it for, and whether it may back paid features. Not legal advice: confirm commercial use in writing with each provider before charging money. Re-check each row before launch.

| Source | Used for | Terms | Checked | Commercial status | Contact log |
| --- | --- | --- | --- | --- | --- |
| RIPEstat Data API | State and activity signals (Phase 1) | [T&C](https://www.ripe.net/about-us/legal/ripestat-service-terms-and-conditions/), article 3 | 2026-10-06 | Needs written permission from RIPE NCC | Sent 2026-10-10, waiting for reply 
| RIS raw data (MRT) and RIS Live | Raw events, incident replay, paid alerts | [RIS commercial use](https://ripe.net/analyse/internet-measurements/routing-information-service-ris/commercial-use) | 2026-10-06 | Default, revocable permission with RIPE NCC logo, link and credit | Asked in RIPE NCC email 2026-10-10, waiting for reply |
| RIPE Data Repository | Not used | [T&C](https://ripe.net/analyse/raw-data-sets/terms-conditions) | 2026-10-06 | No commercial use | — |
| RouteViews | US vantage points, 15-minute history | [Commercial terms](https://www.routeviews.org/routeviews/licenses/): CC BY 4.0; research: cite DOI 10.7264/1y7v-2d90 | 2026-10-12 | Allowed under CC BY 4.0 with attribution, logo, boilerplate and change notice; licence revocable | Reply from Steve Huter 2026-10-12 (PDF in docs/correspondence/, local only) || CAIDA AS Rank | Watchlist selection | [AUA](https://www.caida.org/about/legal/aua/) | 2026-10-06 | Research, education and internal commercial testing; confirm before a paid launch | — |
| APNIC per-AS user estimates | Watchlist selection | [aspop](https://stats.labs.apnic.net/aspop); no licence terms found | 2026-10-06 | Unknown; email APNIC Labs before any commercial use | — |
| PeeringDB | Manual checks only | [AUP](https://peeringdb.com/aup) | 2026-10-06 | No commercial use or bulk storage; never store its data | — |
| Cloudflare Radar API | Learning, free public dashboard | [About](https://v2.radar.cloudflare.com/about): CC BY-NC 4.0 | 2026-10-06 | Non-commercial only | — |

## Questions for RIPE NCC

1. Is a free public dashboard alongside a paid product "commercial use" of the RIPEstat Data API?
2. Are paid alerts built on RIS raw data covered by the default RIS commercial-use permission?
3. Does RIS data fetched through RIPEstat fall under the RIS terms or the RIPEstat terms?

## Attribution to show

- RIS: RIPE NCC logo, a link to RIS and the credit text from the RIS commercial-use page.
- RouteViews: for paid use, their exact attribution sentence with a link to www.routeviews.org, the RouteViews logo and their boilerplate description (copy verbatim from the licences page), plus a note that NetSentinel processed the data. For research, cite DOI 10.7264/1y7v-2d90.

## Permission requests

| Date sent  | Provider   | Sent to             | About                                  | Status            |
|------------|------------|---------------------|----------------------------------------|-------------------|
| 2026-10-10 | RIPE NCC   | stat@ripe.net       | Commercial use of RIPEstat and RIS     | Waiting for reply |
| 2026-10-10 | RouteViews | help@routeviews.org | Commercial use and attribution         | Replied 2026-10-12|