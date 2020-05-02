"""
Convert English text to owo-speak!

References:
https://www.reddit.com/r/furry/comments/9v3snn/how_to_speak_in_owo_talk/
"""

from functools import reduce


REPLACEMENTS = {
    "l": "w",
    "r": "w",
    "na": "nya",
    "ne": "nye",
    "ni": "nyi",
    "no": "nyo",
    "nu": "nyu",
    "ove": "uv"
}

def owoify(text: str) -> str:
    """
    Returns the text argument converted to owo-speak!
    """
    return reduce(
        lambda text, key: text.replace(key, REPLACEMENTS[key]),
        REPLACEMENTS.keys(),
        text.lower()
    )
