terraform {
  required_version = ">= 1.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 6.0"
    }
    google-beta = {
      source  = "hashicorp/google-beta"
      version = "~> 6.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

provider "google-beta" {
  project = var.project_id
  region  = var.region
}

module "project_services" {
  source  = "terraform-google-modules/project-factory/google//modules/project_services"
  version = "~> 17.0"

  project_id                  = var.project_id
  disable_services_on_destroy = false

  activate_apis = [
    "compute.googleapis.com",
    "iam.googleapis.com",
    "cloudresourcemanager.googleapis.com",
    "run.googleapis.com",
    "sqladmin.googleapis.com",
    "redis.googleapis.com",
    "bigquery.googleapis.com",
    "aiplatform.googleapis.com",
    "secretmanager.googleapis.com",
    "artifactregistry.googleapis.com",
    "vpcaccess.googleapis.com",
    "cloudbuild.googleapis.com",
  ]
}
