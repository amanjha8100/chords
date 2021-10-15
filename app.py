from help import Help
from music import Music
import os
import discord
from discord.ext import commands

from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="_", intents=intents)
bot.remove_command("help")
with open('prefix.txt', 'r') as fp:
    prefix = fp.read()

bot = commands.Bot(command_prefix=prefix, intents=intents)
bot.remove_command('help')
bot.add_cog(Music(bot))
bot.add_cog(Help(bot))

bot.run(os.getenv("TOKEN"))
