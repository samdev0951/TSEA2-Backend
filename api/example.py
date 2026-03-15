from fastapi import APIRouter, Depends

from MySQLdb import cursors
from database.dbconn import get_cursor

router = APIRouter(tags=["example"], prefix="/example")

@router.post("/")
def replace_me(
    cursor: cursors.Cursor = Depends(get_cursor)
):
    return { "replace_me": True }