import settings
import discord
from discord.ext import commands

class ChatModCog(commands.cog):
    def __init__(self, bot):
        self.bot = bot

    @client.event
    async def on_message(message):
