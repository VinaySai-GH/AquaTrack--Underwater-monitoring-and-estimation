from fastapi import APIRouter,Header,HTTPException
from fastapi.responses import RedirectResponse,JSONResponse
import os
import requests
from dotenv import load_dotenv

# Load env
env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..", ".env"))
load_dotenv(dotenv_path=env_path)

SUPABASE_URL = os.getenv("SUPABASE_URL")
FRONTEND_URL = os.getenv("FRONTEND_URL")  #TODO Add the  Frontend redirect after login 
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")
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



# --------------------------
@router.post("/logout")
async def logout(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid Authorization header")
    
    token = authorization.replace("Bearer ", "")

    resp = requests.post(
        f"{SUPABASE_URL}/auth/v1/logout",
        headers={
            "Authorization": f"Bearer {token}",
            "apikey": SUPABASE_SERVICE_KEY
        }
    )

    if resp.status_code != 200:
        raise HTTPException(status_code=400, detail="Failed to logout from Supabase")

    return JSONResponse(content={"message": "Logged out successfully"}) 
