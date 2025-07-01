from app.repositories.user_repository import UserRepository

class DeleteUserCommand:
    def __init__(self, user_id: str):
        self.user_id = user_id

class DeleteUserHandler:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def handle(self, command: DeleteUserCommand) -> bool:
        return self.repository.delete_user(command.user_id)
