terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.18.0"
    }
  }
}

provider "google" {
  # Configuration options
  credentials = file(var.credentials)
  project     = var.project
  region      = var.region
}

resource "google_storage_bucket" "seattle-crime-data-bucket" { # Provide bucket name here but does not need to be uniquely identifiable 
  name          = var.gcs_bucket_name                          # Uniquely identifiable bucket name needs to be provided here
  location      = var.location
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

resource "google_bigquery_dataset" "seattle_crime_dataset" { # Provide name for new terraform resource
  dataset_id                 = var.bq_dataset_name
  location                   = var.location
  delete_contents_on_destroy = true # Provide a unique ID for this dataset, without the project name
}