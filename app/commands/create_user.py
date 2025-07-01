from app.schemas.user import UserCreate, UserRead
from app.repositories.user_repository import UserRepository
import uuid

class CreateUserCommand:
    def __init__(self, user_create: UserCreate):
        self.user_create = user_create

class CreateUserHandler:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def handle(self, command: CreateUserCommand) -> UserRead:
        user_id = str(uuid.uuid4())
        user_dict = command.user_create.model_dump()
        user_dict["id"] = user_id
        created = self.repository.create_user(user_dict)
        return UserRead(**created)
