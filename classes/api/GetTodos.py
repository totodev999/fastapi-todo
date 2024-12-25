from pydantic import BaseModel
from uuid import UUID
from enum import Enum


class Status(str, Enum):
    not_started = "not_started"
    in_progress = "in_progress"
    done = "done"
    hold = "hold"


class GetTodo(BaseModel):
    id: UUID
    title: str
    content: str
    status: Status
    created_at: str
    updated_at: str


class GetTodos(BaseModel):
    todos: list[GetTodo]
