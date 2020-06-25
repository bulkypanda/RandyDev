import discord
import json
import requests
import random
from discord.ext import commands
import covid19_data
import wikipediaapi

global tokens
with open('tokens.json', 'r') as l:
    tokens = json.load(l)

class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Info cog is online.")

    async def cv(self, ctx, id):
        id = ctx.message.author.id
        bruh = {
            "Authorization": tokens['topgg']}
        url = requests.get("https://top.gg/api/bots/696185454759903264/check?userId=" + str(id), headers=bruh).json()
        if url['voted'] == 1:
            return True

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
        id = ctx.message.author.id
        if await self.cv(ctx, id) == True:
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
        else:
            await ctx.send('You need to upvote the bot in order to access this command! Give it 5 minutes to update.')
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            embed = discord.Embed(
                title='Vote for Randy',
                color=discord.Colour.from_rgb(r, g, b),
            )
            embed.add_field(name='top.gg', value='https://top.gg/bot/696185454759903264/vote')
            embed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/706338290693046283/707085433552764968/RandyLogo.png')
            await ctx.send(embed=embed)

    @commands.command(brief='News from NYT', aliases=['nyt'])
    async def NYT(self, ctx):
        result = requests.get(
            "https://api.nytimes.com/svc/topstories/v2/home.json?api-key=" + tokens['NYT']).json()
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
    async def news(self, ctx, *, x):
        results = requests.get(
            'http://newsapi.org/v2/everything?q=' + x + '&apiKey=' + tokens['newsapi']).json()
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

    @commands.command()
    async def github(self, ctx, role, username):
        if role == 'user':
            username1 = username
            url = f"https://api.github.com/users/{username1}"
            response = requests.get(url).json()
            a = response["created_at"].split("T")
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            embed = discord.Embed(title=response['login'], color=discord.Colour.from_rgb(r, g, b))
            embed.add_field(name='Created on', value=a[0], inline=True)
            embed.add_field(name='Followers', value=response['followers'], inline=True)
            embed.add_field(name='Following', value=response['following'], inline=True)
            embed.set_thumbnail(url=response['avatar_url'])
            await ctx.send(embed=embed)
        if role == 'repo':
            username1 = username
            url = f"https://api.github.com/search/repositories?q={username1}"
            response = requests.get(url).json()
            a = response["items"][0]['created_at'].split("T")
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            embed = discord.Embed(title=response['items'][0]["name"], color=discord.Colour.from_rgb(r, g, b))
            embed.add_field(name='Created on', value=a[0], inline=True)
            embed.add_field(name='Language', value=response['items'][0]['language'], inline=True)
            embed.add_field(name='Description', value=response['items'][0]['description'], inline=False)
            embed.set_thumbnail(url=response['items'][0]['owner']['avatar_url'])
            await ctx.send(embed=embed)
    

def setup(client):
    client.add_cog(Info(client))
