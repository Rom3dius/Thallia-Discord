import os
import discord
import settings
from discord.ext import commands

class AdminCogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def ping(self, ctx):
        await ctx.send(f"I'm connected with a ping of {bot.latency}")

    @commands.command()
    @commands.is_owner()
    async def loadcog(self, ctx, cog: str):
        if cog in settings.cog_list:
            try:
                self.bot.load_extension(cog)
            except Exception as e:
                await ctx.send("Could not load cog!" + "\n" + e)

    @commands.command()
    @commands.is_owner()
    async def unloadcog(self, ctx, cog: str):
        if cog in settings.cog_list:
            try:
                self.bot.unload_extension(cog)
            except Exception as e:
                await ctx.send("Could not unload cog!" + "\n" + e)

    @commands.command()
    @commands.is_owner()
    async def presence(self, ctx, presence_type: ActivityTypeConverter, *message: str, ):
        """
        Sets the presence status of the bot

        presence_type can be any of:
        - listening
        - watching
        - streaming
        - playing

        """
        if presence_type.cleaned_value != discord.ActivityType.unknown:
            activity = discord.Activity(
                name=" ".join(message), type=presence_type.cleaned_value)
            await self.bot.change_presence(activity=activity)
            await ctx.send("Presence update. Please wait a few seconds to see the change.")
        else:
            await ctx.send("This is an unknown type. Please use !help presence to learn more about the types.")
