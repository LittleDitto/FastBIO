# src/routes/auth.py

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from utils import create_access_token, verify_password
from app.db.database import db
import logging

router = APIRouter()

logger = logging.getLogger(__name__)

@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # Mengambil data akun dari database
    user = await db.akun.find_one({"username": form_data.username})
    if user is None:
        logger.error(f"Login failed for username: {form_data.username}")
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    if not verify_password(form_data.password, user["password"]):
        logger.error(f"Incorrect password for username: {form_data.username}")
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    # Mengambil level akses untuk pengguna
    level_akses = await db.level_akses.find_one({"id_level_akses": user["id_level_akses"]})
    if not level_akses:
        logger.error(f"Level akses tidak ditemukan untuk user: {form_data.username}")
        raise HTTPException(status_code=400, detail="Level akses tidak ditemukan")

    # Membuat token
    access_token = create_access_token(data={"sub": user["username"]})
    logger.info(f"Token created for username: {form_data.username}")

    # Mengirimkan token beserta informasi akun dan level akses
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id_akun": user["id_akun"],
            "username": user["username"],
            "level_akses": {
                "id_level_akses": level_akses["id_level_akses"],
                "hak_akses": level_akses["hak_akses"],
                "priority_akses": level_akses["priority_akses"]
            }
        }
    }
