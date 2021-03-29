"""
runs the bot using command-line arguments
"""

from . import bot
from argparse import ArgumentParser
from sys import exit

def parse_args() -> tuple[str, bool]:
    """
    gets and returns the token command-line argument
    """
    parser = ArgumentParser(
        description = "a Discord bot for Backup Potion!",
        prog = "homun"
    )
    parser.add_argument("token", type = str, help = "Discord bot token")
    parser.add_argument("-f", "--file", action = "store_true", help = "interpret token as file")
    args = parser.parse_args()
    return args.token, args.file

def main(pretoken: str, isfile: bool = False) -> int:
    if isfile:
        try:
            with open(pretoken, "r") as ifile:
                token = ifile.read().strip()
        except OSError as e:
            print(f"os error: `{e}`!")
            return 1
    else:
        token = pretoken.strip()
    bot.run(token)
    return 0

if __name__ == "__main__":
    print("starting homun...")
    exit(main(*parse_args()))
