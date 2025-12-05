from fastapi import APIRouter, status, Depends
from .schemas import UserCreateModel, UserModel
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from src.auth.service import UserService
from src.auth.utils import generate_password_hash
from fastapi import HTTPException

auth_router = APIRouter()
user_service = UserService()

@auth_router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=UserModel)
async def create_user_Account(
    user_data: UserCreateModel, 
    session: AsyncSession = Depends(get_session)
):
    email = user_data.email
    user_exists = await user_service.user_exists(email, session)
    if user_exists:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    
    new_user = await user_service.create_user(user_data, session)
    
    return new_user
