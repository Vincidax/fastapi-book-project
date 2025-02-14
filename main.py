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
    # Check if the stage2 has been merged or not
    if os.getenv("STAGE2_MERGED", "false") == "false":
        raise HTTPException(status_code=404, detail="Not Found")
    return {"message": "welcome to stage 2"}
