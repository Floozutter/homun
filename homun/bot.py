"""
Contains the Bot object.
"""

import discord
from discord.ext import commands

from homun.lib import owoify as owoifymodule
from homun.lib import smh as smhmodule


bot = commands.Bot(command_prefix=">")

@bot.command()
async def ping(ctx):
    """Pongs a ping."""
    await ctx.send("pong")

@bot.command()
async def owoify(ctx, *, text: str):
    """Owoifies text."""
    await ctx.send(owoifymodule.owoify(text))

@bot.command()
async def owoify2(ctx, *, text: str):
    """Owoifies text, but worse."""
    await ctx.send(owoifymodule.owoify2(text))

@bot.command()
async def smh(ctx, *, text: str):
    """Expands instances of smh."""
    await ctx.send(smhmodule.expand(text))


def run(token: str):
    """Runs the Bot object using the token argument."""
    bot.run(token)
