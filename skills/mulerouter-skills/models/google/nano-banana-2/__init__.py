"""Nano Banana 2 model endpoints."""

from .edit import ENDPOINT as EDIT_ENDPOINT
from .edit import NanaBanana2Edit
from .generation import ENDPOINT as GENERATION_ENDPOINT
from .generation import NanaBanana2Generation

__all__ = [
    "GENERATION_ENDPOINT",
    "EDIT_ENDPOINT",
    "NanaBanana2Generation",
    "NanaBanana2Edit",
]
