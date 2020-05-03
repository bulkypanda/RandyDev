# Work with Python 3.6
import discord
from discord.ext import commands
import requests
import random
import asyncio
import aiohttp
import urllib
import urllib.parse, urllib.request, re
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get
from ftplib import FTP
from yahoo_fin import stock_info as si
from googletrans import Translator
from discord.voice_client import VoiceClient
from discord.utils import get

translator = Translator()


class Language(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Language cog is online.")

    @commands.command(aliases=['Quote'])
    async def quote(self, ctx):
        results = requests.get('https://type.fit/api/quotes').json()
        num = random.randint(0, 1636)
        author = results[num]['author']
        y = '"' + results[num]['text'] + '"' + " -" + author
        await ctx.send(y)


    @commands.command()
    async def urban(self, ctx, *, word):
        if ctx.channel.is_nsfw():
            r = requests.get("http://api.urbandictionary.com/v0/define?term=" + word).json()
            final = str(r['list'][0]['definition']).replace('[', '**')
            final2 = final.replace(']', '**')
            await ctx.send(final2)
        else:
            await ctx.send ('This command works only in a nsfw channel.')



def setup(client):
    client.add_cog(Language(client))
