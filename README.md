# AERONAUT flight simulator

[Play the latest game](https://hackyult.github.io/?v=124)

Release 124 fixes airport transition terrain work, source-aware imagery levels, Lhasa startup, mapped taxi pavement grading, separate taxi and takeoff clearances, runway side phraseology and six placeholder airport identifiers. Ground thrust is increased about 7% while the longer rollout from release 123 is retained. Systems default to a compact collapsed panel; all controls remain available.

97 targeted checks and eight fleet reference takeoff/dry-wet rollout scenarios passed. Browser verification completed a VHHH gate to ZULS runway transition. These are game checks, not certified aircraft performance.

The directory contains 1,153 records, including 1,095 with runway geometry. Imagery availability was sampled at their centres and runway ends; 323 require lower native detail. This is not visual verification of every airport against current satellite imagery. Mapped taxi geometry covers 382 airports; 57 automatic departure connections pass the current route audit. Missing connections remain unavailable rather than invented. Terminal-wall stands and interiors remain estimates.

Earlier city night streaming, minimized tower, airport/model and weather work is retained. The global enroute reference contains 70,285 historical airway segments, cycle 2012.08; it is not current worldwide AIRAC. Regional FAA/OpenFlightMaps and global navaids remain available.

[Release details](https://github.com/HackYult/HackYult.github.io/releases/tag/v0.1.124) · [Sources / licences](https://hackyult.github.io/sources/). The deployed archive is verified by SHA-256 in GitHub Actions. Source documentation includes the primary AIP/ICAO references for identifier corrections and explicit coverage limits.
