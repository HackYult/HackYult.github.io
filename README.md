# AERONAUT flight simulator

[Play the game](https://hackyult.github.io/?v=121)

Release `v0.1.121` upgrades the shared terminal architecture system across 80 airport regions and 763 mapped footprints. Continuous curtain glazing, mullions, foundation plinths, bounded lounge furnishings, English wayfinding and a Lounge camera improve airport views. Source roofs and mapped outlines are retained. Model elevation follows the runway and graded apron datum instead of DEM roof spikes.

Aircraft rotation contact uses a precomputed envelope from actual supplied tyre vertices, with smooth liftoff blending. Grounded aircraft no longer receive whole-model cosmetic shake that moves tyres through pavement. Eight deployed aircraft were checked at five rotation pitches; 43 targeted checks pass.

The verified release archive is attached to the release. GitHub Actions checks its SHA-256 and publishes the static game through GitHub Pages. Earlier aircraft, terrain, aviation-chart and dynamics repairs are retained.

Interiors, building heights and aircraft dynamics remain approximations. The shared architecture upgrade is not 80 individually surveyed airport replicas. Exact real-world equivalence is not claimed. Satellite resolution and photographic colour depend on the imagery provider. OpenFlightMaps coverage is regional; FAA charts cover the United States.

Game and model source packages, attribution and restoration scripts are available under [/sources/](https://hackyult.github.io/sources/). Consult `ATTRIBUTION.md` for individual asset licences, including noncommercial restrictions.

No account credentials or private server are required to play. Public imagery and chart services require an internet connection.
