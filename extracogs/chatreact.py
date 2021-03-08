import os
import discord
import settings
from discord.ext import commands
from main import bot


class ChatReactCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.listen('on_message')
    async def f_in_chat(message):
        words = message.content.lower().split()
        for x in words:
            if x == "f" or x == "fs":
                if message.author.bot == False:
                    await message.channel.send("F")
                    return
        if message.author.id == 591548628968144916:
            if message.channel.id == 785931425357889536:
                await message.channel.send("https://i.kym-cdn.com/photos/images/original/001/400/617/6dc.png")

    @bot.listen('on_reaction_add')
    async def verify(reaction, user):
        if reaction.message.id == 788114495561138192:
            x = reaction.message.guild.get_role(784890045752279081)
            await user.remove_roles(x)

def setup(bot):
    bot.add_cog(ChatReactCog(bot))
