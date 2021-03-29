"""
bot commands
"""

from . import bot

from ..lib.owoify import owoify, owoify2
from ..lib.smh import expand

bot.add_formatter(owoify, "owoify", "owoifies text")
bot.add_formatter(owoify2, "owoify2", "owoifies text, but worse")
bot.add_formatter(expand, "smh", "expands instances of smh")

import discord
import os.path

@bot.command()
async def ping(ctx):
    """pongs a ping"""
    await ctx.send("pong")

@bot.command()
async def echo(ctx, *, text: str):
    """echos the text argument"""
    await ctx.send(text)

@bot.command()
async def gn(ctx):
    """emotes goodnight"""
    await ctx.send("<:megauwu:679614776267243559>")

@bot.command()
async def kirbcult(ctx, leftwardarm: str, rightwardarm: str):
    """makes a cult of Kirbys from the arm args"""
    l, r = leftwardarm, rightwardarm
    await ctx.send(f"({r}O_O){r} {l}(O_O){r} {l}(O_O{l})")

@bot.command()
async def play(ctx, *, filename: str):
    """plays a local sound file (ANY IN THE FILESYSTEM)"""
    # Get audio source.
    filepath = f"resources/audio/{filename}"
    if not os.path.isfile(filepath):
        await ctx.send("File not found!")
        return
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(
        filepath
    ))
    # Join voice channel.
    if ctx.voice_client is not None:
        await ctx.voice_client.move_to(ctx.author.voice.channel)
    else:
        await ctx.author.voice.channel.connect()
    # Play the audio source.
    ctx.voice_client.play(
        source,
        after=lambda e: print('Player error: %s' % e) if e else None
    )
    # Announce.
    await ctx.send(f"Playing: {filename}")

@bot.command()
async def leave(ctx):
    """leaves voice channel"""
    await ctx.voice_client.disconnect()
    await ctx.send(f"Bye-bye!")
