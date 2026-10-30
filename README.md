# AERONAUT flight simulator

[Play release 148](https://hackyult.github.io/?v=148) · ZBAA → VHHH · Boeing 787-9.

Release 148 checks the entire playable airport catalog, corrects 61 runway fields, quarantines two invalid runway-less duplicates, refreshes 103 airports from FAA cycle 2611 and adds five representative public-reference approaches. Displaced thresholds and historical physical-runway aliases now participate in arrival matching. Hong Kong's dated official centre-runway procedure tables are connected to the flight route.

Of 1,151 playable airports, 1,081 archived-airway/approach combinations pass the continuity audit. 68 lack an imported IAP. LPPD retains a historical airway-network gap; PTSA lacks a complete supported final. The runway audit retains 203 source discrepancies for further review. Public API lateral references and historical tables are not certified current navigation data. [Per-airport sources and gaps](https://hackyult.github.io/data/procedures136/coverage.html).

Arrival joins now preserve both tangents with bounded turns. Source transitions and shared STAR/IAF fixes are retained. Ordered tracking prevents jumps across nearby return legs; descent planning avoids an unintended climb in long-route arrival starts. Four numerical 787 arrivals (VHHH, ZULS, KJFK, EGLL) reached landing and gate / verified runway hold.

Wind varies smoothly with height, position and time; wet braking varies continuously with speed. Final guidance uses ground speed for descent and applies crosswind correction once. Shorter procedural lookahead preserves tight turns. Original paint artwork is retained; exposed metal, glass, rubber and painted surfaces now have distinct reflection response. Apple compatibility mode uses a lightweight highlight shader. These are reduced-order game models, not the Microsoft Flight Simulator engine.

Pilot Navigation follows the aircraft and keeps its map visible when enlarged. Global dialogs occupy the browser top layer; Controls can expand and collapse. Terrain streaming retains the prior release's upload budgets and blended geometry / image transitions. Network/source-image differences and hardware limits still apply.

[Release 148 validation, sources and known limits](https://hackyult.github.io/sources/release148/). Default arrival start remains 5% of route remaining. Simulation only.
