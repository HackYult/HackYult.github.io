# AERONAUT flight simulator

[Play release 134](https://hackyult.github.io/?v=134) · Default VNKT → ZULS.

Release 134 adds 59 original FlightGear structures at 41 airports. Source geometry, textures, authorship, source archives and published placement remain bundled. Batched source draws fall from 4,546 to 526.

Actual browser flights exposed an automatic-landing handoff that retracted landing configuration on stable final. This is repaired, with staged configuration recovery. A fixed exterior light pool and preflight camera-material preparation reduce shader-compilation triggers during flight.

[Coverage, flown checks, source dates and limitations](https://hackyult.github.io/sources/release134/).

A380 ZULS approach through gate parking and 777 EHAM moderate-wind approach through touchdown and taxi were flown in the actual renderer. 72 landing scenarios and full A380/787 VNKT–ZULS physics routes pass. 110 related regression checks and 18 final affected checks pass.

Source-authored structures cover 115 airports; 151 have packaged models including mapped-footprint structures. Mapped centreline data covers 383 airports, while 58 currently pass complete automatic-route checks. Exact current terminal replication, surveyed satellite registration, certified flight dynamics and zero frame hitches are not claimed.

Prior scenery, airport loading, tug, terrain transitions and continuous-flight repairs are retained.
