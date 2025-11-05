from fastapi import APIRouter
import os

router=APIRouter()

@router.get('/task')
def taskRoute():
    return {f"Task Route Reached: {os.getenv('TEST_MSG')}"}