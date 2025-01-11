from fastapi import APIRouter, HTTPException
from app.models.model import Akun
from app.db.database import db
from utils import get_password_hash
from bson import ObjectId
from fastapi.encoders import jsonable_encoder

router = APIRouter()

@router.post("/create")
async def create_akun(akun: Akun):
    akun.password = get_password_hash(akun.password)
    akun_data = jsonable_encoder(akun)
    await db.akun.insert_one(akun_data)
    return {"message": "Akun created"}

@router.get("/get/{id}")
async def get_akun(id: str):
    try:
        akun = await db.akun.find_one({"id_akun": id})
        if akun:
            akun["_id"] = str(akun["_id"])
            return akun
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    raise HTTPException(status_code=404, detail="Akun not found")

@router.put("/update/{id}")
async def update_akun(id: str, akun: Akun):
    try:
        akun.password = get_password_hash(akun.password)
        akun_data = jsonable_encoder(akun)
        result = await db.akun.update_one(
            {"id_akun": id},
            {"$set": akun_data}
        )
        if result.modified_count:
            return {"message": "Akun updated"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    raise HTTPException(status_code=404, detail="Akun not found")

@router.delete("/delete/{id}")
async def delete_akun(id: str):
    try:
        result = await db.akun.delete_one({"id_akun": id})
        if result.deleted_count:
            return {"message": "Akun deleted"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    raise HTTPException(status_code=404, detail="Akun not found")

@router.get("/getAll")
async def get_all_akun():
    try:
        akun_list = await db.akun.find().to_list(100)
        if akun_list:
            for akun in akun_list:
                akun["_id"] = str(akun["_id"])
            return akun_list
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    raise HTTPException(status_code=404, detail="No accounts found")

