# Flask vs. FastAPI: A Quick Comparison

This note outlines the core differences between Flask and FastAPI to help in choosing the right framework for a project.

## Core Philosophy

-   **Flask**: A "micro-framework" that is lightweight, flexible, and unopinionated. It provides the basics (routing, request handling) and lets you choose your own libraries for everything else (like data validation or database integration). It is built on **WSGI** (Web Server Gateway Interface), which is synchronous by nature.
-   **FastAPI**: A modern, high-performance framework designed specifically for building APIs. It is more opinionated and comes with "batteries included" for key features like data validation and API documentation. It is built on **ASGI** (Asynchronous Server Gateway Interface), enabling it to handle requests asynchronously.

## Key Differences

| Feature               | Flask                                        | FastAPI                                                               |
| --------------------- | -------------------------------------------- | --------------------------------------------------------------------- |
| **Asynchronicity** | Synchronous by default (WSGI).               | Asynchronous by default (ASGI). Much better for high-concurrency I/O. |
| **Data Validation** | Not built-in. Requires extensions like WTForms. | **Built-in** using Pydantic models and Python type hints.             |
| **API Documentation** | Not built-in. Requires extensions like Flasgger. | **Automatic & Interactive** (Swagger UI and ReDoc) out of the box.    |
| **Performance** | Good for many use cases.                     | **Extremely high**. One of the fastest Python frameworks available.      |
| **Dependencies** | Minimal (Werkzeug for WSGI, Jinja2 for templates). | Modern (Starlette for web, Pydantic for data).                        |

## When to Use Which?

-   **Use Flask when:**
    -   You are building a traditional, server-rendered web application (e.g., a blog, a company website with forms).
    -   You need maximum flexibility and want to choose every component of your stack.
    -   The project is small and high-performance API speed is not the primary concern.

-   **Use FastAPI when:**
    -   You are building a dedicated API (e.g., a backend for a mobile or JavaScript app).
    -   Performance and concurrency are critical.
    -   You want automatic data validation, type safety, and API documentation to speed up development.