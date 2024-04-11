
# Seattle Crime Data Pipeline: From Raw Data to Insights (2008 - present)
![Seattle Crime Image](images/seattle_crime_image.png)

## Table of Contents
  - [Project Description](#project-description)
    - [Questions Addressed:](#questions-addressed)
  - [Dataset](#dataset)
  - [Findings and Dashboard](#findings-and-dashboard)
    - [Seattle Crime Data Analysis](#seattle-crime-data-analysis)
    - [A Focus on Seattle Crime Data Over Last 7 Days From Latest Run](#a-focus-on-seattle-crime-data-over-last-7-days-from-latest-run)
    - [Some Recommendations](#some-recommendations)
  - [Technology and Tools](#technology-and-tools)
  - [Pipeline Overview](#pipeline-overview)
  - [Project Reproducibility](#project-reproducibility)
    - [Prerequisites:](#prerequisites)
    - [Step 1: Clone the repository](#step-1-clone-the-repository)
    - [Step 2: Setup of GCP Project](#step-2-setup-of-gcp-project)
    - [Step 3: Terraform Setup for Resource Management](#step-3-terraform-setup-for-resource-management)
    - [Step 4: Mage Setup for Extract/Load](#step-4-mage-setup-for-extractload)
    - [Step 5: dbt Setup for Transformations](#step-5-dbt-setup-for-transformations)
    - [Step 6: Setup Visualizations using Looker Studio](#step-6-setup-visualizations-using-looker-studio)
  - [Resource Clean Up](#resource-clean-up)
  - [Future Enhancements](#future-enhancements)
  - [Special Thanks](#special-thanks)

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
The insights derived from the data are visualized in a dashboard that provides an interactive interface for stakeholders to explore the crime data. The dashboard highlights key metrics and allows users to filter data based on different criteria such as year, crime type, and Seattle precinct.

![Seattle Crime Dashboard 1](images/seattle_crime_dashboard.png)

### Seattle Crime Data Analysis

This analysis leverages data from over 1 million reported crimes in Seattle, yielding the following insights:

- **Theft Incidents**: Theft from motor vehicles is the most reported offense, tallying 176,053 incidents, suggesting a significant issue with vehicle-related property crimes.
- **Property Crime**: A staggering 74.7% of crimes fall under property-related offenses, with "All Other Larceny" and "Burglary/Breaking & Entering" accounting for 93,774 and 126,027 incidents, respectively.
- **Assault Reports**: Notably, simple and aggravated assaults together account for over 122,000 reports, indicating prevalent violent crime.
- **Precinct Disparities**: The North precinct reports the highest crime numbers at 358,051 incidents, followed closely by the West (Downtown) precinct with 297,941 incidents.
- **Hourly Crime Peaks**: Afternoon hours, particularly around 1 PM and 2 PM, show the highest crime activity, suggesting a need for increased vigilance during these times.
- **Day of the Week Variation**: Crime reports are fairly consistent across the week, with a slight uptick during weekends, emphasizing the need for constant readiness.
- **Crime Category Distribution**: In the Crime Category Distribution, the "NOT_A_CRIME" label may raise questions. This category typically includes incidents that are initially reported as crimes but are later found to fall outside the scope of criminal activity, such as justifiable homicides, police actions deemed lawful, or cases that are reclassified upon further investigation.

### A Focus on Seattle Crime Data Over Last 7 Days From Latest Run
![Seattle Crime Dashboard 2](images/crimes_last_7_days.png)
The bar chart offers a breakdown of criminal activities in Seattle by precinct over the last week. Notably, the North and West (Downtown) precincts exhibit the highest diversity and volume of crimes. In these areas, `Burglary/Breaking & Entering`, `Motor Vehicle Theft`, and `Theft From Motor Vehicle` are the most common offenses, suggesting a particular vulnerability to property-related crimes. Across all precincts, these three crime types consistently appear as the top concerns, underscoring the need for enhanced vehicle and property security measures in Seattle. The prevalence of `Aggravated Assault` and `Simple Assault` in the North precinct may also indicate a hotspot for violent crime, warranting focused policing and community intervention efforts. Conversely, the `UNKNOWN` category suggests data recording discrepancies or incidents with unestablished locations, which highlights an area for administrative improvement. 

### Some Recommendations

- Enhance vehicle security protocols due to high theft from motor vehicles.
- Given the significant portion of crime represented by theft and burglary, it's likely that future efforts in crime prevention will need to continue focusing on these areas.
- Bolster property crime prevention strategies to tackle the dominant crime category.
- Implement targeted patrols during peak hours to mitigate afternoon crime spikes.
- Allocate resources efficiently across precincts, with a focus on North and West precincts.
- Maintain steady law enforcement coverage throughout the week, considering the marginal increase on weekends.

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

The source data for this project was found to be fairly high quality with minimal issues. For this project, utilizing the dataset required only minimal transformations. These transformations were efficiently carried out using Mage.ai during the initial extract and load stages of our workflow. Subsequent adjustments were made during the DBT (Data Build Tool) phase to ensure the data was suited for analysis needs.

In the development and optimization of the data storage strategy for this project, a key decision was made to partition the dataset by year. This strategic choice, implemented in the data export process, was driven by reasons rooted in efficiency, performance, and the specific characteristics of this dataset, which encompasses over 1.1 million rows of crime data spanning from 2008 to the present.

The decision to partition the Seattle Crime dataset by year was made for optimizing data storage costs, simplifying data management, and ensuring high-performance data access for analysis and reporting. The partitioning strategy is a testament to implementing best practices in data engineering to support the efficient, scalable handling of large-scale datasets.

**click image to view full-size**

<img src="images/seattle_crime_pipeline.png" width="800" height="auto" alt="Pipeline Flow">


## Project Reproducibility

### Prerequisites:
- [Docker installed](https://docs.docker.com/get-docker/)
- [Google Cloud Platform (GCP)](https://cloud.google.com/) account for remote setup
- [Git installed](https://git-scm.com/) for repository cloning 
- [Terraform is installed](https://learn.hashicorp.com/tutorials/terraform/install-cli) to create GCP resources
- [dbt cloud](https://www.getdbt.com/) account
-  [Google SDK installed](https://cloud.google.com/sdk/docs/install-sdk) to interact with GCP from your prompt

**Note:** this setup was only tested in a Windows environment but should work in other environments with minimal modifications, if any at all

### Step 1: Clone the repository

   ```bash
    git clone https://github.com/dwimbush/Seattle_Crime_Data_Pipeline.git
  ```

### Step 2: Setup of GCP Project
- Creation of new GCP project and note its ID. 
- Activated the following API's within your GCP project:
   * https://console.cloud.google.com/apis/library/iam.googleapis.com
   * https://console.cloud.google.com/apis/library/iamcredentials.googleapis.com

- Create a [service account](https://console.cloud.google.com/iam-admin/serviceaccounts) and grant appropriate roles and permissions:
  * BigQuery Admin
  * Storage Admin
  * Storage Object Admin 
- Download the JSON authentication key and rename to a more appropriate name if preferred.  For example: `seattle-crime-service-account-key.json` 
- Move this key to the `key` folder within the project's `Terraform` directory - **IMPORTANT: Do not share this key with anyone!**
- Set and export the GOOGLE_APPLICATION_CREDENTIALS using the following command from your prompt:
  ```bash
  export GOOGLE_APPLICATION_CREDENTIALS="<path/to/authkeys>.json"
  ```
- Make sure you have [Google SDK](https://cloud.google.com/sdk/docs/install-sdk) installed in order to authenticate against GCP
- You will now be able to authenticate with GCP by running the following commands from your prompt: 
  ```
  gcloud auth activate-service-account --key-file="$GOOGLE_APPLICATION_CREDENTIALS"
  ```
  ```bash
  gcloud auth application-default login
  ```
- To ensure these settings persist across sessions, add the `export` command to your `.bashrc` or equivalent shell configuration file.

### Step 3: Terraform Setup for Resource Management
- Alter the variables values in the `variables.tf` file located within the project's Terraform directory to match up with your specific project values: 
   * credentials
   * project name
   * location
   * region
   * bq_dataset_name
   * gcs_bucket_name
   * gcs_storage_class 
- Run the following Terraform commands within the project's Terraform directory from your command line:
  ```bash
    # Terraform initialization process
    terraform init
  ```
  ```bash
    # View what's planned to change
    terraform plan
  ```
  ```bash
    # Apply those new changes
    terraform apply
  ```
**Note:** Ensure your variables.tf file accurately reflects your project's specifics to avoid any resource misconfigurations.

### Step 4: Mage Setup for Extract/Load 
* Create a GCP service account for mage in the same why you created service accounts before and give it the permisson of an `owner` 
* Create and download a json key for this service account
* Rename the json file to "key.json" and move to the `mage` folder located within the project directory.
* Make sure you are in the `mage` and rename the `dev.env` file to `.env`. This file will contain environment variables that Mage uses, including your dbt API token if you intend to integrate Mage with dbt for automated transformations. 

* **Configure dbt Integration (Optional):**

  * If you want Mage to automatically trigger dbt transformations, you'll need to add your dbt API token to the .env file. 
  
    **Note:** You may need to carry out the following steps after you've setup dbt cloud in the instructions further below.
  * Find the line corresponding to the dbt API token and replace the placeholder with your actual token.
  * Alternatively, if you prefer not to use Mage for triggering dbt, you can set up dbt Cloud to trigger transformations on a schedule. This approach requires configuring the dbt Cloud project separately.
  
    **NOTE:** The use of the dbt API is not available on the free tier of dbt. To utilize this feature, you'll need to upgrade to the paid Team version of dbt.

 **Start Mage and Supporting Services:**
* Ensure you are in the `mage` folder where the `docker-compose.yml` file is located.
* Execute the following command to build the Docker images specified in a docker-compose.yml file:
  ```bash
  docker compose build
  ``` 
* Excute the following command to pull the latest maga.ai docker image:
  ```bash
  docker pull mageai/mageai:latest
  ```
* Execute the following command to start the `mage` application along with a PostgreSQL database container:
  ```bash
  docker compose up
  ```
  This command initializes and starts the necessary Docker containers for Mage and a PostgreSQL database, setting up the environment for your data pipelines.

* Open a web browser and navigate to http://localhost:6789 to access the Mage UI.
* Within the Mage UI, review the code in various blocks in the pipeline to update with your CGP project ID, GCP bucket name, etc
* Navigate to the pipelines section to initiate and monitor the execution of the data pipelines.
  
  **NOTE:** The last block in the second pipeline is a custom block to trigger dbt.  You might want to comment out the code in this block until you have dbt cloud setup.  Specifcally, you will need the Team version to utilize the dbt API capability otherwise you can trigger the dbt cloud project on a schedule that should run after the schedule set for the mage pipelines.

### Step 5: dbt Setup for Transformations

* Create a new dbt Project in dbt Cloud: Sync the repository of this project to the dbt folder. Ensure you're selecting the correct repository location and syncing it under the project subfolder `/dbt`.
* Select the BigQuery connection in dbt Cloud.
Create a new service account in GCP specifically for dbt. This is important for isolating permissions and managing access securely.
* Download the JSON key for the new service account and set up the authentication in dbt Cloud by providing the necessary credentials.
* Edit the `dbt_project.yml` to update the `name` a to match your project's naming convention.
* Update the `models` section as needed to reflect the structure and dependencies of the dbt models.  This is for the Team version of dbt only
* Setup a `dbt api token` to trigger dbt via API from mage
* Run the following command in the terminal dbt cloud to execute the transformations:
  
	```
	dbt build
	``` 
 ### Step 6: Setup Visualizations using Looker Studio

 * Go to [Looker Studio](https://datastudio.google.com/) and sign in with your Google account.
 * Click on the `+ Create` button and select `Report` from the dropdown. Looker Studio will prompt you to choose a data source for the new report.
 * In the `Create a new data source` panel, select `BigQuery` from the list of connectors.
 * Navigate through the project and dataset to find the BigQuery tables you have prepared for this project.
 * Once you've found the correct table, select it and then click on the `Connect` button in the upper right corner.
 * After connecting your BigQuery table, Looker Studio will load the fields from your dataset on the right-hand side.
 * Use the various visualization tools (charts, tables, graphs, etc.) provided by Looker Studio to create your dashboard. Drag and drop fields to the appropriate axes to create visualizations.
 * Customize your visualizations with filters, styles, and controls according to the insights you wish to highlight.
  
    **Note:** Remember to review the access permissions of the BigQuery tables to ensure that your Google account has the necessary permissions to connect them with Looker Studio

 ## Resource Clean Up
Here are instructions for cleaning up Terraform resources to avoid incurring unnecessary cloud costs. You will want to tear down infrastructure provisioned by Terraform and immediately remove data from GCS and BigQuery.

When it's time to clean up resources on Google Cloud Platform (GCP) and prevent additional charges, Terraform provides a straightforward method for resource destruction. The `terraform destroy` command is designed to remove infrastructure managed by Terraform. It's always good practice to double-check which resources are slated for removal before confirming the action to avoid unintended data loss or service interruption. 

Here's how you use it - before running the destroy command, ensure that you are in the correct Terraform working directory and that your Terraform state reflects the current infrastructure you intend to delete. Additionally, review the plan output carefully before confirming the destruction of resources. Finally type the following command at your prompt:

```sh
terraform destroy
```

## Future Enhancements
- Implement additional data sources to make correlations for broader insights.
- Fully host pipeline in the cloud. The mage docker container is the only remaining piece.
- Improve the dashboard with more interactive features and improve the visualizations.
- General respository clean up of unecessary files
- Make the Project Reproducibility section more user-friendly  

## Special Thanks
**Thanks to [DataTalks.Club](https://datatalks.club) for the knowledge gained to complete this project. It truly is a great community.**