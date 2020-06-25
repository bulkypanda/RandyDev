import requests
import random
from discord.ext import commands
from googletrans import Translator
import json

translator = Translator()
global tokens
with open('tokens.json', 'r') as l:
    tokens = json.load(l)

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
        results = requests.get('https://api.wordnik.com/v4/words.json/wordOfTheDay?api_key=' + tokens['wordday']).json()
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
        r = requests.get("http://api.urbandictionary.com/v0/define?term=" + word).json()
        final = str(r['list'][0]['definition']).replace('[', '**')
        final2 = final.replace(']', '**')
        await ctx.send(final2)

    @commands.command(brief='Definitions')
    async def define(self, ctx, *, word):
        r = requests.get(
            'https://www.dictionaryapi.com/api/v3/references/collegiate/json/%s?key=' + tokens['dictapi'] % word).json()
        await ctx.send(str(r[0]['shortdef'][0]).capitalize())

    @commands.command(aliases=['ant', 'Antonym'], brief='Antonym')
    async def antonym(self, ctx, *, word):
        lis = ""
        r = requests.get(
            'https://www.dictionaryapi.com/api/v3/references/thesaurus/json/%s?key=' + tokens['synapi'] % word).json()
        daddy = (r[0]['meta']['ants'][0])
        for i in daddy:
            lis += i + ", "
        await ctx.send(lis)

    @commands.command(aliases=['syn', 'Synonym'], brief='Synonym')
    async def synonym(self, ctx, *, word):
        lis = ""
        r = requests.get(
            'https://www.dictionaryapi.com/api/v3/references/thesaurus/json/%s?key=' + tokens['synapi'] % word).json()
        daddy = (r[0]['meta']['syns'][0])
        for i in daddy:
            lis += i + ", "
        await ctx.send(lis)


def setup(client):
    client.add_cog(Language(client))
