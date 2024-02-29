variable "credentials" {
  description = "My Google Credentials"
  default     = "./key/seattle-crime-service-account-key.json"

}

variable "project" {
  description = "Project Name"
  default     = "seattle-crime-48435"

}

variable "location" {
  description = "Project location"
  default     = "US"

}

variable "region" {
  description = "Project region"
  default     = "us-central"

}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "crime_dataset"

}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "seattle-crime-48435-bucket"

}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "Standard"

}