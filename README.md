# AERONAUT flight simulator

[Play the latest game](https://hackyult.github.io/?v=128)

Release 128 grades Lhasa ZULS using 25 sourced hard-pavement polygons and the 28-vertex airport boundary from Gateway scenery 107849. The intervening airfield ground is flat at the game runway datum, with smooth transitions to surrounding DEM. Mapped taxi corridors have a wider flat core across airports. Source vertices approximate curved pavement edges; current surveyed slopes or satellite pixel alignment are not claimed.

Full-power departure ground thrust increases 83%, blended with engine output and removed under wheel braking. Eight reference presets lift off 47–50% sooner. Ordinary taxi/airborne thrust and idle dry/wet stopping outcomes are retained. This is a requested gameplay acceleration boost, not certified performance.

Radar defaults to CLEARANCE, computed as aircraft MSL minus terrain MSL. Closer or higher terrain is darker, larger vertical separation lighter. Ten continuous colour anchors, minimum-separation readout, a clearance legend and terrain-above-aircraft hatching replace the prior default absolute-height palette. The one-second sweep, panel controls and optional absolute-elevation mode remain available.

102 focused and regression checks passed, with browser comparisons of actual Himalayan terrain at two aircraft altitudes. The previous release's smooth landing response and local short pushback remain available. [Validation](https://hackyult.github.io/sources/release128/validation.json).

Source pavement: X-Plane Scenery Gateway 107849, atag5, approved 2025-08-22, GPL-2.0. Source and attribution are bundled. Earlier airport-wide coverage limits remain: only 57 automatic taxi connections are validated across 1,095 selectable airports. [Airport audit](https://hackyult.github.io/sources/release126/all-airports.json).

[Release details](https://github.com/HackYult/HackYult.github.io/releases/tag/v0.1.128) · [Sources / licences](https://hackyult.github.io/sources/). GitHub Actions checks the release archive SHA-256 before deployment.
