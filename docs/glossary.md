## Software System

**Definition**

A collection of cooperating components that together achieve a common goal.

**Purpose**

Provides the fundamental abstraction used throughout Systems Mastery for reasoning about software beyond individual programs.

**Systems Context**

Every major topic in Systems Mastery explores one aspect of how software systems are built, interact and evolve.

**Related Concepts**

* Component
* Responsibility
* Interface
* Dependency

**Introduced In**

Module 0.1 — Software Systems Map

---

## Component

**Definition**

A distinct part of a software system responsible for performing a specific function.

**Purpose**

Allows complex systems to be decomposed into smaller units with well-defined responsibilities.

**Systems Context**

Components cooperate through interfaces to produce the overall behavior of a software system.

**Related Concepts**

* Software System
* Responsibility
* Interface

**Introduced In**

Module 0.1 — Software Systems Map

---

## Responsibility

**Definition**

The specific capability or problem that a component or system is expected to own.

**Purpose**

Provides a stable way to reason about systems independently of their implementation or the technologies used.

**Systems Context**

Systems Mastery emphasizes understanding software through responsibilities rather than through tools or frameworks.

**Related Concepts**

* Component
* Dependency

**Introduced In**

Module 0.1 — Software Systems Map

---

## Interface

**Definition**

The boundary through which one component communicates with another.

**Purpose**

Allows components to cooperate while remaining internally independent.

**Systems Context**

Interfaces define how systems interact without requiring knowledge of each other's internal implementation.

**Related Concepts**

* Component
* Dependency

**Introduced In**

Module 0.1 — Software Systems Map

---

## Dependency

**Definition**

A relationship in which one component or system relies on another to fulfill its responsibility.

**Purpose**

Explains how independent systems combine to produce larger system behavior.

**Systems Context**

Understanding dependencies is essential for reasoning about software ecosystems.

**Related Concepts**

* Component
* Responsibility
* Software System

**Introduced In**

Module 0.1 — Software Systems Map

---

## Software Ecosystem

**Definition**

A collection of cooperating software systems whose interactions produce capabilities that no individual system could provide alone.

**Purpose**

Introduces the central mental model of Systems Mastery.

**Systems Context**

Modern applications are better understood as ecosystems of cooperating systems than as single programs.

**Related Concepts**

* Software System
* Dependency
* Responsibility

**Introduced In**

Module 0.1 — Software Systems Map

---

## Ownership

**Definition**

The assignment of a responsibility to the component primarily accountable for fulfilling it.

**Purpose**

Provides a clear way to reason about where decisions and behaviors belong within a system.

**Systems Context**

Clear ownership reduces ambiguity and makes systems easier to understand, evolve and maintain.

**Related Concepts**

* Responsibility
* Component
* Boundary

**Introduced In**

Module 0.2 — Thinking in Systems

---

## Information Flow

**Definition**

The movement of information between cooperating components as they work together to fulfill a responsibility.

**Purpose**

Helps explain system behavior by following how information is produced, transformed and consumed rather than how code is organized.

**Systems Context**

Information flow often reveals the true structure of a system more clearly than its implementation.

**Related Concepts**

* Responsibility
* Interface
* Dependency
* Ownership

**Introduced In**

Module 0.2 — Thinking in Systems

---

## Boundary

**Definition**

The point at which one component's responsibility ends and another's begins.

**Purpose**

Separates responsibilities, limits complexity and defines how components interact.

**Systems Context**

Well-defined boundaries make systems easier to reason about by reducing unnecessary coupling between components.

**Related Concepts**

* Component
* Responsibility
* Interface
* Ownership

**Introduced In**

Module 0.2 — Thinking in Systems

---

## Assumption

**Definition**

A condition that a component expects to be true in order to fulfill its responsibility.

**Purpose**

Makes implicit expectations visible, helping engineers identify hidden risks and dependencies within a system.

**Systems Context**

Many system failures occur when assumptions about dependencies, inputs or environments no longer hold.

**Related Concepts**

* Dependency
* Responsibility
* Component

**Introduced In**

Module 0.2 — Thinking in Systems

---

## State

**Definition**

The complete information describing a system at a specific point in time.

**Purpose**

Provides the fundamental model for reasoning about computation independently of any implementation or programming language.

**Systems Context**

Software components can be understood as machines that observe state, apply transformations and produce new states. This perspective reappears throughout Systems Mastery, from algorithms to distributed systems and AI runtimes.

**Related Concepts**

* Invariant
* Responsibility
* Information Flow

**Introduced In**

Module 0.3 — Computational Thinking

---

## Invariant

**Definition**

A property that must remain true regardless of how a system's state changes.

**Purpose**

Provides a systematic way to reason about correctness by defining which states are always considered valid.

**Systems Context**

State transformations may modify a system, but they should preserve its invariants. Protecting invariants is a fundamental responsibility of software components and will remain a recurring concept throughout Systems Mastery.

**Related Concepts**

* State
* Responsibility
* Assumption

**Introduced In**

Module 0.3 — Computational Thinking