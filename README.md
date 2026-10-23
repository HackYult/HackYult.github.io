# AERONAUT flight simulator

[Play the game](https://hackyult.github.io/)

The verified release archive is attached to release `v0.1.118`. GitHub Actions checks its SHA-256 and publishes the compiled static game through GitHub Pages. The website uses the domain root so its aircraft, cockpit, imagery and navigation data paths resolve correctly.

Release 118 adds ISA-based true airspeed for airborne movement and coordinated turns, TAS-based wind correction, bank-induced drag and wing loading, and ground speed / ETE on the route chart. Real DEM terrain now streams a bounded flight lookahead, limits simultaneous downloads, publishes incremental height updates and retries failed requests. Terrain planning reuses per-level projection coordinates. It retains Release 117 aircraft, moderate wind, terrain seam protection, airport and lighting refinements, and aviation chart layers.

Flight dynamics remain a simplified game model, not certified aircraft performance. OpenFlightMaps coverage is regional; FAA charts cover the United States.

Game source, model source packages, attribution and restoration scripts are included in the archive at `dist/sources/` and are also served at [/sources/](https://hackyult.github.io/sources/). Consult `ATTRIBUTION.md` for each asset's licence. This game includes assets restricted to noncommercial use; no single blanket licence replaces individual asset licences.

No account credentials or private server are required to play. Public third-party imagery and chart services require an internet connection.
