import uvicorn
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
import uuid

from utils.custom_formatter import request_id_var, method_var, url_var, app_logger
from routers.todos_router import router as todos_router
from classes.errors.DB import DBCommonException

app = FastAPI()


@app.middleware("http")
async def logging_middleware(request: Request, call_next):
    request_id_var.set(str(uuid.uuid4()))
    method_var.set(request.method)
    url_var.set(str(request.url.path))

    app_logger.info("access start")
    response = await call_next(request)
    app_logger.info(f"access end status_code:{response.status_code}")
    return response


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors: list[dict] = exc.errors()
    formatted_errors = []
    for error in errors:
        formatted_errors.append(
            {
                "field": ".".join(error.get("loc")),
                "message": error.get("msg"),
                "type": error.get("type"),
            }
        )
    app_logger.info(f"Bad request: {str(exc)}")
    return JSONResponse(
        status_code=400, content={"message": "Bad Request", "detail": formatted_errors}
    )


@app.exception_handler(DBCommonException)
async def db_exception_handler(request: Request, exc: DBCommonException):
    app_logger.error("db error occurred")
    return JSONResponse(
        status_code=500, content={"message": "Sorry something went wrong!"}
    )


@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    app_logger.error(f"error occurred: {str(exc)}")
    return JSONResponse(
        status_code=500, content={"message": "Sorry something went wrong!"}
    )


app.include_router(todos_router)


def main():
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, access_log=False)


if __name__ == "__main__":
    main()
