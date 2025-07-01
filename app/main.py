from fastapi import FastAPI
from sentry_sdk.integrations.fastapi import FastApiIntegration
import sentry_sdk
from app.api.router import router as api_router
from app.config.settings import settings
from fastapi.middleware.cors import CORSMiddleware

sentry_sdk.init(
    dsn=settings.SENTRY_DSN,
    integrations=[FastApiIntegration()],
    traces_sample_rate=1.0,
    environment=settings.ENVIRONMENT,
)

app = FastAPI(title="Health Bot API", docs_url="/docs", redoc_url="/redoc", openapi_url="/openapi.json")

# Add CORS middleware (best practice for APIs)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
