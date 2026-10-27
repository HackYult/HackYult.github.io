# AERONAUT flight simulator

[Play release 147](https://hackyult.github.io/?v=147) · Default ZBAA → VHHH · Boeing 787-9 · Arrival starts with 5% remaining.

Approach fixes use one combined map label: purple waypoint name and blue altitude. Duplicate route labels are removed immediately when a procedure loads or changes, including the initial asynchronous load.

This update adds 967 representative approaches from the public AIRAC API and official CAAT coding-table approaches at six airports. It addresses 973 of the original 1,044 missing-airport records; 71 remain unresolved. API lateral main sequences are checked for coordinate continuity and physical runway alignment. They are not independently certified official-chart transcriptions; missing restriction rules or maneuver geometry are not invented.

Arrival guidance uses the same runway and direction as the selected source approach. Paro follows its continuous published cloud-break track through PR708; missed approach is selectable separately and the visual landing segment is not fabricated. Daxing can connect through its real approach entry. Ponta Delgada remains disconnected in the historical airway network.

36 focused navigation checks passed. [Coverage and remaining gaps](https://hackyult.github.io/data/procedures136/coverage.html) · [Evidence, tests and limitations](https://hackyult.github.io/sources/release146/).

Graphics recovery and terrain transitions from release 144 remain included. Pilot Navigation stays below the map; Route chart keeps its original small button and Controls starts folded.

Release 147 fixes global-dialog stacking, bounded left/right tool windows and Controls access. Pilot Navigation follows the aircraft through automatic arrival chart loading; overview and manual pan remain available. Terrain upload work is budgeted, repeated source images share GPU storage, moving coverage and DEM seams transition from the rendered pose, and inactive cached scenery avoids matrix traversal.

75 related regression checks passed. Real-game checks confirmed centred navigation, topmost world dialogs and Controls reopening. A synthetic 64-subtile test used 1 shared GPU texture instead of 64 duplicates; no whole-game FPS percentage or universal zero-pop guarantee is claimed. [Release 147 checks](https://hackyult.github.io/sources/release147/).
