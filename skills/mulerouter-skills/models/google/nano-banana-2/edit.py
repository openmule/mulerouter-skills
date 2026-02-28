"""Nano Banana 2 Image-to-Image edit endpoint."""

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
    action="edit",
    provider="google",
    model_name="nano-banana-2",
    description="Edit images based on text prompts using Google Nano Banana 2 model. Supports up to 14 reference images (10 object + 4 character).",
    input_types=[InputType.IMAGE, InputType.TEXT],
    output_type=OutputType.IMAGE,
    api_path="/vendors/google/v1/nano-banana-2/edit",
    result_key="images",
    available_on=["mulerouter", "mulerun"],
    tags=["SOTA"],
    parameters=[
        ModelParameter(
            name="prompt",
            type="string",
            description="Text prompt for image editing",
            required=True,
        ),
        ModelParameter(
            name="images",
            type="array",
            description="List of reference images to edit (URLs or base64). Min 1, max 14 images (up to 10 object images + 4 character images)",
            required=True,
        ),
        ModelParameter(
            name="aspect_ratio",
            type="string",
            description="Aspect ratio of the edited image",
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


class NanaBanana2Edit(BaseModelEndpoint):
    """Nano Banana 2 image editing endpoint."""

    @property
    def endpoint_info(self) -> ModelEndpoint:
        return ENDPOINT


def main() -> int:
    """CLI entry point."""
    return NanaBanana2Edit().run()


if __name__ == "__main__":
    raise SystemExit(main())
