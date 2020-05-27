# Work with Python 3.6
import smtplib
import ssl
import webbrowser
import discord
import requests
import random
import asyncio
import aiohttp
import urllib
import urllib.parse, urllib.request, re
import lyricwikia
import youtube_dl
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext.commands import has_permissions, CheckFailure
from discord.utils import get
from ftplib import FTP
from yahoo_fin import stock_info as si
from googletrans import Translator
from discord.voice_client import VoiceClient
from discord import FFmpegPCMAudio
from discord.utils import get
import sys
import os
# from dotenv import load_dotenv
import json
import ffmpeg
from youtube_search import YoutubeSearch

# load_dotenv()
# TOKEN = os.getenv("token")
TOKEN = ''

# os.chdir(r'D:\BSD405-Bot')
client = commands.Bot(command_prefix='>')


def check(ctx):
    return lambda m: m.author == ctx.author and m.channel == ctx.channel


async def get_input_of_type(func, ctx):
    while True:
        try:
            msg = await client.wait_for('message', check=check(ctx))
            return func(msg.content)
        except ValueError:
            continue


@client.command()
async def add(ctx):
    await ctx.send("What is the first number?")
    firstnum = await get_input_of_type(int, ctx)
    await ctx.send("What is the second number?")
    secondnum = await get_input_of_type(int, ctx)
    await ctx.send(f"{firstnum} + {secondnum} = {firstnum + secondnum}")


@client.command(aliases=['sub'])
async def subtract(ctx):
    await ctx.send("What is the first number?")
    firstnum = await get_input_of_type(int, ctx)
    await ctx.send("What is the second number?")
    secondnum = await get_input_of_type(int, ctx)
    await ctx.send(f"{firstnum} - {secondnum} = {firstnum - secondnum}")


@client.command(aliases=['multiply'])
async def mult(ctx):
    await ctx.send("What is the first number?")
    firstnum = await get_input_of_type(int, ctx)
    await ctx.send("What is the second number?")
    secondnum = await get_input_of_type(int, ctx)
    await ctx.send(f"{firstnum} * {secondnum} = {firstnum * secondnum}")


@client.command(aliases=['division', 'div'])
async def divide(ctx):
    await ctx.send("What is the first number?")
    firstnum = await get_input_of_type(int, ctx)
    await ctx.send("What is the second number?")
    secondnum = await get_input_of_type(int, ctx)
    await ctx.send(f"{firstnum} / {secondnum} = {firstnum / secondnum}")


@client.command()
async def vote(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(
        title='Vote for Randy',
        description='Vote for Randy',
        color=discord.Colour.from_rgb(r, g, b),
    )
    embed.add_field(name='BFD', value='https://botsfordiscord.com/bot/696185454759903264/vote')
    embed.add_field(name='top.gg', value='https://top.gg/bot/696185454759903264/vote')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/706338290693046283/707085433552764968/RandyLogo.png')
    embed.add_field(name='DBL', value='https://discordbotlist.com/bots/randy/upvote')
    await ctx.send(embed=embed)

    
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
    

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


@client.command()
async def reload(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    client.unload_extension(f'cogs.{extension}')


@client.command(brief='Kick')
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason='None'):
    await member.kick(reason=reason)
    await ctx.send('Kicked!')


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send('Sorry, you do not have permissions to kick users!')


@client.command(brief='Ban')
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason='None'):
    await member.ban(reason=reason)
    await ctx.send('Banned!')


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send('Sorry, you do not have permissions to ban users!')


@client.command(aliases=["arya", "Clear"], brief='Clear Messages')
@has_permissions(manage_messages=True)
async def clear(ctx, amount):
    amount = int(amount) + 1
    await ctx.channel.purge(limit=amount)


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send('Sorry, you do not have permissions to clear messages!')


@client.command(aliases=['msg', 'Message', 'broadcast', 'broad'], brief='Only for admins!')
@has_permissions(administrator=True)
async def message(ctx, *, message):
    amount = 1
    await ctx.channel.purge(limit=amount)
    await ctx.channel.send(message)


@message.error
async def message_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send('Sorry, you do not have permissions to broadcast!')


@client.command(brief="About the bot!", aliases=['About'], pass_context='True')
async def about(ctx):
    aryaid = '<@626913781779267594>'
    ishaanid = '<@469939274783916032>'
    adityaid = '<@410943247754592256>'
    razaid = '<@425315544070356992>'
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
    embed.set_author(name="Credits")
    embed.add_field(name='Bot Commands', value=aryaid + ', ' + ishaanid, inline=False)
    embed.add_field(name='Website', value=adityaid, inline=False)
    embed.add_field(name='Graphics', value=razaid, inline=False)
    await ctx.send(embed=embed)



@client.remove_command("help")
@client.command(pass_context=True)
async def help(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
    embed.set_author(name='Randy Command List')
    embed.add_field(name='`>about`', value=':eyes: About!', inline=True)
    embed.add_field(name='`>vote`', value=':v: Vote for Randy!', inline=True)
    embed.add_field(name='`>server`', value='Link to invite Randy & help server', inline=True)
    embed.add_field(name='`>help_fun`', value=':smile: Fun Commands', inline=True)
    embed.add_field(name='`>help_lang`', value=':blue_book: Language Commands', inline=True)
    embed.add_field(name='`>help_math`', value=':regional_indicator_m: Math Commands', inline=True)
    embed.add_field(name='`>help_mod`', value=':hammer_pick: Moderation Commands', inline=True)
    embed.add_field(name='`>help_money`', value=':moneybag: Money Commands', inline=True)
    embed.add_field(name='`>help_music`', value=':musical_note:  Music Commands', inline=True)
    embed.add_field(name='`>help_features`', value=':fork_and_knife: Other Features', inline=True)
    await ctx.send(embed=embed)


@client.command(pass_context=True, aliases=['help_fun'])
async def helpfun(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
    embed.set_author(name='Fun Commands')
    embed.add_field(name='`>8ball (question)`', value=':8ball: Predictions', inline=True)
    embed.add_field(name='`>dice`', value=':1234: Roll dice', inline=True)
    embed.add_field(name='`>flip`', value=':first_place: Flip coin', inline=True)
    await ctx.send(embed=embed)




@client.command(pass_context=True, aliases=['help_lang'])
async def helplanguage(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
    embed.set_author(name='Language Commands')
    embed.add_field(name='`>quote`', value=':orange_book: Quote', inline=True)
    embed.add_field(name='`>urban (word)`', value=':closed_book: Urban Dictionary', inline=True)
    await ctx.send(embed=embed)


@client.command(pass_context=True, aliases=['help_math'])
async def helpmath(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
    embed.set_author(name='General Information Commands')
    embed.add_field(name='`>add`', value=':heavy_plus_sign: Add numbers', inline=True)
    embed.add_field(name='`>sub`', value=':heavy_minus_sign: Subtract numbers', inline=True)
    embed.add_field(name='`>mult`', value=':x: Multiply numbers', inline=True)
    embed.add_field(name='`>div`', value=':heavy_division_sign: Divide numbers', inline=True)
    await ctx.send(embed=embed)


@client.command(pass_context=True, aliases=['help_moderator', 'help_mod'])
async def helpmoderator(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
    embed.set_author(name='Moderation Commands')
    embed.add_field(name='>ban (user)', value=':hammer: Bans a user', inline=True)
    # embed.add_field(name='>unban (user)', value=':hammer: Unbans a user', inline=True)
    embed.add_field(name='>kick (user)', value=':interrobang: Kicks a user', inline=True)
    embed.add_field(name='>clear (num)', value=':x: Clear messages', inline=True)
    embed.add_field(name='>msg (broadcast)', value=':loudspeaker: Broadcast a message', inline=True)
    await ctx.send(embed=embed)


@client.command(pass_context=True, aliases=['help_money'])
async def helpmoney(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
    embed.set_author(name='Money Commands')
    embed.add_field(name='`>bitcoin`', value=':money_mouth: Bitcoin value', inline=True)
    await ctx.send(embed=embed)


@client.command(pass_context=True, aliases=['help_features'])
async def helpfeatures(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
    embed.set_author(name='Other Features')
    embed.add_field(name='>ping', value='Pings!', inline=True)
    embed.add_field(name='>website', value="Sends the bot's website", inline=True)
    await ctx.send(embed=embed)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
