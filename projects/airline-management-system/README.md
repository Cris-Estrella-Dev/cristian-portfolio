# Airline Management System

## Project Overview

The **Airline Management System** is a software engineering project designed to simulate the core operations of a modern airline.

The goal of this project is not only to build a functional application, but also to demonstrate professional software engineering practices such as object-oriented programming, software architecture, clean code, documentation, version control, and scalable system design.

This project is being developed incrementally, following the same mindset used in professional software development: understanding the business domain first, designing the architecture, and then implementing the solution.

---

## Why this project?

Airline systems involve many real-world business concepts such as customers, flights, reservations, employees, airports, and baggage.

Because of this complexity, they provide an excellent opportunity to practice object-oriented design, domain modeling, and software architecture while building a realistic application.

As the project evolves, additional technologies such as databases, REST APIs, Docker, and AWS will be incorporated.

---

## Goals

* Apply Object-Oriented Programming (OOP)
* Design software before implementation
* Practice UML and domain modeling
* Build a scalable and maintainable codebase
* Learn software architecture principles
* Practice Git and GitHub workflows
* Build a professional portfolio project

---

## Planned Features

* Employee Management
* Customer Management
* Flight Management
* Airport Management
* Booking System
* Reservation System
* Baggage Tracking
* Flight Crew Assignment
* Flight Staff Assignment
* Data Persistence
* Search Functionality

---

## Project Structure

```text
airline-management-system/

├── docs/
│   ├── architecture/
│   └── screenshots/
│
├── src/
│
├── tests/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Architecture

The project architecture is designed before implementation using UML diagrams.

The current domain model includes:

* Employee hierarchy
* Customer
* Booking
* Reservation
* Flight
* Airport
* Baggage
* Flight Crew Assignment
* Flight Staff Assignment

Architecture diagrams are located inside:

```text
docs/architecture/
```

---

## Technologies

Current technologies:

* Python 3
* Git
* GitHub
* draw.io
* JSON

Future technologies:

* SQLite
* PostgreSQL
* FastAPI
* Docker
* AWS
* CI/CD

---

## Development Roadmap

### Phase 1 — Domain Modeling

* UML Design
* Employee hierarchy
* Customer
* Booking
* Reservation
* Flight
* Airport

### Phase 2 — Core Functionality

* CRUD Operations
* Search
* Validation

### Phase 3 — Persistence

* JSON
* SQLite

### Phase 4 — Backend

* REST API
* FastAPI

### Phase 5 — Deployment

* Docker
* AWS

---

## Current Status

Project currently under active development.

The project is following an architecture-first approach, where the domain is modeled before implementation.

---

## Author

**Cristian Estrella**

Software Engineering Student

This repository is part of my software engineering portfolio and documents my learning journey while building production-style software projects.



## Engineering Journal

This project is being developed incrementally.

Instead of writing code immediately, every major feature follows this workflow:

1. Understand the business problem.
2. Design the solution using UML.
3. Review class responsibilities.
4. Implement the feature.
5. Refactor if necessary.
6. Document architectural decisions.
7. Commit changes to Git.

This journal reflects the engineering mindset used throughout the project.


## Current Progress

The first functional version of the Airline Management System has been implemented.

The project now includes a complete object-oriented flow connecting the main business entities of an airline system:

- Airports
- Flights
- Customers
- Bookings
- Reservations
- Baggage
- Employees
- Flight crew assignments
- Flight staff assignments
- Booking service logic

The system currently supports creating a customer booking through a service layer, adding a reservation to that booking, assigning baggage to the reservation, assigning pilots and flight attendants to a flight crew, and assigning operations and ramp agents to flight staff.

This version demonstrates the core object-oriented relationships designed in the UML class diagram, including object references, lists of related objects, inheritance, abstraction, and service-layer coordination.

Next steps include improving validation, adding JSON persistence, writing tests, and preparing the system for future API and database integration.