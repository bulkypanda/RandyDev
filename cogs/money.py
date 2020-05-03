# Work with Python 3.6
import discord
from discord.ext import commands
import json
# import fin as fin
import getpass
# import praw
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
import covid19_data
import webbrowser
import os
import bs4
import wikipediaapi
import webbrowser
import youtube_dl
from googletrans import Translator
from discord.voice_client import VoiceClient
from discord.utils import get


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



def setup(client):
    client.add_cog(Money(client))
