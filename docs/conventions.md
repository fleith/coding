# Conventions

## Code
- Keep functions pure when possible.
- Prefer clear names over compact syntax.
- Avoid hidden global state.

## File Naming
- Algorithms: `snake_case.py`
- Tests: `test_<module>.py`

## Tests
- Include at least:
  - empty input
  - single element
  - duplicates
  - already sorted (if applicable)
  - reverse sorted (if applicable)

## Complexity Notes
Each module should include:
- Time complexity
- Space complexity
- Stability (for sorting algorithms)
