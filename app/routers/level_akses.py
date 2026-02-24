from fastapi import APIRouter, HTTPException, Depends
from app.models.model import LevelAkses
from app.db.database import get_db
from app.schemas import LevelAksesCreate, LevelAksesResponse
from sqlalchemy.orm import Session
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/create")
async def create_level_akses(level: LevelAksesCreate, db: Session = Depends(get_db)):
    """Create a new level akses."""
    try:
        new_level = LevelAkses(
            id_level_akses=level.id_level_akses,
            hak_akses=level.hak_akses,
            priority_akses=level.priority_akses
        )
        db.add(new_level)
        db.commit()
        db.refresh(new_level)
        logger.info(f"Success: Created level akses '{level.id_level_akses}'")
        return {"message": "Level akses created"}
    except Exception as e:
        logger.error(f"Create level akses failed: {str(e)}")
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/get/{id}", response_model=LevelAksesResponse)
async def get_level_akses(id: str, db: Session = Depends(get_db)):
    """Get level akses by ID."""
    try:
        level = db.query(LevelAkses).filter(LevelAkses.id_level_akses == id).first()
        if level:
            logger.info(f"Success: Retrieved level akses '{id}'")
            return level
    except Exception as e:
        logger.error(f"Get level akses '{id}' failed: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
    logger.warning(f"Get failed: Level akses '{id}' not found")
    raise HTTPException(status_code=404, detail="Level akses not found")

@router.put("/update/{id}")
async def update_level_akses(id: str, level: LevelAksesCreate, db: Session = Depends(get_db)):
    """Update level akses by ID."""
    try:
        existing = db.query(LevelAkses).filter(LevelAkses.id_level_akses == id).first()
        if not existing:
            logger.warning(f"Update failed: Level akses '{id}' not found")
            raise HTTPException(status_code=404, detail="Level akses not found")
        
        # Update using SQLAlchemy ORM
        existing.hak_akses = level.hak_akses
        existing.priority_akses = level.priority_akses
        db.commit()
        
        logger.info(f"Success: Updated level akses '{id}'")
        return {"message": "Level akses updated"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Update level akses '{id}' failed: {str(e)}")
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/delete/{id}")
async def delete_level_akses(id: str, db: Session = Depends(get_db)):
    """Delete level akses by ID."""
    try:
        result = db.query(LevelAkses).filter(LevelAkses.id_level_akses == id).delete()
        if result:
            db.commit()
            logger.info(f"Success: Deleted level akses '{id}'")
            return {"message": "Level akses deleted"}
    except Exception as e:
        logger.error(f"Delete level akses '{id}' failed: {str(e)}")
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    
    logger.warning(f"Delete failed: Level akses '{id}' not found")
    raise HTTPException(status_code=404, detail="Level akses not found")

@router.get("/getAll", response_model=list[LevelAksesResponse])
async def get_all_level_akses(db: Session = Depends(get_db)):
    """Get all level akses."""
    try:
        level_list = db.query(LevelAkses).all()
        if level_list:
            logger.info(f"Success: Retrieved {len(level_list)} level akses")
            return level_list
    except Exception as e:
        logger.error(f"Get all level akses failed: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
    logger.warning("Get all level akses: No records found")
    raise HTTPException(status_code=404, detail="No level akses found")
