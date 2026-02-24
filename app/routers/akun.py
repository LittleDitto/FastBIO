from fastapi import APIRouter, HTTPException, Depends
from app.models.model import Akun
from app.db.database import get_db
from app.schemas import AkunCreate, AkunResponse
from utils import get_password_hash
from sqlalchemy.orm import Session
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/create", response_model=dict)
async def create_akun(akun: AkunCreate, db: Session = Depends(get_db)):
    """Create a new account. Requires authentication."""
    try:
        # Check for duplicate username
        existing_user = db.query(Akun).filter(Akun.username == akun.username).first()
        if existing_user:
            logger.warning(f"Create failed: Username '{akun.username}' already exists")
            raise HTTPException(status_code=400, detail="Username already exists")
        
        # Check for duplicate id_akun
        existing_id = db.query(Akun).filter(Akun.id_akun == akun.id_akun).first()
        if existing_id:
            logger.warning(f"Create failed: ID Akun '{akun.id_akun}' already exists")
            raise HTTPException(status_code=400, detail="ID Akun already exists")
        
        # Hash password and create account using SQLAlchemy ORM
        hashed_password = get_password_hash(akun.password)
        new_akun = Akun(
            id_akun=akun.id_akun,
            id_level_akses=akun.id_level_akses,
            username=akun.username,
            password=hashed_password
        )
        db.add(new_akun)
        db.commit()
        db.refresh(new_akun)
        
        logger.info(f"Success: Created account '{akun.id_akun}'")
        return {"message": "Akun created"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Create failed: {str(e)}")
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/get/{id}", response_model=AkunResponse)
async def get_akun(id: str, db: Session = Depends(get_db)):
    """Get account by ID. Requires authentication."""
    try:
        akun = db.query(Akun).filter(Akun.id_akun == id).first()
        if akun:
            logger.info(f"Success: Retrieved account '{id}'")
            return akun
    except Exception as e:
        logger.error(f"Get account '{id}' failed: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
    logger.warning(f"Get failed: Account '{id}' not found")
    raise HTTPException(status_code=404, detail="Akun not found")

@router.put("/update/{id}")
async def update_akun(id: str, akun: AkunCreate, db: Session = Depends(get_db)):
    """Update account by ID. Requires authentication."""
    try:
        existing_akun = db.query(Akun).filter(Akun.id_akun == id).first()
        if not existing_akun:
            logger.warning(f"Update failed: Account '{id}' not found")
            raise HTTPException(status_code=404, detail="Akun not found")
        
        # Hash the new password
        hashed_password = get_password_hash(akun.password)
        
        # Update fields using SQLAlchemy ORM
        existing_akun.id_level_akses = akun.id_level_akses
        existing_akun.username = akun.username
        existing_akun.password = hashed_password
        db.commit()
        
        logger.info(f"Success: Updated account '{id}'")
        return {"message": "Akun updated"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Update account '{id}' failed: {str(e)}")
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/delete/{id}")
async def delete_akun(id: str, db: Session = Depends(get_db)):
    """Delete account by ID. Requires authentication."""
    try:
        result = db.query(Akun).filter(Akun.id_akun == id).delete()
        if result:
            db.commit()
            logger.info(f"Success: Deleted account '{id}'")
            return {"message": "Akun deleted"}
    except Exception as e:
        logger.error(f"Delete account '{id}' failed: {str(e)}")
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    
    logger.warning(f"Delete failed: Account '{id}' not found")
    raise HTTPException(status_code=404, detail="Akun not found")

@router.get("/getAll", response_model=list[AkunResponse])
async def get_all_akun(db: Session = Depends(get_db)):
    """Get all accounts. Requires authentication."""
    try:
        akun_list = db.query(Akun).all()
        if akun_list:
            logger.info(f"Success: Retrieved {len(akun_list)} accounts")
            return akun_list
    except Exception as e:
        logger.error(f"Get all accounts failed: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
    logger.warning("Get all accounts: No accounts found")
    raise HTTPException(status_code=404, detail="No accounts found")
