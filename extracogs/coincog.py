import pickle, pprint
from discord.ext import commands, tasks
from main import bot
from pycoingecko import CoinGeckoAPI

class CoinCog(commands.Cog):
    def __init__(self, bot):
        try:
            self.subscriptions = pickle.load(open("subbed.p", "rb"))
        except:
            print("subbed.p missing!")
        self.bot = bot
        self.cg = CoinGeckoAPI()
        self.pp = pprint.PrettyPrinter(indent=2)
        self.notify.start()
    async def savesubs(self):
        await pickle.dump(self.subscriptions, open("subbed.p", "wb"))
    @commands.group()
    async def coin(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid coin command passed!')
    @coin.command()
    async def subscribe(self, ctx, coin: str):
        if not bool(self.cg.get_price(ids=coin, vs_currencies='usd')):
            await ctx.send("That coin doesn't exist!")
            return
        try:
            self.subscriptions[ctx.author.id]
        except KeyError:
            self.subscriptions[ctx.author.id] = coin
            return
        self.subscriptions[ctx.author.id] += f",{coin}"
    @coin.command()
    async def unsubscribe(self, ctx, coin: str):
        try:
            coins = self.subscriptions[ctx.author.id].split(',')
            for x in coins:
                if x == 'coin':
                    coins.pop(x)
                    for x in coins:
                        str += f"{coins[x]}"
                    self.subscriptions[ctx.author.id] = str[:-1]
        except KeyError:
            await ctx.send("You're not subscribed to that coin!")
    @tasks.loop(minutes=12.0)
    async def notify(self):
        for x in self.subscriptions:
            dict = self.cg.get_price(ids=self.subscriptions[ctx.author.id], vs_currencies='usd', include_24hr_change='true', include_last_updated_at='true')
            await self.bot.get_user(x).send(content=self.pp.pprint(dict))

def setup(bot):
    bot.add_cog(CoinCog(bot))
