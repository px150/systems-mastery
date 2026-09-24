# Systems Mastery Roadmap (V1.1)

> *A living engineering curriculum for mastering modern software systems.*

---

# Purpose

This roadmap defines the long-term learning path of Systems Mastery.

Its objective is not simply to cover technologies, but to progressively build the knowledge, engineering skills, and practical experience required to understand, design, implement, operate, and contribute to modern software systems.

Every module contributes to three parallel goals:

* expanding engineering knowledge;
* extending the Systems Mastery repository;
* strengthening the mental model of the complete software systems ecosystem.

---

# Learning Strategy

The curriculum follows a spiral learning approach.

New systems concepts, algorithms, architectural patterns, and engineering techniques are introduced only when they become necessary to solve real implementation problems.

Concepts are revisited multiple times with increasing depth throughout the journey.

Progress is measured by understanding and implementation rather than by the number of completed modules.

---

## Mastery

Module completion is governed by the criteria defined in `docs/mastery.md`.

Progress is determined by demonstrated understanding rather than by content consumption or implementation alone.

---

## Repository Structure

```text
systems-mastery/
├── docs/
│   ├── modules/
│   │   ├── 0/
│   │   │   ├── 0.1-software-systems-map.md
│   │   │   ├── 0.2-thinking-in-systems.md
│   │   │   ├── 0.3-computational-thinking.md
│   │   │   └── 0.4/
│   │   │       ├── 0.4.1-complexity-fundamentals.md
│   │   │       ├── 0.4.2-arrays-and-memory-layout.md
│   │   │       └── ...
│   │   └── ...
│   ├── engineering-notebook.md
│   ├── glossary.md
│   ├── manifesto.md
│   ├── mastery.md
│   └── roadmap.md
├── src/
│   └── modules/
│       ├── fundamental-algorithms-and-data-structures/
│       │   ├── arrays/
│       │   │   ├── address.py
│       │   │   ├── delete.py
│       │   │   ├── dynamic_array.py
│       │   │   ├── fixed_array.py
│       │   │   ├── insert.py
│       │   │   └── tests/
│       │   │       ├── test_address.py
│       │   │       ├── test_delete.py
│       │   │       ├── test_dynamic_array.py
│       │   │       ├── test_fixed_array.py
│       │   │       └── test_insert.py
│       │   └── ...
│       ├── computer-architecture/
│       ├── low-level-programming/
│       ├── operating-systems/
│       ├── concurrency/
│       ├── networking/
│       ├── backend-systems/
│       ├── data-storage/
│       ├── distributed-systems/
│       ├── observability/
│       ├── infrastructure/
│       ├── reliability/
│       └── security/
├── LICENSE
└── README.md
```

The repository separates curriculum documentation from executable learning artifacts.

The `docs/modules/` directory contains the publication-quality chapters produced after each module has been studied and assessed.

The `src/modules/` directory contains the implementations, experiments, tests, and supporting code developed throughout the curriculum.

Its structure follows the roadmap rather than a fixed technology stack. Directories are introduced progressively as new areas of the curriculum begin, and individual modules may contain their own implementations, tests, benchmarks, or experiments.

Each part of the repository should remain independently understandable while contributing to the broader software systems journey.


---

# Language Roles

## C

Introduced after Computer Architecture as the primary language for low-level systems work.

Used when direct exposure to machine and operating-system mechanisms is part of the learning objective, especially for:

* memory representation and layout;
* pointers and explicit resource lifetime;
* operating-system interfaces and system calls;
* low-level concurrency;
* sockets and network I/O;
* performance-oriented experiments.

C is intentionally used as a transparent systems tool rather than as a language-mastery objective. The curriculum should introduce only the language features required to expose the underlying mechanism being studied.

---

## Python

Primary language during the foundational phases of the curriculum.

Used for:

* algorithms and data structures;
* experiments;
* automation;
* tooling;
* benchmarking;
* supporting utilities.

Python minimizes unnecessary language complexity while foundational engineering concepts are being developed.

It remains available throughout the curriculum whenever rapid experimentation is more valuable than low-level control.

---

## Go

Introduced selectively when the curriculum moves from low-level mechanisms toward network services, distributed systems, observability, and infrastructure.

Go is used when a small implementation surface helps keep attention on system architecture rather than language complexity, especially for:

* backend services;
* concurrent network services;
* distributed-system experiments;
* infrastructure-oriented components;
* production-style service implementations.

Go is not a separate language-learning track. Required language features are introduced on demand inside the module that needs them.

---

## Production Code Reading

Throughout the journey, production systems written in C, C++, Go, Rust, and other languages are continuously studied.

C++ remains important as a production language to read and understand, but it is no longer a mandatory implementation language for the curriculum.

The objective is to understand architecture, engineering decisions, and implementation trade-offs independently of the implementation language.

---

# Module Workflow

Every module follows the same engineering process.

---

## Alignment Check

Before starting:

* What do we already know?
* What is missing?
* Why are we studying this now?
* How does it connect to previous modules?
* What concrete outcome should exist when we finish?

---

## Five Learning Levels

Every important concept progresses through:

1. Intuition
2. Theory
3. Implementation
4. Production
5. Trade-offs

---

## Expected Artifacts

Every module must produce at least one tangible artifact.

Possible artifacts include:

* repository component;
* implementation;
* experiment;
* benchmark;
* documented code reading;
* Engineering Notebook entry.

---

## Mastery Assessment

A module is considered completed only after successfully passing the criteria defined in `docs/mastery.md`.

---

# Curriculum

---

## Repository Components

Repository components indicate the primary area affected by each module.

They are intended as guidance rather than strict boundaries.

As the repository evolves, a single module may contribute to multiple components, and individual components may be revisited, refined, or extended by later modules.

The repository is designed to evolve organically, reflecting the interconnected nature of modern software systems.

---

# Phase 0 — Orientation & Repository

## Objective

Build the mental map of the software systems ecosystem and establish the development environment.

### Modules

* 0.1 Software Systems Map
* 0.2 Thinking in Systems
* 0.3 Computational Thinking
* 0.4 Fundamental Algorithms & Data Structures
    * 0.4.1 Complexity Fundamentals
    * 0.4.2 Arrays & Memory Layout
    * 0.4.3 Linked Structures
    * 0.4.4 Stack & Queue
    * 0.4.5 Trees
    * 0.4.6 Tree Traversal
    * 0.4.7 Graphs
    * 0.4.8 Graph Traversal
    * 0.4.9 Hash Tables
    * 0.4.10 Heaps
    * 0.4.11 Searching
    * 0.4.12 Sorting

Repository components:

* notebook

---

# Phase 1 — Computer Architecture

## Objective

Understand how software executes on modern hardware.

### Modules

* 1.1 Binary Representation
* 1.2 CPU Architecture
* 1.3 Memory Hierarchy
* 1.4 Instruction Execution
* 1.5 Performance Fundamentals

Repository components:

* architecture
* experiments

---

# Phase 2 — Low-Level Programming Foundations

## Objective

Introduce the subset of C required to investigate low-level software behavior directly and to support the operating-system, concurrency, and networking phases that follow.

This phase deliberately avoids turning Systems Mastery into a language-learning curriculum. C is used because it exposes memory, data layout, compilation, resource lifetime, and operating-system interfaces with minimal abstraction overhead.

The objective is not C mastery, but sufficient low-level fluency to reason about what the machine and operating system are doing.

### Modules

* 2.1 Compilation, Linking, and Object Files
* 2.2 Pointers, Arrays, and Memory Addresses
* 2.3 Stack, Heap, and Object Lifetime
* 2.4 Structs, Data Layout, and Alignment
* 2.5 Manual Resource Management and Error Handling
* 2.6 Essential C Runtime and Systems Interfaces

Repository components:

* experiments

---

# Phase 3 — Operating System Fundamentals

## Objective

Understand how operating systems manage hardware resources and expose abstractions to applications.

### Modules

* 3.1 Processes
* 3.2 Threads
* 3.3 Virtual Memory
* 3.4 File Systems
* 3.5 System Calls

Repository components:

* operating-system

---

# Integration Checkpoint A — Single Machine

## Goal

Validate the understanding of software execution on a single computer.

### Repository

* architecture
* operating-system

### Capabilities

* understand CPU execution
* reason about memory
* understand process lifecycle
* understand threads
* understand system calls
* understand filesystem fundamentals

### Outcome

A complete mental model of software execution from hardware to user-space applications.

---

# Phase 4 — Concurrency

## Objective

Understand how modern software executes multiple tasks safely and efficiently.

### Modules

* 4.1 Synchronization
* 4.2 Mutexes
* 4.3 Condition Variables
* 4.4 Thread Pools
* 4.5 Lock-Free Fundamentals

Repository components:

* concurrency

---

# Phase 5 — Networking

## Objective

Understand how software systems communicate across machines and exchange data reliably.

### Modules

* 5.1 Network Fundamentals
* 5.2 The TCP/IP Stack
* 5.3 Sockets
* 5.4 HTTP Fundamentals
* 5.5 HTTP Servers and Clients
* 5.6 RPC and gRPC

Repository components:

* networking

---

# Phase 6 — Backend Systems

## Objective

Understand how modern backend services are structured and how requests flow through an application.

### Modules

* 6.1 Minimal HTTP Server
* 6.2 Routing
* 6.3 Middleware
* 6.4 Request Lifecycle
* 6.5 Authentication Fundamentals
* 6.6 Configuration and Dependency Injection

Repository components:

* backend

---

# Integration Checkpoint B — Network Services

## Goal

Validate the transition from standalone applications to networked software systems.

### Repository

* networking
* backend

### Capabilities

* implement a minimal HTTP server
* understand the lifecycle of an HTTP request
* expose REST APIs
* understand sockets and TCP communication
* reason about request processing
* understand the architecture of production web servers

### Outcome

A production-style HTTP service implemented entirely from first principles.

---

# Phase 7 — Data Storage

## Objective

Understand how modern software systems store, retrieve, and organize data efficiently.

### Modules

* 7.1 Storage Fundamentals
* 7.2 B-Trees and Indexes
* 7.3 Transactions
* 7.4 Query Processing
* 7.5 Caching
* 7.6 Key-Value Storage

Repository components:

* storage

---

# Phase 8 — Distributed Systems

## Objective

Understand how software systems scale beyond a single machine while remaining reliable and consistent.

### Modules

* 8.1 Distributed Systems Fundamentals
* 8.2 Remote Communication
* 8.3 Replication
* 8.4 Consistency Models
* 8.5 Consensus
* 8.6 Message Queues
* 8.7 Event-Driven Architectures

Repository components:

* distributed

---

# Integration Checkpoint C — Distributed Applications

## Goal

Validate the understanding of distributed software architecture.

### Repository

* backend
* storage
* distributed

### Capabilities

* design client-server systems
* understand distributed communication
* reason about consistency
* understand replication strategies
* implement simple messaging systems
* understand the architecture of production distributed systems

### Outcome

A minimal distributed application integrating networking, storage, and inter-service communication.

---

# Phase 9 — Observability

## Objective

Understand how production systems are monitored, measured, debugged, and analyzed.

### Modules

* 9.1 Logging Fundamentals
* 9.2 Metrics
* 9.3 Distributed Tracing
* 9.4 Profiling
* 9.5 Debugging Production Systems
* 9.6 Observability Pipelines

Repository components:

* observability
* experiments

---

# Phase 10 — Infrastructure

## Objective

Understand how modern software systems are packaged, deployed, and executed reliably across different environments.

### Modules

* 10.1 Virtualization and Containers
* 10.2 Docker Fundamentals
* 10.3 Container Networking
* 10.4 Orchestration Fundamentals
* 10.5 Kubernetes Architecture
* 10.6 Service Discovery

Repository components:

* infrastructure

---

# Integration Checkpoint D — Production Infrastructure

## Goal

Validate the transition from standalone applications to deployable production systems.

### Repository

* backend
* distributed
* observability
* infrastructure

### Capabilities

* containerize applications
* understand container networking
* deploy services
* observe system behavior
* debug distributed applications
* understand production deployment architectures

### Outcome

A production-ready service that can be deployed, monitored, and analyzed.

---

# Phase 11 — Reliability Engineering

## Objective

Understand how production systems remain available, scalable, resilient, and maintainable under real-world conditions.

### Modules

* 11.1 Reliability Fundamentals
* 11.2 Fault Tolerance
* 11.3 Load Balancing
* 11.4 Rate Limiting
* 11.5 Circuit Breakers
* 11.6 Retries and Backoff
* 11.7 Graceful Shutdown

Repository components:

* infrastructure
* observability

---

# Phase 12 — Security

## Objective

Understand how modern software systems protect data, services, and infrastructure.

### Modules

* 12.1 Authentication
* 12.2 Authorization
* 12.3 Cryptography Fundamentals
* 12.4 TLS
* 12.5 Secrets Management
* 12.6 Common Vulnerabilities
* 12.7 Secure Software Engineering

Repository components:

* security

---

# Integration Checkpoint E — Production Systems

## Goal

Validate that the software stack is secure, observable, reliable, and production-ready.

### Repository

* observability
* infrastructure
* security

### Capabilities

* reason about system reliability
* understand production observability
* secure software services
* identify common failure modes
* understand production operational practices
* evaluate engineering trade-offs in real systems

### Outcome

A complete production-oriented software system built upon strong engineering foundations.

---

# Phase 13 — Systems Engineering Capstone

## Objective

Integrate all previously developed components into a coherent, production-quality software system.

Rather than introducing new concepts, this phase focuses on integration, refinement, validation, documentation, and engineering maturity.

### Goals

* integrate every repository component into a coherent architecture;
* improve software quality and maintainability;
* validate the complete system through benchmarks and experiments;
* analyze runtime behavior through observability;
* evaluate performance bottlenecks;
* assess reliability and security;
* document architecture, design decisions, and trade-offs;
* demonstrate a complete understanding of the interactions between all major software system components.

---

### Capstone Deliverables

The final software systems stack should include, at an appropriate level of complexity:

* networking layer
* backend service
* storage engine
* concurrency primitives
* distributed communication
* observability pipeline
* deployment infrastructure
* security mechanisms
* benchmarks and experiments
* engineering documentation

Repository components:

* architecture
* operating-system
* concurrency
* networking
* backend
* storage
* distributed
* observability
* infrastructure
* security
* benchmarks
* experiments
* notebook

The Capstone serves as the final integration milestone of Systems Mastery, demonstrating not only the ability to build individual components, but also the engineering judgment required to design, integrate, operate, observe, and evolve modern software systems.

The Capstone is not a new learning phase, but the integration and validation of everything built throughout Systems Mastery.

---

# Roadmap Status

| Phase     | Status         | Started     | Completed | Last Updated |
|-----------|----------------|-------------|-----------|--------------|
| Phase 0   | 🟡 In Progress | 2026-07-07 |           |              |
| Phase 1   | ⚪ Not Started |            |           |              |
| Phase 2   | ⚪ Not Started |            |           |              |
| Phase 3   | ⚪ Not Started |            |           |              |
| Phase 4   | ⚪ Not Started |            |           |              |
| Phase 5   | ⚪ Not Started |            |           |              |
| Phase 6   | ⚪ Not Started |            |           |              |
| Phase 7   | ⚪ Not Started |            |           |              |
| Phase 8   | ⚪ Not Started |            |           |              |
| Phase 9   | ⚪ Not Started |            |           |              |
| Phase 10  | ⚪ Not Started |            |           |              |
| Phase 11  | ⚪ Not Started |            |           |              |
| Phase 12  | ⚪ Not Started |            |           |              |
| Phase 13  | ⚪ Not Started |            |           |              |

---

| Module                         | Status        | Started   | Completed  |
|--------------------------------|---------------|-----------|------------|
| 0.1 Software Systems Map       | ✅ Completed | 2026-07-07 | 2026-07-07 |
| 0.2 Thinking in Systems        | ✅ Completed | 2026-07-07 | 2026-07-07 |
| 0.3 Computational Thinking     | ✅ Completed | 2026-07-07 | 2026-07-07 |
| 0.4.1 Complexity Fundamentals  | ✅ Completed | 2026-07-10 | 2026-07-11 |
| 0.4.2 Arrays & Memory Layout   | ✅ Completed | 2026-07-12 | 2026-07-12 |
| 0.4.3 Linked Structures        | ✅ Completed | 2026-07-12 | 2026-07-15 |
| 0.4.4 Stack & Queue            | ✅ Completed | 2026-07-21 | 2026-07-23 |
| 0.4.5 Trees                    | ✅ Completed | 2026-07-23 | 2026-07-25 |
| 0.4.6 Tree Traversal           | ✅ Completed | 2026-07-25 | 2026-07-27 |
| 0.4.7 Graphs                   | ✅ Completed | 2026-07-27 | 2026-07-31 |
| 0.4.8 Graph Traversal          | ✅ Completed | 2026-07-31 | 2026-08-01 |
| 0.4.9 Hash Tables              | ✅ Completed | 2026-08-04 | 2026-08-06 |
| 0.4.10 Heaps                   | ✅ Completed | 2026-08-07 | 2026-08-09 |
| 0.4.11 Searching               | ✅ Completed | 2026-09-24 | 2026-09-24 |

---

# Reference Projects

Throughout the journey, production-grade open-source projects are continuously studied.

They serve as engineering references rather than implementation targets.

Different phases naturally emphasize different systems.

| Area | Example Projects |
|------|------------------|
| Computer Architecture | LLVM |
| Operating Systems | Linux |
| Concurrency | Folly, Abseil |
| Networking | nginx, Envoy |
| Backend | Caddy, Drogon |
| Storage | SQLite, PostgreSQL, Redis |
| Distributed Systems | etcd, NATS |
| Observability | OpenTelemetry, Prometheus |
| Infrastructure | Docker, Kubernetes |
| Security | OpenSSL |

The objective is not to understand every line of these projects.

The objective is to progressively become comfortable reading industrial-scale software and recognizing familiar engineering concepts.

---

# Living Roadmap

The roadmap represents the best known learning strategy at a given point in time.

It is intentionally stable but not immutable.

Changes are expected to be rare and must always produce clear long-term benefits.

The roadmap exists to maximize learning—not to constrain it.

---

# Roadmap Governance

**Version:** V1.1

**Status:** Approved

**Approval Date:** 2026-09-21


## V1.1 Approved Modification — Language Strategy

### Observation

Using C++ as the mandatory implementation language for most later phases adds a substantial language-learning burden that is not required to achieve the curriculum's primary systems-engineering objectives. The learner already has some C familiarity, while many core mechanisms in operating systems, concurrency, and networking can be exposed more directly through C.

### Proposal

* Replace the dedicated **C++ for Systems** phase with **Low-Level Programming Foundations** based on C.
* Use C where low-level mechanisms are the subject of study.
* Introduce Go selectively for higher-level backend, distributed-system, observability, and infrastructure implementations when doing so reduces incidental complexity.
* Retain C++ as an important production language for code reading rather than as a mandatory implementation language.

### Motivation

The change preserves low-level depth while reducing incidental language complexity. It keeps implementation choices subordinate to the actual learning objective: understanding systems, architecture, runtime behavior, and engineering trade-offs.

### Impact

* Phase 2 is renamed and redesigned around C.
* The repository component `cpp-for-systems/` becomes `low-level-programming/`.
* Later modules may choose C, Python, or Go according to the mechanism being studied.
* No systems topic or integration checkpoint is removed.
* Existing completed Phase 0 work is unaffected.

Future modifications are permitted only when justified by one of the following:

* a missing prerequisite discovered during the journey;
* limitations revealed by implementations, experiments, or benchmarks;
* significant changes in software engineering practices;
* demonstrable improvements to the curriculum organization.

Every approved modification must include:

1. Observation
2. Proposal
3. Motivation
4. Impact

Unless one of these conditions is satisfied, this roadmap should be considered frozen.

The objective is no longer to design Systems Mastery.

The objective is to complete it.