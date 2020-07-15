import os
import logging
import settings

from discord.ext import commands

#logger = logging.getLogger("Main")

bot = commands.Bot(command_prefix=settings.command_prefix)

# load legit cogs
for filename in os.listdir("corecogs"):
    settings.cog_list.append(filename)
    bot.load_extension(f'cogs.{filename}')
    
# add third-party cogs to list
for filename in os.listdir("extracogs"):
    settings.cog_list.append(filename)


# start bot
bot.run(settings.discord_token)
