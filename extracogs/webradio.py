import settings
import discord
from discord import FFmpegPCMAudio
from discord.ext import commands

class WebRadioCog(commands.cog):
    def __init__(self, bot):
        self.bot = bot
        self.players = {}

    @client.command
    async def play(ctx, url: str = 'https://stream.radioparadise.com/mp3-192'):
        channel = ctx.message.author.voice.channel
        guild = ctx.message.guild.name
        try:
            player = await channel.connect()
            self.players[guild] = player
        except Exception as err:
            ctx.send("The following error occured: " + str(err))
        player.play(FFmpegPCMAudio(url))

    @client.command
    async def stop(ctx):
        guild = ctx.message.guild.name
        try:
            self.players[guild].stop()
            ctx.send('Stopped player!')
        except Exception as err:
            ctx.send("The following error occured: " + str(err))
