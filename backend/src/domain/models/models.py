from datetime import datetime
from typing import List, Optional
from sqlalchemy import String, ForeignKey, DateTime, JSON, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
import enum
import uuid

class Base(DeclarativeBase):
    pass

class UserRole(str, enum.Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    USER = "user"

class Tenant(Base):
    __tablename__ = "tenants"
    
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(255), unique=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    
    users: Mapped[List["User"]] = relationship(back_populates="tenant", cascade="all, delete-orphan")
    documents: Mapped[List["Document"]] = relationship(back_populates="tenant", cascade="all, delete-orphan")

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    full_name: Mapped[Optional[str]] = mapped_column(String(255))
    role: Mapped[UserRole] = mapped_column(SQLEnum(UserRole), default=UserRole.USER)
    tenant_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("tenants.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    
    tenant: Mapped["Tenant"] = relationship(back_populates="users")

class Document(Base):
    __tablename__ = "documents"
    
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(255))
    content: Mapped[str] = mapped_column(String)
    metadata_json: Mapped[dict] = mapped_column(JSON, default=dict)
    tenant_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("tenants.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    tenant: Mapped["Tenant"] = relationship(back_populates="documents")

class ToolIntegration(Base):
    __tablename__ = "tool_integrations"
    
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    tenant_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("tenants.id"))
    tool_type: Mapped[str] = mapped_column(String(50)) # e.g., 'google_drive', 'github', 'jira'
    config: Mapped[dict] = mapped_column(JSON)
    status: Mapped[str] = mapped_column(String(50), default="active")
    last_sync: Mapped[Optional[datetime]] = mapped_column(DateTime)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
