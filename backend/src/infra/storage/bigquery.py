from google.cloud import bigquery
from pydantic_settings import BaseSettings

class BigQuerySettings(BaseSettings):
    BQ_PROJECT_ID: str = "agentbridge-dev"
    BQ_DATASET_ID: str = "platform_data"

bq_settings = BigQuerySettings()

class BigQueryAdapter:
    def __init__(self):
        self.client = bigquery.Client(project=bq_settings.BQ_PROJECT_ID)

    def insert_rows(self, table_id: str, rows: List[dict]):
        table_ref = self.client.dataset(bq_settings.BQ_DATASET_ID).table(table_id)
        errors = self.client.insert_rows_json(table_ref, rows)
        if errors:
            raise Exception(f"BigQuery insertion errors: {errors}")
