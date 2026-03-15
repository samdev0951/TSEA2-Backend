from fastapi import FastAPI
import api.example

app = FastAPI(title="TSE Assignment 2 API", version="1.0.0")

# Initialise routers
app.include_router(api.example.router)