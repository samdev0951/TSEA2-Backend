from fastapi import APIRouter, Depends

from database.dborm import get_db
from database.models.User import User
from sqlalchemy.orm import Session
from stores.CourseStore import CourseStore

router = APIRouter(tags=["courses"], prefix="/courses")

@router.get("/")
def courses():
    return CourseStore.get_courses()

@router.get("/{course_slug}")
def course(course_slug: str):
    return CourseStore.get_course_with_contents_meta(course_slug)