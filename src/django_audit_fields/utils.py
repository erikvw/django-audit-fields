from datetime import datetime
from zoneinfo import ZoneInfo


def utcnow() -> datetime:
    return datetime.now().astimezone(ZoneInfo("UTC"))
