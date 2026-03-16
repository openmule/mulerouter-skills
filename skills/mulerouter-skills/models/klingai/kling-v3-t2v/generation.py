"""Kling V3 Text-to-Video generation endpoint."""

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
    model_id="klingai/kling-v3-t2v",
    action="generation",
    provider="klingai",
    model_name="kling-v3-t2v",
    description="Generate videos from text prompts using Kling V3 model. Supports 3-15s duration, sound generation, multi-shot mode.",
    input_types=[InputType.TEXT],
    output_type=OutputType.VIDEO,
    api_path="/vendors/klingai/v1/kling-v3/text-to-video/generation",
    result_key="videos",
    available_on=["mulerouter", "mulerun"],
    tags=["SOTA"],
    parameters=[
        ModelParameter(
            name="prompt",
            type="string",
            description="Text description for video content (max 2500 characters). Used for single-shot mode. Mutually exclusive with multi_prompt.",
            required=False,
        ),
        ModelParameter(
            name="negative_prompt",
            type="string",
            description="Negative prompt describing unwanted content (max 2500 characters)",
            required=False,
        ),
        ModelParameter(
            name="mode",
            type="string",
            description="Generation mode: std (standard/economy) or pro (high quality)",
            required=False,
            default="std",
            enum=["std", "pro"],
        ),
        ModelParameter(
            name="multi_shot",
            type="string",
            description="Enable multi-shot mode for multi-scene video generation",
            required=False,
            default="false",
            enum=["false", "true"],
        ),
        ModelParameter(
            name="shot_type",
            type="string",
            description="Shot type when multi_shot is true: customize (manual) or intelligence (auto)",
            required=False,
            default="customize",
            enum=["customize", "intelligence"],
        ),
        ModelParameter(
            name="multi_prompt",
            type="array",
            description='Multi-shot prompt list (JSON array). Required when multi_shot=true and shot_type=customize. Each item has "prompt" (string) and "duration" (string, seconds). Total duration must equal the duration parameter. Example: \'[{"prompt":"scene 1","duration":"5"},{"prompt":"scene 2","duration":"5"}]\'',
            required=False,
        ),
        ModelParameter(
            name="aspect_ratio",
            type="string",
            description="Video aspect ratio",
            required=False,
            default="16:9",
            enum=["16:9", "9:16", "1:1"],
        ),
        ModelParameter(
            name="duration",
            type="integer",
            description="Video duration in seconds (3-15)",
            required=False,
            default=5,
        ),
        ModelParameter(
            name="sound",
            type="string",
            description="Enable sound generation in the video",
            required=False,
            default="off",
            enum=["off", "on"],
        )
    ],
)

# Register with global registry
register_endpoint(ENDPOINT)


class KlingV3T2VGeneration(BaseModelEndpoint):
    """Kling V3 Text-to-Video generation endpoint."""

    @property
    def endpoint_info(self) -> ModelEndpoint:
        return ENDPOINT


def main() -> int:
    """CLI entry point."""
    return KlingV3T2VGeneration().run()


if __name__ == "__main__":
    raise SystemExit(main())
