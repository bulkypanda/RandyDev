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
from discord.voice_client import VoiceClient
from discord.utils import get


class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Info cog is online.")

    @commands.command(brief='Gives a summary about anything')
    async def wiki(self, ctx, *, page):
        wiki_wiki = wikipediaapi.Wikipedia('en')
        page_py = wiki_wiki.page(page)
        if page_py.exists() == True:
            await ctx.send(page_py.summary[0:1900])
        else:
            await ctx.send('This page does not exist. Try Again')

    @commands.command(brief="Covid-19 related info.", aliases=['corona', 'Covid', 'covid19', 'coronavirus', 'covid-19'])
    async def covid(self, ctx, *, place):
        length = len(place)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
        if length > 2:
            result = covid19_data.dataByName(place)
            embed.set_author(name='Covid-19 Statistics')
            embed.add_field(name='`Cases`', value=str(result.cases), inline=True)
            embed.add_field(name='`Deaths`', value=str(result.deaths), inline=True)
            embed.add_field(name='`Recovered`', value=str(result.recovered), inline=True)
            await ctx.send(embed=embed)
        elif place == 'US':
            result = covid19_data.dataByName(place)
            embed.set_author(name='Covid-19 Statistics')
            embed.add_field(name='`Cases`', value=str(result.cases), inline=True)
            embed.add_field(name='`Deaths`', value=str(result.deaths), inline=True)
            embed.add_field(name='`Recovered`', value=str(result.recovered), inline=True)
            await ctx.send(embed=embed)
        else:
            result = covid19_data.dataByNameShort(place)
            embed.set_author(name='Covid-19 Statistics')
            embed.add_field(name='`Cases`', value=str(result.cases), inline=True)
            embed.add_field(name='`Deaths`', value=str(result.deaths), inline=True)
            embed.add_field(name='`Recovered`', value=str(result.recovered), inline=True)
            await ctx.send(embed=embed)
                    
    @commands.command(brief='News from NYT', aliases=['nyt'])
    async def NYT(self, ctx):
        result = requests.get(
            "https://api.nytimes.com/svc/topstories/v2/home.json?api-key=NCofMShCyDvmh3YvYcWAFGSqCDo8g3FG").json()
        articlenum = random.randint(0, 56)
        formatted_data = result["results"][articlenum]["title"]
        formatted_data2 = result["results"][articlenum]["abstract"]
        formatted_data3 = result["results"][articlenum]["url"]
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
        embed.set_author(name='%s' %formatted_data)
        embed.add_field(name='Description:', value=formatted_data2, inline=True)
        await ctx.send(embed=embed)
        await ctx.send(formatted_data3)

    @commands.command(brief='News')
    async def news(self, ctx, x):
        results = requests.get(
            'http://newsapi.org/v2/everything?q=' + x + '&apiKey=1cd7416e8c114c569072cf55d1a3ef4e').json()
        a = random.randint(0, 20)
        g = results['articles'][a]['title']
        y = results['articles'][a]['url']
        z = results['articles'][a]['description']
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
        embed.set_author(name='%s' %g)
        embed.add_field(name='Description:', value=z, inline=True)
        await ctx.send(embed=embed)
        await ctx.send(str(y))

    

def setup(client):
    client.add_cog(Info(client))
