import os
from pydantic_settings import BaseSettings
from .keyvault_client import AzureKeyVaultClient
from dotenv import load_dotenv

load_dotenv()
class Settings(BaseSettings):
    SENTRY_DSN: str = ""
    ENVIRONMENT: str = "development"
    COSMOS_ENDPOINT: str = ""
    COSMOS_KEY: str = ""
    COSMOS_DATABASE: str = ""
    JWT_SECRET_KEY: str = "supersecret"
    JWT_ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Get Key Vault URL from environment or default
KEY_VAULT_NAME = os.getenv("KEY_VAULT_NAME", "0GDQNkpj0ki9OQ5krgAtDtqQEpfywI5g")
KEY_VAULT_URL = f"https://{KEY_VAULT_NAME}.vault.azure.net/"

# Initialize Key Vault client
keyvault_client = AzureKeyVaultClient(KEY_VAULT_URL)

def get_secret_or_env(secret_name: str, default: str = "") -> str:
    keyvault_name = secret_name.replace("_", "-")
    try:
        return keyvault_client.get_secret(keyvault_name)
    except Exception:
        return os.getenv(secret_name, default)

if os.getenv("ENVIRONMENT", "development") == "development":
    settings = Settings()
else:
    settings = Settings(
        SENTRY_DSN=os.getenv("SENTRY_DSN", ""),
        ENVIRONMENT=os.getenv("ENVIRONMENT", "production"),
        COSMOS_ENDPOINT=get_secret_or_env("COSMOS_ENDPOINT"),
        COSMOS_KEY=get_secret_or_env("COSMOS_KEY"),
        COSMOS_DATABASE=get_secret_or_env("COSMOS_DATABASE"),
        JWT_SECRET_KEY=get_secret_or_env("JWT_SECRET_KEY", "gcm+[;?J;doL;Ec?)dl+),{ki4Zr@:"),
        JWT_ALGORITHM=get_secret_or_env("JWT_ALGORITHM", "HS256"),
    )
