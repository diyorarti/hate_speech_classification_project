from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def home():
    return {"message":"Hate-Speech model API is running successfully 🚀"}