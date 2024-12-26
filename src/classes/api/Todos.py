from pydantic import BaseModel
from uuid import UUID
from enum import Enum


class Status(str, Enum):
    not_started = "not_started"
    in_progress = "in_progress"
    done = "done"
    hold = "hold"


class BaseTodo(BaseModel):
    title: str
    content: str
    status: Status


class Todo(BaseTodo):
    id: UUID
    created_at: str
    updated_at: str


class Todos(BaseModel):
    todos: list[Todo]


class PostTodoRequest(BaseModel):
    title: str
    content: str
