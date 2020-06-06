"""
Bot commands.
"""

from homun.bot import bot

from homun.lib.owoify import owoify, owoify2
from homun.lib.smh import expand


bot.add_formatter(owoify, "owoify", "Owoifies text.")
bot.add_formatter(owoify2, "owoify2", "Owoifies text, but worse.")
bot.add_formatter(expand, "smh", "Expands instances of smh.")


@bot.command()
async def ping(ctx):
    """Pongs a ping."""
    await ctx.send("pong")

@bot.command()
async def echo(ctx, *, text: str):
    """Echos the text argument."""
    await ctx.send(text)

@bot.command()
async def gn(ctx):
    """Emotes goodnight."""
    await ctx.send("<:megauwu:679614776267243559>")

@bot.command()
async def kirbcult(ctx, leftwardarm: str, rightwardarm: str):
    """Makes a cult of Kirbys using the arm args."""
    l, r = leftwardarm, rightwardarm
    await ctx.send(f"({r}O_O){r} {l}(O_O){r} {l}(O_O{l})")

