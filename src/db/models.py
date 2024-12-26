from sqlmodel import SQLModel, Field
from uuid import UUID
import uuid
from datetime import datetime

from classes.api.Todos import Status


class Todo(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str
    content: str
    status: Status
    created_at: str = Field(
        default_factory=lambda: datetime.now().isoformat()
    )  # 作成日時
    updated_at: str = Field(
        default_factory=lambda: datetime.now().isoformat()
    )  # 更新日時
