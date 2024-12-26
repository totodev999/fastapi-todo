from fastapi import APIRouter, Depends
from sqlmodel import Session
from uuid import UUID

from src.classes.api.Todos import Todo, PostTodoRequest, Todos, Status
from db.database import get_session
from repositories.todo_repository import TodoRepository
from usecases.todo_usecase import TodoUsecase

router = APIRouter(prefix="/todos", tags=["todos"])


@router.post("/", response_model=Todo)
def create_todo(input: PostTodoRequest, session: Session = Depends(get_session)):
    todo_repository = TodoRepository(session=session)
    todo = TodoUsecase(todo_repository=todo_repository).create(
        input.title, input.content
    )

    return todo


@router.get("/", response_model=Todos)
def get_todo(status: Status = None, session: Session = Depends(get_session)):
    todo_repository = TodoRepository(session=session)
    if status:
        todos = TodoUsecase(todo_repository=todo_repository).get_by_status(status)
    else:
        todos = TodoUsecase(todo_repository=todo_repository).get_all()

    return {"todos": todos}


@router.get("/{id}", response_model=Todo | None)
def get_todo_by_id(id: UUID, session: Session = Depends(get_session)):
    todo_repository = TodoRepository(session=session)
    todos = TodoUsecase(todo_repository=todo_repository).get_by_id(id)

    return todos
