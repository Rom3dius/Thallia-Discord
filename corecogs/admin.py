import os
import discord
import settings
from discord.ext import commands
from main import bot, cog_list

def setup(bot):
    bot.add_cog(AdminCogs(bot))

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
        try:
            self.bot.load_extension(f'extracogs.{cog}')
            print(f'Loaded {cog}!')
        except Exception as e:
            await ctx.send("Could not load cog!" + "\n" + str(e))

    @commands.command()
    @commands.is_owner()
    async def unloadcog(self, ctx, cog: str):
        try:
            if cog not in cog_list:
                self.bot.unload_extension(f'extracogs.{cog}')
                print(f'Unloaded {cog}!')
            else:
                await ctx.send('Crucial cog, cannot unload!')
        except Exception as e:
            await ctx.send("Could not unload cog!" + "\n" + str(e))

    @commands.command()
    @commands.is_owner()
    async def reloadcog(self, ctx, cog: str):
        try:
            if cog not in cog_list:
                self.bot.reload_extension(f'extracogs.{cog}')
            else:
                self.bot.reload_extension(f'corecogs.{cog}')
            print(f'Reloaded {cog}!')
        except Exception as e:
            await ctx.send("Could not reload cog!" + "\n" + str(e))

    @commands.command()
    @commands.is_owner()
    async def presence(self, ctx, presence_type: str):
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
