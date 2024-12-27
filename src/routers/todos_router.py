from fastapi import APIRouter
from uuid import UUID

from src.classes.api.Todos import Todo, PostTodoRequest, Todos, Status
from db.database import sessionDep
from repositories.todo_repository import TodoRepository
from usecases.todo_usecase import TodoUsecase

router = APIRouter(prefix="/todos", tags=["todos"])


@router.post("/", response_model=Todo)
def create_todo(input: PostTodoRequest, session: sessionDep):
    todo_repository = TodoRepository(session=session)
    todo = TodoUsecase(todo_repository=todo_repository).create(
        input.title, input.content
    )

    return todo


@router.get("/", response_model=Todos)
def get_todo(session: sessionDep, status: Status = None):
    todo_repository = TodoRepository(session=session)
    if status:
        todos = TodoUsecase(todo_repository=todo_repository).get_by_status(status)
    else:
        todos = TodoUsecase(todo_repository=todo_repository).get_all()

    return {"todos": todos}


@router.get("/{id}", response_model=Todo | None)
def get_todo_by_id(id: UUID, session: sessionDep):
    todo_repository = TodoRepository(session=session)
    todos = TodoUsecase(todo_repository=todo_repository).get_by_id(id)

    return todos
