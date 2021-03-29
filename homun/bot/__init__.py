"""
exposes the bot object as a package-level variable
"""

from .bottle import BotInABottle

bot = BotInABottle(command_prefix=">")

from . import config
from . import commands
