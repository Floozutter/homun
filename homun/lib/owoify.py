"""
convert English text to owo-speak!

references:
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
    """returns the text argument converted to owo-speak!"""
    return reduce(
        lambda text, key: text.replace(key, REPLACEMENTS[key]),
        REPLACEMENTS.keys(),
        text.lower()
    )

REPLACEMENTS2 = {
    "o": "owo",
    "u": "uwu"
}
def owoify2(text: str) -> str:
    """returns the text argument converted to owo-speak, but worse!"""
    return reduce(
        lambda text, key: text.replace(key, REPLACEMENTS2[key]),
        REPLACEMENTS2.keys(),
        owoify(text)
    )
