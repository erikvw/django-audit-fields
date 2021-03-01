from datetime import datetime
from typing import Protocol
from uuid import UUID


class AuditModelStub(Protocol):
    id: UUID
    created: datetime
    modified: datetime
    user_created: str
    user_modified: str
    hostname_created: str
    hostname_modified: str
    device_created: str
    device_modified: str
