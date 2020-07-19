import os
import discord
import settings
from discord.ext import commands, tasks
from main import bot

def setup(bot):
    bot.add_cog(SpawnVoiceCogs(bot))

class SpawnVoiceCogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.created_channels = []
        self.delete_voice.start()

    @commands.command()
    async def voice(self, ctx, name: str, limit: int=99):
        try:
            if ctx.author.voice.channel.name == name:
                await ctx.author.voice.channel.edit(user_limit=limit)
                return
        except:
            pass
        for x in ctx.guild.categories:
            if x.name == "Temp Channels":
                await x.create_voice_channel(name, user_limit=limit, bitrate=32000)
                self.created_channels.append(x)
                return
        x = await guild.create_category_channel('Temp Channels')
        await x.create_voice_channel(name, user_limit=limit, bitrate=32000)

    @tasks.loop(minutes=5.0)
    async def delete_voice(self):
        print("Looking for empty game channels...")
        for x in self.bot.guilds:
            for a in x.categories:
                if a.name == "Temp Channels":
                    for v in a.voice_channels:
                        if len(v.members) == 0:
                            print(f"Deleting {v.name}")
                            await v.delete()
