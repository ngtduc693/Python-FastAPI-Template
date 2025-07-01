from app.repositories.user_repository import UserRepository
from app.schemas.user import UserRead

class GetUserQuery:
    def __init__(self, user_id: str):
        self.user_id = user_id

class GetUserHandler:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def handle(self, query: GetUserQuery) -> UserRead:
        user = self.repository.get_user(query.user_id)
        if not user:
            return None
        return UserRead(**user)
