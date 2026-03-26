"""MiniMax Music 2.5 text-to-music generation endpoint."""

import argparse
import sys
from pathlib import Path
from typing import Any

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
    model_id="minimax/music-2.5",
    action="generation",
    provider="minimax",
    model_name="music-2.5",
    description="Latest music generation from style description and lyrics. Supports structure tags ([Intro], [Verse], [Chorus], [Bridge], [Outro]). Up to 5 minutes per song. $0.15/song.",
    input_types=[InputType.TEXT],
    output_type=OutputType.AUDIO,
    api_path="/vendors/minimax/v1/music-2.5/text-to-music/generation",
    result_key="audios",
    available_on=["mulerun"],
    parameters=[
        ModelParameter(
            name="prompt",
            type="string",
            description="A description of the music, specifying style, mood, and scenario (max 2000 characters). Optional for non-instrumental music.",
            required=False,
        ),
        ModelParameter(
            name="lyrics_prompt",
            type="string",
            description="Lyrics of the song (max 3000 characters). Use \\n to separate lines. Structure tags: [Intro], [Verse], [Chorus], [Bridge], [Outro]. Optional when lyrics_optimizer is true.",
            required=False,
        ),
        ModelParameter(
            name="lyrics_optimizer",
            type="boolean",
            description="Automatically generate lyrics based on prompt. When true and lyrics_prompt is empty, the system generates lyrics from prompt.",
            required=False,
            default=False,
        ),
        ModelParameter(
            name="audio_format",
            type="string",
            description="Audio file format",
            required=False,
            default="mp3",
            enum=["mp3", "pcm", "flac"],
        ),
        ModelParameter(
            name="sample_rate",
            type="integer",
            description="Sample rate of generated audio (Hz)",
            required=False,
            default=44100,
            enum=[8000, 16000, 22050, 24000, 32000, 44100],
        ),
        ModelParameter(
            name="bitrate",
            type="integer",
            description="Bitrate of generated audio (bps)",
            required=False,
            default=256000,
            enum=[32000, 64000, 128000, 256000],
        ),
    ],
)

# Register with global registry
register_endpoint(ENDPOINT)


class Music25Generation(BaseModelEndpoint):
    """MiniMax Music 2.5 text-to-music generation endpoint."""

    @property
    def endpoint_info(self) -> ModelEndpoint:
        return ENDPOINT

    def build_request_body(self, args: argparse.Namespace) -> dict[str, Any]:
        """Build request body with nested audio_setting object."""
        body: dict[str, Any] = {}

        if getattr(args, "prompt", None):
            body["prompt"] = args.prompt
        if getattr(args, "lyrics_prompt", None):
            body["lyrics_prompt"] = args.lyrics_prompt
        if getattr(args, "lyrics_optimizer", False):
            body["lyrics_optimizer"] = True

        # Build audio_setting
        audio_setting: dict[str, Any] = {}
        if getattr(args, "audio_format", None):
            audio_setting["format"] = args.audio_format
        if getattr(args, "sample_rate", None) is not None:
            audio_setting["sample_rate"] = args.sample_rate
        if getattr(args, "bitrate", None) is not None:
            audio_setting["bitrate"] = args.bitrate
        if audio_setting:
            body["audio_setting"] = audio_setting

        # Extra parameters
        if args.extra:
            for extra in args.extra:
                if "=" in extra:
                    key, value = extra.split("=", 1)
                    body[key] = value

        return body


def main() -> int:
    """CLI entry point."""
    return Music25Generation().run()


if __name__ == "__main__":
    raise SystemExit(main())
