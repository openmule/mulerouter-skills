"""GPT Image 2 model endpoints."""

from .edit import ENDPOINT as EDIT_ENDPOINT
from .edit import GptImage2Edit
from .generation import ENDPOINT as GENERATION_ENDPOINT
from .generation import GptImage2Generation

__all__ = [
    "GENERATION_ENDPOINT",
    "EDIT_ENDPOINT",
    "GptImage2Generation",
    "GptImage2Edit",
]
