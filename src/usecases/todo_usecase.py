from dataclasses import dataclass
from uuid import UUID

from repositories.todo_repository import TodoRepository
from src.classes.api.Todos import Status


@dataclass
class TodoUsecase:
    todo_repository: TodoRepository

    def create(self, title: str, content: str):
        return self.todo_repository.create(title, content)

    def get_all(self):
        return self.todo_repository.get_all()

    def get_by_status(self, status: Status):
        return self.todo_repository.get_by_status(status)

    def get_by_id(self, id: UUID):
        return self.todo_repository.get_by_id(id)
