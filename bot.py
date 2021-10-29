import os
import traceback
import json
import discord
from discord.ext import commands


DESCRIPTION = """
A self-hosted music discord bot, with detailed
documentation and constantly upgrading features.
"""

with open("config.json", "r") as config_file:
    config = json.load(config_file)
    prefix = config["PREFIX"]


class Chords(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        super().__init__(
            command_prefix=prefix,
            description=DESCRIPTION,
            heartbeat_timeout=150.0,
            intents=intents,
            help_command=None,
        )
        self._load_extensions()

    def _load_extensions(self) -> None:
        cogs_dir = os.listdir("cogs")
        for filename in cogs_dir:
            if filename.endswith(".py"):
                cog = filename[:-3]
                try:
                    self.load_extension(f"cogs.{cog}")
                except Exception as e:
                    traceback.print_exc()
