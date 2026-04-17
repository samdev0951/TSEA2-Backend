from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stores.CourseStore import CourseStore



router = APIRouter()

class PointsUpdate(BaseModel):
    points: int


@router.put("/users/{user_id}/points")
def update_points(user_id: str, body: PointsUpdate):
    success = UserStore.update_points(user_id, body.points)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "Points updated"}




















