from fastapi import APIRouter
from typing import Union
from classes.api.GetTodos import GetTodo, Status, GetTodos
from uuid import UUID

router = APIRouter(prefix="/todos", tags=["todos"])


@router.get("/", response_model=GetTodos)
def read_root():
    todos = [
        GetTodo(
            id=UUID(hex="00000000-0000-0000-0000-000000000000"),
            title="title",
            content="content",
            status=Status.done,
            created_at="2021-01-01T00:00:00Z",
            updated_at="2021-01-01T00:00:00Z",
        )
        for _ in range(10)
    ]
    todos = {"todos": todos}
    return todos


@router.get("/{todo_id}", response_model=GetTodo)
def read_item(todo_id: UUID, q: Union[str, None] = None):
    todo = GetTodo(
        id=todo_id,
        title="title",
        content="content",
        status=Status.done,
        created_at="2021-01-01T00:00:00Z",
        updated_at="2021-01-01T00:00:00Z",
    )
    return todo
