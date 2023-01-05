"""Base handler to implement a chain of responsability."""
import abc
from typing import Any, TypeVar, Union

from whats_this_payload.base.payload_type import BasePayloadType

THandler = TypeVar("THandler", bound="BaseHandler")


class BaseHandler(abc.ABC):
    """Base handler class."""

    _next_handler: Union["BaseHandler", None] = None

    def set_next_handler(self, handler: THandler) -> THandler:
        """Set next handler in the responsability chain."""
        self._next_handler = handler
        return handler

    @abc.abstractmethod
    def handle(self, payload: dict[Any, Any]) -> BasePayloadType | None:
        """Evaluate the payload type."""
        if self._next_handler:
            return self._next_handler.handle(payload=payload)

        return None
