from fastapi import APIRouter, Depends, HTTPException, status
from src.domain.models.models import User, UserRole
from src.infra.db.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import uuid

router = APIRouter()

async def get_current_user(db: AsyncSession = Depends(get_db)):
    # In a real app, this would validate a JWT token
    # For simulation, we return the first user in the DB
    result = await db.execute(select(User).limit(1))
    user = result.scalar_one_or_none()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )
    return user

@router.post("/login")
async def login():
    return {"access_token": "simulated_jwt_token", "token_type": "bearer"}

@router.get("/me")
async def get_me(user: User = Depends(get_current_user)):
    return {
        "email": user.email,
        "full_name": user.full_name,
        "role": user.role,
        "tenant_id": user.tenant_id
    }
