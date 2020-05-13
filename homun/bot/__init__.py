"""
Handles the bot object as a package-level variable.
"""

from discord.ext import commands

bot = commands.Bot(command_prefix=">")

import homun.bot.config
import homun.bot.commands


def run(token: str):
    """Runs the bot object using the token argument."""
    bot.run(token)