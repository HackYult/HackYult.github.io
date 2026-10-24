# AERONAUT flight simulator

[Play the latest game](https://hackyult.github.io/?v=127)

Release 127 smooths touchdown onset and damped rebound, scales the cabin response with sink rate, and softens the wing touchdown impulse. Pavement vibration follows travelled distance and diminishes at taxi speed. These are estimated game suspension cues, not a certified aircraft model.

The terrain display defaults to continuous sea-level elevation colours with contours and optional relative-height warning mode. Zoom-15 near-aircraft DEM shares the renderer's coordinate system and airport grading; finer pixel spacing does not guarantee native survey accuracy. The bundled coarse global fallback remains available. Missing data stays grey.

Where no verified taxi route exists, a tug can approach, connect, push back 20–32 m, disconnect and leave the aircraft braked for manual taxi. Obstructed or uneven paths are rejected. Verified mapped extended tow routes are retained.

89 focused checks passed, including eight aircraft across four pushback headings, touchdown/wing continuity, bounded radar requests and prior HUD, physics, ground-service and terrain regressions.

The earlier audit covers all 1,095 selectable airports, but only 57 automatic taxi connections are validated. Missing centreline/stand coverage and unavailable public query services prevent exact automatic routes at every airport. Stored runway endpoint agreement does not establish satellite pixel alignment. [Airport audit](https://hackyult.github.io/sources/release126/all-airports.json).

[Release details](https://github.com/HackYult/HackYult.github.io/releases/tag/v0.1.127) · [Sources / licences](https://hackyult.github.io/sources/). GitHub Actions checks the release archive SHA-256 before deployment.
