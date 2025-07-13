# FastAPI + Pydantic v2 + CQRS Project

## Features
- FastAPI with Pydantic v2
- CRUD with Azure Cosmos NoSQL
- Repository and CQRS (Command/Query) patterns
- Best practices for API design, error handling, and security
- Sentry integration for error monitoring
- Alembic for migrations
- Pytest and coverage for testing
- All dependencies managed via `pyproject.toml`

## Project Structure
- `app/api/` - API routers
- `app/commands/` - Command handlers (write operations)
- `app/queries/` - Query handlers (read operations)
- `app/repositories/` - Data access layer
- `app/models/` - Database models
- `app/schemas/` - Pydantic schemas
- `app/core/` - Core logic (JWT, security, etc.)
- `app/config/` - Configuration and settings
- `tests/` - Test cases

## Getting Started
1. Install dependencies:
   ```sh
   pip install poetry
   poetry install
   ```
2. Run the app:
   ```sh
   poetry run uvicorn app.main:app --reload
   ```
3. Run tests:
   ```sh
   poetry run pytest --cov=app
   ```

## Deployment
- Ready for CI/CD on Azure Cloud.
- Use Alembic for migrations, if you use the NOSQL like Azure Cosmos NoSQL, just skip it.
- Use Sentry for error monitoring.

## Notes
- All business logic should use command/query handlers.
- All data access should go through repositories.
- All models should use Pydantic v2.
