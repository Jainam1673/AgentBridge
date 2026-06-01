from fastapi import APIRouter, Depends, HTTPException, status
from src.domain.models.models import User, UserRole
import uuid

router = APIRouter()

# Mock user for development
MOCK_USER = User(
    id=uuid.uuid4(),
    email="admin@agentbridge.ai",
    full_name="Admin User",
    role=UserRole.ADMIN,
    tenant_id=uuid.uuid4()
)

async def get_current_user():
    # Placeholder for actual OAuth2 logic
    return MOCK_USER

@router.post("/login")
async def login():
    return {"access_token": "mock_token", "token_type": "bearer"}

@router.get("/me")
async def get_me(user: User = Depends(get_current_user)):
    return {
        "email": user.email,
        "full_name": user.full_name,
        "role": user.role,
        "tenant_id": user.tenant_id
    }
