"""Happy Horse 1.0 Text-to-Video generation endpoint."""

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
    model_id="alibaba/happy-horse-1-0-t2v",
    action="generation",
    provider="alibaba",
    model_name="happy-horse-1-0-t2v",
    description="Generate videos from text prompts using Happy Horse 1.0 Text-to-Video model",
    input_types=[InputType.TEXT],
    output_type=OutputType.VIDEO,
    api_path="/vendors/alibaba/v1/happy-horse-1-0-t2v/generation",
    result_key="videos",
    available_on=["mulerouter", "mulerun"],
    parameters=[
        ModelParameter(
            name="prompt",
            type="string",
            description="Text description for video content (max 2500 characters)",
            required=True,
        ),
        ModelParameter(
            name="resolution",
            type="string",
            description="Output video resolution",
            required=False,
            default="1080P",
            enum=["720P", "1080P"],
        ),
        ModelParameter(
            name="duration",
            type="integer",
            description="Video duration in seconds (3-15)",
            required=False,
            default=5,
        ),
        ModelParameter(
            name="seed",
            type="integer",
            description="Random seed for reproducibility (omit for auto-generated seed)",
            required=False,
        ),
    ],
)

# Register with global registry
register_endpoint(ENDPOINT)


class HappyHorse10T2VGeneration(BaseModelEndpoint):
    """Happy Horse 1.0 Text-to-Video generation endpoint."""

    @property
    def endpoint_info(self) -> ModelEndpoint:
        return ENDPOINT


def main() -> int:
    """CLI entry point."""
    return HappyHorse10T2VGeneration().run()


if __name__ == "__main__":
    raise SystemExit(main())
