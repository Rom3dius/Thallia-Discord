import os, discord, settings, asyncio
from discord.ext import commands, tasks
from main import bot, timestamp

def setup(bot):
    bot.add_cog(SpawnVoiceCogs(bot))

class SpawnVoiceCogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.created_channels = []
        #self.delete_voice.start()

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def vsetup(self, ctx):
        x = await ctx.guild.create_category_channel('Temp Channels')
        await x.create_text_channel("spawn-voice-commands")
        await x.create_voice_channel("Joiner", user_limit=99)

    @commands.command()
    async def voice(self, ctx, name: str, limit: int=99):
        try:
            if ctx.author.voice.channel.category.name == "Temp Channels":
                if ctx.author.voice.channel.name == name:
                    await ctx.author.voice.channel.edit(user_limit=limit)
                    return
                if ctx.author.voice.channel.name == "Joiner":
                    c = await ctx.author.voice.channel.category.create_voice_channel(name, user_limit=limit)
                    await ctx.author.move_to(c, reason="Spawned voice channel")
                    return
                await ctx.send("Please join the Joiner VC in order to spawn voice channels or pass your channels name to adjust its user limit!")
                return
        except:
            await ctx.send("Please join the Joiner VC in order to spawn voice channels! (or run -vsetup)")
            return
        for x in ctx.guild.categories:
            if x.name == "Temp Channels":
                return

    @bot.event
    async def on_voice_state_update(member, before, after):
        if before.channel == None:
            return
        if before.channel.category == None:
            return
        if before.channel.category.name == "Temp Channels":
            if before.channel.name == "Joiner":
                return
            await asyncio.sleep(5)
            if len(before.channel.members) == 0:
                await before.channel.delete(reason="Empty temp channel")
