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
        description='Vote Randy on top.gg and BFD',
        color=discord.Colour.from_rgb(r, g, b),
    )
    embed.add_field(name='BFD', value='https://botsfordiscord.com/bot/696185454759903264/vote')
    await ctx.send(embed=embed)


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


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


async def joinMusicChannel(ctx):
    try:
        channel = ctx.author.voice.channel
    except:
        await ctx.send("Please join a voice channel.")
        return False

    vc = ctx.voice_client
    if vc == None:
        await channel.connect()
    return True


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


def endSong(guild, path):
    os.remove(path)


@client.command()
async def play(ctx, *, url):
    data = await joinMusicChannel(ctx)
    songs = 0
    if data == True:
        results = YoutubeSearch(url, max_results=1).to_json()
        result = json.loads(results)
        formatted_data = result["videos"][0]["link"]
        title = result["videos"][0]["title"]
        final = "https://www.youtube.com" + formatted_data
        await ctx.send('Loading...')
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            file = ydl.extract_info(final, download=True)
        await ctx.channel.purge(limit=1)
        guild = ctx.message.guild
        voice_client = guild.voice_client
        path = str(file['title']) + "-" + str(file['id'] + ".mp3")
        queued.append(title)
        songs += 1
        voice_client.play(discord.FFmpegPCMAudio(path), after=lambda x: endSong(guild, path))
        voice_client.source = discord.PCMVolumeTransformer(voice_client.source, 1)
        await ctx.send(':musical_note: **Playing:** `' + title + '`')


@client.command()
async def queue(ctx):
    print(queued)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
    embed.set_author(name='Queue')
    embed.add_field(name=queued[0], value='1', inline=True)
    await ctx.send(embed=embed)


'''@client.command()
async def spotify(ctx, *, url):
    import subprocess
    y = url.split("/")
    z = y[4]
    command = 'curl -X "GET" "https://api.spotify.com/v1/playlists/' + z + '/tracks?market=ES&fields=items(added_by.id%2Ctrack(name%2Chref%2Calbum(name%2Chref)))&limit=100&offset=5" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer BQA_mONCRp0yJl7LUPeUl-usDBOel_H_Bv2laRvXTGI8RA1gXCsJj0XuuG4SgXHIBWhQjJGBYOyCQvwtDB3KWaPyhQgROB1sF4hVGnqMYeCPAOjM4WGWiF5guudZYU0FBNnttZKSWkuWe-bSCjGFBbAf4sxRFR0Jav-Pz5Z8vKAR"'
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    a = json.loads(out)
    def resultfunction(num):
        if num > -1:
            results = a['items'][num]['track']['name']
            return results
    x = 0
    data = await joinMusicChannel(ctx)
    if data == True:
        a = resultfunction(x)
        results = YoutubeSearch(str(a), max_results=1).to_json()
        x = x + 1
        result = json.loads(results)
        formatted_data = result["videos"][0]["link"]
        title = result["videos"][0]["title"]
        final = "https://www.youtube.com" + formatted_data
        await ctx.send('Loading...')
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            file = ydl.extract_info(final, download=True)
        await ctx.channel.purge(limit=1)
        guild = ctx.message.guild
        voice_client = guild.voice_client
        path = str(file['title']) + "-" + str(file['id'] + ".mp3")
        voice_client.play(discord.FFmpegPCMAudio(path), after=lambda x: endSong(guild, path))
        voice_client.source = discord.PCMVolumeTransformer(voice_client.source, 1)
        await ctx.send(':musical_note: **Playing:** `' + title + '`')'''


@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@client.command(pass_context=True)
async def leave(ctx):
    await ctx.voice_client.disconnect()


@client.command(pass_context=True)
async def pause(ctx):
    """Pauses currently playing song [Format: %pause]"""
    SongPlaying = ctx.voice_client.is_playing()
    Paused = ctx.voice_client.is_paused()
    if Paused != True:
        ctx.voice_client.pause()
        await ctx.send("**Song Paused**")
    else:
        if SongPlaying == True:
            await ctx.send("**The song is already paused.**")
        else:
            await ctx.send("**The song is already paused.**")


@client.command(pass_context=True)
async def resume(ctx):
    """Resumes a paused song [Format: %resume]"""
    Paused = ctx.voice_client.is_paused()
    if Paused == True:
        ctx.voice_client.resume()
        await ctx.send('**Resuming...**')
    else:
        await ctx.send('**The song is not paused**')


'''
@client.command(pass_contxt=True)
async def queue(ctx, url):
    server = ctx.message.server
    voice_client = ctx.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)

    if server.id in queues:
        queues[server.id].append(player)
    else:
        queues[server.id] = [player]
    await ctx.send('Video queued')
    '''


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
    embed.add_field(name='Bot Commands', value=aryaid + ', ' + ishaanid + ', ' + adityaid, inline=False)
    embed.add_field(name='Website', value=ishaanid, inline=False)
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
    embed.add_field(name='`>avatar (user)`', value=':clown: Avatar', inline=True)
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


@client.command(pass_context=True, aliases=['help_music'])
async def helpmusic(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
    embed.set_author(name='Music Commands')
    embed.add_field(name='`>join`', value=':thumbsup: Joins a voice channel', inline=True)
    embed.add_field(name='`>leave`', value=':thumbsdown: Leaves a voice channel', inline=True)
    embed.add_field(name='`>lyrics (singer),(song) [comma is necessary]`', value=':page_with_curl: Song Lyrics',
                    inline=True)
    embed.add_field(name='`>pause`', value=':speaker:  Resume a song!', inline=True)
    embed.add_field(name='`>play (name)`', value=':person_tipping_hand: Plays a song!', inline=True)
    embed.add_field(name='`>resume`', value=':mute: Pause a song!', inline=True)
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


def servermemberlista():
    x = 0
    y = 0
    for guild in client.guilds:
        for member in guild.members:
            x = x + 1
            # print(x)
    return x


def servermemberlistb():
    y = 0
    for guild in client.guilds:
        y = y + 1
    # y = y - 70
    return y


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    servers = client.guilds
    x = servermemberlista()
    y = servermemberlistb()
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game(name=">help for " + str(x) + ' users in ' + str(y) + " servers",
                                                       type=3))
    print('------')


client.run(TOKEN)
