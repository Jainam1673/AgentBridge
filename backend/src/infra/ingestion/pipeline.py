from abc import ABC, abstractmethod
from typing import Any, List
from src.domain.models.models import Document
import uuid

class IngestionPipeline(ABC):
    @abstractmethod
    async def extract(self, source: Any) -> List[dict]:
        pass

    @abstractmethod
    async def transform(self, data: List[dict]) -> List[dict]:
        pass

    @abstractmethod
    async def load(self, data: List[dict], tenant_id: uuid.UUID):
        pass

    async def run(self, source: Any, tenant_id: uuid.UUID):
        raw_data = await self.extract(source)
        transformed_data = await self.transform(raw_data)
        await self.load(transformed_data, tenant_id)
