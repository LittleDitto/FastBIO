from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Pydantic schemas for API request/response (NOT SQLAlchemy models)

class LevelAksesBase(BaseModel):
    id_level_akses: str
    hak_akses: str
    priority_akses: str

class LevelAksesCreate(LevelAksesBase):
    pass

class LevelAksesResponse(LevelAksesBase):
    class Config:
        from_attributes = True

class AkunBase(BaseModel):
    id_akun: str
    id_level_akses: str
    username: str

class AkunCreate(AkunBase):
    password: str

class AkunUpdate(BaseModel):
    id_level_akses: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None

class AkunResponse(AkunBase):
    class Config:
        from_attributes = True

class DetailAkunBase(BaseModel):
    id_detail: str
    id_akun: str
    id_level_akses: str
    nama_depan: str

class DetailAkunCreate(DetailAkunBase):
    nama_belakang: Optional[str] = None
    nik: Optional[str] = None
    tempat_lahir: Optional[str] = None
    tanggal_lahir: Optional[str] = None
    email: Optional[str] = None
    no_telepon: Optional[str] = None
    jenis_kelamin: Optional[str] = None
    agama: Optional[str] = None
    kewarganegaraan: Optional[str] = None
    provinsi: Optional[str] = None
    kabupaten: Optional[str] = None
    kecamatan: Optional[str] = None
    kelurahan: Optional[str] = None
    jalan: Optional[str] = None
    transportasi: Optional[str] = None

class DetailAkunUpdate(BaseModel):
    nama_depan: Optional[str] = None
    nama_belakang: Optional[str] = None
    nik: Optional[str] = None
    tempat_lahir: Optional[str] = None
    tanggal_lahir: Optional[str] = None
    email: Optional[str] = None
    no_telepon: Optional[str] = None
    jenis_kelamin: Optional[str] = None
    agama: Optional[str] = None
    kewarganegaraan: Optional[str] = None
    provinsi: Optional[str] = None
    kabupaten: Optional[str] = None
    kecamatan: Optional[str] = None
    kelurahan: Optional[str] = None
    jalan: Optional[str] = None
    transportasi: Optional[str] = None

class DetailAkunResponse(DetailAkunCreate):
    dibuat: Optional[datetime] = None
    
    class Config:
        from_attributes = True
