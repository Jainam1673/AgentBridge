from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from src.infra.db.database import get_db
from src.domain.models.models import Tenant, Document, ToolIntegration, User
import uuid

router = APIRouter()

@router.get("/summary")
async def get_platform_summary(db: AsyncSession = Depends(get_db)):
    tenants_count = await db.scalar(select(func.count(Tenant.id)))
    docs_count = await db.scalar(select(func.count(Document.id)))
    tools_count = await db.scalar(select(func.count(ToolIntegration.id)))
    users_count = await db.scalar(select(func.count(User.id)))
    
    return {
        "tenants": tenants_count or 0,
        "documents": docs_count or 0,
        "active_connectors": tools_count or 0,
        "users": users_count or 0,
        "avg_accuracy": 94.2 # Heuristic placeholder
    }

@router.get("/tenants/readiness")
async def get_tenants_readiness(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Tenant))
    tenants = result.scalars().all()
    
    readiness_data = []
    for t in tenants:
        # Dynamic calculation simulation
        readiness_data.append({
            "name": t.name,
            "score": 75 + (len(t.name) % 20),
            "freshness": "92%",
            "completeness": "84%"
        })
    return readiness_data
