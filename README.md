# AERONAUT flight simulator

[Play the latest game](https://hackyult.github.io/?v=129) · [Search the all-airport terrain report](https://hackyult.github.io/sources/release129/)

Release 129 audits all 1,095 selectable airports and 1,680 runways, sampling 1,331,655 stored runway/taxi/terminal locations. Actual zoom-12 DEM checks cover 5,040 runway endpoints/centres from 1,748 tiles; all were available.

The grading priority that caused height conflicts at 258 airports is corrected. Secondary runway cores now match the physical collision datum, shoulders transition smoothly, terminal foundations remain protected, and automatic ground travel follows sampled graded terrain. The full after audit finds zero conflicts under the stored-surface criteria. This is not a visual or surveyed-flatness certification of every airport.

Zhangjiajie ZGDY's incorrect airport reference of 2,599.944 m is corrected to the charted 217.2 m. Its flat game runway uses the threshold mean, 209.9 m. Persistent import overrides prevent the erroneous public database height returning. Source: [archived CAAC AIP chart copy](https://yinlei.org/x-plane10/doc/ZGDY.pdf).

65 regression checks passed. Remaining flags are explicit in the report: 100 airports have intersecting-runway source mean-height differences requiring slope/datum review; 725 lack complete mapped apron coverage. All rows distinguish stored-surface checks from independent visual review. No missing apron geometry or surveyed profiles are invented.

The prior clearance radar, takeoff acceleration boost, smooth landing response and short local tug pushback are retained. Earlier navigation/automatic taxi coverage limits remain documented in the bundled sources.

[Release details](https://github.com/HackYult/HackYult.github.io/releases/tag/v0.1.129) · [Sources / licences](https://hackyult.github.io/sources/). GitHub Actions checks the release archive SHA-256 before deployment.
