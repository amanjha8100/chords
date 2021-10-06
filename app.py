from music import music
import os
import discord
from discord.ext import commands

from dotenv import load_dotenv
load_dotenv()

bot = commands.Bot(command_prefix='_')
bot.remove_command('help')
bot.add_cog(music(bot))


bot.run(os.getenv('TOKEN'))
