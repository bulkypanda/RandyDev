# Work with Python 3.6
import discord
from discord.ext import commands
import requests
import random
import json
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get
import os
import sys
import re
import bs4
from googletrans import Translator
from discord.voice_client import VoiceClient
#from discord import FFmpegPCMAudio
from discord.utils import get
from PIL import Image
import requests
from io import BytesIO
import time

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun cog is online.")

    @commands.command(brief='TicTacToe')
    async def tictactoe(self, ctx, user):
        await ctx.send("Start the game by reacting to one of the emoji's")
        msg = await ctx.send("working")
        reactions = ['RandyLogo']
        for emoji in reactions:
            await ctx.add_reaction(msg, emoji)

    @commands.command(aliases=['Dice', 'role', 'Role'])
    async def dice(self, ctx):
        await ctx.send(random.randint(1, 6))

    @commands.command(name='8ball',
                      description="Answers a yes/no question.",
                      brief="Answers from the beyond.",
                      aliases=['eight_ball', 'eightball', '8-ball'],
                      pass_context=True)
    async def eight_ball(self, ctx):
        possible_responses = [
            'That is a resounding no',
            'It is not looking likely',
            'Too hard to tell',
            'It is quite possible',
            'Definitely',
        ]
        await ctx.send(random.choice(possible_responses) + ", " + ctx.message.author.mention)

    @commands.command(brief="Shares a Chuck Norris joke!", aliases=['Joke'])
    async def joke(self, ctx):
        results = requests.get('http://api.icndb.com/jokes/random')
        y = json.loads(results.content)
        z = y["value"]
        joke = z["joke"]
        final = re.sub('&quot;', '"', joke)
        await ctx.send(final)

    @commands.command(brief="Prison")
    async def prison(self, ctx, member: discord.Member):
        API = '{}'.format(member.avatar_url)
        results = ('https://eclyssia-api.tk/api/v1/prison?url=' + API)
        final = re.sub('webp', 'png', results)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        show_avatar = discord.Embed(
            color=discord.Colour.from_rgb(r, g, b)
        )
        show_avatar.set_image(url=final)
        await ctx.send(embed=show_avatar)

    @commands.command(brief="Beautiful")
    async def beautiful(self, ctx, member: discord.Member):
        API = '{}'.format(member.avatar_url)
        results = ('https://eclyssia-api.tk/api/v1/beautiful?url=' + API)
        final = re.sub('webp', 'png', results)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        show_avatar = discord.Embed(
            color=discord.Colour.from_rgb(r, g, b)
        )
        show_avatar.set_image(url=final)
        await ctx.send(embed=show_avatar)

    @commands.command(brief="Blood")
    async def blood(self, ctx, member: discord.Member):
        API = '{}'.format(member.avatar_url)
        results = ('https://eclyssia-api.tk/api/v1/blood?url=' + API)
        final = re.sub('webp', 'png', results)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        show_avatar = discord.Embed(
            color=discord.Colour.from_rgb(r, g, b)
        )
        show_avatar.set_image(url=final)
        await ctx.send(embed=show_avatar)

    @commands.command(brief="Bobross")
    async def bobross(self, ctx, member: discord.Member):
        API = '{}'.format(member.avatar_url)
        results = ('https://eclyssia-api.tk/api/v1/bobross?url=' + API)
        final = re.sub('webp', 'png', results)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        show_avatar = discord.Embed(
            color=discord.Colour.from_rgb(r, g, b)
        )
        show_avatar.set_image(url=final)
        await ctx.send(embed=show_avatar)

    @commands.command(brief="Jackolantern")
    async def jackolantern(self, ctx, member: discord.Member):
        API = '{}'.format(member.avatar_url)
        results = ('https://eclyssia-api.tk/api/v1/jackolantern?url=' + API)
        final = re.sub('webp', 'png', results)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        show_avatar = discord.Embed(
            color=discord.Colour.from_rgb(r, g, b)
        )
        show_avatar.set_image(url=final)
        await ctx.send(embed=show_avatar)

    @commands.command(brief="Treasure")
    async def treasure(self, ctx, member: discord.Member):
        API = '{}'.format(member.avatar_url)
        results = ('https://eclyssia-api.tk/api/v1/treasure?url=' + API)
        final = re.sub('webp', 'png', results)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        show_avatar = discord.Embed(
            color=discord.Colour.from_rgb(r, g, b)
        )
        show_avatar.set_image(url=final)
        await ctx.send(embed=show_avatar)

    @commands.command(brief="captcha")
    async def captcha(self, ctx, member: discord.Member, *, cot):
        API = '{}'.format(member.avatar_url)
        results = ('https://eclyssia-api.tk/api/v1/captcha?username=' + cot + '&url=' + API)
        final = re.sub('webp', 'png', results)
        final = re.sub(' ', '+', final)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        show_avatar = discord.Embed(
            color=discord.Colour.from_rgb(r, g, b)
        )
        show_avatar.set_image(url=final)
        await ctx.send(embed=show_avatar)

    @commands.command(brief="Triggered")
    async def triggered(self, ctx, member: discord.Member):
        API = '{}'.format(member.avatar_url)
        results = ('https://eclyssia-api.tk/api/v1/triggered?url=' + API)
        final = re.sub('webp', 'png', results)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        show_avatar = discord.Embed(
            color=discord.Colour.from_rgb(r, g, b)
        )
        show_avatar.set_image(url=final)
        await ctx.send(embed=show_avatar)

    @commands.command(brief="Rainbow")
    async def rainbow(self, ctx, member: discord.Member):
        API = '{}'.format(member.avatar_url)
        results = ('https://eclyssia-api.tk/api/v1/rainbow?url=' + API)
        final = re.sub('webp', 'png', results)
        print(final)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        show_avatar = discord.Embed(
            color=discord.Colour.from_rgb(r, g, b)
        )
        show_avatar.set_thumbnail(url=final)
        await ctx.send(embed=show_avatar)

    @commands.command(brief='Avatar')
    async def avatar(self, ctx, member: discord.Member):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        show_avatar = discord.Embed(
            color=discord.Colour.from_rgb(r, g, b)
        )
        show_avatar.set_image(url='{}'.format(member.avatar_url))
        await ctx.send(embed=show_avatar)

    @commands.command(brief="Whatspokemon")
    async def whatspokemon(self, ctx, member: discord.Member):
        API = '{}'.format(member.avatar_url)
        results = ('https://eclyssia-api.tk/api/v1/whatspokemon?url=' + API)
        final = re.sub('webp', 'png', results)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        show_avatar = discord.Embed(
            color=discord.Colour.from_rgb(r, g, b)
        )
        show_avatar.set_image(url=final)
        await ctx.send(embed=show_avatar)

    @commands.command(brief='Sends a meme!')
    async def meme(self, ctx):
        results = requests.get('https://meme-api.herokuapp.com/gimme').json()
        meme = results['url']
        await ctx.send(meme)

    @commands.command(pass_context=True, brief='Flips a coin.', aliases=['Flip', 'coin', 'Coin'])
    async def flip(self, ctx):
        flip = random.choice(['Heads', 'Tails', 'lol, ngl the coin landed on the edge!'])
        await ctx.send(flip)

    @commands.command(aliases=["office"])
    async def officequote(self, ctx):
        print("hi1")
        with open("officequotes.json", 'r') as f:
            print("hi2")
            data = json.load(f)
            print("hi3")
        print("hi4")
        print(data.get["quotes"])
        print('hi5')
        # await ctx.send(str(quote["quotes"][random.randint(1,2)]["quote"]))

    @commands.command()
    async def nice(self, ctx):
        nicelist = ["69", "ecin", "420", "Are you Arya?"]
        await ctx.send(random.choice(nicelist))

    @commands.command(brief='Type')
    async def type(self, ctx):
        i = 1
        while i < 3:
            async with ctx.typing():
                time.sleep(5)




def setup(client):
    client.add_cog(Fun(client))
