# Coding Interview Practice

Repository for learning and practicing data structures and algorithms in Python.

## Goals
- Keep implementations simple and interview-friendly.
- Track learning progress by topic.
- Run consistently on Windows, Linux, and macOS.

## Project Structure

```text
coding/
  docs/                    # Roadmap and study notes
  src/
    algorithms/
      sorting/             # Bubble, quick, merge, heap sort
      legacy/              # Older algorithms kept for reference
    data_structures/
      legacy/              # Older implementations kept for reference
  tests/                   # Test suite (pytest)
  problems/                # Practice problems (ctci, interview, misc)
  playground/              # Experiments and scratch code
  .github/workflows/       # CI workflows
```

## Quick Start

1. Create and activate a virtual environment.

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Linux/macOS (bash/zsh):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies.

```bash
python -m pip install -r requirements.txt
```

3. Run tests.

```bash
python -m pytest
```

## Learning Path
- Start with sorting in `src/algorithms/sorting`.
- Add one new algorithm/data structure at a time.
- Add matching tests under `tests/`.
- Update `docs/roadmap.md` as progress changes.
