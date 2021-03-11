"""
runs the bot using command-line arguments
"""

from argparse import ArgumentParser
from homun.bot import run

def parse_args() -> str:
    """
    gets and returns the token command-line argument
    """
    parser = ArgumentParser(
        description = "Backup Potion's Discord bot",
        prog = "homun"
    )
    parser.add_argument("token", type = str, help = "Discord bot token")
    args = parser.parse_args()
    return args.token

if __name__ == "__main__":
    print("starting homun...")
    run(parse_args())
