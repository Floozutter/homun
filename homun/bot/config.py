"""
bot configuration
"""

from . import bot

# dirty magic to let the bot get the full invocation context for its own messages
bot._skip_check = lambda x, y: False

# dirty magic to let other Discord bots invoke commands
@bot.event
async def on_message(message):
    # strip off a zero-width space prefix, for Ayana
    # (Ayana's responses to =say start with this character, for some reason)
    if message.content and ord(message.content[0]) == 8203:
        message.content = message.content[1:]
    ctx = await bot.get_context(message)
    await bot.invoke(ctx)
