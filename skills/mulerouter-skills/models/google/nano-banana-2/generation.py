"""Nano Banana 2 Text-to-Image generation endpoint."""

import sys
from pathlib import Path

# Support both direct execution and package import
_file_dir = Path(__file__).parent
_models_dir = _file_dir.parent.parent
_root_dir = _models_dir.parent

if str(_root_dir) not in sys.path:
    sys.path.insert(0, str(_root_dir))

from core import InputType, ModelEndpoint, ModelParameter, OutputType, register_endpoint
from models.base import BaseModelEndpoint

# Define the endpoint
ENDPOINT = ModelEndpoint(
    model_id="google/nano-banana-2",
    action="generation",
    provider="google",
    model_name="nano-banana-2",
    description="Generate images from text prompts using Google Nano Banana 2 model (Gemini 3.1 Flash Image Preview). Supports up to 4K resolution and 14 aspect ratios.",
    input_types=[InputType.TEXT],
    output_type=OutputType.IMAGE,
    api_path="/vendors/google/v1/nano-banana-2/generation",
    result_key="images",
    available_on=["mulerouter", "mulerun"],
    tags=["SOTA"],
    parameters=[
        ModelParameter(
            name="prompt",
            type="string",
            description="Text prompt for image generation",
            required=True,
        ),
        ModelParameter(
            name="aspect_ratio",
            type="string",
            description="Aspect ratio of the generated image",
            required=False,
            default="1:1",
            enum=[
                "1:1",
                "1:4",
                "1:8",
                "2:3",
                "3:2",
                "3:4",
                "4:1",
                "4:3",
                "4:5",
                "5:4",
                "8:1",
                "9:16",
                "16:9",
                "21:9",
            ],
        ),
        ModelParameter(
            name="resolution",
            type="string",
            description="Output resolution preset (must use uppercase K, e.g. 1K, 2K, 4K)",
            required=False,
            default="1K",
            enum=["1K", "2K", "4K"],
        ),
        ModelParameter(
            name="web_search",
            type="boolean",
            description="Enable Google Search grounding for real-time data and accurate depictions of real-world subjects",
            required=False,
            default=False,
        ),
    ],
)

register_endpoint(ENDPOINT)


class NanaBanana2Generation(BaseModelEndpoint):
    """Nano Banana 2 text-to-image generation endpoint."""

    @property
    def endpoint_info(self) -> ModelEndpoint:
        return ENDPOINT


def main() -> int:
    """CLI entry point."""
    return NanaBanana2Generation().run()


if __name__ == "__main__":
    raise SystemExit(main())
