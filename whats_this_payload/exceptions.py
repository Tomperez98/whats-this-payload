"""Customed defined exceptions."""


from typing import Any


class NotIdentifiedPayloadError(Exception):
    """Raised when a payload couldn't been identified."""

    def __init__(self, payload: dict[Any, Any]) -> None:
        """Constructor."""
        super().__init__(
            "payload=`{payload}` couldn't been identified.".format(payload=payload)
        )
