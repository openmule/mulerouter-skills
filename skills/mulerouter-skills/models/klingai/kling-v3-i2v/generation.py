"""Kling V3 Image-to-Video generation endpoint."""

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
    model_id="klingai/kling-v3-i2v",
    action="generation",
    provider="klingai",
    model_name="kling-v3-i2v",
    description="Generate videos from images using Kling V3 model. Supports 3-15s duration, sound generation, multi-shot mode, and element references",
    input_types=[InputType.IMAGE, InputType.TEXT],
    output_type=OutputType.VIDEO,
    api_path="/vendors/klingai/v1/kling-v3/image-to-video/generation",
    result_key="videos",
    available_on=["mulerouter", "mulerun"],
    tags=["SOTA"],
    parameters=[
        ModelParameter(
            name="first_frame",
            type="string",
            description="First-frame reference image (URL, Base64, or local path). Must be <10MB, at least 300x300px, aspect ratio 1:2.5~2.5:1",
            required=True,
        ),
        ModelParameter(
            name="last_frame",
            type="string",
            description="End frame reference image (URL, Base64, or local path). Optional",
            required=False,
        ),
        ModelParameter(
            name="elements",
            type="array",
            description='Element list (JSON array) for subject/character references, max 3 elements. '
            "Use <<<element_1>>>, <<<element_2>>>, etc. in prompt to reference them by index order. "
            "Each item requires: "
            '"type" ("image" or "video"); '
            'For image type: "frontal_image" (required, exactly 1, URL or Base64, jpg/png <=10MB >=300px) and "reference_images" (required, array of 1-3 URLs or Base64); '
            'For video type: "reference_videos" (list of video URLs). '
            "Example: '[{\"type\":\"image\",\"frontal_image\":\"https://example.com/face.jpg\",\"reference_images\":[\"https://example.com/side.jpg\"]}]'",
            required=False,
        ),
        ModelParameter(
            name="prompt",
            type="string",
            description="Motion/story description for the video (max 2500 characters). Use <<<element_1>>>, <<<element_2>>> etc. to reference elements by their index in elements. Used for single-shot mode. Either prompt or multi-shot must be used",
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
        ),
    ],
)

# Register with global registry
register_endpoint(ENDPOINT)


class KlingV3I2VGeneration(BaseModelEndpoint):
    """Kling V3 Image-to-Video generation endpoint."""

    @property
    def endpoint_info(self) -> ModelEndpoint:
        return ENDPOINT


def main() -> int:
    """CLI entry point."""
    return KlingV3I2VGeneration().run()


if __name__ == "__main__":
    raise SystemExit(main())
