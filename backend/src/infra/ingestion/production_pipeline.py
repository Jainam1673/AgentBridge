from typing import List, Any
import uuid
import logging
from src.domain.models.models import Document
from sqlalchemy.ext.asyncio import AsyncSession
from src.infra.db.database import get_db

logger = logging.getLogger(__name__)

class ProductionIngestionPipeline:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def validate(self, data: List[dict]) -> List[dict]:
        # Implementation of schema validation
        valid_records = []
        for record in data:
            if "title" in record and "content" in record:
                valid_records.append(record)
            else:
                logger.warning(f"Skipping invalid record: {record.get('title', 'Unknown')}")
        return valid_records

    async def normalize(self, data: List[dict]) -> List[dict]:
        # Implementation of text normalization
        for record in data:
            record["content"] = record["content"].strip()
            record["title"] = record["title"].title()
        return data

    async def deduplicate(self, data: List[dict], tenant_id: uuid.UUID) -> List[dict]:
        # Logic to check for existing documents in the DB
        # For simplicity, we just filter current batch duplicates
        seen = set()
        unique_data = []
        for record in data:
            if record["title"] not in seen:
                unique_data.append(record)
                seen.add(record["title"])
        return unique_data

    async def load(self, data: List[dict], tenant_id: uuid.UUID):
        for record in data:
            doc = Document(
                id=uuid.uuid4(),
                title=record["title"],
                content=record["content"],
                metadata_json=record.get("metadata", {}),
                tenant_id=tenant_id
            )
            self.db.add(doc)
        await self.db.commit()

    async def process_batch(self, raw_data: List[dict], tenant_id: uuid.UUID):
        valid = await self.validate(raw_data)
        normalized = await self.normalize(valid)
        unique = await self.deduplicate(normalized, tenant_id)
        await self.load(unique, tenant_id)
        return len(unique)
