"""Kling V3 Omni Video-to-Video generation endpoint."""

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
    model_id="klingai/kling-v3-omni-v2v",
    action="generation",
    provider="klingai",
    model_name="kling-v3-omni-v2v",
    description="Generate new videos from reference videos using Kling V3 Omni model. Uses reference videos as feature guidance, requires prompt and video_list. Use @Video1 in prompt to reference videos",
    input_types=[InputType.VIDEO, InputType.TEXT],
    output_type=OutputType.VIDEO,
    api_path="/vendors/klingai/v1/kling-v3-omni/reference-video-to-video/generation",
    result_key="videos",
    available_on=["mulerouter", "mulerun"],
    tags=["SOTA"],
    parameters=[
        ModelParameter(
            name="prompt",
            type="string",
            description="Text description for video content (max 2500 characters). Required. Use @Video1 to reference videos from video_list. Use <<<element_1>>>, <<<element_2>>> etc. to reference elements by their index in elements",
            required=True,
        ),
        ModelParameter(
            name="negative_prompt",
            type="string",
            description="Negative prompt describing unwanted content (max 2500 characters)",
            required=False,
        ),
        ModelParameter(
            name="video_list",
            type="array",
            description='Reference video list (JSON array, required). Only 1 video allowed, duration must be at least 3s. Each item has: '
            '"video_url" (string, required, must be a URL); '
            '"refer_type" (must be "feature" for this endpoint); '
            '"keep_original_sound" ("yes" or "no", default "no"). '
            "Video constraints: mp4/mov, >=3s, 720-2160px, max 200MB. "
            'Example: \'[{"video_url":"https://example.com/video.mp4","refer_type":"feature","keep_original_sound":"no"}]\'',
            required=True,
        ),
        ModelParameter(
            name="first_frame",
            type="string",
            description="First-frame reference image (URL or Base64). Optional",
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
            "Total count of elements + images + first_frame + last_frame must not exceed 4. "
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
            description="Video aspect ratio. Not required; auto-inferred from reference video if not specified",
            required=False,
            enum=["16:9", "9:16", "1:1"],
        ),
        ModelParameter(
            name="duration",
            type="integer",
            description="Video duration in seconds (3-15). Not required; auto-inferred from reference video if not specified",
            required=False,
            default=5,
        ),
    ],
)

# Register with global registry
register_endpoint(ENDPOINT)


class KlingV3OmniV2VGeneration(BaseModelEndpoint):
    """Kling V3 Omni Video-to-Video generation endpoint."""

    @property
    def endpoint_info(self) -> ModelEndpoint:
        return ENDPOINT


def main() -> int:
    """CLI entry point."""
    return KlingV3OmniV2VGeneration().run()


if __name__ == "__main__":
    raise SystemExit(main())
