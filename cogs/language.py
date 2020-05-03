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
        
    @commands.command(aliases=['Wordoftheday'])
    async def wordoftheday(self, ctx):
        results = requests.get('https://api.wordnik.com/v4/words.json/wordOfTheDay?api_key=sewizgnt4hgj5ef6joysiin270d15z2ouqs86t3k46z1nuw4n').json()
        word = results['word']
        definition = results['definitions'][0]['text']
        await ctx.send(word + ': ' + definition)    

    @commands.command(brief='Translations')
    async def translate(self, ctx, src, dest, *, words):
        translated = translator.translate(words, src=src, dest=dest)  # Pass both source and destination
        if translated.text == words:
            await ctx.send('Translation Not Available')
        else:
            await ctx.send(translated.text)

    @commands.command()
    async def urban(self, ctx, *, word):
        if ctx.channel.is_nsfw():
            r = requests.get("http://api.urbandictionary.com/v0/define?term=" + word).json()
            final = str(r['list'][0]['definition']).replace('[', '**')
            final2 = final.replace(']', '**')
            await ctx.send(final2)
        else:
            await ctx.send ('This command works only in a nsfw channel.')

    @commands.command(brief='Definitions')
    async def define(self, ctx, *, word):
        r = requests.get(
            'https://www.dictionaryapi.com/api/v3/references/collegiate/json/%s?key=24a25133-bab8-4e4a-9975-7c51e1950e87' % word).json()
        await ctx.send(str(r[0]['shortdef'][0]).capitalize())

    @commands.command(aliases=['ant', 'Antonym'], brief='Antonym')
    async def antonym(self, ctx, *, word):
        lis = ""
        r = requests.get(
            'https://www.dictionaryapi.com/api/v3/references/thesaurus/json/%s?key=d36a8f62-e308-469c-a200-1429c97d2775' % word).json()
        daddy = (r[0]['meta']['ants'][0])
        for i in daddy:
            lis += i + ", "
        await ctx.send(lis)

    @commands.command(aliases=['syn', 'Synonym'], brief='Synonym')
    async def synonym(self, ctx, *, word):
        lis = ""
        r = requests.get(
            'https://www.dictionaryapi.com/api/v3/references/thesaurus/json/%s?key=d36a8f62-e308-469c-a200-1429c97d2775' % word).json()
        daddy = (r[0]['meta']['syns'][0])
        for i in daddy:
            lis += i + ", "
        await ctx.send(lis)


def setup(client):
    client.add_cog(Language(client))
