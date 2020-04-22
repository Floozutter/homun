"""
Contains the Bot object.
"""

import discord
from discord.ext import commands


bot = commands.Bot(command_prefix=">")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")


def run(token: str):
    """Runs the Bot object using the token argument."""
    bot.run(token)
