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


    @commands.command(pass_context=True, brief='Flips a coin.', aliases=['Flip', 'coin', 'Coin'])
    async def flip(self, ctx):
        flip = random.choice(['Heads', 'Tails', 'lol, ngl the coin landed on the edge!'])
        await ctx.send(flip)



def setup(client):
    client.add_cog(Fun(client))
