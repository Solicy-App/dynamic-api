from __future__ import annotations

from dataclasses import dataclass
from dataclasses_json import dataclass_json

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    _ = object


@dataclass_json
@dataclass
class Response(dict):
    success: bool
    message: str
    status: int = 200
    data: _ = object()

    def serialize(self):
        return {
            'success': self.success,
            'message': self.message,
            'status': self.status,
            'data': self.data,
        }
