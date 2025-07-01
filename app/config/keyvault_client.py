from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import os

class AzureKeyVaultClient:
    def __init__(self, vault_url: str):
        self.credential = DefaultAzureCredential()
        self.client = SecretClient(vault_url=vault_url, credential=self.credential)

    def get_secret(self, secret_name: str) -> str:
        return self.client.get_secret(secret_name).value
