import asyncio
import os, time
import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='-')
slash = SlashCommand(bot, sync_commands=True, sync_on_cog_reload=True)

cog_list = []
guilds = [733783194695893033] #  733783194695893033

async def embed(msg):
    try:
        embedVar = discord.Embed(title=msg["title"], description=msg["body"], color=0xcd7f32)
    except IndexError:
        return False
    try:
        for x in msg['fields']:
            embedVar.add_field(x, msg['fields'][x])
    except KeyError:
        pass
    embedVar.set_author(name="Locum Tenens", icon_url="https://cdn.discordapp.com/avatars/647533563323088947/12f4c3b3c24a239bc3d45943ed8d70c3.webp?size=128&quot;")
    return embedVar

@bot.event
async def on_ready():
    print('Ready!')

#load legit cogs
for filename in os.listdir("corecogs"):
    if filename [-3:] == '.py':
        try:
            cog_list.append(filename[:-3])
            bot.load_extension(f'corecogs.{filename[:-3]}')
            #logging.info(timestamp() + f'Corecog {filename[:-3]} has been loaded!')
        except Exception as err:
            print(err)

bot.run()
