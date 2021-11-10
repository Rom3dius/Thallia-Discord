import discord, asyncio
from discord.ext import commands
from main import cog_list, guilds, embed, bot
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_permission

def setup(bot):
    bot.add_cog(AdminCogs(bot))

class AdminCogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cogs = ["admin"]

    @cog_ext.cog_slash(name="ping", description="Prints bot ping", guild_ids = guilds)
    async def ping(self, ctx):
        await ctx.send(f"I'm connected with a ping of {self.bot.latency}", hidden=True)

    @cog_ext.cog_slash(name="loadcog", description="Load a cog",
                            options=[
                            create_option(name="cog", description="Cog filename", option_type=3, required=True)
                            ],
                            guild_ids = guilds)
    async def loadcog(self, ctx, cog: str):
        try:
            self.bot.load_extension(f'extracogs.{cog}')
            self.cogs.append(cog)
            #cogsloaded = ""
            #for x in self.cogs:
            #    cogsloaded += f"{x}, "
            #game = discord.Game(f"with {cogsloaded[:-2]}!")
            #await bot.change_presence(status=discord.Status.dnd, activity=game)
            print(f'Loaded {cog}!')
            await ctx.send(f'Loaded {cog}!', hidden=True)
        except Exception as e:
            await ctx.send("Could not load cog!" + "\n" + str(e), hidden=True)
            #logging.warning(timestamp() + 'Failed to load cog: ' + str(e))


    @cog_ext.cog_slash(name="unloadcog", description="Unload a cog",
                            options=[
                            create_option(name="cog", description="Cog filename", option_type=3, required=True)
                            ],
                            guild_ids = guilds)
    async def unloadcog(self, ctx, cog: str):
        try:
            if cog not in cog_list:
                self.bot.unload_extension(f'extracogs.{cog}')
                self.cogs.remove(cog)
                #cogsloaded = ""
                #for x in self.cogs:
                #    cogsloaded += f"{x}, "
                #game = discord.Game(f"with {cogsloaded[:-2]}!")
                #await bot.change_presence(status=discord.Status.dnd, activity=game)
                print(f'Unloaded {cog}!')
                await ctx.send(f'Unloaded {cog}!', hidden=True)
            else:
                await ctx.send('Crucial cog, cannot unload!', hidden=True)
        except Exception as e:
            await ctx.send("Could not unload cog!" + "\n" + str(e), hidden=True)
            #logging.warning(timestamp() + 'Failed to unload cog: ' + str(e))

    @cog_ext.cog_slash(name="reloadcog", description="Reload a cog",
                            options=[
                            create_option(name="cog", description="Name of cog to reload", option_type=3, required=True)
                            ],
                            guild_ids = guilds)
    async def reloadcog(self, ctx, cog: str):
        try:
            if cog not in cog_list:
                self.bot.reload_extension(f'extracogs.{cog}')
            else:
                self.bot.reload_extension(f'corecogs.{cog}')
            print(f'Reloaded {cog}!')
            await ctx.send(f'Reloaded {cog}!', hidden=True)
        except Exception as e:
            await ctx.send("Could not reload cog!" + "\n" + str(e), hidden=True)
            #logging.warning(timestamp() + 'Failed to reload cog: ' + str(e))
