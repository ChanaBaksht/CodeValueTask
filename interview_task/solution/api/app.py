from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from solution import globals

app = FastAPI()
router = APIRouter(prefix="/solution", tags=["solution"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=globals.ORIGIN,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
