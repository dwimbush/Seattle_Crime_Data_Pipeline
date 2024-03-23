
# Seattle Crime [2008 - 2024] Data Pipeline
![Seattle Crime Image](images/seattle_crime_image.png)

## Table of Contents
- [Seattle Crime \[2008 - 2024\] Data Pipeline](#seattle-crime-2008---2024-data-pipeline)
  - [Table of Contents](#table-of-contents)
  - [Project Description](#project-description)
    - [Questions Addressed:](#questions-addressed)
  - [Dataset](#dataset)
  - [Findings and Dashboard](#findings-and-dashboard)
  - [Technology and Tools](#technology-and-tools)
  - [Pipeline Overview](#pipeline-overview)
  - [Project Reproducibility](#project-reproducibility)
    - [Prerequisites:](#prerequisites)
    - [Steps:](#steps)
  - [Clean Up](#clean-up)
  - [Enhancements and Future Work](#enhancements-and-future-work)
  - [Contact](#contact)

## Project Description
In this project, we aim to build a robust data pipeline that takes Seattle crime data from the years 2008 to 2024, processes it, and makes it available for analysis and visualization. The project encapsulates best practices in data engineering, including the use of containerization, infrastructure as code, and workflow orchestration.

### Questions Addressed:
- What are the common trends in crime incidents over the years?
- How do crime rates vary by location and time?
- What can we predict about future crime rates based on historical data?

## Dataset
The dataset consists of Seattle crime data, capturing various aspects such as the offense type, location, and time. The data includes the following fields:
- `report_number`
- `offense_id`
- `offense_start_datetime`
- `offense_end_datetime`
- `report_datetime`
- ... (and so on)

Each record in the dataset provides detailed information about individual crime incidents, which allows for a granular analysis of crime patterns and trends.

## Findings and Dashboard
The insights derived from the data are visualized in a dashboard that provides an interactive interface for stakeholders to explore the crime data. The dashboard highlights key metrics and allows users to filter data based on different criteria such as date range, crime type, and geographic area.

## Technology and Tools
This project utilized the following:
- **Containerization:** [Docker](https://www.docker.com/)
- **Infrastructure as code (IaC):** [Terraform](https://www.terraform.io/)
- **Workflow orchestration:** [Mage](https://www.mage.ai/)
- **Data Lake:** [Google Cloud Storage (GCS)](https://cloud.google.com/storage/)
- **Data Warehouse:** [BigQuery](https://cloud.google.com/bigquery)
- **Data Transformation:** [dbt](https://www.getdbt.com/)
- **DataVisualization:** [Looker Studio](https://cloud.google.com/looker-studio?hl=en)
- **Dev Database:** [PostgreSQL](https://www.postgresql.org/)
- **Version Control:** [git](https://git-scm.com/)
- **Programming Language:** [Python](https://www.python.org/), [SQL](https://en.wikipedia.org/wiki/SQL)

## Pipeline Overview
The pipeline consists of several stages:
1. Data ingestion from source to the data lake.
2. Data cleaning and transformation.
3. Data loading into the data warehouse.
4. Data analysis and visualization.

Each stage is designed to be modular and reusable, facilitating easy maintenance and scalability of the pipeline.

## Project Reproducibility
To ensure the project can be reproduced:
- All code is stored in a version-controlled git repository.
- Detailed setup and installation instructions are provided.
- Environment variables and configurations are managed through `io_config.yaml`.

### Prerequisites:
- Docker installed for local setup.
- Google Cloud account for remote setup.

### Steps:
1. Clone the repository.
2. Set up environment variables.
3. Run the Docker containers.
4. ... (additional steps)

## Clean Up
Instructions for cleaning up resources to avoid incurring unnecessary cloud costs are provided in the documentation. This includes steps for tearing down infrastructure provisioned by Terraform and removing data from GCS and BigQuery.

## Enhancements and Future Work
- Implement additional data sources.
- Integrate advanced machine learning models for predictive analysis.
- Improve the dashboard with more interactive features.

## Contact
For any queries regarding the project, reach out to [example@email.com](mailto:example@email.com).
"""


