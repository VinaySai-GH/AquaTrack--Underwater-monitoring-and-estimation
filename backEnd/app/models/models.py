#Implemented by Karthik  Tamarapalli

from sqlalchemy import Column, String, DateTime, Text, func,Integer,ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database.database import Base
import uuid


class User(Base):
    __tablename__ = "profiles"  # matches Supabase table name

    # --- Column Definitions (Aligned with Supabase Table) ---
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True, nullable=False)
    full_name = Column(Text, nullable=True)
    email = Column(Text, nullable=True, unique=True, index=True)
    avatar_url = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)
    role = Column(Text, server_default="'user'::text", nullable=True)

    # Relationship with chat messages (optional)
    chat_messages = relationship("ChatMessage", back_populates="user", cascade="all, delete-orphan")

class ChatMessage(Base):
    __tablename__ = "chat_messages"

    # --- Column definitions (exactly matching Supabase) ---   
    id = Column(Integer, primary_key=True, nullable=False, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("profiles.id"), nullable=False)
    message = Column(Text, nullable=False)
    response = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.current_timestamp(), nullable=True)

    # Relationship back to User (profiles)
    user = relationship("User", back_populates="chat_messages")
