import os
import discord
import settings
from discord.ext import commands
from main import bot

import valve.rcon

class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.send("Hello I'm Thalia!")

    @commands.command()
    async def cye_text(self, ctx):
        embed=discord.Embed(title="LFP Cyphered Enigma  [EU][PC]", description="We are looking for new players for our Rainbow Six: Siege eSports teams. We participate in CoR, T4/T3 Leagues and Tourneys. We have the determination and commitment to see that our goals are reached and we aspire to improve in any way we can.\n", color=0x008040)
        embed.set_author(name="CharlesS#7996", icon_url='https://cdn.discordapp.com/avatars/498786655038210048/13f4245241a411853c2afd71a6c57d56.png?size=128')
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/753122568839626774/763768990887051264/Cyphered_Enigma.jpg')
        embed.add_field(name="What we are looking for:", value="- Positivity and professionalism\n- Determination\n- Maturity\n- Commitment\n- Activity\n- Prepared to improve", inline=True)
        embed.add_field(name="Requirements:", value="- 15+\n- Communication\n- Map knowledge\n- Gold2+ for two seasons\n- Maturity\n- Team cooperation\n- Can take criticism", inline=True)
        embed.add_field(name="Contact Info:", value="- Send R6Tabs/R6Stats\n - Mention competitive experience\n- DM CharlesS#7996", inline=True)
        embed.set_footer(text="Thank you for taking your time to read this, we hope to hear from you!")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def clone_category(self, ctx, str: str, str2: str):
        for x in ctx.guild.categories:
            if x.name == str:
                a = x
                break
        b = await ctx.guild.create_category(f"{str2}")
        for x in a.text_channels:
            await b.create_text_channel(x.name)        

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def delete_category(self, ctx, str: str):
        for x in ctx.guild.categories:
            if x.name == str:
                a = x
                break
        for x in a.text_channels:
            await x.delete()

    @commands.command()
    async def r_whitelist(self, ctx, str: str):
        if ctx.guild.name == "Romedius ex Senatu":
            x = valve.rcon.execute(("151.248.224.137", 28015), "19283746", f"oxide.grant user {str} whitelist.allow")
            await ctx.send(x)

def setup(bot):
    bot.add_cog(TestCog(bot))
