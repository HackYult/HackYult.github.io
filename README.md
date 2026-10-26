# AERONAUT flight simulator

[Play release 141](https://hackyult.github.io/?v=141) · Default VNKT → ZULS.

PILOT NAVIGATION is docked below the right live map, with six flight readouts in compact expansion and all chart/procedure controls in half-screen enlargement. Route chart retains its original small button. Controls starts folded and remains accessible; its parent stacking boundary no longer hides it behind navigation.

A380 uses element-backed image decoding and CPU-owned RGBA textures for graphics-context recovery. The cached decompressed download buffer is released after parsing. Apple mobile rendering buffers are capped at 1.5x to reduce memory pressure.

31 checks pass. Both PBR and Apple-compatible rendering passed simulated flight-position, bank, gear and forced graphics-context recovery checks. Physical iPad verification and conclusive diagnosis of that device's reported fault remain outstanding. [Validation and measured results](https://hackyult.github.io/sources/release141/).

[Airport chart coverage and gaps](https://hackyult.github.io/sources/release138/coverage.html).
