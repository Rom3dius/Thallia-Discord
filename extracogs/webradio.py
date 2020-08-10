import settings
import discord
from discord import FFmpegPCMAudio
from discord.ext import commands
from main import bot

class WebRadioCog(commands.cog):
    def __init__(self, bot):
        self.bot = bot
        self.players = {}

    @commands.command()
    async def play(self, ctx, url: str = 'https://stream.radioparadise.com/mp3-192'):
        channel = ctx.message.author.voice.channel
        guild = ctx.message.guild.name
        try:
            player = await channel.connect()
            self.players[guild] = player
        except Exception as err:
            ctx.send("The following error occured: " + str(err))
        player.play(FFmpegPCMAudio(url))

    @commands.command()
    async def stop(self, ctx):
        guild = ctx.message.guild.name
        try:
            self.players[guild].stop()
            ctx.send('Stopped player!')
        except Exception as err:
            ctx.send("The following error occured: " + str(err))


def setup(bot):
    bot.add_cog(WebRadioCog(bot))
