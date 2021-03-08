import discord
import settings
from discord.ext import commands
from main import bot


class TicketsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tickets = []

    @commands.command()
    async def support_tickets(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("""```
Tickets usage:
-tickets create (opens a ticket with staff)
-tickets close (requires confirmation from two staff)

Anyone with admin rights on the server will see the ticket.
```""")

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def ticket_create(self, ctx):
        for x in ctx.guild.categories:
            if x.name == "Tickets":
                y = await x.create_text_channel(f"{ctx.author.name}'s Ticket")
                await y.set_permissions(ctx.author, read_messages=True, send_message=True)

    @commands.command()
    async def tickets_setup(self, ctx):
        cat = await ctx.create_category("tickets")
        await cat.set_permissions(ctx.guild.default_role, read_messages=False, send_messages=False)
        
    @commands.command()
    async def ticket_close(self, ctx):
        return

def setup(bot):
    bot.add_cog(TicketsCog(bot))
