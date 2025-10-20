from fastapi import APIRouter
from fastapi.responses import RedirectResponse
import os
from dotenv import load_dotenv

# Load env
env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..", ".env"))
load_dotenv(dotenv_path=env_path)

SUPABASE_URL = os.getenv("SUPABASE_URL")
FRONTEND_URL = os.getenv("FRONTEND_URL")  # Frontend redirect after login 

router = APIRouter(prefix="/auth", tags=["Authentication"])

# --------------------------
# Redirect to Supabase Google OAuth
# --------------------------
@router.get("/google/login")
async def google_login():
    """
    Redirect user to Supabase's Google OAuth endpoint.
    """
    # This endpoint triggers Google login in Supabase
    supabase_oauth_url = (
        f"{SUPABASE_URL}/auth/v1/authorize?"
        "provider=google&"
        f"redirect_to={FRONTEND_URL}/auth/success"
    )
    return RedirectResponse(url=supabase_oauth_url)
