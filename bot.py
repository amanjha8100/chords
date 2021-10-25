from help import Help
from music import Music
import os
import discord
from discord.ext import commands
import json

from dotenv import load_dotenv

load_dotenv()

with open("config.json", "r") as config_file:
    config = json.load(config_file)
    prefix = config["PREFIX"]

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command("help")


bot.add_cog(Music(bot))
bot.add_cog(Help(bot))

bot.run(os.getenv("TOKEN"))
