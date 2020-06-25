import json
import requests
import aiohttp
from discord.ext import commands
from yahoo_fin import stock_info as si

global tokens
with open('tokens.json', 'r') as l:
    tokens = json.load(l)

class Money(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Money cog is online.")

    @commands.command(brief="Checks the price of bitcoin.")
    async def bitcoin(self, ctx):
        url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
        async with aiohttp.ClientSession() as session:  # Async HTTP request
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            await ctx.send("Bitcoin price is: $" + response['bpi']['USD']['rate'])

    @commands.command(brief="Currency Exchange!", aliases=['Currency'])
    async def currency(self, ctx, src, dest, num):
        results = requests.get(
            'https://free.currconv.com/api/v7/convert?q=%s_%s&compact=ultra&apiKey=' + tokens['exchange'] % (
                src, dest)).json()
        y = float(num) * float(results[src + "_" + dest])
        final = round(y, 3)
        await ctx.send(str(final))

    @commands.command(brief="Checks the stock price.")
    async def stock(self, ctx, ticker):
        price = si.get_live_price(ticker)
        price = round(price, 2)
        await ctx.send('$' + str(price))


def setup(client):
    client.add_cog(Money(client))
