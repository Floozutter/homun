"""
subclass of discord.py's Bot class with additional helpers
"""

from discord.ext.commands import Bot, Command
from typing import Callable

class BotInABottle(Bot):
    def add_formatter(self,
        formatter: Callable[[str], str],
        name: str,
        doc: str
    ) -> None:
        """creates and registers a command from a simple text formatter"""
        async def func(ctx, *, text: str):
            await ctx.send(formatter(text))
        command = Command(func, name=name, help=doc)
        self.add_command(command)
