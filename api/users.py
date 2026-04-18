from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
 
from database.dborm import get_db
from database.repositories.UserRepository import UserRepository


router = APIRouter(tags=["users"], prefix="/users")

class PointsUpdate(BaseModel):
    points: int


@router.put("/{user_id}/points")
def update_points(user_id: str, body: PointsUpdate, db: Session = Depends(get_db)):
    user = UserRepository.get_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
 
    UserRepository.update_points(db, user_id, body.points)
    return {"message": "Points updated"}




















