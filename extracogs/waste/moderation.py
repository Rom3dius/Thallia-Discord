from discord.ext import commands, tasks
from main import bot, timestamp
import time

def setup(bot):
    bot.add_cog(SpawnVoiceCogs(bot))

class SpawnVoiceCogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.muted = {}

    @bot.event
    async def on_voice_state_update(member, before, after):
        if after.channel != None:
            if self.muted[id] < time.time():
                self.muted.pop(ctx.author.id)
                return
            await member.edit(deafen=True)
        else:
            await member.edit(deafen=False)

    @commands.command()
    async def mute(self, ctx, id: id, time: int=120):
        muted_time = time.time() + time
        self.muted[id] = muted_time

    @bot.event
    async def on_message(self, message):
        if message.id in self.muted:
            if self.muted[message.id] < time.time():
                self.muted.pop(message.id)
                return
            await message.delete()
