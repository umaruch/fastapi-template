from fastapi import Request, status
from fastapi.responses import JSONResponse

async def handle_validation_error(req: Request, err: Exception):
    pass
