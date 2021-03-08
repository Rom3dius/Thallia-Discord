import os
import discord
import settings
import requests
import json
from discord.ext import tasks, commands
import time
from main import bot

api_key = "01510ef0dbfb10fefce9fc43aa76e5e8c15578a1b0f54a82091d861628d1e72c"

class CalendarCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.schedule.start()

    @commands.command()
    @commands.is_owner()
    async def testapi(self, ctx):
        x = requests.get("https://api.teamup.com/check-access", headers={"Teamup-Token": api_key})
        y = json.loads(x.content)
        if y["access"] == "ok":
            await ctx.send("API connection successful!")
        else:
            await ctx.send("API connection unsuccessful!")

    @commands.command()
    @commands.is_owner()
    async def scheduletest(self, ctx):
        timeformatted = time.strftime("%H%M", time.localtime())
        await ctx.send(timeformatted)
        date = time.strftime("%Y-%m-%d", time.localtime())
        x = requests.get(f"https://api.teamup.com/kszz48jtiq5nmusdy1/events?startDate={date}&endDate={date}", headers={"Teamup-Token": api_key})
        events = json.loads(x.content)
        guild = bot.get_guild(720378040798019664)
        channel = guild.get_channel(747943778786083006)
        for x in events['events']:
            # if x["subcalendar_id"] ==
            text = "**Title:** " + x["title"] + "\nStarts: " + x["start_dt"] + "\nEnds: " + x["end_dt"] + "\nNotes: " + x["notes"]
            #text = f"**{x["title"]}**\nStarts: {x["start_dt"]}\nEnds: {x["end_dt"]}\nNotes: {x["notes"]}\nThis is a test! Please disregard! It will be deleted in a few seconds!"
            await channel.send(content=text, delete_after=6)

    @tasks.loop(minutes=1)
    async def schedule(self):
        timeformatted = time.strftime("%H%M", time.localtime())
        if timeformatted != "0730":
            return
        date = time.strftime("%Y-%m-%d", time.localtime())
        x = requests.get(f"https://api.teamup.com/kszz48jtiq5nmusdy1/events?startDate={date}&endDate={date}", headers={"Teamup-Token": api_key})
        events = json.loads(x.content)
        guild = bot.get_guild(720378040798019664)
        channel = guild.get_channel(747943778786083006)
        for x in events['events']:
            # if x["subcalendar_id"] ==
            text = "**Title:** " + x["title"] + "\nStarts: " + x["start_dt"] + "\nEnds: " + x["end_dt"] + "\nNotes: " + x["notes"]
            #text = f"**{x["title"]}**\nStarts: {x["start_dt"]}\nEnds: {x["end_dt"]}\nNotes: {x["notes"]}"
            await channel.send(content=text)

def setup(bot):
    bot.add_cog(CalendarCog(bot))
