import settings
import discord, os, time
from discord.ext import commands
from main import bot

class TimeCog(commands.cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def time(self, ctx):
        await ctx.send()

    @time.command()
    async def unix(self, ctx):
        await ctx.send(f'Current UNIX timestamp: {time.time()}\nUTC time: {time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())}\nLocaltime of bot: {time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())}')

def setup(bot):
    bot.add_cog(TimeCog(bot))
