"""
Contains the Bot object.
"""

import discord
from discord.ext import commands
from discord.ext.commands.view import StringView

from homun.lib import owoify as owoifymodule
from homun.lib import smh as smhmodule


bot = commands.Bot(command_prefix=">")


# This is dirty magic.
# It lets the bot get the full invocation context for its own messages.
bot._skip_check = lambda x, y: False

# This is also dirty magic.
# This skips the check that prevents Discord bots from invoking commands.
@bot.event
async def on_message(message):
    # Strip off a zero-width space prefix, for Ayana.
    # (Ayana's responses to =say start with this character, for some reason.)
    if message.content and ord(message.content[0]) == 8203:
        message.content = message.content[1:]
    ctx = await bot.get_context(message)
    await bot.invoke(ctx)


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


def run(token: str):
    """Runs the Bot object using the token argument."""
    bot.run(token)
