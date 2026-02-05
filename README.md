# MuleRouter Agent Skill

Agent Skill for calling MuleRouter / MuleRun multimodal APIs to generate images and videos.

## Features

- **Multiple Sites**: Supports both [MuleRouter](https://mulerouter.ai) and [MuleRun](https://mulerun.com) APIs
- **Various Models**: Wan2.6 series (T2V, I2V, T2I, Image), Nano Banana Pro and more
- **Easy Configuration**: Environment variables or .env file
- **Async Task Handling**: Automatic polling for long-running tasks
- **AI-Friendly**: Clear parameter documentation via `--list-params`

## Installation

### Install By Claude Code Plugin

#### Install via CLI

```bash
claude plugin marketplace add openmule/mulerouter-skills
claude plugin install mulerouter-skills
```

#### Install via Claude Code

In a Claude Code session:

```bash
/plugin marketplace add openmule/mulerouter-skills
/plugin install mulerouter-skills
```

After installation, **RESTART Claude Code** to load the new skill.

## Configuration

### Required Environment Variables

| Variable | Description |
|----------|-------------|
| `MULEROUTER_API_KEY` | API key for authentication |

### API Endpoint Configuration (one required)

| Variable | Description | Priority |
|----------|-------------|----------|
| `MULEROUTER_BASE_URL` | Custom API base URL (e.g., `https://api.mulerouter.ai`) | Higher |
| `MULEROUTER_SITE` | API site: `mulerouter` or `mulerun` | Lower |

**Note:** `MULEROUTER_BASE_URL` takes priority over `MULEROUTER_SITE`. If both are set, `MULEROUTER_BASE_URL` is used.

Get your API key on the [MuleRouter website](https://www.mulerouter.ai/app/api-keys?utm_source=github_claude_plugin)

### Option 1: Environment Variables (with custom base URL)

```bash
export MULEROUTER_BASE_URL="https://api.mulerouter.ai"
export MULEROUTER_API_KEY="your-api-key"
```

### Option 2: Environment Variables (with site)

```bash
export MULEROUTER_SITE="mulerouter"      # or "mulerun"
export MULEROUTER_API_KEY="your-api-key"
```

### Option 3: .env File

Create a `.env` file in your skill directory:

```env
# Option 1: Use custom base URL (takes priority)
MULEROUTER_BASE_URL=https://api.mulerouter.ai
MULEROUTER_API_KEY=your-api-key-here

# Option 2: Use site (if BASE_URL not set)
# MULEROUTER_SITE=mulerun
# MULEROUTER_API_KEY=your-api-key-here
```

**Note:** The tool only reads `.env` from the current working directory. Always run scripts from the skill root.

### Verify Configuration

```bash
# Check environment variables
echo "MULEROUTER_BASE_URL: $MULEROUTER_BASE_URL"
echo "MULEROUTER_SITE: $MULEROUTER_SITE"
echo "MULEROUTER_API_KEY: ${MULEROUTER_API_KEY:+[SET]}"

# Check for .env file
ls -la .env 2>/dev/null || echo "No .env in current directory"
```

## Quick Start

Let Claude Code run `/mulerouter-skills:mulerouter-skills` to use the skill.

Or just ask Claude to use MuleRouter to generate some images or videos.

## Project Structure

```
skills/mulerouter/
├── SKILL.md              # Agent skill entry point
├── scripts/              # Utility scripts
│   └── list_models.py    # Model listing utility
├── models/               # Model endpoints (executable)
├── core/                 # Core infrastructure
│   ├── config.py         # Configuration management
│   ├── client.py         # HTTP client
│   ├── registry.py       # Model registry
│   └── task.py           # Task polling
├── references/           # Documentation
│   ├── REFERENCE.md      # API reference
│   └── MODELS.md         # Model specifications
└── tests/                # Unit tests
```

## CLI Options

All model scripts support:

| Option | Description |
|--------|-------------|
| `--api-key KEY` | Override API key |
| `--base-url URL` | Override base URL (takes priority over --site) |
| `--site SITE` | Override site (mulerouter/mulerun) |
| `--json` | Output as JSON |
| `--list-params` | Show parameters and exit |
| `--no-wait` | Don't wait for task completion |
| `--quiet` | Suppress progress output |

## Development

### Format and Lint

```bash
uv run ruff format .
uv run ruff check --fix .
```

### Run Tests

```bash
uv run pytest
```

## License

MIT
