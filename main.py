import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from api.router import api_router
from core.config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_PREFIX)


@app.get("/healthcheck")
async def health_check():
    """Checks if server is active."""
    return {"status": "active"}

'''@app.get("/stage2")
async def stage2():
    return {"message": "welcome to stage 2"}
'''



@app.get("/stage2")
async def stage2():
    try:
        stage2_merged = os.getenv("STAGE2_MERGED", "false")
        if stage2_merged == "false":
            raise HTTPException(status_code=404, detail="Not Found")
        return {"message": "welcome to stage 2"}
    except Exception as e:
        # Log the error for easier debugging
        print(f"Error in /stage2: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
