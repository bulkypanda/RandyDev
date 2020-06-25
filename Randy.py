import smtplib
import ssl
import discord
import time
import requests
import random
import re
from discord.ext import commands
from discord.ext.commands import MissingPermissions
from discord.ext.commands import has_permissions
from googletrans import Translator
import os
import json
import sqlite3



global tokens
with open('tokens.json', 'r') as l:
    tokens = json.load(l)

TOKEN = tokens['bottoken']

client = commands.Bot(command_prefix=">")
translator = Translator()


@client.command()
async def userinfo(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author
    roles = [role for role in member.roles]
    embed = discord.Embed(title='User Info', colour=member.color, timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_author(name=f'{member}', icon_url=member.avatar_url)
    embed.set_footer(text=f'Requested by {ctx.author}')
    embed.add_field(name='Name', value=f'{member}', inline=True)
    embed.add_field(name='ID:', value=member.id, inline=True)
    embed.add_field(name='Guild Name:', value=member.display_name, inline=False)
    embed.add_field(name='Created At:', value=member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'), inline=False)
    embed.add_field(name='Joined At:', value=member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'), inline=False)
    embed.add_field(name=f'Roles ({len(roles)})', value=" ".join([role.mention for role in roles]), inline=False)
    embed.add_field(name='Top Role:', value=member.top_role.mention, inline=False)
    await ctx.send(embed=embed)



@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "member-log":
            await channel.send(f"""Welcome to the server {member.mention}!""")

    await update_data(member)


@client.event
async def on_message(message):
    if message.author.bot == False:
        await update_data(message.author)
        await add_experience(message.author, 5)
        await level_up(message.author, message)

    await client.process_commands(message)


async def update_data(user):
    sqliteConnection = sqlite3.connect(r'C:\sqlite\users.db')
    cursor = sqliteConnection.cursor()
    a = user.id
    a = str(a)
    b = cursor.execute('Select userid from usersjson where userid = ?', (a,))
    c = b.fetchone()
    if c is None:
        cursor.execute("INSERT INTO usersjson (userid, experience, level) VALUES(?, ?, ?)",
                       (a, 0, 1))
        sqliteConnection.commit()
        cursor.close()


async def add_experience(user, exp):
    sqliteConnection = sqlite3.connect(r'C:\sqlite\users.db')
    cursor = sqliteConnection.cursor()
    a = user.id
    a = str(a)
    c = cursor.execute('Select experience from usersjson where userid = ?', (a,))
    c = c.fetchone()
    c = c[0]
    c = c + 5
    cursor.execute('Update usersjson SET experience = ? where userid = ?', (c, a))
    sqliteConnection.commit()
    cursor.close()


async def level_up(user, message):
    sqliteConnection = sqlite3.connect(r'C:\sqlite\users.db')
    cursor = sqliteConnection.cursor()
    a = user.id
    a = str(a)
    c = cursor.execute('Select experience from usersjson where userid = ?', (a,))
    c = c.fetchone()
    c = c[0]
    experience = c
    d = cursor.execute('Select level from usersjson where userid = ?', (a,))
    d = d.fetchone()
    d = d[0]
    lvl_start = d
    lvl_end = int(experience ** (1 / 4))
    sqliteConnection.commit()
    cursor.close()
    if lvl_start < lvl_end:
        sqliteConnection = sqlite3.connect(r'C:\sqlite\users.db')
        cursor = sqliteConnection.cursor()
        cursor.execute('Update usersjson SET level = ? where userid = ?', (lvl_end, a,))
        guild = message.guild
        f = guild.id
        sqliteConnection.commit()
        cursor.close()
        sqliteConnection = sqlite3.connect(r'C:\sqlite\users.db')
        cursor = sqliteConnection.cursor()
        e = cursor.execute('Select * from levelsjson where  guildid = ?', (f,))
        e = e.fetchall()
        e = e[0][1]
        sqliteConnection.commit()
        cursor.close()
        if e == 'on':
            sqliteConnection = sqlite3.connect(r'C:\sqlite\users.db')
            cursor = sqliteConnection.cursor()
            d = cursor.execute('Select level from usersjson where userid = ?', (a,))
            d = d.fetchone()
            d = d[0]
            lvl = d
            sqliteConnection.commit()
            cursor.close()
            await message.add_reaction('lev: 712873162437820427')
            await message.add_reaction('🇻')
            await message.add_reaction('🇱')
            a = list(str(lvl))
            n = 1
            o = 1
            p = 1
            q = 1
            r = 1
            s = 1
            t = 1
            u = 1
            v = 1
            w = 1
            for i in a:
                if i == '1':
                    if n == 1:
                        await message.add_reaction('1️⃣')
                        n = n + 1
                    elif n == 2:
                        await message.add_reaction('one: 712884652918177822')
                if i == '2':
                    if o == 1:
                        await message.add_reaction('2️⃣')
                        o = o + 1
                    elif 0 == 2:
                        await message.add_reaction('two: 712887818111680513')
                if i == '3':
                    if p == 1:
                        await message.add_reaction('3️⃣')
                        p = p + 1
                    elif p == 2:
                        await message.add_reaction('three: 712887844300914738')
                if i == '4':
                    if q == 1:
                        await message.add_reaction('4️⃣')
                        q = q + 1
                    elif q == 2:
                        await message.add_reaction('four: 712887869244571658')
                if i == '5':
                    if r == 1:
                        await message.add_reaction('5️⃣')
                        r = r + 1
                    elif r == 2:
                        await message.add_reaction('five: 712887892547993660')
                if i == '6':
                    if s == 1:
                        await message.add_reaction('6️⃣')
                        s = s + 1
                    elif s == 2:
                        await message.add_reaction('six: 712887915218206741')
                if i == '7':
                    if t == 1:
                        await message.add_reaction('7️⃣')
                        t = t + 1
                    elif t == 2:
                        await message.add_reaction('seven: 712887949284343840')
                if i == '8':
                    if u == 1:
                        await message.add_reaction('8️⃣')
                        u = u + 1
                    elif u == 2:
                        await message.add_reaction('eight: 712887971434725404')
                if i == '9':
                    if v == 1:
                        await message.add_reaction('9️⃣')
                        v = v + 1
                    elif v == 2:
                        await message.add_reaction('nine: 712887993102237790')
                if i == '0':
                    if w == 1:
                        await message.add_reaction('0️⃣')
                        w = w + 1
                    elif w == 2:
                        await message.add_reaction('zero: 712888015869050919')


@client.command()
async def removemydata(ctx):
    await ctx.send(
        'Are you sure you want to delete your data? All your progress in the level system will be lost! (Y/N)')
    a = await get_input_of_type(str, ctx)
    a = a.capitalize()
    if a == 'Y':
        a = ctx.message.author.id
        sqliteConnection = sqlite3.connect(r'C:\sqlite\users.db')
        cursor = sqliteConnection.cursor()
        cursor.execute("DELETE FROM usersjson WHERE userid = ?",
                       (a,))
        sqliteConnection.commit()
        cursor.close()
        await ctx.send('Your data has been successfully deleted!')
    if a == 'N':
        await ctx.send("Alright, let's pretend that never happened!")


@client.command(aliases=['top'])
async def globalleaderboard(ctx):
    sqliteConnection = sqlite3.connect(r'C:\sqlite\users.db')
    cursor = sqliteConnection.cursor()
    c = cursor.execute('select * from usersjson order by experience desc  limit 3')
    c = c.fetchall()
    b = c[0][0]
    d = c[1][0]
    f = c[2][0]
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    embed = discord.Embed(title='Leaderboard', description='Top Globally',
                          color=discord.Colour.from_rgb(red, green, blue), )
    user1 = client.get_user(int(b))
    user2 = client.get_user(int(d))
    user3 = client.get_user(int(f))
    embed.add_field(name='1st Place',
                    value=str(user1) + ' with ' + str(c[0][1]) + ' experience points (level ' + str(c[0][2]) + ')')
    embed.add_field(name='2nd Place',
                    value=str(user2) + ' with ' + str(c[1][1]) + ' experience points (level ' + str(c[1][2]) + ')')
    embed.add_field(name='3rd Place',
                    value=str(user3) + ' with ' + str(c[2][1]) + ' experience points (level ' + str(c[2][2]) + ')')
    await ctx.send(embed=embed)
    sqliteConnection.commit()
    cursor.close()


@client.command()
async def level(ctx, member: discord.Member = None):
    if not member:
        id = ctx.message.author.id
        id = str(id)
        sqliteConnection = sqlite3.connect(r'C:\sqlite\users.db')
        cursor = sqliteConnection.cursor()
        c = cursor.execute('Select level from usersjson where userid = ?', (id,))
        c = c.fetchone()
        c = c[0]
        lvl = c
        await ctx.send(f'You are at level {lvl}!')
        sqliteConnection.commit()
        cursor.close()
    else:
        id = member.id
        id = str(id)
        sqliteConnection = sqlite3.connect(r'C:\sqlite\users.db')
        cursor = sqliteConnection.cursor()
        c = cursor.execute('Select level from usersjson where userid = ?', (id,))
        c = c.fetchone()
        c = c[0]
        lvl = c
        await ctx.send(f'{member} is at level {lvl}!')
        sqliteConnection.commit()
        cursor.close()


@client.command()
@has_permissions(manage_messages=True)
async def levels(ctx, arg):
    if arg == 'on':
        a = ctx.guild.id
        sqliteConnection = sqlite3.connect(r'C:\sqlite\users.db')
        cursor = sqliteConnection.cursor()
        cursor.execute('update levelsjson set tf = ? where guildid = ?', ('on', a))
        sqliteConnection.commit()
        cursor.close()
        await ctx.send('Levelling reactions have been turned on!')
    if arg == 'off':
        a = ctx.guild.id
        sqliteConnection = sqlite3.connect(r'C:\sqlite\users.db')
        cursor = sqliteConnection.cursor()
        cursor.execute('update levelsjson set tf = ? where guildid = ?', ('off', a))
        sqliteConnection.commit()
        cursor.close()
        await ctx.send('Levelling reactions have been turned off.')


@levels.error
async def levels_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("Sorry, you do not have permissions to change this setting!")


@client.event
async def on_guild_join(guild):
    a = guild.id
    sqliteConnection = sqlite3.connect(r'C:\sqlite\users.db')
    cursor = sqliteConnection.cursor()
    cursor.execute("INSERT INTO levelsjson (guildid, tf) VALUES(?, ?)",
                   (a, "off"))
    sqliteConnection.commit()
    cursor.close()


@client.event
async def on_guild_remove(guild):
    a = guild.id
    sqliteConnection = sqlite3.connect(r'C:\sqlite\users.db')
    cursor = sqliteConnection.cursor()
    cursor.execute("DELETE FROM levelsjson WHERE guildid = ?",
                   (a,))
    sqliteConnection.commit()
    cursor.close()



@client.command()
async def servers(ctx):
    servers = list(client.guilds)
    await ctx.send(f"Connected on {str(len(servers))} servers!")


@client.command()
async def bruhs(ctx):
    servers = list(client.guilds)
    await ctx.send(f"Connected on {str(len(servers))} servers:")
    await ctx.send('\n'.join(server.name for server in servers))


@client.command()
async def rip(ctx):
    await ctx.send("Guilds with <3 users:")
    for guild in client.guilds:
        if len(guild.members) < 3:
            await ctx.send(f"{guild.name}")


@client.command(aliases=['guess', 'guessnum', 'guessnumber'])
async def ngg(ctx):
    await ctx.send("Number guessing game!")
    number = random.randint(1, 9)
    chances = 0
    await ctx.send("Guess a number (between 1 and 9):")
    while chances < 3:
        guess = await get_input_of_type(int, ctx)
        if guess == number:
            await ctx.send("Congratulation YOU WON!!!")
            break
        elif guess < number:
            await ctx.send("Your guess was too low: Guess a number higher than " + str(guess))
            chances += 1
        else:
            await ctx.send("Your guess was too high: Guess a number lower than " + str(guess))
            chances += 1
    if not chances < 3:
        await ctx.send("YOU LOSE!!! The number is " + str(number))


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


@client.command(pass_context=True, aliases=['nickname'])
@has_permissions(manage_nicknames=True)
async def nick(ctx, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    await ctx.send('Enter nickname: ')
    nick = await get_input_of_type(str, ctx)
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')


@nick.error
async def nick_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("Sorry, you do not have permissions to change users' nickname!")


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
    firstnum = await get_input_of_type(float, ctx)
    await ctx.send("What is the second number?")
    secondnum = await get_input_of_type(float, ctx)
    await ctx.send(f"{firstnum} + {secondnum} = {firstnum + secondnum}")


@client.command(aliases=['sub'])
async def subtract(ctx):
    await ctx.send("What is the first number?")
    firstnum = await get_input_of_type(float, ctx)
    await ctx.send("What is the second number?")
    secondnum = await get_input_of_type(float, ctx)
    await ctx.send(f"{firstnum} - {secondnum} = {firstnum - secondnum}")


@client.command(aliases=['multiply'])
async def mult(ctx):
    await ctx.send("What is the first number?")
    firstnum = await get_input_of_type(float, ctx)
    await ctx.send("What is the second number?")
    secondnum = await get_input_of_type(float, ctx)
    await ctx.send(f"{firstnum} * {secondnum} = {firstnum * secondnum}")


@client.command(aliases=['division', 'div'])
async def divide(ctx):
    await ctx.send("What is the first number?")
    firstnum = await get_input_of_type(float, ctx)
    await ctx.send("What is the second number?")
    secondnum = await get_input_of_type(float, ctx)
    await ctx.send(f"{firstnum} / {secondnum} = {firstnum / secondnum}")


@client.command(brief='Lyrics')
async def lyrics(ctx, *, song):
    song = 'http://some-random-api.ml/lyrics?title=' + song
    song = re.sub(' ', '%20', song)
    lyrics = requests.get(song).json()
    lyrics = lyrics['lyrics']
    await ctx.send(lyrics[0:1900])
    await ctx.send(lyrics[1900:-1])


@client.command()
async def email(ctx, email, *, content):
    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = tokens['email']
    receiver_email = email
    message = """\
    Subject: Sent from Randy-Discord Bot

    """ + content
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, tokens['password'])
        server.sendmail(sender_email, receiver_email, message)
    await ctx.send('Email has been sent!')


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
    embed.add_field(name='BFD', value='[Vote here](https://botsfordiscord.com/bot/696185454759903264/vote)')
    embed.add_field(name='top.gg', value='[Vote here](https://top.gg/bot/696185454759903264/vote)')
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/706338290693046283/707085433552764968/RandyLogo.png')
    embed.add_field(name='DBL', value='[Vote here](https://discordbotlist.com/bots/randy/upvote)')
    embed.add_field(name='Bulkypanda Discord Bio', value='[Vote here](https://dsc.bio/bulkypanda)')
    embed.add_field(name='Hvhvuu Discord Bio', value='[Vote here](https://dsc.bio/hvhvuu)')
    await ctx.send(embed=embed)


@client.command()
async def chat(ctx):
    await ctx.send('Hello!')
    text = await get_input_of_type(str, ctx)
    if text == 'stop':
        await ctx.send('Nice talking to you, cya!')
    result = requests.get('https://some-random-api.ml/chatbot?message=' + text).json()
    response = result['response']
    try:
        await ctx.send(response)
    except:
        await ctx.send('ok')
    inp = await get_input_of_type(str, ctx)
    if inp == 'stop':
        await ctx.send('Nice talking to you, cya!')
    while inp != 'stop':
        result = requests.get('https://some-random-api.ml/chatbot?message=' + inp).json()
        response = result['response']
        try:
            await ctx.send(response)
        except:
            await ctx.send('ok')
        inp = await get_input_of_type(str, ctx)
        if inp == 'stop':
            await ctx.send('Nice talking to you, cya!')


@client.command(brief='Translations')
async def trans(ctx, src, dest, tim):
    await ctx.send('Translation has started!')
    x = float(tim) * 60
    y = time.time()
    while str(y) < str(x):
        inp = await get_input_of_type(str, ctx)
        translated = translator.translate(inp, src=src, dest=dest)
        await ctx.send(translated.text)
        end = time.time()
        y = int(end) - int(y)
        y = str(y)
    await ctx.send('Translation has ended!')


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


@client.command(brief='Unban')
@has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return


@unban.error
async def unban_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send('Sorry, you do not have permissions to unban users!')


@client.command()
@has_permissions(manage_roles=True)
async def mute(ctx, members: commands.Greedy[discord.Member], *, reason=""):
    if len(members) < 1:
        return await ctx.send("Please specify a user!")
    for member in members:
        await ctx.channel.set_permissions(member, send_messages=False, reason=reason)
    await ctx.send("Successfully muted {1} {0}".format("for " + reason if not reason == "" else "",
                                                       ", ".join(["<@" + str(member.id) + ">" for member in members])))


@mute.error
async def mute_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send('Sorry, you do not have permissions to mute users!')


@client.command()
@has_permissions(manage_roles=True)
async def unmute(ctx, members: commands.Greedy[discord.Member], *, reason=""):
    if len(members) < 1:
        return await ctx.send("Please specify a user!")
    for member in members:
        await ctx.channel.set_permissions(member, send_messages=None, reason=reason)
    await ctx.send("Successfully unmuted {1} {0}".format("for " + reason if not reason == "" else "", ", ".join(
        ["<@" + str(member.id) + ">" for member in members])))


@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send('Sorry, you do not have permissions to unmute users!')


@client.command()
@has_permissions(manage_messages=True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send('Locked!')


@lock.error
async def lock_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send('Sorry, you do not have permissions to lock channels!')


@client.command()
@has_permissions(manage_messages=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send('Unlocked!')


@unlock.error
async def unlock_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send('Sorry, you do not have permissions to unlock channels!')


@client.command(aliases=["arya", "Clear"], brief='Clear Messages')
@has_permissions(manage_messages=True)
async def clear(ctx, amount):
    amount = int(amount) + 1
    await ctx.channel.purge(limit=amount)


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send('Sorry, you do not have permissions to clear messages!')


@client.command()
async def ids(ctx):
    for guild in client.guilds:
        print(guild.id)


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


@client.command(aliases=['dev'])
async def script(ctx):
    await ctx.send('https://github.com/bulkypanda/RandyDev')


async def cv(ctx, id):
    bruh = {"Authorization": tokens['topgg']}
    url = requests.get("https://top.gg/api/bots/696185454759903264/check?userId=" + str(id), headers=bruh).json()
    if url['voted'] == 1:
        return True


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
    embed.add_field(name='Website', value=aryaid, inline=False)
    embed.add_field(name='Graphics', value=razaid, inline=False)
    await ctx.send(embed=embed)


@client.event
async def on_member_remove(member):
    for channel in member.guild.channels:
        if str(channel) == "member-log":  # We check to make sure we are sending the message in the general channel
            await channel.send(f"""Bye Bye {member.mention}!""")


@client.remove_command("help")
@client.command(pass_context=True)
async def help(ctx, arg='yo'):
    if arg == 'yo':
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(title="Randy Command List", color=discord.Colour.from_rgb(r, g, b))
        embed.set_author(name=f'Randy',
                         icon_url='https://cdn.discordapp.com/attachments/711007670924083221/719285425008803910/RandyPFP.png')
        embed.add_field(name='`>about`', value=':eyes: About!', inline=True)
        # embed.add_field(name='`>changeprefix (prefix)`', value=':100: Change the bot prefix!', inline=True)
        embed.add_field(name='`>email (to) (message)`', value=':e_mail: Send an email!', inline=True)
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/706665974484566138/717442170214154320/1200px-Fist.svg.webp')
        # embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/706338290693046283/707085433552764968/RandyLogo.png')
        embed.add_field(name='`>vote`', value=':v: Vote for Randy!', inline=True)
        embed.add_field(name='`>feedback (feedback)`', value=':incoming_envelope: Feedback for devs.',
                        inline=True)
        embed.add_field(name='`>server`', value='Link to invite Randy & help server', inline=True)
        embed.add_field(name='`>help fun`', value=':smile: Fun Commands', inline=True)
        embed.add_field(name='`>help image`', value=':yum: Image Commands', inline=True)
        embed.add_field(name='`>help info`', value=':newspaper: General Information', inline=True)
        embed.add_field(name='`>help lang`', value=':blue_book: Language Commands', inline=True)
        embed.add_field(name='`>help level`', value='🆙 Level System Commands', inline=True)
        embed.add_field(name='`>help math`', value=':regional_indicator_m: Math Commands', inline=True)
        embed.add_field(name='`>help mg`', value=':video_game: Minigames!', inline=True)
        embed.add_field(name='`>help mod`', value=':hammer_pick: Moderation Commands', inline=True)
        embed.add_field(name='`>help money`', value=':moneybag: Money Commands', inline=True)
        embed.add_field(name='`>help music`', value=':musical_note:  Music Commands', inline=True)
        embed.add_field(name='`>help text`', value=':regional_indicator_t: Text Manipulation Commands',
                        inline=True)
        embed.add_field(name='`>help util`', value=':fork_and_knife: Utility Commands', inline=True)
        embed.add_field(name='`>help weather`', value=':cloud_tornado: Weather Commands', inline=True)
        await ctx.send(embed=embed)
    elif arg == 'fun':
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
        embed.set_author(name='Fun Commands')
        embed.add_field(name='`>8ball (question)`', value=':8ball: Predictions', inline=True)
        embed.add_field(name='`>animal (animal)`',
                        value=':dog: Animal images (Dog, Cat, Panda, Red Panda, Birb, Fox, Koala, Kngaroo, Racoon)',
                        inline=True)
        embed.add_field(name='`>anime (anime)`', value=':tv: Anime Info', inline=True)
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/706665974484566138/717442170214154320/1200px-Fist.svg.webp')
        # embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/706338290693046283/707085433552764968/RandyLogo.png')
        embed.add_field(name='`>avatar (user)`', value=':clown: Avatar', inline=True)
        embed.add_field(name='`>chat`', value=":speech_balloon: Chat with the bot, 'stop' to stop", inline=True)
        embed.add_field(name='`>dice`', value=':1234: Roll dice', inline=True)
        embed.add_field(name='`>fact (animal)`',
                        value=':paperclip: Animal facts (Dog, Cat, Panda, Bird, Koala, Racoon, Kangaroo, Elephant, Giraffe, Whale)',
                        inline=True)
        embed.add_field(name='`>flip`', value=':first_place: Flip coin', inline=True)
        embed.add_field(name='`>gif (gif)`', value=':gift: GIFs', inline=True)
        embed.add_field(name='`>img (image)`', value=':flag_im: Google Image Search', inline=True)
        embed.add_field(name='`>userinfo (user)`', value=':frame_photo: User Info', inline=True)
        embed.add_field(name='`>joke`', value=':black_joker: Joke', inline=True)
        embed.add_field(name='`>meme`', value=':stuck_out_tongue_winking_eye: Sends a meme', inline=True)
        embed.add_field(name='`>pokemon (pokemon)`', value=':lion_face: Pokemon Info', inline=True)
        # embed.add_field(name='`>trivia`', value=':smirk: Trivia!', inline=True)
        embed.add_field(name='`>xkcd`', value=':bookmark_tabs: Comics!', inline=True)
        embed.add_field(name='`>yt (name)`', value=':paperclips: Youtube Search', inline=True)
        await ctx.send(embed=embed)
    elif arg == 'image' or arg == 'img':
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
        embed.set_author(name='Image Fun Commands')
        embed.add_field(name='`>blur (user)`', value=':blush: Blurred image of a user', inline=True)
        embed.add_field(name='`>blurple (user)`', value=':purple_circle: Blurple tinted image of a user',
                        inline=True)
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/706665974484566138/717442170214154320/1200px-Fist.svg.webp')
        # embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/706338290693046283/707085433552764968/RandyLogo.png')
        embed.add_field(name='`>glass (user)`', value=':wine_glass: Image of a user behind a glass',
                        inline=True)
        embed.add_field(name='`>invert (user)`', value=':blue_circle: Tinted image of a user', inline=True)
        embed.add_field(name='`>pixelate (user)`', value=':smiley_cat: Pixelated image of a user', inline=True)
        embed.add_field(name='`>sepia (user)`', value=':yellow_circle: Yellowish tinted image of a user',
                        inline=True)
        embed.add_field(name='`>spin (user)`', value=':carousel_horse: Spinning gif of a user', inline=True)
        embed.add_field(name='`>triggered (user)`',
                        value=":triangular_flag_on_post: User's image with the triggered tag", inline=True)
        embed.add_field(name='`>wasted (user)`', value=":wastebasket: Wasted tag on a user's image",
                        inline=True)
        embed.add_field(name='`>pat (user)`', value=":man_gesturing_ok:Pat another user",
                        inline=True)
        embed.add_field(name='`>wink (user)`', value=":wink:Wink at another user",
                        inline=True)
        embed.add_field(name='`>hug (user)`', value=":hugging:Hug another user",
                        inline=True)
        await ctx.send(embed=embed)
    elif arg == 'info':
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
        embed.set_author(name='General Information Commands')
        embed.add_field(name='`>covid (place)`', value=':mask: Covid-19 Related info', inline=True)
        embed.add_field(name='`>github user (username)`', value=':ghost: User Info', inline=True)
        embed.add_field(name='`>github repo (repository)`', value=':file_folder: Repository Info', inline=True)
        embed.add_field(name='`>news (topic)`', value=':newspaper: News', inline=True)
        embed.add_field(name='`>NYT`', value=':newspaper2: News from NYT', inline=True)
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/706665974484566138/717442170214154320/1200px-Fist.svg.webp')
        # embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/706338290693046283/707085433552764968/RandyLogo.png')
        embed.add_field(name='`>wiki (noun)`', value=':bookmark: Wikipedia', inline=True)
        await ctx.send(embed=embed)
    elif arg == 'language' or arg == 'lang':
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
        embed.set_author(name='Language Commands')
        # embed.add_field(name='`>ant (word)`', value=':bookmark_tabs: Antonym', inline=True)
        embed.add_field(name='`>define (word)`', value=':notebook_with_decorative_cover: Dictionary',
                        inline=True)
        embed.add_field(name='`>quote`', value=':orange_book: Quote', inline=True)
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/706665974484566138/717442170214154320/1200px-Fist.svg.webp')
        # embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/706338290693046283/707085433552764968/RandyLogo.png')
        # embed.add_field(name='`>syn (word)`', value=':bookmark_tabs: Synonym', inline=True)
        embed.add_field(name='`>translate (src) (dest) (word)`', value=':earth_americas: Translate',
                        inline=True)
        embed.add_field(name='`>trans (src) (dest) (time-mins)`',
                        value=':earth_africa: Translate for specified number of minutes', inline=True)
        embed.add_field(name='`>urban (word)`', value=':closed_book: Urban Dictionary', inline=True)
        embed.add_field(name='`>wordoftheday`', value=':blue_book: Word of the day', inline=True)
        await ctx.send(embed=embed)
    elif arg == 'math':
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
        embed.set_author(name='Maths Commands')
        embed.add_field(name='`>add`', value=':heavy_plus_sign: Add numbers', inline=True)
        embed.add_field(name='`>sub`', value=':heavy_minus_sign: Subtract numbers', inline=True)
        embed.add_field(name='`>mult`', value=':x: Multiply numbers', inline=True)
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/706665974484566138/717442170214154320/1200px-Fist.svg.webp')
        # embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/706338290693046283/707085433552764968/RandyLogo.png')
        embed.add_field(name='`>div`', value=':heavy_division_sign: Divide numbers', inline=True)
        await ctx.send(embed=embed)
    elif arg == 'mg' or arg == 'minigames':
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
        embed.set_author(name='Minigames')
        embed.add_field(name='`>blackjack`', value=':diamonds: BlackJack', inline=True)
        embed.add_field(name='`>dice`', value=':1234: Roll dice', inline=True)
        embed.add_field(name='`>flip`', value=':first_place: Flip coin', inline=True)
        embed.add_field(name='`>ngg`', value=':1234: Number Guessing Game', inline=True)
        embed.add_field(name='`>rps (choice)`', value=':rocket: Rock Paper Scissors', inline=True)
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/706665974484566138/717442170214154320/1200px-Fist.svg.webp')
        # embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/706338290693046283/707085433552764968/RandyLogo.png')
        await ctx.send(embed=embed)
    elif arg == 'mod' or arg == 'moderator':
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
        embed.set_author(name='Moderation Commands')
        embed.add_field(name='`>ban (user)`', value=':hammer: Bans a user', inline=True)
        embed.add_field(name='`>clear (num)`', value=':x: Clear messages', inline=True)
        # embed.add_field(name='>unban (user)', value=':hammer: Unbans a user', inline=True)
        embed.add_field(name='`>kick (user)`', value=':interrobang: Kicks a user', inline=True)
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/706665974484566138/717442170214154320/1200px-Fist.svg.webp')
        # embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/706338290693046283/707085433552764968/RandyLogo.png')
        embed.add_field(name='`>lock`', value=':lock: Lock the channel', inline=True)
        embed.add_field(name='`>msg (broadcast)`', value=':loudspeaker: Broadcast a message', inline=True)
        embed.add_field(name='`>mute (user)`', value=':mute: Mute a user', inline=True)
        embed.add_field(name='`>unlock`', value=':unlock: Unlock the channel', inline=True)
        embed.add_field(name='`>unmute (user)`', value=':loud_sound: Unmute a user', inline=True)
        await ctx.send(embed=embed)
    elif arg == 'money':
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
        embed.set_author(name='Money Commands')
        embed.add_field(name='`>bitcoin`', value=':money_mouth: Bitcoin value', inline=True)
        embed.add_field(name='`>currency (src) (dest) (value)`', value=':moneybag: Currency Conversion',
                        inline=True)
        embed.add_field(name='`>stock (company)`', value=':money_with_wings: Stock', inline=True)
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/706665974484566138/717442170214154320/1200px-Fist.svg.webp')
        # embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/706338290693046283/707085433552764968/RandyLogo.png')
        await ctx.send(embed=embed)
    elif arg == 'text':
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
        embed.set_author(name='Text Manipulation Commands')
        embed.add_field(name='`>clap (text)`', value=':clap: Adds clap emoji between letters', inline=True)
        embed.add_field(name='`>code (lang) (code)`', value=':reminder_ribbon: Code blocks', inline=True)
        embed.add_field(name='`>doot (text)`',
                        value=':skull: :trumpet: Adds skull and trumpet emoji between letters', inline=True)
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/706665974484566138/717442170214154320/1200px-Fist.svg.webp')
        # embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/706338290693046283/707085433552764968/RandyLogo.png')
        embed.add_field(name='`>emojify (text)`', value=":regional_indicator_p: Converts text to emojis",
                        inline=True)
        embed.add_field(name='`>greentext (text)`', value=':green_square: Converts text to green color',
                        inline=True)
        embed.add_field(name='`>imagine (text)`', value=':thinking: Asks u to imagine', inline=True)
        embed.add_field(name='`>lenny (text)`', value=':face_with_monocle: ( ͡° ͜ʖ ͡°)', inline=True)
        embed.add_field(name='`>owo (text)`', value=':owl: OwO', inline=True)
        embed.add_field(name='`>partyfrog (text)`', value=':frog: Frog emoji between letters', inline=True)
        embed.add_field(name='`>say (text)`', value=':loudspeaker: Says the text', inline=True)
        embed.add_field(name='`>spoiler (text)`', value=':race_car: Marks as spoiler', inline=True)
        embed.add_field(name='`>vaporwave (text)`', value=':space_invader: Seperates the letters', inline=True)
        await ctx.send(embed=embed)
    elif arg == 'util':
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
        embed.set_author(name='Utility Commands')
        embed.add_field(name='Welcomes users on join', value='In channel member-log', inline=True)
        embed.add_field(name='Leave message on user leave', value='In channel member-log', inline=True)
        embed.add_field(name='ping', value='Pings!', inline=True)
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/706665974484566138/717442170214154320/1200px-Fist.svg.webp')
        # embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/706338290693046283/707085433552764968/RandyLogo.png')
        embed.add_field(name='website', value="Sends the bot's website", inline=True)
        await ctx.send(embed=embed)
    elif arg == 'weather':
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
        embed.set_author(name='Weather Commands')
        embed.add_field(name='`>humdidity (place)`', value=':hot_face: Humidity', inline=True)
        embed.add_field(name='`>temp (place)`', value=':cold_face: Temperature', inline=True)
        embed.add_field(name='`>tempfeels (place)`', value=':sweat: Temperature Feel', inline=True)
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/706665974484566138/717442170214154320/1200px-Fist.svg.webp')
        # embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/706338290693046283/707085433552764968/RandyLogo.png')
        embed.add_field(name='`>weather (place)`', value=':cold_sweat: Weather', inline=True)
        embed.add_field(name='`>wind (place)`', value=':wind_blowing_face: Wind', inline=True)
        await ctx.send(embed=embed)
    elif arg == 'level':
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
        embed.set_author(name='Level Commands')
        embed.add_field(name='`>level (user)`', value='🏅 Check Level', inline=True)
        embed.add_field(name='`>levels (off/on)`', value='📴 Turn the level system on or off', inline=True)
        embed.add_field(name='`top`', value=':chart_with_upwards_trend: Global Leaderboard', inline=True)
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/706665974484566138/717442170214154320/1200px-Fist.svg.webp')
        # embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/706338290693046283/707085433552764968/RandyLogo.png')
        await ctx.send(embed=embed)
    elif arg == 'music':
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
        embed.set_author(name='Music Commands')
        embed.add_field(name='`>loop`', value=':loop: Turn the loop off or on', inline=True)
        embed.add_field(name='`>lyrics (singer),(song) [comma is necessary]`',
                        value=':page_with_curl: Song Lyrics',
                        inline=True)
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/706665974484566138/717442170214154320/1200px-Fist.svg.webp')
        # embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/706338290693046283/707085433552764968/RandyLogo.png')
        embed.add_field(name='`>pause`', value=':speaker:  Resume a song!', inline=True)
        embed.add_field(name='`>pause`', value=':speaker:  Resume a song!', inline=True)
        embed.add_field(name='`>play (name/url)`', value=':person_tipping_hand: Plays a song!', inline=True)
        embed.add_field(name='`>playlist (name/url)`', value=':man_playing_water_polo: Plays a playlist!', inline=True)
        embed.add_field(name='`>queue`', value=':bouquet: Check the queue', inline=True)
        embed.add_field(name='`>remove (num)`', value=':x: Remove a song from the queue', inline=True)
        embed.add_field(name='`>resume`', value=':mute: Pause a song!', inline=True)
        embed.add_field(name='`>shuffle`', value=':shushing_face: Shuffle the queue', inline=True)
        embed.add_field(name='`>skip`', value=':ski: Skip the song', inline=True)
        embed.add_field(name='`>stop`', value=':stop_button: Stop playing!', inline=True)
        embed.add_field(name='`>volume`', value=':loud_sound: Change the volume', inline=True)
        await ctx.send(embed=embed)


@client.command()
async def property(ctx):
    id = ctx.message.author.id
    if await cv(ctx, id) == True:
        await ctx.send('Please enter city: ')
        city = await get_input_of_type(str, ctx)
        await ctx.send('Please enter state: ')
        state = await get_input_of_type(str, ctx)
        await ctx.send('Please enter zip: ')
        zip = await get_input_of_type(str, ctx)
        await ctx.send('Please enter address (without city, state or zip code): ')
        add = await get_input_of_type(str, ctx)
        await ctx.send('Processing your data...')
        response = requests.get(
            'https://apis.estated.com/v4/property?token=' + tokens['property'] + '&street_address=' + add + '&city=' + city + '&state=' + state + '&zip_code=' + zip).json()
        area = response['data']['parcel']['area_sq_ft']
        county = response['data']['parcel']['county_name']
        yr = response['data']['structure']['year_built']
        bds = response['data']['structure']['beds_count']
        bths = response['data']['structure']['baths']
        ptbths = response['data']['structure']['partial_baths_count']
        prk = response['data']['structure']['parking_spaces_count']
        prktp = response['data']['structure']['parking_type']
        nam = response['data']['owner']['name']
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
        embed.set_author(name='Property Info')
        embed.add_field(name='Owner Name', value=nam, inline=True)
        embed.add_field(name='Area', value=str(area) + ' sq ft', inline=True)
        embed.add_field(name='Year Built', value=yr, inline=True)
        embed.add_field(name='Beds', value=bds, inline=True)
        embed.add_field(name='Baths', value=bths, inline=True)
        embed.add_field(name='Partial Baths', value=ptbths, inline=True)
        embed.add_field(name='Parkings', value=prk, inline=True)
        embed.add_field(name='Parking Type', value=prktp, inline=True)
        embed.add_field(name='County', value=county, inline=True)
        embed.set_footer(text=add + ', ' + city + ', ' + state + ', ' + zip)
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


@client.command()
async def lol(ctx, member: discord.Member, role: discord.Role):
    if role in member.roles:
        await member.remove_roles(role)
    else:
        await member.add_roles(role)


@client.command()
async def feedback(ctx, *, msg):
    channel = client.get_channel(699699497206415401)
    await ctx.send('Feedback has been sent')
    await channel.send("\"" + str(msg).capitalize() + "\"" + ' from ' + ctx.message.author.mention)


@client.command()
async def animal(ctx, *, animal):
    results = requests.get('https://some-random-api.ml/img/' + animal).json()
    results = results['link']
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
    embed.set_image(url=results)
    await ctx.send(embed=embed)


@client.command()
async def fact(ctx, *, animal):
    results = requests.get('https://some-random-api.ml/facts/' + animal).json()
    results = results['fact']
    await ctx.send(results)


@client.command(aliases=['Dice', 'roll', 'Roll'])
async def dice(ctx):
    await ctx.send(random.randint(1, 6))


@client.command(pass_context=True, brief='Flips a coin.', aliases=['Flip', 'coin', 'Coin'])
async def flip(ctx):
    flip = random.choice(['Heads', 'Tails', 'lol, ngl the coin landed on the edge!'])
    await ctx.send(flip)


@client.command()
async def presence(ctx, type, *, status):
    if ctx.message.author.id == 626913781779267594 or ctx.message.author.id == 469939274783916032:
        type = type.lower()
        if type == 'streaming':
            await client.change_presence(activity=discord.Streaming(name=status, url='https://www.twitch.tv/hvhvuu'))

        if type == 'listening':
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=status))

        if type == 'watching':
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))

        await ctx.send('Presence has been changed!')

    else:
        await ctx.send("bro, this command owner only. r u owner? no right? then don't use it")


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
    # activity = discord.Activity(name=">help in " + str(y) + " servers", type=discord.ActivityType.listening)
    await client.change_presence(
        activity=discord.Streaming(name=">help || Randy", url='https://www.twitch.tv/hvhvuu'))
    # await client.change_presence(activity=activity)
    print('------')


client.run(TOKEN)
