import logging
from fastapi import FastAPI
from app.routers.akun import router as akun_router
from app.routers.level_akses import router as level_akses_router
from app.routers.detail_akun import router as detail_akun_router
from app.routers.auth import router as auth_router

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Atau tambahkan URL frontend spesifik
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(level_akses_router, prefix="/level-akses", tags=["Level Akses"])
app.include_router(akun_router, prefix="/akun", tags=["Akun"])
app.include_router(detail_akun_router, prefix="/detail-akun", tags=["Detail Akun"])
app.include_router(auth_router, prefix="/auth",tags=["Auth"])

@app.get("/")
async def root():
    return {"message": "Welcome to the API"}
