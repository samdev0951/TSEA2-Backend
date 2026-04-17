from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from stores.UserStore import UserStore

router = APIRouter()


class PointsUpdate(BaseModel):
    points: int


@router.put("/users/{user_id}/points")
def update_points(user_id: str, body: PointsUpdate):
    success = UserStore.update_points(user_id, body.points)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "Points updated"}




















