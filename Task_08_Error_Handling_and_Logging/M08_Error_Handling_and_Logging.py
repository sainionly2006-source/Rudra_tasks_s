"""Structured local logging for sensor processing events."""
import json
import logging
from datetime import datetime, timezone

def configure_logger(log_file="sensor_processing.log", level=logging.INFO):
    logger = logging.getLogger("rudraedge")
    logger.setLevel(level)
    logger.propagate = False
    if not logger.handlers:
        handler = logging.FileHandler(log_file, encoding="utf-8")
        handler.setFormatter(logging.Formatter("%(message)s"))
        logger.addHandler(handler)
    return logger

def log_event(logger, event, **details):
    record = {
        "time": datetime.now(timezone.utc).isoformat(),
        "event": event,
        **details
    }
    logger.info(json.dumps(record, ensure_ascii=False, default=str))
