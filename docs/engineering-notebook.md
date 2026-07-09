## Software Systems Are Ecosystems, Not Programs

**Context**

Module 0.1 — Software Systems Map

---

### Observation

Modern software is rarely a single program.

Instead, it is an ecosystem of cooperating systems, each responsible for solving a distinct engineering problem.

Applications emerge from the interaction of these systems rather than from any individual component.

---

### Reasoning

Studying technologies in isolation creates fragmented knowledge.

Understanding the responsibilities, interfaces and dependencies between systems provides a stable mental model that remains useful even as individual technologies evolve.

This shifts the focus from learning tools to understanding why those tools exist.

---

### Implications

When encountering a new technology, the first questions should not be:

- How does it work?
- Which API does it expose?

Instead, begin by asking:

- Which engineering problem does it solve?
- Which responsibility does it own?
- How does it integrate with the surrounding ecosystem?
- Which systems does it depend on?

This perspective will guide every future module of Systems Mastery.

---

### Related Concepts

* Software System
* Component
* Responsibility
* Interface
* Dependency

--------------------------------------------------------------------------------------------

## Understanding a System Means Understanding Relationships

**Context**

Module 0.2 — Thinking in Systems

---

### Observation

A software system is understood by the relationships between its components, not by reading their implementations in isolation.

Responsibilities, ownership, information flow, boundaries and dependencies collectively define the behavior of the system.

---

### Reasoning

Individual components rarely provide enough context to explain why they exist.

Their purpose emerges from how they cooperate with other components, what information they exchange, which responsibilities they own and which assumptions they make about the rest of the system.

Following these relationships often reveals the structure of a system more effectively than reading source code.

---

### Implications

When approaching an unfamiliar system, resist starting from the implementation.

Instead, first identify:

* the responsibilities that exist;
* who owns each responsibility;
* how information flows through the system;
* where boundaries exist;
* which dependencies and assumptions connect the components.

Only then examine the implementation details.

---

### Related Concepts

* Responsibility
* Ownership
* Information Flow
* Boundary
* Dependency
* Assumption

--------------------------------------------------------------------------------------------
