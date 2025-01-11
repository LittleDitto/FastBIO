from pydantic import BaseModel
from datetime import datetime

class LevelAkses(BaseModel):
    id_level_akses: str
    hak_akses: str
    priority_akses: str

class Akun(BaseModel):
    id_akun: str
    id_level_akses: str
    username: str
    password: str

class DetailAkun(BaseModel):
    id_detail: str
    id_akun: str
    id_level_akses: str
    nama_depan: str
    nama_belakang: str
    nik: str
    tempat_lahir: str
    tanggal_lahir: str
    email: str
    no_telepon: str
    jenis_kelamin: str
    agama: str
    kewarganegaraan: str
    provinsi: str
    kabupaten: str
    kecamatan: str
    kelurahan: str
    jalan: str
    transportasi: str
    dibuat: datetime
