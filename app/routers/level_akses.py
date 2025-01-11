from fastapi import APIRouter, HTTPException
from app.models.model import LevelAkses
from app.db.database import db
from bson import ObjectId

router = APIRouter()

@router.post("/create")
async def create_level_akses(level: LevelAkses):
    await db.level_akses.insert_one(level.dict())
    return {"message": "Level akses created"}

@router.get("/get/{id}")
async def get_level_akses(id: str):
    level = await db.level_akses.find_one({"id_level_akses": id})
    if level:
        level["_id"] = str(level["_id"])  # Mengubah _id menjadi string
        return level
    raise HTTPException(status_code=404, detail="Level akses not found")

@router.put("/update/{id}")
async def update_level_akses(id: str, level: LevelAkses):
    result = await db.level_akses.update_one(
        {"id_level_akses": id},
        {"$set": level.dict()}
    )
    if result.modified_count:
        return {"message": "Level akses updated"}
    raise HTTPException(status_code=404, detail="Level akses not found")

@router.delete("/delete/{id}")
async def delete_level_akses(id: str):
    result = await db.level_akses.delete_one({"id_level_akses": id})
    if result.deleted_count:
        return {"message": "Level akses deleted"}
    raise HTTPException(status_code=404, detail="Level akses not found")


@router.get("/getAll")
async def get_all_level_akses():
    try:
        level_list = await db.level_akses.find().to_list(100)  # Mengambil sampai 100 akun
        if level_list:
            # Mengonversi _id setiap akun menjadi string sebelum mengembalikan akun
            for level_akses in level_list:
                level_akses["_id"] = str(level_akses["_id"])  # Mengonversi _id menjadi string
            return level_list
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error reading data from MongoDB")
