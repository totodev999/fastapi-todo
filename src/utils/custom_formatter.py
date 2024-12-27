import logging
import logging.config
from contextvars import ContextVar

request_id_var = ContextVar("request_id", default="")
method_var = ContextVar("method", default="")
url_var = ContextVar("url", default="")


class SingleLineFormatter(logging.Formatter):
    """
    Fomtter for all logger
    [YYYY-MM-DD hh:mm:ss]-[loglevel]-[request_id]-[method]-[request_url]-message
    """

    def format(self, record: logging.LogRecord) -> str:
        request_id = request_id_var.get("")
        method = method_var.get("")
        url = url_var.get("")

        from datetime import datetime

        asctime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        loglevel = record.levelname
        # replace newline with space to log in a single line
        message = record.getMessage().replace("\n", " ")

        # log stacktrace if exists
        if record.exc_info:
            stacktrace = super().formatException(record.exc_info)
            stacktrace = stacktrace
            message = f"{message} {stacktrace}"

        return f"[{asctime}]-[{loglevel}]-[{request_id}]-[{method}]-[{url}]-{message}"


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "single_line": {
            "()": SingleLineFormatter,
        },
    },
    "handlers": {
        "console": {
            # log something in standard output(console)
            "class": "logging.StreamHandler",
            "formatter": "single_line",
        },
    },
    "loggers": {
        # if some libraries which I don't know try to log, this root logger will catch it
        "": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": True,
        },
        "sqlalchemy.engine.Engine": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False,
        },
        "uvicorn": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False,
        },
        "uvicorn.error": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False,
        },
        "uvicorn.access": {
            "level": "WARNING",
            "handlers": ["console"],
            "propagate": False,
        },
        "app_logger": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False,
        },
    },
}


def get_app_logger():
    logging.config.dictConfig(LOGGING_CONFIG)
    return logging.getLogger("app_logger")


app_logger = get_app_logger()
