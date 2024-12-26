from dataclasses import dataclass
from sqlmodel import Session, select
from uuid import UUID

from db.models import Todo, Status


@dataclass
class TodoRepository:
    session: Session

    def create(self, title: str, content: str) -> Todo:
        todo = Todo(title=title, content=content, status=Status.not_started)
        self.session.add(todo)
        self.session.commit()
        self.session.refresh(todo)
        return todo

    def get_all(self) -> list[Todo]:
        statement = select(Todo)
        return self.session.exec(statement)

    def get_by_status(self, status: Status) -> list[Todo]:
        statement = select(Todo).where(Todo.status == status)
        return self.session.exec(statement)

    def get_by_id(self, id: UUID) -> Todo | None:
        todo = self.session.get(Todo, id)
        return todo
