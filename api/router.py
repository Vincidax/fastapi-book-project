from fastapi import APIRouter

from api.routes import books

api_router = APIRouter()
api_router.include_router(books.router, prefix="/books", tags=["books"])

# Define the /stage2 route to return 404
@api_router.get("/stage2")
async def override_stage2():
    raise HTTPException(status_code=404, detail="Not Found")