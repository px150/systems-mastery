# Systems Mastery

> Building a modern software systems stack from first principles: operating systems, networking, databases, distributed systems, observability, infrastructure, and production engineering.

## Overview

Systems Mastery is a long-term, hands-on learning journey focused on understanding how modern software systems are built—from low-level foundations to production-ready distributed applications.

The goal is not simply to use existing technologies, but to understand, implement, analyze, and eventually contribute to the systems that power modern software.

Over time, this repository will grow into a miniature software systems stack built component by component.

## Objectives

* Build a deep understanding of modern software systems.
* Learn by implementing core components from scratch.
* Read and analyze real-world open-source code.
* Explore the engineering trade-offs behind production systems.
* Develop the skills required to understand and contribute to projects such as Linux, nginx, PostgreSQL, Redis, Envoy, Kubernetes, and similar systems.
* Learn how to design, debug, observe, and operate production software systems.

## Learning Philosophy

Systems Mastery follows a few core principles:

* Learn from first principles.
* Build instead of only consuming.
* Progress through small, incremental modules.
* Connect theory with implementation.
* Read real production code continuously.
* Validate ideas through experiments and benchmarks.
* Focus on understanding trade-offs rather than memorizing technologies.

The journey covers the complete software systems stack, from computer architecture and operating systems to networking, databases, distributed systems, observability, cloud infrastructure, and production engineering.

## Repository Structure

```text
systems-mastery/
├── docs/
├── computer-architecture/
├── operating-system/
├── memory/
├── concurrency/
├── networking/
├── database/
├── distributed-systems/
├── observability/
├── infrastructure/
├── experiments/
└── ...
```

Each directory will evolve throughout the journey and represent a concrete building block of the overall software systems stack.

## Technologies

Different languages are used for different purposes:

* **C++** — implementations, systems programming, infrastructure, networking, concurrency, and understanding the implementation of major software systems.
* **Python** — experiments, automation, tooling, benchmarking, and supporting utilities.

Throughout the journey, real-world systems written in C, Go, and other languages are also studied to understand their architecture and engineering decisions.

## Documentation

The repository documentation lives under `docs/`.

* `manifesto.md` — learning philosophy and guiding principles.
* `roadmap.md` — curriculum and roadmap.
* `engineering-notebook.md` — technical notes, insights, and architectural observations.
* `module-checkpoints/` — summaries of completed modules.

## Progress

The project is organized into incremental modules.

Each completed module should produce at least one tangible artifact:

* a new component;
* an implementation;
* an experiment;
* a benchmark;
* a code-reading analysis;
* or a meaningful engineering note.

## Disclaimer

This repository is intentionally educational.

The implementations prioritize clarity and understanding before performance or completeness.

Whenever possible, simplified implementations are later compared with production-grade open-source projects to understand the engineering decisions behind them.

## License

MIT