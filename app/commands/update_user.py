from app.schemas.user import UserCreate, UserRead
from app.repositories.user_repository import UserRepository

class UpdateUserCommand:
    def __init__(self, user_id: str, user_update: UserCreate):
        self.user_id = user_id
        self.user_update = user_update

class UpdateUserHandler:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def handle(self, command: UpdateUserCommand) -> UserRead:
        updated = self.repository.update_user(command.user_id, command.user_update.model_dump())
        return UserRead(**updated)
