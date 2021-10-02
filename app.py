import discord
from discord.ext import commands

from music import music
bot = commands.Bot(command_prefix='__')
bot.remove_command('help')
bot.add_cog(music(bot))

import os
 
# token = "" 
# with open("tokens.txt") as file:
#     token = file.read()

# bot.run(token)

bot.run(os.getenv('TOKEN'))
