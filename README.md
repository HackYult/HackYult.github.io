# AERONAUT flight simulator

[Play release 152](https://hackyult.github.io/?v=152). Flight terrain/DEM/stitch residency improvements, zero-light work skipping, retained HUD nodes and minimap order caching, and exact-pixel PAPI instancing. Includes terminal repairs from releases 150–151. 91 relevant regression checks pass. [Verification and scope](https://hackyult.github.io/sources/release152/). Resolution and detail settings retained; microbenchmarks are not whole-game FPS results.

[Play release 151](https://hackyult.github.io/?v=151). Mountain LOD seam/camera corrections, terminal eaves-aligned details, static-transform caching, bounded higher High supersampling and tighter sun shadows. [Verification and limits](https://hackyult.github.io/sources/release151/). CPU transform microbenchmark gains are not a whole-game FPS guarantee.

Release 150 corrects common terminal roof/eaves/glazing geometry and unit conversion, adds the HTDA source outline and mapped jetbridge paths, and enables bounded apron shadows at night. This remains a partial architectural reconstruction: 934 airports still lack independent source models or detailed building outlines. [Changes and known gaps](https://hackyult.github.io/sources/release150/).

[Play release 150](https://hackyult.github.io/?v=150) · ZBAA → VHHH · Boeing 787-9.

Release 148 checks the entire playable airport catalog, corrects 61 runway fields, quarantines two invalid runway-less duplicates, refreshes 103 airports from FAA cycle 2611 and adds five representative public-reference approaches. Displaced thresholds and historical physical-runway aliases now participate in arrival matching. Hong Kong's dated official centre-runway procedure tables are connected to the flight route.

Of 1,151 playable airports, 1,081 archived-airway/approach combinations pass the continuity audit. 68 lack an imported IAP. LPPD retains a historical airway-network gap; PTSA lacks a complete supported final. The runway audit retains 203 source discrepancies for further review. Public API lateral references and historical tables are not certified current navigation data. [Per-airport sources and gaps](https://hackyult.github.io/data/procedures136/coverage.html).

Arrival joins now preserve both tangents with bounded turns. Source transitions and shared STAR/IAF fixes are retained. Ordered tracking prevents jumps across nearby return legs; descent planning avoids an unintended climb in long-route arrival starts. Four numerical 787 arrivals (VHHH, ZULS, KJFK, EGLL) reached landing and gate / verified runway hold.

Wind varies smoothly with height, position and time; wet braking varies continuously with speed. Final guidance uses ground speed for descent and applies crosswind correction once. Shorter procedural lookahead preserves tight turns. Original paint artwork is retained; exposed metal, glass, rubber and painted surfaces now have distinct reflection response. Apple compatibility mode uses a lightweight highlight shader. These are reduced-order game models, not the Microsoft Flight Simulator engine.

Pilot Navigation follows the aircraft and keeps its map visible when enlarged. Global dialogs occupy the browser top layer; Controls can expand and collapse. Terrain streaming retains the prior release's upload budgets and blended geometry / image transitions. Network/source-image differences and hardware limits still apply.

[Release 148 validation, sources and known limits](https://hackyult.github.io/sources/release148/). Default arrival start remains 5% of route remaining. Simulation only.

Release 149 raises bounded High / Ultra framebuffer clarity, enables aircraft-local sun/self/contact shadows, keeps paint grain fixed to UVs, propagates parent photograph fades to child terrain and limits the per-frame progress after stalls. Landing contact uses one damped compression / recovery, nose-contact timing and simulation-clock tyre smoke. The 787 upper gear is clipped against its measured wing skin in colour and shadow passes.

A full FlightGear model-catalog comparison adds 138 source-authored airport structures at 77 airports, retaining original geometry, preferred source packages, licences and coordinates. The full catalog now has entries for 201 airports (including distinct map-derived entries); this is not 1,000 exact independent terminal models. Source vintage and positional accuracy vary.
