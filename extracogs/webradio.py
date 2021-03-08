import os
import discord
import settings
import pickle
from discord import FFmpegPCMAudio
from discord.ext import commands, tasks
from main import bot

class StreamCog(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
        self.list = pickle.load(open("stations.p", "rb"))
        self.players = {}
        self.quit_voice.start()

    @commands.command()
    async def streamurls(self, ctx):
        str = ""
        for x in self.list:
            str += x + ": "
            str += self.list[x] + "\n"
        await ctx.send(str)

    @commands.command()
    async def streamadd(self, ctx, name: str, url: str):
        self.list[name] = url
        pickle.dump(self.list, open("stations.p", "wb"))
        await ctx.send("Added station to the list!")

    @commands.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def streamremove(self, ctx, name: str):
        try:
            del self.list[name]
        except KeyError:
            await ctx.send("Station not found!")
            return
        await ctx.send(f"Deleted the {name} station!")

    @commands.command()
    async def streamurl(self, ctx, url: str = 'http://stream.radioparadise.com/rock-128'):
        channel = ctx.author.voice.channel
        try:
            self.players[ctx.guild.name] = await channel.connect()
        except:
            pass
        try:
            self.players[ctx.guild.name].play(FFmpegPCMAudio(url))
        except:
            await ctx.send("Either I ran into an error, or I'm already playing audio!")
            await self.players[ctx.guild.name].disconnect()

    @commands.command()
    async def streamplay(self, ctx, station: str):
        channel = ctx.author.voice.channel
        station = station.replace(" ", "").lower()
        try:
            self.players[ctx.guild.name].stop()
            self.players[ctx.guild.name].cleanup()
            try:
                self.players[ctx.guild.name].play(FFmpegPCMAudio(f"https://0n-{station}.radionetz.de/0n-{station}.mp3"))
            except:
                await ctx.send("Channel doesn't exist! Check webradios.de")
        except KeyError:
            self.players[ctx.guild.name] = await channel.connect()
            try:
                self.players[ctx.guild.name].play(FFmpegPCMAudio(f"https://0n-{station}.radionetz.de/0n-{station}.mp3"))
            except:
                await ctx.send("Channel doesn't exist! Check webradios.de")
                self.players[ctx.guild.name].cleanup()
                await self.players[x].disconnect()

    @commands.command()
    async def streamstop(self, ctx):
        await self.players[ctx.guild.name].disconnect()
        del self.players[ctx.guild.name]

    @tasks.loop(minutes=5.0)
    async def quit_voice(self):
        for x in self.players:
            if len(self.players[x].channel.members) == 1:
                await self.players[x].source.cleanup()
                await self.players[x].disconnect()

def setup(bot):
    bot.add_cog(StreamCog(bot))
