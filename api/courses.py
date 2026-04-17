from fastapi import APIRouter, Depends

from database.dborm import get_db
from database.models.User import User
from sqlalchemy.orm import Session
from stores.CourseStore import CourseStore

from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(tags=["courses"], prefix="/courses")

@router.get("/")
def courses():
    return CourseStore.get_courses()

@router.get("/{course_slug}")
def course(course_slug: str):
    return CourseStore.get_course_with_contents_meta(course_slug)


#Endpoint: GET /api/courses/{course_id}/{content_id}

@router.get("/{course_id}/{content_id}")
def get_content(course_id: str, content_id: str):
    content = CourseStore.get__course_content(course_id, content_id)
    if content is None:
        raise HTTPException(status_code=404, detail="Content not found")
    return content

# 



