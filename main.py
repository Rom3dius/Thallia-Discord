import os
import logging
import settings
from dotenv import load_dotenv
load_dotenv()

from discord.ext import commands

#logger = logging.getLogger("Main")

bot = commands.Bot(command_prefix=settings.command_prefix)
cog_list = []

# load legit cogs
for filename in os.listdir("corecogs"):
    if filename [-3:] == '.py':
        cog_list.append(filename[:-3])
        bot.load_extension(f'corecogs.{filename[:-3]}')
        print(f'{filename} cog has been loaded!')

# add third-party cogs to list

@bot.event
async def on_ready():
    print('Ready!')

# start bot
bot.run(settings.discord_token)
