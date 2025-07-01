
from azure.cosmos import CosmosClient, exceptions
from app.config.settings import settings

class UserRepository:
    CONTAINER_NAME = "users"
    def __init__(self):
        self.client = CosmosClient(settings.COSMOS_ENDPOINT, settings.COSMOS_KEY)
        self.database = self.client.get_database_client(settings.COSMOS_DATABASE)
        self.container = self.database.get_container_client(self.CONTAINER_NAME)

    def create_user(self, user: dict) -> dict:
        return self.container.create_item(body=user)

    def get_user(self, user_id: str) -> dict:
        try:
            return self.container.read_item(item=user_id, partition_key=user_id)
        except exceptions.CosmosResourceNotFoundError:
            return None

    def update_user(self, user_id: str, user_update: dict) -> dict:
        user = self.get_user(user_id)
        if not user:
            raise Exception("User not found")
        user.update(user_update)
        return self.container.replace_item(item=user_id, body=user)

    def delete_user(self, user_id: str) -> bool:
        try:
            self.container.delete_item(item=user_id, partition_key=user_id)
            return True
        except exceptions.CosmosResourceNotFoundError:
            return False
