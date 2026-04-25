import config
from fastapi import APIRouter, Request, Depends 
from fastapi.responses import RedirectResponse
from auth.auth import oauth

from database.dborm import get_db
from database.models.User import User
from sqlalchemy.orm import Session
from database.repositories.UserRepository import UserRepository

router = APIRouter(tags=["auth"], prefix="/auth")

@router.get("/login")
async def login(request: Request):
    redirect_uri = str(request.base_url) + "api/auth/callback"
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get("/callback")
async def auth_callback(request: Request, db: Session = Depends(get_db)):
    token = await oauth.google.authorize_access_token(request)
    user_info = token.get("userinfo")

    email = user_info["email"]
    google_id = user_info["sub"]

    user = UserRepository.get_by_email(db, email)
    if not user:
        user = UserRepository.create(db, email, google_id)
    
    request.session["user_id"] = user.id
    return RedirectResponse(url=config.FRONTEND_URL + "/src/pages/courseSelection.html")

@router.delete("/logout")
async def login(request: Request):
    request.session.clear()
    return { "success": True }

@router.get("/me")
async def get_current_user(request: Request, db: Session = Depends(get_db)):
    user_id = request.session.get("user_id")
    if not user_id:
        return { "user": None }

    user = UserRepository.get_by_id(db, user_id)
    return { "user": user }