from fastapi import FastAPI
import api.example
from stores.CourseStore import CourseStore

# Initialise stores
CourseStore.load()

# Initialise app
app = FastAPI(title="TSE Assignment 2 API", version="1.0.0")

# Initialise routers
app.include_router(api.example.router)
