"""
Contains the Bot object.
"""

import discord
from discord.ext import commands

from homun.lib import owoify as owoifymodule


bot = commands.Bot(command_prefix=">")

@bot.command()
async def ping(ctx):
    """Pongs a ping."""
    await ctx.send("pong")

@bot.command()
async def owoify(ctx, *, text: str):
    """Owoifies text."""
    await ctx.send(owoifymodule.owoify(text))


def run(token: str):
    """Runs the Bot object using the token argument."""
    bot.run(token)
