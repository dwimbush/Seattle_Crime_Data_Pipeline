
# Seattle Crime Data Pipeline: From Raw Data to Insights (2008 - 2024)
![Seattle Crime Image](images/seattle_crime_image.png)

## Table of Contents
- [Seattle Crime Data Pipeline: From Raw Data to Insights (2008 - 2024)](#seattle-crime-data-pipeline-from-raw-data-to-insights-2008---2024)
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
  - [Resource Clean Up](#resource-clean-up)
  - [Future Enhancements](#future-enhancements)

## Project Description
In this project, we aim to build a robust data pipeline that takes Seattle crime data from the years 2008 to 2024, processes it, and makes it available for analysis and visualization. The project encapsulates best practices in data engineering, including the use of containerization, infrastructure as code, and workflow orchestration.

### Questions Addressed:
- What are the common trends in crime incidents over the years?
- How do crime rates vary by location and time?
- What can we predict about future crime rates based on historical data?

## Dataset
The dataset contains detailed records of crime data from the Seattle Police Department, spanning from 2008 to the present. It offers a granular view of crime incidents, covering a variety of offenses, locations, and times.

Key attributes of the dataset include:
- `report_number`: A unique identifier for the crime report.
- `offense_id`: A distinctive code for each offense.
- `offense_start_datetime` and `offense_end_datetime`: Indicating when the crime was believed to have occurred.
- `report_datetime`: When the crime was reported to law enforcement.
- `group_a_b`: Classifying the offense as part of Group A or B crimes.
- `crime_against_category`: Denoting whether the crime was against an individual, property, or society.
- `offense_parent_group`: A broader category for the type of offense.
- `offense`: Description of the offense.
- `offense_code`: A code that classifies the offense.
- Geographic identifiers like `precinct`, `sector`, `beat`, and `mcpp` provide precise locations for where the incidents took place.
- `longitude` and `latitude`: Geolocational data for mapping the incident.

This dataset is utilized for the analytics pipeline in this project to uncover insights and hopefully inform decision-making related to crime. The dataset also facilitates transparency and community engagement by making the information accessible and actionable.

For more detailed information and to explore the dataset further, please visit the official [Seattle Police Department Crime Data](https://data.seattle.gov/Public-Safety/SPD-Crime-Data-2008-Present/tazs-3rd5/about_data) page.


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
1. Data ingestion from source to local database (for exploratory analysis) and cloud data lake.
2. Data cleaning and transformation.
3. Data loading into the data warehouse.
4. Data analysis and visualization.
5. IaC for cloud resource management

Each stage is designed to be modular and reusable, facilitating easy maintenance and scalability of the pipeline.

<img src="images/Seattle_Crime_Pipeline.png" width="800" height="auto" alt="Pipeline Flow">


## Project Reproducibility
To ensure the project can be reproduced:
- All code is stored in a version-controlled git repository.
- Detailed setup and installation instructions are provided.
- Environment variables and configurations are managed through `io_config.yaml`.

### Prerequisites:
- Docker installed for local setup.
- Google Cloud account for remote setup.
- Git for repository cloning

### Steps:
1. Clone the repository.
2. Set up environment variables.
3. Run the Docker containers.
4. ... (additional steps)

## Resource Clean Up
Instructions for cleaning up resources to avoid incurring unnecessary cloud costs are provided in the documentation. This includes steps for tearing down infrastructure provisioned by Terraform and removing data from GCS and BigQuery.

## Future Enhancements
- Implement additional data sources to make correlations for broader insights.
- Fully host pipeline in the cloud.
- Improve the dashboard with more interactive features.



