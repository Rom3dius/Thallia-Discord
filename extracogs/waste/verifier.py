import os, discord, settings, pickle
from discord.ext import tasks, commands
from main import bot

def setup(bot):
    bot.add_cog(VerifierCog(bot))

class VerifierCog(commands.Cog):
    def __init__(self, bot):
        try:
            infile = open('data.pickle','rb')
            self.data = pickle.load(infile)
            infile.close()
        except (FileNotFoundError, TypeError):
            self.data = {'Guilds': {'ExampleGuild': {'Verifier': True}}}
            self.data["VerifierMessages"] = []
            outfile = open('data.pickle','wb')
            pickle.dump(self.data,outfile)
            outfile.close
        self.check_for_reactions.start()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def verifier(self, ctx, string: str):
        try:
            y = self.data["Guilds"][ctx.guild.id]
        except KeyError:
            self.data["Guilds"][ctx.guild.id] = {}
        if string == 'True':
            self.data["Guilds"][ctx.guild.id]["Verifier"] = True
            role = await ctx.guild.create_role(name="Unverified")
            self.data["Guilds"][ctx.guild.id]["VerifierRole"] = role
            for x in ctx.guild.channels:
                if x.name != ctx.channel.name:
                    await x.set_permissions(role, view_channel=False)
            message = await ctx.send('Welcome to the server! By clicking the checkmark below you confirm you have read the rules and will abide by them during this stay!')
            self.data["Guilds"][ctx.guild.id]["VerifierMessage"] = message.id
        elif string == 'False':
            self.data["Guilds"][ctx.guild.id]["Verifier"] = False
            await self.data["Guilds"][ctx.guild.id]["VerifierRole"].delete()
        else:
            await ctx.send("Please pass either 'True' or 'False' to the command!")

    @bot.event
    async def on_member_join(self, member):
        try:
            if self.data["Guilds"][member.guild.id]["Verifier"] == True:
                await member.add_roles(self.data["Guilds"][member.guild.id]["VerifierRole"])
        except KeyError:
            self.data["Guilds"][member.guild.id] = {}

    @tasks.loop(seconds=10)
    async def check_for_reactions(self):
        for x in self.data["VerifierMessages"]
            message = await fetch_message(x)
                for reaction in message.reactions:
                    async for user in reaction.users():
                        try:
                            await user.remove_roles(x["VerifierRole"])
                        except:
                            return
