# My-Zootopia with API

A small Python application that fetches animal data from the API Ninjas “Animals” endpoint and generates a static HTML page.
The project demonstrates clean separation of concerns, environment-based configuration, API consumption, and simple static site generation.

---

## Description

This project is structured into two independent components:

1. **Data Fetcher** — implemented in [`data_fetcher.py`](data_fetcher.py).
   Responsible for retrieving animal information from the API Ninjas Animals API.
   It uses:
   - the `requests` HTTP client
   - environment-based secret loading via `python-dotenv`
   - JSON parsing with Python’s built-in [`json`](https://docs.python.org/3/library/json.html)

2. **Website Generator** — implemented in [`animal_web_generator.py`](animal_web_generator.py).
   This module:
   - receives normalized data from the fetcher
   - fills values into an HTML template using simple string replacement
   - writes the resulting static page into `animals.html`

These two layers are fully decoupled: any data provider returning the correct schema can replace the current API implementation without modifying the generator.

---

## Interesting Techniques Used

### **Environment-based secret loading (`.env`)**
Secrets are not hardcoded.
`python-dotenv` loads the API key from a `.env` file at runtime:

- https://pypi.org/project/python-dotenv/

Every user must create **their own `.env`** containing:
