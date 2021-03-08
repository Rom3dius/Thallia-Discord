import os, logging, settings, time, discord
from discord.ext import commands

#logging.basicConfig(filename='thallia.log', level=logging.debug)

token = "NjQ3NTMzNTYzMzIzMDg4OTQ3.XdhEoA.-MygaOxXf4tuaxqzrkWgYQOMvpI"

intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix=settings.command_prefix, intents=intents)
cog_list = []

def timestamp():
    time = time.strftime("%Y-%m-%d:%H-%M-%S", time.localtime())
    return time

@bot.event
async def on_ready():
    pass

#load legit cogs
for filename in os.listdir("corecogs"):
    if filename [-3:] == '.py':
        try:
            cog_list.append(filename[:-3])
            bot.load_extension(f'corecogs.{filename[:-3]}')
            #logging.info(timestamp() + f'Corecog {filename[:-3]} has been loaded!')
        except Exception as err:
            print(err)
            #logging.error(timestamp() + f'Corecog {filename[:-3]}, failed to load!' + str(err))

# start bot
bot.run(token)
