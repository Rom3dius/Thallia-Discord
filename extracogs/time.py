import os
import discord
import settings
import requests
from discord.ext import commands
from main import bot
import time


class TimeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def time(self, ctx, rest: str):
        if rest == "":
            await ctx.send("Please input a continent! Such as:\nAmerica\nAfrica\nAsia")

    @time.command()
    async def continents(self, ctx):


    @time.command()
    async def unix(self, ctx):
        await ctx.send(str(time.time()))

    @time.command()
    async def info(self, ctx):
        await ctx.send(f'Current UNIX timestamp: {time.time()}\nUTC time: {time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())}\nLocaltime of bot: {time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())}')

def setup(bot):
    bot.add_cog(TimeCog(bot))
