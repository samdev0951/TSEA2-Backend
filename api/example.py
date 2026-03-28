from fastapi import APIRouter, Depends

from MySQLdb import cursors
from database.dborm import get_db
from database.models.User import User
from sqlalchemy.orm import Session

router = APIRouter(tags=["example"], prefix="/example")

@router.post("/")
def replace_me(
    db: Session = Depends(get_db)
):
    user_count = db.query(User).count()
    return {"replace_me": user_count}