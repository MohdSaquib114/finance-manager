from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.v1.records import router as records_router 
from .api.v1.users import router as users_router
from app.api.v1 import records

from app.api.v1 import users

# from .routers import auth, users, posts


def create_app():
    app = FastAPI(title="Finance Manager API", version="1.0.0")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(records.router, prefix="/api/v1", tags=["records"])
    app.include_router(users.router, prefix="/api/v1", tags=["users"]) 
    
    return app
app = create_app()
