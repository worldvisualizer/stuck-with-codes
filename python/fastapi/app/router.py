from fastapi import APIRouter

import app.google as google

router = APIRouter()
router.include_router(google.router)
