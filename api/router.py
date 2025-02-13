from fastapi import APIRouter

from api.routes import books

api_router = APIRouter()

# Add the /stage2 route
@api_router.get("/stage2")
async def stage2_override():
    return {"message": "Not Found"}, 404

api_router.include_router(books.router, prefix="/books", tags=["books"])
