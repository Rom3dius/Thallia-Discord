import discord, settings
from discord.ext import commands
from discord import FFmpegPCMAudio
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
        try:
            player = await channel.connect()
            player.play(FFmpegPCMAudio('http://stream.radioparadise.com/rock-128', executable='ffmpeg'))
        except Exception as e:
            await ctx.send(f"Apologies, failed to play audio! {e}")
            await player.disconnect()



    @commands.command(aliases=['s', 'sto'])
    async def stop(self, ctx):
        voice_connection = ctx.guild.voice_client
        await voice_connection.disconnect()
