# Hub'Eau Water Quality Data Platform

## Overview

Academic project completed as part of the BUT Informatique programme. The application explores a hybrid data architecture for visualising French water-quality monitoring stations and retrieving measurement data from the public **Hub'Eau** API.

This was a team academic project. The repository is presented as evidence of work with Python, Flask, relational data and external APIs, not as an individual production product.

## Architecture

The application follows an MVC-style structure and separates two categories of data:

1. **Local reference data**
   - station metadata and geographic information stored in PostgreSQL;
   - used to avoid repeatedly downloading information that changes infrequently.

2. **Remote measurement data**
   - water-quality measurements requested from the Hub'Eau API when needed;
   - retrieved dynamically for the selected station.

## Technology Stack

```text
Python 3
Flask / Jinja2
PostgreSQL
Hub'Eau REST API
HTML / CSS / JavaScript
```

## Repository Structure

- `controller.py` - Flask routes and application orchestration
- `model/` - data-access and application logic
- `acces_postgre.py` - PostgreSQL access utilities
- `templates/` - HTML/Jinja views
- `static/` - frontend assets
- `graphiques.py` - data visualisation-related code
- `Flexible_ChatBot/` - additional chatbot/RAG experimentation kept in the original academic repository

## Skills Demonstrated

- integration of an external REST API;
- relational database access;
- separation of local and remote data sources;
- Python web development with Flask;
- MVC-style application organisation;
- collaborative academic development.

## Naming Note

The repository was originally published under the name `Maritime-Data-Analytics-Platform`, but the code in this repository corresponds primarily to the Hub'Eau water-quality project. The README uses the accurate project name to avoid misrepresenting its contents.
