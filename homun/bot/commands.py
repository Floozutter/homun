"""
Bot commands.
"""

from homun.bot import bot

from homun.lib import owoify as owoifymodule
from homun.lib import smh as smhmodule


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

@bot.command()
async def gn(ctx):
    """Emotes goodnight."""
    await ctx.send("<:megauwu:679614776267243559>")

@bot.command()
async def echo(ctx, *, text: str):
    """Echos the text argument."""
    await ctx.send(text)