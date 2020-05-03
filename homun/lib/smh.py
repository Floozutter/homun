"""
Expand an smh!
"""

from functools import reduce


REPLACEMENTS = {
    "smh": "smh my head",
    "smH": "smH my Head",
    "sMh": "sMh My head",
    "sMH": "sMH My Head",
    "Smh": "Smh my head",
    "SmH": "SmH my Head",
    "SMh": "SMh My head",
    "SMH": "SMH My Head"
}

def expand(text: str, depth: int = 1) -> str:
    """Expands all occurrences of "smh" in the argument text."""
    if depth == 0:
        return text
    else:
        return expand(
            reduce(
                lambda text, key: text.replace(key, REPLACEMENTS[key]),
                REPLACEMENTS.keys(),
                text
            ),
            depth - 1
        )
