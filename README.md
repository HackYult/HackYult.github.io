# AERONAUT flight simulator

[Play release 130](https://hackyult.github.io/?v=130) · Default route VNKT → ZULS.

The permanent in-flight freeze is fixed: leaving all nearby airport coverage previously made ground-service UI dereference an undefined airport layout before scheduling the next frame. Ground services now handle empty coverage, and view exceptions cannot terminate subsequent frames.

A380 and 787 complete the Kathmandu–Lhasa takeoff-to-rollout regression with 169 actual approach DEM tiles, 100% progress, no crash and zero final speed. Unverified taxi exits remain manual after rollout. Arrival circuits now check forward terrain.

Terrain meshes are created incrementally, geographic rebasing releases stale worker ownership, and visible satellite refinements commit in cohorts. Cold shader compilation, network delays and GPU hitches are not claimed eliminated.

The user-supplied 787 cockpit geometry is installed with four live main screens. Cockpit and Flight displays share state and rendering. Nine external PNGs were absent; neutral panel materials do not pretend to restore missing artwork.

All 1,095 airports / 1,680 runways were sampled again at 1,331,655 stored-surface points. 100 crossing-runway components share a flat game datum without overwriting source heights; 725 airports still lack complete apron mapping. This is not an independent visual survey or exact satellite-alignment certification.

29 final focused checks passed; 39 earlier broad checks passed. Browser terrain/render continuity: 10%–95.01%, 2,907 frames, seven rebases, zero errors. [Validation and images](https://hackyult.github.io/sources/release130/) · [Per-airport audit](https://hackyult.github.io/sources/release129/).

[Release details](https://github.com/HackYult/HackYult.github.io/releases/tag/v0.1.130) · [Sources / licences](https://hackyult.github.io/sources/). GitHub Actions verifies the archive SHA-256 before deployment.
