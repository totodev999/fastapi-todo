import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uuid

from utils.custom_formatter import request_id_var, method_var, url_var, get_app_logger
from routers.todos_router import router as todos_router

logger = get_app_logger()
app = FastAPI()


@app.middleware("http")
async def logging_middleware(request: Request, call_next):
    request_id_var.set(str(uuid.uuid4()))
    method_var.set(request.method)
    url_var.set(str(request.url.path))

    logger.info("access start")
    response = await call_next(request)
    logger.info("access end")
    return response


@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    logger.error(f"error occurred: {str(exc)}")
    return JSONResponse(
        status_code=500, content={"message": "Sorry something went wrong!"}
    )


app.include_router(todos_router)


def main():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, access_log=False)


if __name__ == "__main__":
    main()
