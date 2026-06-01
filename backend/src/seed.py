import asyncio
import json
import uuid
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from src.domain.models.models import Tenant, User, UserRole, ToolIntegration
from src.infra.db.database import settings

async def seed_data():
    engine = create_async_engine(settings.DATABASE_URL)
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    with open('../data/tenants.json', 'r') as f:
        tenants_data = json.load(f)

    async with async_session() as session:
        for t_data in tenants_data:
            tenant = Tenant(
                id=uuid.uuid4(),
                name=t_data['name']
            )
            session.add(tenant)
            await session.flush()

            # Add an admin user for each tenant
            admin = User(
                id=uuid.uuid4(),
                email=f"admin@{t_data['domain']}",
                full_name=f"{t_data['name']} Admin",
                role=UserRole.ADMIN,
                tenant_id=tenant.id
            )
            session.add(admin)

            # Add tool integrations
            for tool in t_data['connectors']:
                integration = ToolIntegration(
                    id=uuid.uuid4(),
                    tenant_id=tenant.id,
                    tool_type=tool,
                    config={"mock": True},
                    status="active"
                )
                session.add(integration)

        await session.commit()
    print("Seed data inserted successfully.")

if __name__ == "__main__":
    asyncio.run(seed_data())
