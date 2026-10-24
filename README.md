# AERONAUT flight simulator

[Play the latest game](https://hackyult.github.io/?v=123)

Release 123 reduces wheel braking, reverse thrust and rolling resistance, giving about 33% longer dry landing rollout in the eight-aircraft reference scenarios. Parking-brake holding force is retained.

Release 122 improves wide city night streaming with retained overlapping tiles, bounded look-ahead and gradual light transitions. Ground thrust now uses a force-based reference-load estimate; wind response, touchdown drift and dry/wet braking are more gradual. Tower radio can be manually minimized and remembers its state.

The Global enroute reference adds 70,285 historical airway segments and 30,181 endpoint fixes. **It is archived cycle 2012.08, not current worldwide AIRAC or a complete current chart service.** Existing regional FAA/OpenFlightMaps and global OurAirports navaids remain available. Data is loaded on demand when opening/zooming the chart.

51 targeted checks and eight aircraft reference takeoff/dry-wet rollout scenarios passed. These are game-model checks, not certified type performance. Aircraft mass/thrust calibration, weather presets and scenery remain approximations. Earlier terminal and aircraft repairs are retained.

Game/model source, individual asset licences and navigation data attribution remain available through [Sources / licences](https://hackyult.github.io/sources/) and ATTRIBUTION.md. The verified release archive is deployed by GitHub Actions with a SHA-256 check.
