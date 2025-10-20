from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.auth.auth import router as auth_router  # make sure this path is correct
from app.routes.user.user import user_router as user_router
app = FastAPI(title="SIH Backend")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include auth routes
app.include_router(auth_router)
app.include_router(user_router)
# Example unprotected route
@app.get("/")
async def home():
    return {"message": "Backend is running"}
