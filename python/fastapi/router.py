from fastapi import APIRouter

import google

router = APIRouter()
router.include_router(google.router)
