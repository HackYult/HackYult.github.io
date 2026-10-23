# AERONAUT flight simulator

[Play the game](https://hackyult.github.io/?v=120)

Release `v0.1.120` fixes A380 wheel-well lining emerging through the passenger cabin during gear transit, fits wing lights to the supplied geometry and carries them with wing flex. Wind-relative runway airspeed, bank support/drag, ground effect and independent damped gust response extend the existing flight model. Cockpit pavement cues and wind-advected touchdown smoke improve takeoff/landing feedback.

Terrain skirts/lips and bounded low-frequency imagery colour correction reduce seams. Complete parent/detail coverage can start the game while slower high-resolution tiles continue loading. Visible city tiles remain until a complete staged replacement is ready. Eight aircraft were checked at 41 gear positions; 83 targeted checks pass after correction.

The verified release archive is attached to the release. GitHub Actions checks its SHA-256 and publishes the static game through GitHub Pages. Release 119 factory liveries, aviation charts and airport data are retained. Individual redesigns of more than 50 terminals are not included in this exterior/dynamics-focused update.

Flight dynamics and structural coefficients remain reduced-order game estimates, not certified aircraft performance or an embedded Microsoft engine. Exact real-world visual equivalence is not claimed. Satellite resolution and photographic colour still depend on the imagery provider. OpenFlightMaps coverage is regional; FAA charts cover the United States.

Game and model source packages, attribution and restoration scripts are available under [/sources/](https://hackyult.github.io/sources/). Consult `ATTRIBUTION.md` for individual asset licences, including noncommercial restrictions.

No account credentials or private server are required to play. Public imagery and chart services require an internet connection.
