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
TOKEN = 'NzA2MzM3NDg1MjYwNTg3MDQ4.Xq46bQ.gyak4rLejkdoPNqneuIRO0yA6vI'

# os.chdir(r'D:\BSD405-Bot')
client = commands.Bot(command_prefix='>')
players = {}
queues = {}
queued = ["why"]


@client.command()
async def servers(ctx):
    servers = list(client.guilds)
    await ctx.send(f"Connected on {str(len(servers))} servers:")
    await ctx.send('\n'.join(server.name for server in servers))
    for guild in client.guilds:
        print(guild)
        for member in guild.members:
            print(member)
        print(' ')


@client.command(aliases=['black', 'bj', 'blacks'])
async def blackjack(ctx):
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4

    async def deal(deck):
        hand = []
        for i in range(2):
            random.shuffle(deck)
            card = deck.pop()
            if card == 11:
                card = "J"
            if card == 12:
                card = "Q"
            if card == 13:
                card = "K"
            if card == 14:
                card = "A"
            hand.append(card)
        return hand

    async def total(hand):
        total = 0
        for card in hand:
            if card == "J" or card == "Q" or card == "K":
                total += 10
            elif card == "A":
                if total >= 11:
                    total += 1
                else:
                    total += 11
            else:
                total += card
        return total

    async def hit(hand):
        card = deck.pop()
        if card == 11:
            card = "J"
        if card == 12:
            card = "Q"
        if card == 13:
            card = "K"
        if card == 14:
            card = "A"
        hand.append(card)
        return hand

    async def print_results(dealer_hand, player_hand):
        await ctx.send("The dealer has a " + str(dealer_hand) + " for a total of " + str(await total(dealer_hand)))
        await ctx.send("You have a " + str(player_hand) + " for a total of " + str(await total(player_hand)))

    async def blackjack(dealer_hand, player_hand):
        if await total(player_hand) == 21:
            await print_results(dealer_hand, player_hand)
            await ctx.send("Congratulations! You got a Blackjack!\n")
        elif await total(dealer_hand) == 21:
            await print_results(dealer_hand, player_hand)
            await ctx.send("Sorry, you lose. The dealer got a blackjack.\n")

    async def score(dealer_hand, player_hand):
        if await total(player_hand) == 21:
            await print_results(dealer_hand, player_hand)
            await ctx.send("Congratulations! You got a Blackjack!\n")
        elif await total(dealer_hand) == 21:
            await print_results(dealer_hand, player_hand)
            await ctx.send("Sorry, you lose. The dealer got a blackjack.\n")
        elif await total(player_hand) > 21:
            await print_results(dealer_hand, player_hand)
            await ctx.send("Sorry. You busted. You lose.\n")
        elif await total(dealer_hand) > 21:
            await print_results(dealer_hand, player_hand)
            await ctx.send("Dealer busts. You win!\n")
        elif total(player_hand) < total(dealer_hand):
            await print_results(dealer_hand, player_hand)
            await ctx.send("Sorry. Your score isn't higher than the dealer. You lose")
        elif await total(player_hand) > total(dealer_hand):
            await print_results(dealer_hand, player_hand)
            await ctx.send("ur score is higher than the dealer. You win")

    def check(ctx):
        return lambda m: m.author == ctx.author and m.channel == ctx.channel

    async def get_input_of_type(func, ctx):
        while True:
            try:
                msg = await client.wait_for('message', check=check(ctx))
                return func(msg.content)
            except ValueError:
                continue

    await ctx.send("WELCOME TO BLACKJACK!")
    dealer_hand = await deal(deck)
    player_hand = await deal(deck)
    await ctx.send("The dealer is showing a " + str(dealer_hand[0]))
    await ctx.send("You have a " + str(player_hand) + " for a total of " + str(await total(player_hand)))
    await blackjack(dealer_hand, player_hand)
    quit = False
    while not quit:
        await ctx.send("Do you want to [H]it, [S]tand, or [Q]uit")
        choice = await get_input_of_type(str, ctx)
        choice = choice.lower()
        if choice == 'h':
            await hit(player_hand)
            await ctx.send(player_hand)
            await ctx.send("Hand total: " + str(await total(player_hand)))
            if await total(player_hand) > 21:
                await ctx.send('You busted')
                quit = True
        elif choice == 's':
            while await total(dealer_hand) < 17:
                await hit(dealer_hand)
                await ctx.send(dealer_hand)
                if await total(dealer_hand) > 21:
                    await ctx.send('Dealer busts, you win!')
                    quit = True
            await score(dealer_hand, player_hand)
        elif choice == "q":
            await ctx.send("Bye!")
            quit = True


@client.command(brief='Trivia')
async def trivia(ctx):
    results = requests.get('https://opentdb.com/api.php?amount=1&type=boolean').json()
    y = results['results'][0]['question'] + ' (T/F)'
    y = re.sub('&quot;', '"', y)
    await ctx.send(str(y))
    ans = results['results'][0]['correct_answer']
    us_ans = await get_input_of_type(str, ctx)
    if ans == 'True':
        ans = 'T'
    elif ans == 'False':
        ans = 'F'
    if ans == us_ans:
        await ctx.send('You are correct!')
    else:
        await ctx.send('You are wrong.')


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


@client.command(brief='Lyrics')
async def lyrics(ctx, *, arg):
    x = arg.split(',')
    lyrics = lyricwikia.get_lyrics(str(x[0]), str(x[1]))
    await ctx.send(lyrics[0:1900])
    await ctx.send(lyrics[1900:-1])


@client.command()
async def email(ctx, email, *, content):
    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = "anonymousrandyboy@gmail.com"
    receiver_email = email
    message = """\
    Subject: Sent from Randy-Discord Bot

    """ + content
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, 'randasswor2')
        server.sendmail(sender_email, receiver_email, message)
    await ctx.send('Email has been sent!')


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


@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "member-log":  # We check to make sure we are sending the message in the general channel
            await channel.send(f"""Welcome to the server {member.mention}!""")


@client.event
async def on_member_remove(member):
    for channel in member.guild.channels:
        if str(channel) == "member-log":  # We check to make sure we are sending the message in the general channel
            await channel.send(f"""Bye Bye {member.mention}!""")


@client.remove_command("help")
@client.command(pass_context=True)
async def help(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
    embed.set_author(name='Randy Command List')
    embed.add_field(name='`>about`', value=':eyes: About!', inline=True)
    embed.add_field(name='`>email (to) (message)`', value=':e_mail: Send an email!', inline=True)
    embed.add_field(name='`>vote`', value=':v: Vote for Randy!', inline=True)
    embed.add_field(name='`>feedback (feedback)`', value=':incoming_envelope: Feedback for devs.', inline=True)
    embed.add_field(name='`>server`', value='Link to invite Randy & help server', inline=True)
    embed.add_field(name='`>help_fun`', value=':smile: Fun Commands', inline=True)
    embed.add_field(name='`>help_info`', value=':newspaper: General Information', inline=True)
    embed.add_field(name='`>help_lang`', value=':blue_book: Language Commands', inline=True)
    embed.add_field(name='`>help_math`', value=':regional_indicator_m: Math Commands', inline=True)
    embed.add_field(name='`>help_mod`', value=':hammer_pick: Moderation Commands', inline=True)
    embed.add_field(name='`>help_money`', value=':moneybag: Money Commands', inline=True)
    embed.add_field(name='`>help_music`', value=':musical_note:  Music Commands', inline=True)
    embed.add_field(name='`>help_weather`', value=':cloud_tornado: Weather Commands', inline=True)
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
    # embed.add_field(name='`>help_fun_image`', value=':yum: Image Commands', inline=True)
    embed.add_field(name='`>joke`', value=':black_joker: Joke', inline=True)
    embed.add_field(name='`>meme`', value=':stuck_out_tongue_winking_eye: Sends a meme', inline=True)
    embed.add_field(name='`>trivia`', value=':smirk: Trivia!', inline=True)
    await ctx.send(embed=embed)


'''@client.command(pass_context=True, aliases=['help_fun_image'])
async def helpfunimage(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
    embed.set_author(name='Image Fun Commands')
    embed.add_field(name='`>avatar (user)`', value=':clown: Avatar', inline=True)
    embed.add_field(name='`>beautiful (user)`', value=':grimacing: Beautiful image of a user', inline=True)
    embed.add_field(name='`>blood (user)`', value=':drop_of_blood: Image of a user with blood', inline=True)
    embed.add_field(name='`>bobross (user)`', value=":paintbrush: Bobross painting a user's image", inline=True)
    embed.add_field(name='`>captcha (user) (text)`', value=":beverage_box: Captcha with a user's image", inline=True)
    embed.add_field(name='`>jackolantern (user)`', value=':jack_o_lantern: Jackolantern image of a user', inline=True)
    embed.add_field(name='`>prison (user)`', value=':police_officer: Image of a user in the prison', inline=True)
    embed.add_field(name='`>treasure (user)`', value=":moneybag: User's image on a treasure map", inline=True)
    embed.add_field(name='`>triggered (user)`', value=":triangular_flag_on_post: User's image with the triggered tag",
                    inline=True)
    embed.add_field(name='`>rainbow (user)`', value=":rainbow: Rainbow colors on a user's image", inline=True)
    embed.add_field(name='`>whatspokemon (user)`', value=":dog: User's image on a pokemon template", inline=True)
    await ctx.send(embed=embed)'''


@client.command(pass_context=True, aliases=['help_info'])
async def helpinfo(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
    embed.set_author(name='General Information Commands')
    embed.add_field(name='`>covid (place)`', value=':mask: Covid-19 Related info', inline=True)
    embed.add_field(name='`>news (topic)`', value=':newspaper: News', inline=True)
    embed.add_field(name='`>NYT`', value=':newspaper2: News from NYT', inline=True)
    embed.add_field(name='`>wiki (noun)`', value=':bookmark: Wikipedia', inline=True)
    await ctx.send(embed=embed)


@client.command(pass_context=True, aliases=['help_lang'])
async def helplanguage(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
    embed.set_author(name='Language Commands')
    embed.add_field(name='`>ant (word)`', value=':bookmark_tabs: Antonym', inline=True)
    embed.add_field(name='`>define (word)`', value=':notebook_with_decorative_cover: Dictionary', inline=True)
    embed.add_field(name='`>quote`', value=':orange_book: Quote', inline=True)
    embed.add_field(name='`>syn (word)`', value=':bookmark_tabs: Synonym', inline=True)
    embed.add_field(name='`>translate (src) (dest) (word)`', value=':earth_americas: Translate', inline=True)
    embed.add_field(name='`>urban (word)`', value=':closed_book: Urban Dictionary', inline=True)
    embed.add_field(name='`>wordoftheday`', value=':blue_book: Word of the day', inline=True)
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
    embed.add_field(name='`>currency (src) (dest) (value)`', value=':moneybag: Currency Conversion', inline=True)
    embed.add_field(name='`>stock (company)`', value=':money_with_wings: Stock', inline=True)
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


@client.command(pass_context=True, aliases=['help_weather'])
async def helpweather(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
    embed.set_author(name='Weather Commands')
    embed.add_field(name='`>humdidity (place)`', value=':hot_face: Humidity', inline=True)
    embed.add_field(name='`>temp (place)`', value=':cold_face: Temperature', inline=True)
    embed.add_field(name='`>tempfeels (place)`', value=':sweat: Temperature Feel', inline=True)
    embed.add_field(name='`>weather (place)`', value=':cold_sweat: Weather', inline=True)
    embed.add_field(name='`>wind (place)`', value=':wind_blowing_face: Wind', inline=True)
    await ctx.send(embed=embed)


@client.command(pass_context=True, aliases=['help_features'])
async def helpfeatures(ctx):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
    embed.set_author(name='Other Features')
    embed.add_field(name='Welcomes users on join', value='In channel member-log', inline=True)
    embed.add_field(name='Leave message on user leave', value='In channel member-log', inline=True)
    embed.add_field(name='>ping', value='Pings!', inline=True)
    embed.add_field(name='>website', value="Sends the bot's website", inline=True)
    await ctx.send(embed=embed)


@client.command()
async def feedback(ctx, *, msg):
    channel = client.get_channel(699699497206415401)
    await ctx.send('Feedback has been sent')
    await channel.send("\"" + str(msg).capitalize() + "\"" + ' from ' + ctx.message.author.mention)


'''@client.command(brief='Money Minigame!')
async def money(ctx):
    money = random.randint(0, 75)
    print('hi')
    await ctx.send('Ishaan donated ')
    print('hi')
    with open('money.json', 'r') as f:
        user = json.load(f)
        print('hi')
    await add_user(user)
    print('hi')
    with open('money.json', 'w') as f:
        json.dump(user, f)
        print('hi')
async def add_user(user):
    print('hello')
    for i in money.json:
        print('hello')
        if i == user.id:
            print('hello')
            user[user.id] = {}
            print('hello')
    print('yo')
    if user.id not in money.json:
        print('yo')
        print(user.id)
        print('yo')
        user[user.id] = {}
        print('yo')'''

'''
@client.event
async def on_member_join(member):
    with open('users.json', 'w') as f:
        users = users.load(f)
    for user in guild:
        for i in f:
            if f["userscores"][i] != user:
                with open('users.json', mode='w', encoding='utf-8') as feedsjson:
                    entry = {}
                    entry["userscores"]["user"] = i
                    entry["userscores"]['exp'] = 0
                    json.dump(entry, feedsjson)'''

'''@client.event
async def on_message(message):
    with open('users.json', 'r') as f:
        users = json.load(f)
    await update_data(users, message.author)
    await add_experience(users, message.author, 5)
    await level_up(users, message.author, message.channel)
    with open('users.json', 'w') as f:
        json.dump(users, f)
async def update_data(users, user):
async def update_data(users, user):
    for i in users.json:
        if i == user.id:
            users[user.id] = {}
            users[user.id]['experience'] = 0
            users[user.id]['level'] = 1

    if user.id not in users:
        print(user.id)
        users[user.id] = {}
        users[user.id]['experience'] = 0
        users[user.id]['level'] = 1
async def add_experience(users, user, exp):
    users[user.id]['experience'] += exp
async def level_up(users, user, channel):
    experience = users[user.id]['experience']
    lvl_start = users[user.id]['level']
    lvl_end = int(experience ** (1 / 4))
    if lvl_start < lvl_end:
        await client.send_message(channel, '{} has leveled up {}'.format(user.mention, lvl_end))
        users[user.id]['level'] = lvl_end
@client.event
async def on_member_remove(member):
    await client.send_message('Bye')'''


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
