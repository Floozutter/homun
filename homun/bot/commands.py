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
import requests_html
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
async def lucario(ctx):
    """posts a random (safe) Lucario image from e621"""
    response = requests_html.HTMLSession().get(
        "https://e621.net/posts.json?"
        "tags=lucario+rating:safe+score:%3E=50+-type:mp4+-type:swf+-type:webm+-type:zip+order:random&limit=1"
    )
    json = response.json()
    post = next(iter(json["posts"]))
    id = post["id"]
    url = post["file"]["url"]
    embed = discord.Embed(title = "a wild lucario appeared!")
    embed.set_image(url = post["file"]["url"])
    embed.set_author(name = post['id'], icon_url = "https://e621.net/favicon.ico")
    await ctx.send(embed = embed)

@bot.command()
async def play(ctx):
    """plays a local coconut-mall.mp3"""
    # read audio file
    filename = "coconut-mall.mp3"
    filepath = f"resources/audio/{filename}"
    if not os.path.isfile(filepath):
        await ctx.send("file not found!")
        return
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(
        filepath
    ))
    # join voice channel
    if ctx.voice_client is not None:
        await ctx.voice_client.move_to(ctx.author.voice.channel)
    else:
        await ctx.author.voice.channel.connect()
    # play audio
    ctx.voice_client.play(
        source,
        after=lambda e: print('player error: %s' % e) if e else None
    )
    # announce
    await ctx.send(f"playing: {filename}")

@bot.command()
async def leave(ctx):
    """leaves voice channel"""
    await ctx.voice_client.disconnect()
    await ctx.send(f"bye-bye!")
