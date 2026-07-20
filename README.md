# learn_hdl_simulator

[![GitHub](https://img.shields.io/badge/GitHub-learn__hdl__simulator-181717?logo=github)](https://github.com/universal-verification-methodology/learn_hdl_simulator)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-green?logo=creativecommons&logoColor=white)](LICENSE)
[![Role](https://img.shields.io/badge/role-Git%20submodule-orange)](https://github.com/universal-verification-methodology/learning)
[![Parent](https://img.shields.io/badge/parent-learning%20monorepo-0A9EDC)](https://github.com/universal-verification-methodology/learning)
[![Labs](https://img.shields.io/badge/labs-GitHub%20Pages-222?logo=githubpages)](https://universal-verification-methodology.github.io/learning/tools/)
[![Domain](https://img.shields.io/badge/domain-HDL%20Simulator%20%7C%20browser%20IDE-purple)](https://github.com/universal-verification-methodology/learn_hdl_simulator)

**learn_hdl_simulator** is the open learning path for the *browser HDL Simulator* — guided `hdl-sim-*` literacy plus free practice in the public IDE.

Authors rebuild slides/audio with **module-slides** in the parent monorepo.

## Table of contents

- [Contents](#contents)
- [Browse or clone](#browse-or-clone)
- [Author: module-slides](#author-module-slides)
- [Two learning tracks](#two-learning-tracks)
- [Module landings](#module-landings)
- [Browser labs](#browser-labs)
- [License](#license)

## Contents

```text
learn_hdl_simulator/
├── README.md
├── LICENSE
├── docs/
│   ├── MODULES.md
│   └── TWO_TRACKS.md
├── scripts/
│   └── module.sh
├── module00-intro/
├── module01-hdl-sim-tour/
├── …
└── module10-wrap/
```

## Browse or clone

- **Public IDE:** [https://universal-verification-methodology.github.io/systemverilog-simulator/](https://universal-verification-methodology.github.io/systemverilog-simulator/)
- **Browser labs:** [tools/#hdl-simulator](https://universal-verification-methodology.github.io/learning/tools/#hdl-simulator)
- **Syllabus:** [`syllabus.md` § learn_hdl_simulator](https://github.com/universal-verification-methodology/learning/blob/main/syllabus.md#9-learn_hdl_simulator)

```bash
git clone --recurse-submodules \
  git@github.com:universal-verification-methodology/learning.git
ls courses/learn_hdl_simulator
./scripts/module.sh 01 --check
```

## Author: module-slides

```bash
cd ../..   # monorepo root
python .cursor/skills/module-slides/scripts/transcript_to_outline.py \
  courses/learn_hdl_simulator/module01-hdl-sim-tour
bash .cursor/skills/module-slides/scripts/narrate_clips.sh \
  courses/learn_hdl_simulator/module01-hdl-sim-tour
```

## Two learning tracks

Details: [docs/TWO_TRACKS.md](docs/TWO_TRACKS.md).

| Track | Practice surface | Start here |
|-------|------------------|------------|
| **A — Public simulator** | [HDL Simulator](https://universal-verification-methodology.github.io/systemverilog-simulator/) | [docs/TWO_TRACKS.md](docs/TWO_TRACKS.md) |
| **B — Browser literacy** | `hdl-sim-*` labs | [hdl-sim-tour](https://universal-verification-methodology.github.io/learning/tools/hdl-sim-tour/) |

Lab status snapshot: **8 shipped** browser/bridge labs (see [docs/MODULES.md](docs/MODULES.md)).

## Module landings

Full status table: **[docs/MODULES.md](docs/MODULES.md)**.

| Module | Landing |
|--------|---------|
| 00 — Welcome to the browser simulator | [module00-intro](module00-intro/README.md) |
| 01 — UI tour | [module01-hdl-sim-tour](module01-hdl-sim-tour/README.md) |
| 02 — Hello DUT | [module02-hdl-sim-hello-dut](module02-hdl-sim-hello-dut/README.md) |
| 03 — Step & continue | [module03-hdl-sim-step-continue](module03-hdl-sim-step-continue/README.md) |
| 04 — Poke / force / release | [module04-hdl-sim-poke-force](module04-hdl-sim-poke-force/README.md) |
| 05 — Full-sim waves | [module05-hdl-sim-waves](module05-hdl-sim-waves/README.md) |
| 06 — Multi-file project | [module06-hdl-sim-multi-file](module06-hdl-sim-multi-file/README.md) |
| 07 — Golden compare | [module07-hdl-sim-compare-golden](module07-hdl-sim-compare-golden/README.md) |
| 08 — Style & synth hints in the IDE | [module08-style-synth-bridge](module08-style-synth-bridge/README.md) |
| 09 — Open public simulator — free practice | [module09-offline-public-sim](module09-offline-public-sim/README.md) |
| 10 — Simulator path complete | [module10-wrap](module10-wrap/README.md) |

## Browser labs

**Shipped:** [hdl-sim-tour](https://universal-verification-methodology.github.io/learning/tools/hdl-sim-tour/) · [hdl-sim-hello-dut](https://universal-verification-methodology.github.io/learning/tools/hdl-sim-hello-dut/) · [hdl-sim-step-continue](https://universal-verification-methodology.github.io/learning/tools/hdl-sim-step-continue/) · [hdl-sim-poke-force](https://universal-verification-methodology.github.io/learning/tools/hdl-sim-poke-force/) · [hdl-sim-waves](https://universal-verification-methodology.github.io/learning/tools/hdl-sim-waves/) · [hdl-sim-multi-file](https://universal-verification-methodology.github.io/learning/tools/hdl-sim-multi-file/) · [hdl-sim-compare-golden](https://universal-verification-methodology.github.io/learning/tools/hdl-sim-compare-golden/) · [hdl-style](https://universal-verification-methodology.github.io/learning/tools/hdl-style/) · [synth-lint](https://universal-verification-methodology.github.io/learning/tools/synth-lint/).

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — see [`LICENSE`](LICENSE).
