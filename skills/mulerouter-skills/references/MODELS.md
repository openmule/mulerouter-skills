# Model Reference

## Discovering Models

Run `python scripts/list_models.py` to see available models:

```bash
# List all models
python scripts/list_models.py

# Filter by provider
python scripts/list_models.py --provider alibaba

# Filter by output type
python scripts/list_models.py --output-type video

# JSON output
python scripts/list_models.py --json
```

## Model Categories

### Text-to-Image (T2I)

| Model | Path | Description |
|-------|------|-------------|
| Wan2.6 T2I | `models/alibaba/wan2.6-t2i/generation.py` | Flagship image generation |
| Wan2.5 T2I Preview | `models/alibaba/wan2.5-t2i-preview/generation.py` | Preview model |
| Nano Banana 2 | `models/google/nano-banana-2/generation.py` | 4K images, 14 aspect ratios, web search grounding |
| Nano Banana Pro | `models/google/nano-banana-pro/generation.py` | High-resolution images |
| Midjourney Diffusion | `models/midjourney/diffusion/generation.py` | Midjourney image generation |
| GPT Image 2 | `models/openai/gpt-image-2/generation.py` | OpenAI GPT Image 2, up to 4K resolution, multiple quality levels, batch up to 4 images (mulerouter only) |

### Text-to-Video (T2V)

| Model | Path | Description |
|-------|------|-------------|
| Wan2.6 T2V | `models/alibaba/wan2.6-t2v/generation.py` | Flagship video generation |
| Wan2.5 T2V Preview | `models/alibaba/wan2.5-t2v-preview/generation.py` | Preview model |
| Wan2.2 T2V Plus | `models/alibaba/wan2.2-t2v-plus/generation.py` | Previous generation |
| Veo 3 | `models/google/veo3/generation.py` | Google Veo 3 video generation (mulerun only) |
| Sora 2 | `models/openai/sora2/generation.py` | OpenAI Sora 2 video generation (mulerun only) |
| Kling V3 T2V | `models/klingai/kling-v3-t2v/generation.py` | Kling V3 text-to-video, 3-15s, sound & multi-shot |
| Kling V3 Omni T2V | `models/klingai/kling-v3-omni-t2v/generation.py` | Kling V3 Omni text-to-video, multi-shot, sound, element refs |

### Image-to-Video (I2V)

| Model | Path | Description |
|-------|------|-------------|
| Wan2.6 I2V | `models/alibaba/wan2.6-i2v/generation.py` | Flagship image animation |
| Wan2.5 I2V Preview | `models/alibaba/wan2.5-i2v-preview/generation.py` | Preview model |
| Wan2.2 I2V Plus | `models/alibaba/wan2.2-i2v-plus/generation.py` | High quality |
| Wan2.2 I2V Flash | `models/alibaba/wan2.2-i2v-flash/generation.py` | 50% faster |
| Veo 3 | `models/google/veo3/generation.py` | Google Veo 3 with image input (mulerun only) |
| Sora 2 | `models/openai/sora2/generation.py` | OpenAI Sora 2 with image input (mulerun only) |
| Midjourney Video | `models/midjourney/video/generation.py` | Image-to-video (prompt must include image URL) |
| Kling V3 I2V | `models/klingai/kling-v3-i2v/generation.py` | Kling V3 image-to-video, 3-15s, sound & multi-shot |
| Kling V3 Omni I2V | `models/klingai/kling-v3-omni-i2v/generation.py` | Kling V3 Omni image-to-video, multi-shot, sound |

### Reference-to-Video (Ref2V)

| Model | Path | Description |
|-------|------|-------------|
| Kling V3 Omni Ref2V | `models/klingai/kling-v3-omni-ref2v/generation.py` | Kling V3 Omni reference-to-video, style/character guidance |

### Video-to-Video (V2V)

| Model | Path | Description |
|-------|------|-------------|
| Kling V3 Omni V2V | `models/klingai/kling-v3-omni-v2v/generation.py` | Kling V3 Omni video-to-video, feature-guided generation |
| Kling V3 Omni V2V Edit | `models/klingai/kling-v3-omni-v2v-edit/generation.py` | Kling V3 Omni video editing, modify existing videos |

### Image-to-Image (I2I)

| Model | Path | Description |
|-------|------|-------------|
| Wan2.5 I2I Preview | `models/alibaba/wan2.5-i2i-preview/generation.py` | Image editing |
| Nano Banana 2 Edit | `models/google/nano-banana-2/edit.py` | Image editing, up to 14 reference images |
| Nano Banana Pro Edit | `models/google/nano-banana-pro/edit.py` | Image editing |
| GPT Image 2 Edit | `models/openai/gpt-image-2/edit.py` | Edit images with text prompts, multiple input images, optional mask for targeted edits, up to 4K (mulerouter only) |

### Advanced Video Editing

| Model | Path | Description |
|-------|------|-------------|
| Wan2.6 Image | `models/alibaba/wan2.6-image/generation.py` | Image processing |
| Wan2.1 VACE Plus | `models/alibaba/wan2.1-vace-plus/generation.py` | Video outpainting |
| Wan2.1 KF2V Plus | `models/alibaba/wan2.1-kf2v-plus/generation.py` | Keyframe interpolation |

### Text-to-Speech (TTS)

| Model | Path | Description |
|-------|------|-------------|
| MiniMax Speech 2.8 HD | `models/minimax/speech-2.8-hd/generation.py` | High-definition TTS, 37+ languages, voice emotions, $100/M chars |
| MiniMax Speech 2.8 Turbo | `models/minimax/speech-2.8-turbo/generation.py` | Fast affordable TTS, 37+ languages, voice emotions, $60/M chars |

### Text-to-Music (TTM)

| Model | Path | Description |
|-------|------|-------------|
| MiniMax Music 2.0 | `models/minimax/music-2.0/generation.py` | Music generation from lyrics and style, up to 5min, $0.03/song |
| MiniMax Music 2.5 | `models/minimax/music-2.5/generation.py` | Latest music generation from lyrics and style, up to 5min, $0.15/song |

## Checking Parameters

Before calling a model, use `--list-params`:

```bash
python models/alibaba/wan2.6-t2v/generation.py --list-params
```

Example output:

```
Parameters for alibaba/wan2.6-t2v generation:

Required:
  --prompt TEXT          Text description for video content (max 2000 chars)

Optional:
  --negative-prompt TEXT Unwanted content description
  --size TEXT            Resolution: 1280*720 (default), 1920*1080, etc.
  --duration INT         Duration: 5 (default), 10, or 15 seconds
  --seed INT             Random seed for reproducibility
```

## Common Parameters

| Parameter | Type | Models | Description |
|-----------|------|--------|-------------|
| `--prompt` | string | All | Content description (required) |
| `--negative-prompt` | string | Most | Unwanted content |
| `--size` | string | Video | Resolution (width*height) |
| `--resolution` | string | Some | 720P, 1080P, 2K |
| `--duration` | int | Video | Length in seconds |
| `--seed` | int | All | Reproducibility seed |
| `--image` | string | I2V/I2I | Input image URL |
| `--safety-filter` | boolean | All Wan | Enable safety content filtering (default: true) |
