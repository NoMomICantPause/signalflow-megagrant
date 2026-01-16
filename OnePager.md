# SignalFlow — Reactive Gameplay & Networking Framework for Unreal Engine 5

## One-Sentence Pitch

SignalFlow enables Unreal Engine developers to build reactive UI, gameplay, and networked systems without polling, boilerplate replication, or actor overhead — at sub-microsecond cost per update.

---

## Problem

Unreal Engine projects repeatedly face the same systemic issues:

- **UI inefficiency:** UMG bindings poll every frame, wasting CPU on all platforms.
- **Replication boilerplate:** Each replicated value requires repetitive C++ code (UPROPERTY, OnRep, DOREPLIFETIME).
- **Actor overhead:** Actor-centric data models introduce unnecessary memory, ticking, and replication channels.
- **Limited attribute systems:** Epic's GAS supports only float attributes, limiting expressiveness.

These patterns negatively impact performance, scalability, and developer productivity, especially on mobile and data-heavy games.

---

## Solution

SignalFlow introduces a reactive, actor-agnostic data layer for Unreal Engine:

- **Reactive signals:** Data propagates only when it changes — zero polling.
- **Automatic replication:** One flag enables full network sync via a singleton replication actor.
- **Global signal registry:** Blueprint-accessible, no casting or dispatchers.
- **Type-agnostic attributes:** Store any type (int, bool, FVector, structs), not just floats.
- **Blueprint + C++ parity:** 13 Blueprint nodes backed by a high-performance C++ core.

---

## Technical Differentiation

- 128-bit cache-aligned signal handles
- Event-driven propagation (no ticks)
- Actor-decoupled replication using FFastArraySerializer
- Computed signals with automatic dependency tracking
- Zero allocations in hot paths

**Measured performance (Jan 2026, AMD Ryzen 5 4600G):**

| Category | Result |
|----------|--------|
| AttributeFlow indexed read | **3.7 ns/op** |
| Simple signal operations | 70–300 ns/op |
| Full reactive pipelines | <0.5 µs/op |
| Spatial queries (10k entities) | ~1–2 µs/op |
| Octree registration | 2.2 µs/op |
| Memory allocations (steady-state) | 0 MB |

This makes SignalFlow viable for gameplay-critical systems, not just UI.

---

## Project Status

- ✅ Core architecture complete
- ✅ Automated tests (37)
- ✅ Performance benchmarks (8 suites)
- ✅ Functional demo available
- ✅ GitHub repository ready

The project is ~70% complete and requires funding to reach production-ready quality.

---

## Community Impact

- Released **free** on the Unreal Marketplace
- Full source code included
- Improves performance and workflow for:
  - Blueprint designers
  - Gameplay programmers
  - Networked games
  - Mobile and console projects

SignalFlow directly addresses common Unreal Engine pain points while remaining fully compatible with Epic's ecosystem.

---

## Funding Request

**€650,000** over **18 months** to:

- Finalize cross-platform support (PC, console, mobile)
- Complete documentation and tutorials
- Perform QA, certification, and devkit testing
- Deliver polished starter templates

---

## Why Epic MegaGrant

SignalFlow strengthens Unreal Engine as a platform by:

- ✅ Encouraging efficient, modern data-driven patterns
- ✅ Reducing common performance antipatterns
- ✅ Empowering Blueprint-only developers with high-performance tools
- ✅ Making Unreal more competitive for mobile and large-scale data-heavy games

---

*Developed by **No Mom I Can't Pause** — Lead Developer: Samir Abdallah-Saleh Gracia*
