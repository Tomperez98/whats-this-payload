"""Customed defined exceptions."""


from typing import Any


class NotIdentifiedPayloadError(Exception):
    """Raised when a payload couldn't been identified."""

    def __init__(self, payload: dict[Any, Any]) -> None:
        """Constructor."""
        super().__init__(
            "payload=`{payload}` couldn't been identified.".format(payload=payload)
        )


class NotSupportedWebhookError(Exception):
    """Raised when a requested identifier is not supported."""

    def __init__(self, webhook: str) -> None:
        """Constructor."""
        super().__init__(
            "Webhook {webhook} is not supported yet.".format(webhook=webhook)
        )
