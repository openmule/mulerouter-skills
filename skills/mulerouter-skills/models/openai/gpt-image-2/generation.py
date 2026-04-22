"""GPT Image 2 Text-to-Image generation endpoint."""

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
    model_id="openai/gpt-image-2",
    action="generation",
    provider="openai",
    model_name="gpt-image-2",
    description="Generate images from text prompts using OpenAI GPT Image 2 model. Supports up to 4K resolution, multiple quality levels, and batch generation of up to 4 images.",
    input_types=[InputType.TEXT],
    output_type=OutputType.IMAGE,
    api_path="/vendors/openai/v1/gpt-image-2/generation",
    result_key="images",
    available_on=["mulerouter"],
    tags=["SOTA"],
    parameters=[
        ModelParameter(
            name="prompt",
            type="string",
            description="Text prompt to guide image generation",
            required=True,
        ),
        ModelParameter(
            name="quality",
            type="string",
            description="Image quality level",
            required=False,
            default="high",
            enum=["high", "medium", "low", "auto"],
        ),
        ModelParameter(
            name="size",
            type="string",
            description="Output image resolution",
            required=False,
            default="auto",
            enum=[
                "1024x1024",
                "1536x1024",
                "1024x1536",
                "2048x2048",
                "2048x1152",
                "3840x2160",
                "2160x3840",
                "auto",
            ],
        ),
        ModelParameter(
            name="n",
            type="integer",
            description="Number of images to generate (1-4)",
            required=False,
            default=1,
        ),
        ModelParameter(
            name="format",
            type="string",
            description="Output image format",
            required=False,
            default="png",
            enum=["png", "jpeg", "webp"],
        ),
    ],
)

register_endpoint(ENDPOINT)


class GptImage2Generation(BaseModelEndpoint):
    """GPT Image 2 text-to-image generation endpoint."""

    @property
    def endpoint_info(self) -> ModelEndpoint:
        return ENDPOINT


def main() -> int:
    """CLI entry point."""
    return GptImage2Generation().run()


if __name__ == "__main__":
    raise SystemExit(main())
