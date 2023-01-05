"""Identifier interface."""
import abc
from typing import Any

from whats_this_payload.base.payload_type import BasePayloadType


class BaseIdentifier(abc.ABC):
    """Abstract class for identifier classes in charge of identify payload types."""

    @abc.abstractmethod
    def __init__(self, payload: dict[Any, Any]) -> None:
        """Constructor definition."""

    @abc.abstractmethod
    def identify_payload_type(self) -> BasePayloadType:
        """Handle the process of identify payload type based on received payload."""
