import config
from fastapi import FastAPI
import api.courses
import api.auth
from starlette.middleware.sessions import SessionMiddleware
from stores.CourseStore import CourseStore

# Initialise stores
CourseStore.load()

# Initialise app
app = FastAPI(title="TSE Assignment 2 API", version="1.0.0")

app.add_middleware(
    SessionMiddleware,
    secret_key=config.SECRET_KEY,
)

# Initialise routers
app.include_router(api.courses.router, prefix="/api")
app.include_router(api.auth.router, prefix="/api")
