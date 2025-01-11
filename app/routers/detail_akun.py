from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from app.models.model import DetailAkun
from app.db.database import db
from datetime import datetime

from app.routers.level_akses import get_level_akses

router = APIRouter()

@router.post("/create")
async def create_detail_akun(detail: DetailAkun):
    detail_data = detail.dict()
    detail_data["id_detail"] = detail_data["id_akun"]
    await db.detail_akun.insert_one(detail_data)
    return {"message": "Detail akun created"}

@router.get("/get/{id}")
async def get_detail_akun(id: str):
    detail = await db.detail_akun.find_one({"id_akun": id})
    if detail:
        detail["_id"] = str(detail["_id"])  # Convert ObjectId to string
        return detail
    raise HTTPException(status_code=404, detail="Detail akun not found")

@router.put("/update/{id}")
async def update_detail_akun(id: str, detail: DetailAkun):
    detail_data = detail.dict(exclude={"id_level_akses","dibuat"})# Exclude id_level_akses from updates
    result = await db.detail_akun.update_one(
        {"id_akun": id},
        {"$set": detail_data}
    )
    if result.modified_count:
        return {"message": "Detail akun updated"}
    else:
        return {"message": "No changes made to the detail akun"}

@router.delete("/delete/{id}")
async def delete_detail_akun(id: str):
    result = await db.detail_akun.delete_one({"id_akun": id})
    if result.deleted_count:
        return {"message": "Detail akun deleted"}
    raise HTTPException(status_code=404, detail="Detail akun not found")

@router.get("/getAll")
async def get_all_detail_akun():
    detail_akun_list = await db.detail_akun.find().to_list(100)
    if detail_akun_list:
        for detail_akun in detail_akun_list:
            detail_akun["_id"] = str(detail_akun["_id"])
        return detail_akun_list
    raise HTTPException(status_code=404, detail="No accounts found")