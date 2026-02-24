from fastapi import APIRouter, HTTPException, Depends
from app.models.model import DetailAkun
from app.db.database import get_db
from app.schemas import DetailAkunCreate, DetailAkunResponse
from sqlalchemy.orm import Session
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/create")
async def create_detail_akun(detail: DetailAkunCreate, db: Session = Depends(get_db)):
    """Create a new detail akun."""
    try:
        new_detail = DetailAkun(
            id_detail=detail.id_detail,
            id_akun=detail.id_akun,
            id_level_akses=detail.id_level_akses,
            nama_depan=detail.nama_depan,
            nama_belakang=detail.nama_belakang,
            nik=detail.nik,
            tempat_lahir=detail.tempat_lahir,
            tanggal_lahir=detail.tanggal_lahir,
            email=detail.email,
            no_telepon=detail.no_telepon,
            jenis_kelamin=detail.jenis_kelamin,
            agama=detail.agama,
            kewarganegaraan=detail.kewarganegaraan,
            provinsi=detail.provinsi,
            kabupaten=detail.kabupaten,
            kecamatan=detail.kecamatan,
            kelurahan=detail.kelurahan,
            jalan=detail.jalan,
            transportasi=detail.transportasi,
        )
        db.add(new_detail)
        db.commit()
        db.refresh(new_detail)
        logger.info(f"Success: Created detail akun '{detail.id_akun}'")
        return {"message": "Detail akun created"}
    except Exception as e:
        logger.error(f"Create detail akun failed: {str(e)}")
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/get/{id}", response_model=DetailAkunResponse)
async def get_detail_akun(id: str, db: Session = Depends(get_db)):
    """Get detail akun by ID."""
    try:
        detail = db.query(DetailAkun).filter(DetailAkun.id_akun == id).first()
        if detail:
            logger.info(f"Success: Retrieved detail akun '{id}'")
            return detail
    except Exception as e:
        logger.error(f"Get detail akun '{id}' failed: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
    logger.warning(f"Get failed: Detail akun '{id}' not found")
    raise HTTPException(status_code=404, detail="Detail akun not found")

@router.put("/update/{id}")
async def update_detail_akun(id: str, detail: DetailAkunCreate, db: Session = Depends(get_db)):
    """Update detail akun by ID."""
    try:
        existing = db.query(DetailAkun).filter(DetailAkun.id_akun == id).first()
        if not existing:
            logger.warning(f"Update failed: Detail akun '{id}' not found")
            raise HTTPException(status_code=404, detail="Detail akun not found")
        
        # Update fields using SQLAlchemy ORM
        existing.nama_depan = detail.nama_depan
        existing.nama_belakang = detail.nama_belakang # type: ignore
        existing.nik = detail.nik # type: ignore
        existing.tempat_lahir = detail.tempat_lahir # type: ignore
        existing.tanggal_lahir = detail.tanggal_lahir # type: ignore
        existing.email = detail.email # type: ignore
        existing.no_telepon = detail.no_telepon # type: ignore
        existing.jenis_kelamin = detail.jenis_kelamin # type: ignore
        existing.agama = detail.agama # type: ignore
        existing.kewarganegaraan = detail.kewarganegaraan # type: ignore
        existing.provinsi = detail.provinsi # type: ignore
        existing.kabupaten = detail.kabupaten # type: ignore
        existing.kecamatan = detail.kecamatan # type: ignore
        existing.kelurahan = detail.kelurahan # type: ignore
        existing.jalan = detail.jalan # type: ignore
        existing.transportasi = detail.transportasi # type: ignore
        db.commit()
        
        logger.info(f"Success: Updated detail akun '{id}'")
        return {"message": "Detail akun updated"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Update detail akun '{id}' failed: {str(e)}")
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/delete/{id}")
async def delete_detail_akun(id: str, db: Session = Depends(get_db)):
    """Delete detail akun by ID."""
    try:
        result = db.query(DetailAkun).filter(DetailAkun.id_akun == id).delete()
        if result:
            db.commit()
            logger.info(f"Success: Deleted detail akun '{id}'")
            return {"message": "Detail akun deleted"}
    except Exception as e:
        logger.error(f"Delete detail akun '{id}' failed: {str(e)}")
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    
    logger.warning(f"Delete failed: Detail akun '{id}' not found")
    raise HTTPException(status_code=404, detail="Detail akun not found")

@router.get("/getAll", response_model=list[DetailAkunResponse])
async def get_all_detail_akun(db: Session = Depends(get_db)):
    """Get all detail akun."""
    try:
        detail_list = db.query(DetailAkun).all()
        if detail_list:
            logger.info(f"Success: Retrieved {len(detail_list)} detail akun")
            return detail_list
    except Exception as e:
        logger.error(f"Get all detail akun failed: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    
    logger.warning("Get all detail akun: No records found")
    raise HTTPException(status_code=404, detail="No accounts found")
