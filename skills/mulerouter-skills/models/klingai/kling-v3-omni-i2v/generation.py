"""Kling V3 Omni Image-to-Video generation endpoint."""

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
    model_id="klingai/kling-v3-omni-i2v",
    action="generation",
    provider="klingai",
    model_name="kling-v3-omni-i2v",
    description="Generate videos from images using Kling V3 Omni model. Uses input image as starting frame, supports multi-shot, sound generation",
    input_types=[InputType.IMAGE, InputType.TEXT],
    output_type=OutputType.VIDEO,
    api_path="/vendors/klingai/v1/kling-v3-omni/image-to-video/generation",
    result_key="videos",
    available_on=["mulerouter", "mulerun"],
    tags=["SOTA"],
    parameters=[
        ModelParameter(
            name="first_frame",
            type="string",
            description="First-frame reference image (URL or Base64)",
            required=False,
        ),
        ModelParameter(
            name="last_frame",
            type="string",
            description="Last-frame reference image (URL or Base64). Requires first_frame; using last_frame alone is not supported",
            required=False,
        ),
        ModelParameter(
            name="prompt",
            type="string",
            description="Text description for video motion/story (max 2500 characters). Used for single-shot mode. Mutually exclusive with multi_prompt. Use <<<element_1>>>, <<<element_2>>> etc. to reference elements by their index in elements",
            required=False,
        ),
        ModelParameter(
            name="multi_prompt",
            type="array",
            description='Multi-shot prompt list (JSON array). Only effective when multi_shot=true and shot_type=customize. Each item has "prompt" (string, max 512 chars) and "duration" (integer, seconds). Max 6 shots. Total duration must equal the duration parameter. Example: \'[{"prompt":"scene 1","duration":5},{"prompt":"scene 2","duration":5}]\'',
            required=False,
        ),
        ModelParameter(
            name="negative_prompt",
            type="string",
            description="Negative prompt describing unwanted content (max 2500 characters)",
            required=False,
        ),
        ModelParameter(
            name="model_name",
            type="string",
            description="Model version identifier",
            required=False,
            default="kling-v3-omni",
            enum=["kling-v3-omni"],
        ),
        ModelParameter(
            name="sound",
            type="string",
            description="Enable sound generation in the video",
            required=False,
            default="off",
            enum=["off", "on"],
        ),
        ModelParameter(
            name="mode",
            type="string",
            description="Generation mode: std (standard) or pro (professional/high quality). Default is pro",
            required=False,
            default="pro",
            enum=["std", "pro"],
        ),
        ModelParameter(
            name="duration",
            type="integer",
            description="Video duration in seconds (3-15)",
            required=False,
            default=5,
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
            enum=["customize", "intelligence"],
        )
    ],
)

# Register with global registry
register_endpoint(ENDPOINT)


class KlingV3OmniI2VGeneration(BaseModelEndpoint):
    """Kling V3 Omni Image-to-Video generation endpoint."""

    @property
    def endpoint_info(self) -> ModelEndpoint:
        return ENDPOINT


def main() -> int:
    """CLI entry point."""
    return KlingV3OmniI2VGeneration().run()


if __name__ == "__main__":
    raise SystemExit(main())
