import settings
import discord
from discord.ext import commands
from time import sleep

class PollCog(commands.cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def poll(self, ctx, time: int, *about: str):
        
