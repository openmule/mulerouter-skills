"""MiniMax Speech 2.8 HD text-to-speech generation endpoint."""

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
    model_id="minimax/speech-2.8-hd",
    action="generation",
    provider="minimax",
    model_name="speech-2.8-hd",
    description="High-definition text-to-speech generation. Supports pause tags, interjection tags, voice settings, 37+ languages. $100/million characters.",
    input_types=[InputType.TEXT],
    output_type=OutputType.AUDIO,
    api_path="/vendors/minimax/v1/speech-2.8-hd/text-to-speech/generation",
    result_key="audios",
    available_on=["mulerun"],
    parameters=[
        ModelParameter(
            name="prompt",
            type="string",
            description="Text to convert to speech (1-50000 characters). Supports pause tags <#x#> (x=0.01-99.99s) and interjection tags: (laughs), (sighs), (coughs), (clears throat), (gasps), (sniffs), (groans), (yawns).",
            required=True,
        ),
        ModelParameter(
            name="voice_id",
            type="string",
            description="Predefined voice ID (required). Examples - Chinese: male-qn-qingse, female-shaonv, female-yujie; English: Charming_Lady, Sweet_Girl, English_Trustworthy_Man; Japanese: Japanese_IntellectualSenior; Korean: Korean_SweetGirl. Full list: references/MINIMAX_VOICES.md",
            required=False,
        ),
        ModelParameter(
            name="speed",
            type="number",
            description="Speech speed, range [0.5, 2.0]",
            required=False,
            default=1.0,
        ),
        ModelParameter(
            name="vol",
            type="number",
            description="Volume, range [0.01, 10.0]",
            required=False,
            default=1.0,
        ),
        ModelParameter(
            name="pitch",
            type="integer",
            description="Voice pitch, range [-12, 12]",
            required=False,
            default=0,
        ),
        ModelParameter(
            name="emotion",
            type="string",
            description="Emotion of the generated speech",
            required=False,
            enum=["happy", "sad", "angry", "fearful", "disgusted", "surprised", "neutral"],
        ),
        ModelParameter(
            name="language_boost",
            type="string",
            description="Enhance recognition of specified language",
            required=False,
            enum=[
                "Chinese", "Chinese,Yue", "English", "Arabic", "Russian", "Spanish",
                "French", "Portuguese", "German", "Turkish", "Dutch", "Ukrainian",
                "Vietnamese", "Indonesian", "Japanese", "Italian", "Korean", "Thai",
                "Polish", "Romanian", "Greek", "Czech", "Finnish", "Hindi",
                "Bulgarian", "Danish", "Hebrew", "Malay", "Slovak", "Swedish",
                "Croatian", "Hungarian", "Norwegian", "Slovenian", "Catalan",
                "Nynorsk", "Afrikaans", "auto",
            ],
        ),
        ModelParameter(
            name="output_format",
            type="string",
            description="Format of the output: url (download link) or hex (hex-encoded audio data)",
            required=False,
            default="url",
            enum=["url", "hex"],
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
            default=32000,
            enum=[8000, 16000, 22050, 24000, 32000, 44100],
        ),
        ModelParameter(
            name="bitrate",
            type="integer",
            description="Bitrate of generated audio (bps)",
            required=False,
            default=128000,
            enum=[32000, 64000, 128000, 256000],
        ),
        ModelParameter(
            name="english_normalization",
            type="boolean",
            description="Enable English text normalization to improve number reading performance",
            required=False,
            default=False,
        ),
    ],
)

# Register with global registry
register_endpoint(ENDPOINT)


class Speech28HdGeneration(BaseModelEndpoint):
    """MiniMax Speech 2.8 HD text-to-speech generation endpoint."""

    @property
    def endpoint_info(self) -> ModelEndpoint:
        return ENDPOINT

    def build_request_body(self, args: argparse.Namespace) -> dict[str, Any]:
        """Build request body with nested voice_setting and audio_setting objects."""
        body: dict[str, Any] = {}

        if args.prompt:
            body["prompt"] = args.prompt

        # Build voice_setting
        voice_setting: dict[str, Any] = {}
        if getattr(args, "voice_id", None):
            voice_setting["voice_id"] = args.voice_id
        if getattr(args, "speed", None) is not None:
            voice_setting["speed"] = args.speed
        if getattr(args, "vol", None) is not None:
            voice_setting["vol"] = args.vol
        if getattr(args, "pitch", None) is not None:
            voice_setting["pitch"] = args.pitch
        if getattr(args, "emotion", None):
            voice_setting["emotion"] = args.emotion
        if getattr(args, "english_normalization", False):
            voice_setting["english_normalization"] = True
        if voice_setting:
            body["voice_setting"] = voice_setting

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

        # Top-level optional fields
        if getattr(args, "language_boost", None):
            body["language_boost"] = args.language_boost
        if getattr(args, "output_format", None):
            body["output_format"] = args.output_format

        # Extra parameters
        if args.extra:
            for extra in args.extra:
                if "=" in extra:
                    key, value = extra.split("=", 1)
                    body[key] = value

        return body


def main() -> int:
    """CLI entry point."""
    return Speech28HdGeneration().run()


if __name__ == "__main__":
    raise SystemExit(main())
