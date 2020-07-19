"""
Bot commands.
"""

from homun.bot import bot

import discord
import os.path

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


@bot.command()
async def play(ctx, *, filename: str):
	"""Plays a sound file on the server."""
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
	"""Leaves voice channel."""
	await ctx.voice_client.disconnect()
	await ctx.send(f"Bye-bye!")