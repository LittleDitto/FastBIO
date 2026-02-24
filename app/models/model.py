from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.sql import func

class Base(DeclarativeBase):
    pass

class LevelAkses(Base):
    __tablename__ = "level_akses"
    
    id_level_akses: Mapped[str] = mapped_column(String, primary_key=True)
    hak_akses: Mapped[str] = mapped_column(String, nullable=False)
    priority_akses: Mapped[str] = mapped_column(String, nullable=False)

class Akun(Base):
    __tablename__ = "akun"
    
    id_akun: Mapped[str] = mapped_column(String, primary_key=True)
    id_level_akses: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)

class DetailAkun(Base):
    __tablename__ = "detail_akun"
    
    id_detail: Mapped[str] = mapped_column(String, primary_key=True)
    id_akun: Mapped[str] = mapped_column(String, nullable=False)
    id_level_akses: Mapped[str] = mapped_column(String, nullable=False)
    nama_depan: Mapped[str] = mapped_column(String, nullable=False)
    nama_belakang: Mapped[str] = mapped_column(String, nullable=True)
    nik: Mapped[str] = mapped_column(String, nullable=True)
    tempat_lahir: Mapped[str] = mapped_column(String, nullable=True)
    tanggal_lahir: Mapped[str] = mapped_column(String, nullable=True)
    email: Mapped[str] = mapped_column(String, nullable=True)
    no_telepon: Mapped[str] = mapped_column(String, nullable=True)
    jenis_kelamin: Mapped[str] = mapped_column(String, nullable=True)
    agama: Mapped[str] = mapped_column(String, nullable=True)
    kewarganegaraan: Mapped[str] = mapped_column(String, nullable=True)
    provinsi: Mapped[str] = mapped_column(String, nullable=True)
    kabupaten: Mapped[str] = mapped_column(String, nullable=True)
    kecamatan: Mapped[str] = mapped_column(String, nullable=True)
    kelurahan: Mapped[str] = mapped_column(String, nullable=True)
    jalan: Mapped[str] = mapped_column(String, nullable=True)
    transportasi: Mapped[str] = mapped_column(String, nullable=True)
    dibuat: Mapped[func] = mapped_column(DateTime, default=func.now()) # type: ignore
