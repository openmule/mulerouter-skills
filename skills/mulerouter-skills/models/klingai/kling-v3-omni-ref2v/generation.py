"""Kling V3 Omni Reference-to-Video generation endpoint."""

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
    model_id="klingai/kling-v3-omni-ref2v",
    action="generation",
    provider="klingai",
    model_name="kling-v3-omni-ref2v",
    description="Generate videos from reference images/elements using Kling V3 Omni model. Uses reference images and elements as style/character guidance, supports multi-shot and sound generation",
    input_types=[InputType.IMAGE, InputType.TEXT],
    output_type=OutputType.VIDEO,
    api_path="/vendors/klingai/v1/kling-v3-omni/reference-image-to-video/generation",
    result_key="videos",
    available_on=["mulerouter", "mulerun"],
    tags=["SOTA"],
    parameters=[
        ModelParameter(
            name="prompt",
            type="string",
            description="Text description for video content (max 2500 characters). Used for single-shot mode. Mutually exclusive with multi_prompt. Use <<<element_1>>>, <<<element_2>>> etc. to reference elements by their index in elements",
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
            name="first_frame",
            type="string",
            description="First-frame reference image (URL or Base64)",
            required=False,
        ),
        ModelParameter(
            name="last_frame",
            type="string",
            description="Last-frame reference image (URL or Base64). Requires first_frame; using last_frame alone is not supported. Not supported when images has more than 1 image and first_frame is set",
            required=False,
        ),
        ModelParameter(
            name="images",
            type="array",
            description="Reference images list (JSON array of URL/Base64 strings) for style/appearance guidance. Note: when images has more than 1 image and first_frame is set, last_frame is not supported",
            required=False,
        ),
        ModelParameter(
            name="elements",
            type="array",
            description='Element list (JSON array) for subject/character references. '
            "Total count of elements + images + first_frame + last_frame must not exceed 7. "
            "Use <<<element_1>>>, <<<element_2>>>, etc. in prompt to reference them by index order. "
            "Each item requires: "
            '"type" ("image" or "video"); '
            'For image type: "frontal_image" (required, exactly 1, URL or Base64) and "reference_images" (required, array of 1-3 URLs or Base64); '
            'For video type: "reference_videos" (list of video URLs). '
            "Example: '[{\"type\":\"image\",\"frontal_image\":\"https://example.com/face.jpg\",\"reference_images\":[\"https://example.com/side.jpg\"]}]'",
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
            name="aspect_ratio",
            type="string",
            description="Video aspect ratio. Default 16:9",
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
        ),
    ],
)

# Register with global registry
register_endpoint(ENDPOINT)


class KlingV3OmniRef2VGeneration(BaseModelEndpoint):
    """Kling V3 Omni Reference-to-Video generation endpoint."""

    @property
    def endpoint_info(self) -> ModelEndpoint:
        return ENDPOINT


def main() -> int:
    """CLI entry point."""
    return KlingV3OmniRef2VGeneration().run()


if __name__ == "__main__":
    raise SystemExit(main())
