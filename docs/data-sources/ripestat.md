# RIPEstat signal catalogue

Fill this in during Week 4 from live calls on three contrasting networks: AS3320 (eyeball), AS3356 (transit) and AS12956 (transit-free). Save one JSON response per call in `tests/fixtures/`.

Checked: YYYY-MM-DD · Usage rules (sourceapp, rate limits): <link>

| Signal | Data call | Resolution | History depth | Suits network type | Fixture |
| --- | --- | --- | --- | --- | --- |
| Visibility and originated prefixes | routing-status | | | | |
| Originated vs transited prefixes | ris-prefixes | | | | |
| Prefix counts over time | prefix-count | | | | |
| Announced prefixes with timelines | announced-prefixes | | | | |
| Announcement and withdrawal activity | bgp-update-activity | | | | |
| Individual updates with AS paths | bgp-updates | | | | |
| Neighbour changes | asn-neighbours-history | | | | |
| Holder and registration | as-overview | | | | |
| RPKI validity per prefix | rpki-validation | | | | |

## Notes per call

Copy this block for each call.

### <data call>

- Parameters used:
- Response fields we keep:
- Response size for a large ASN:
- Warnings and failure modes seen:
- Fixture: `tests/fixtures/<file>.json`
