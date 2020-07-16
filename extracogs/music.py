import discord, settings
from discord.ext import commands
from main import bot

def setup(bot):
    bot.add_cog(MusicCog(bot))

class MusicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['p', 'pla'])
    async def play(self, ctx, url: str = 'http://stream.radioparadise.com/rock-128'):
        try:
            channel = ctx.message.author.voice.channel
        except Exception as e:
            await ctx.send(f"Couldn't join voice channel! {e}")
        global player
        try:
            player = await channel.connect()
        except:
            pass
        player.play(FFmpegPCMAudio('http://stream.radioparadise.com/rock-128'))


    @commands.command(aliases=['s', 'sto'])
    async def stop(self, ctx):
        player.stop()
