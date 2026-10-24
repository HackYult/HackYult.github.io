# AERONAUT flight simulator

[Play the latest game](https://hackyult.github.io/?v=126)

Release 126 replaces generated traffic with a forward terrain-elevation display: one-second sweep, relative height colours, 200 m contours, 5/10/20 NM ranges and minimize/enlarge controls. It uses real DEM, not weather reflectivity or certified TAWS. All 1,024 coarse zoom-5 global terrain tiles are bundled (Web Mercator latitude limits); nearby finer elevations stream on demand. Missing/coarse data is labelled.

HUD instruments are smaller, warnings have reserved space, tape digits cannot overlap fixed readouts, and cockpit/status/HUD IAS share one conversion. External aircraft reference and cockpit horizon use explicit attitude frames. Ground thrust acceleration is increased 41.8%, with the extra gain removed under wheel braking. Eight preset takeoff scenarios are 34–40% quicker; airborne thrust and idle dry/wet stopping distances are retained. This is a requested gameplay boost, not certified aircraft performance.

60 targeted checks passed, with browser verification of real Himalayan DEM, radar controls, warnings and matching IAS readouts. The source/route audit checks all 1,095 selectable airports and 1,680 runways. 1,618 runway records match stored reference endpoints within 5 m; 62 remain unmatched. Only 57 automatic taxi connections are currently validated. Centreline queries at both public OSM endpoints repeatedly timed out. Exact routes at all airports and pixel-by-pixel satellite alignment are not claimed. [Full airport audit](https://hackyult.github.io/sources/release126/all-airports.json).

Earlier preflight weather, factory paint, city night, airport terrain and taxi phraseology work is retained. The global enroute reference is archived cycle 2012.08, not current worldwide AIRAC; regional charts and global navaids remain available.

[Release details](https://github.com/HackYult/HackYult.github.io/releases/tag/v0.1.126) · [Sources / licences](https://hackyult.github.io/sources/). GitHub Actions verifies the release archive by SHA-256 before deployment.
