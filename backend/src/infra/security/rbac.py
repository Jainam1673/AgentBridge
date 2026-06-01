from fastapi import HTTPException, Depends, status
from src.domain.models.models import User, UserRole
from src.api.routes.auth import get_current_user

class RoleChecker:
    def __init__(self, allowed_roles: list[UserRole]):
        self.allowed_roles = allowed_roles

    def __call__(self, user: User = Depends(get_current_user)):
        if user.role not in self.allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Operation not permitted for this user role",
            )
        return user

def admin_required():
    return Depends(RoleChecker([UserRole.ADMIN]))

def manager_required():
    return Depends(RoleChecker([UserRole.ADMIN, UserRole.MANAGER]))
