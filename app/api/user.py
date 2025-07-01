from fastapi import APIRouter, HTTPException, status
from app.schemas.user import UserCreate, UserRead
from app.repositories.user_repository import UserRepository
from app.commands.create_user import CreateUserCommand, CreateUserHandler
from app.queries.get_user import GetUserQuery, GetUserHandler
from app.commands.update_user import UpdateUserCommand, UpdateUserHandler
from app.commands.delete_user import DeleteUserCommand, DeleteUserHandler

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED, description="Tạo mới user")
def create_user(user: UserCreate):
    """Tạo mới một user."""
    repo = UserRepository()
    handler = CreateUserHandler(repo)
    try:
        return handler.handle(CreateUserCommand(user))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}", response_model=UserRead, description="Lấy thông tin user theo ID")
def get_user(user_id: str):
    """Lấy thông tin user theo user_id."""
    repo = UserRepository()
    handler = GetUserHandler(repo)
    user = handler.handle(GetUserQuery(user_id))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserRead, description="Cập nhật thông tin user")
def update_user(user_id: str, user: UserCreate):
    """Cập nhật thông tin user theo user_id."""
    repo = UserRepository()
    handler = UpdateUserHandler(repo)
    try:
        return handler.handle(UpdateUserCommand(user_id, user))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT, description="Xóa user")
def delete_user(user_id: str):
    """Xóa user theo user_id."""
    repo = UserRepository()
    handler = DeleteUserHandler(repo)
    success = handler.handle(DeleteUserCommand(user_id))
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return None
