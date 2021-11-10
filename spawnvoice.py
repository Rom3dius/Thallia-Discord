import discord, asyncio
from discord.ext import commands
from main import cog_list, guilds, embed, bot
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_permission

def setup(bot):
    bot.add_cog(SpawnVoiceCogs(bot))

class SpawnVoiceCogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.created_channels = []
        #self.delete_voice.start()

    @cog_ext.cog_slash(name="vsetup", description="Sets up channels for temporary VCs", guild_ids = guilds)
    async def vsetup(self, ctx):
        """ A command run by an admin which sets up a new category for temporary voice channels """
        for x in ctx.guild.categories:
            if x.name == 'Temp Channels':
                await ctx.send('Category already set up!', hidden=True)
                return
        x = await ctx.guild.create_category_channel('Temp Channels')
        await x.create_text_channel("spawn-voice-commands")
        await x.create_voice_channel("Joiner", user_limit=99)
        await ctx.send('All set up!', hidden=True)

    @cog_ext.cog_slash(name="voice", description="Makes a temporary voice channel if you're in the Joiner VC",
                            options=[
                            create_option(name="name", description="Name of the temporary voice channel", option_type=3, required=True),
                            create_option(name="limit", description="User limit of the voice channel", option_type=4, required=False)
                            ],
                            guild_ids = guilds)
    async def voice(self, ctx, name: str, limit: int=99):
        """ Running -voice {name} {limit} while in the Joiner VC creates a temporary channel """
        try:
            if ctx.author.voice.channel.category.name == "Temp Channels":
                if ctx.author.voice.channel.name == name:
                    await ctx.author.voice.channel.edit(user_limit=limit)
                    await ctx.send(f'Changed user limit to {limit}!', hidden=True)
                    return
                if ctx.author.voice.channel.name == "Joiner":
                    c = await ctx.author.voice.channel.category.create_voice_channel(name, user_limit=limit)
                    await ctx.author.move_to(c, reason="Spawned voice channel")
                    await ctx.send(f'Created a new voice channel {name}', hidden=True)
                    return
                return
        except:
            await ctx.send('Failed to create a channel! Are u in the Joiner VC?', hidden=True)
            return

    @bot.event
    async def on_voice_state_update(member, before, after):
        if before.channel == None:
            return
        if before.channel.category == None:
            return
        if before.channel.category.name == "Temp Channels":
            if before.channel.name == "Joiner":
                return
            await asyncio.sleep(5)
            if len(before.channel.members) == 0:
                await before.channel.delete(reason="Empty temp channel")
