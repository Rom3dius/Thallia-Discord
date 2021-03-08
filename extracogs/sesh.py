import os
import discord
import settings
from discord.ext import commands
from main import bot


class SeshCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sesh

    @commands.command()
    async def test(self, ctx):
        await ctx.send("Hello I'm Thalia!")

    @commands.command()
    async def listvoicemembers(self, ctx):
        await ctx.send(str(ctx.author.voice.channel.members))

def setup(bot):
    bot.add_cog(SeshCog(bot))
