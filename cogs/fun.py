import discord
import random
import json
from discord.ext import commands
import re
import requests
from youtube_search import YoutubeSearch
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

global tokens
with open('tokens.json', 'r') as l:
    tokens = json.load(l)

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun cog is online.")

    async def cv(self, ctx, id):
        id = ctx.message.author.id
        bruh = {"Authorization": tokens['topgg']}
        url = requests.get("https://top.gg/api/bots/696185454759903264/check?userId=" + str(id), headers=bruh).json()
        if url['voted'] == 1:
            return True

    @commands.command()
    async def hug(self, ctx, member: discord.Member):
        id = ctx.message.author.id
        if await self.cv(ctx, id) == True:
            bruh = requests.get('https://some-random-api.ml/animu/hug').json()
            high = bruh['link']
            await ctx.send('You hugged ' + str(member))
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
            embed.set_image(url=high)
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

    @commands.command()
    async def wink(self, ctx, member: discord.Member):
        id = ctx.message.author.id
        if await self.cv(ctx, id) == True:
            bruh = requests.get('https://some-random-api.ml/animu/wink').json()
            high = bruh['link']
            await ctx.send('You winked at ' + str(member))
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
            embed.set_image(url=high)
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

    @commands.command()
    async def pat(self, ctx, member: discord.Member):
        id = ctx.message.author.id
        if await self.cv(ctx, id) == True:
            bruh = requests.get('https://some-random-api.ml/animu/pat').json()
            high = bruh['link']
            await ctx.send('You patted ' + str(member))
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
            embed.set_image(url=high)
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

    @commands.command()
    async def img(self, ctx, *, img):
        id = ctx.message.author.id
        if await self.cv(ctx, id) == True:
            image = requests.get(
                'https://app.zenserp.com/api/v2/search?apikey=' + tokens['zenserp'] + '&q=' + img + '&tbm=isch&device=desktop&location=Manhattan,New%20York,United%20States').json()
            image = image['image_results'][0]['sourceUrl']
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
            embed.set_image(url=image)
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

    @commands.command(aliases=['youtube'])
    async def yt(self, ctx, *, name):
        id = ctx.message.author.id
        if await self.cv(ctx, id) == True:
            results = YoutubeSearch(name, max_results=1).to_json()
            result = json.loads(results)
            formatted_data = result["videos"][0]["link"]
            title = result["videos"][0]["title"]
            final = "https://www.youtube.com" + formatted_data
            await ctx.send(final)
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

    @commands.command(description="Rock Paper Scissors")
    async def rps(self, ctx, msg: str):
        t = ["rock", "paper", "scissors"]
        computer = t[random.randint(0, 2)]
        player = msg.lower()
        if player == computer:
            await ctx.send("Tie!")
        elif player == "rock":
            if computer == "paper":
                await ctx.send("You lose! {0} covers {1}".format(computer, player))
            else:
                await ctx.send("You win! {0} smashes {1}".format(player, computer))
        elif player == "paper":
            if computer == "scissors":
                await ctx.send("You lose! {0} cut {1}".format(computer, player))
            else:
                await ctx.send("You win! {0} covers {1}".format(player, computer))
        elif player == "scissors":
            if computer == "rock":
                await ctx.send("You lose! {0} smashes {1}".format(computer, player))
            else:
                await ctx.send("You win! {0} cut {1}".format(player, computer))
        else:
            await ctx.send("That's not a valid play. Check your spelling!")

    @commands.command()
    async def pokemon(self, ctx, pokemon):
        id = ctx.message.author.id
        if await self.cv(ctx, id) == True:
            response = requests.get('https://pokeapi.co/api/v2/pokemon/' + pokemon).json()
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            weight = response['weight']
            height = response['height']
            img = response['sprites']['front_default']
            types = response['types']
            stats = response['stats']
            speed = stats[0]['base_stat']
            specdef = stats[1]['base_stat']
            specatt = stats[2]['base_stat']
            defense = stats[3]['base_stat']
            att = stats[4]['base_stat']
            Hp = stats[5]['base_stat']
            hehe = []
            if len(types) == 2:
                i = 0
                while i < 2:
                    hehe.append(types[i]['type']['name'])
                    i += 1
                pokemon = pokemon.capitalize()
                embed = discord.Embed(title=pokemon, color=discord.Colour.from_rgb(r, g, b))
                embed.add_field(name=':scales: Weight', value=weight, inline=True)
                embed.add_field(name=':triangular_ruler: Height', value=height, inline=True)
                embed.set_thumbnail(url=img)
                embed.add_field(name=':dividers: Types', value=str(hehe[0]).capitalize() + ', ' + str(hehe[1]).capitalize(),
                                inline=False)
                embed.add_field(name='Speed', value=speed, inline=True)
                embed.add_field(name='Special-defense', value=specdef, inline=True)
                embed.add_field(name='Special-attack', value=specatt, inline=True)
                embed.add_field(name='Defense', value=defense, inline=True)
                embed.add_field(name='Attack', value=att, inline=True)
                embed.add_field(name='Hp', value=Hp, inline=True)
                await ctx.send(embed=embed)
            elif len(types) == 1:
                hehe = types[0]['type']['name']
                pokemon = pokemon.capitalize()
                embed = discord.Embed(title=pokemon, color=discord.Colour.from_rgb(r, g, b))
                embed.set_author(name=pokemon)
                embed.add_field(name=':scales: Weight', value=weight, inline=True)
                embed.add_field(name=':triangular_ruler: Height', value=height, inline=True)
                embed.set_thumbnail(url=img)
                embed.add_field(name=':dividers: Types', value=str(hehe), inline=False)
                embed.add_field(name='Speed', value=speed, inline=True)
                embed.add_field(name='Special-defense', value=specdef, inline=True)
                embed.add_field(name='Special-attack', value=specatt, inline=True)
                embed.add_field(name='Defense', value=defense, inline=True)
                embed.add_field(name='Attack', value=att, inline=True)
                embed.add_field(name='Hp', value=Hp, inline=True)
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

    @commands.command()
    async def anime(self, ctx, *, anime):
        id = ctx.message.author.id
        if await self.cv(ctx, id) == True:
            response = requests.get('https://api.jikan.moe/v3/search/anime?q=%s&limit=16' % anime).json()
            img = response['results'][0]['image_url']
            synopsis = response['results'][0]['synopsis']
            airing = response['results'][0]['airing']
            # genres = response['results'][0]['airing']
            score = response['results'][0]['score']
            eps = response['results'][0]['episodes']
            type = response['results'][0]['type']
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            embed = discord.Embed(title=anime.capitalize(), color=discord.Colour.from_rgb(r, g, b))
            embed.add_field(name='Synopsis', value=synopsis, inline=False)
            embed.add_field(name=':hourglass_flowing_sand: Status', value=airing, inline=True)
            embed.set_thumbnail(url=img)
            embed.add_field(name=':dividers: Type', value=type, inline=True)
            # embed.add_field(name='Aired', value=, inline=False)
            embed.add_field(name=':minidisc: Total Episodes', value=eps, inline=False)
            # embed.add_field(name='Duration', value=, inline=True)
            embed.add_field(name=':star: Average Rating', value=str(score) + '/10', inline=True)
            # embed.add_field(name='Rank', value=, inline=True)
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

    @commands.command(aliases=['Xkcd', 'XKCD'])
    async def xkcd(self, ctx):
        id = ctx.message.author.id
        if await self.cv(ctx, id) == True:
            comicID = random.randint(1, 999)
            site = requests.get('https://xkcd.com/{}/info.0.json'.format(comicID)).json()
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            embed = discord.Embed(title=site['title'], color=discord.Colour.from_rgb(r, g, b))
            embed.set_image(url=site['img'])
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

    @commands.command(brief="Shares a Chuck Norris joke!", aliases=['Joke'])
    async def joke(self, ctx):
        results = requests.get('http://api.icndb.com/jokes/random')
        y = json.loads(results.content)
        z = y["value"]
        joke = z["joke"]
        final = re.sub('&quot;', '"', joke)
        await ctx.send(final)


    @commands.command(brief='Sends a meme!')
    async def meme(self, ctx):
        results = requests.get('https://meme-api.herokuapp.com/gimme').json()
        meme = results['url']
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(
            color=discord.Colour.from_rgb(r, g, b)
        )
        embed.set_image(url=meme)
        await ctx.send(embed=embed)

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
    async def gif(self, ctx, arg, *, item):
        id = ctx.message.author.id
        if await self.cv(ctx, id) == True:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            if arg == 'giphy':
                response = requests.get(
                    'http://api.giphy.com/v1/gifs/search?q=' + item + '&api_key=' + tokens['giphy'] + '&limit=5').json()
                img2 = response['data'][0]["images"]["original"]["url"]
                embed = discord.Embed(title='First Result for "' + item + '" on GIPHY',
                                      color=discord.Colour.from_rgb(r, g, b))
                embed.set_image(url=img2)
                embed.set_thumbnail(
                    url='https://images-ext-1.discordapp.net/external/FW8Emlcxhqqi1YsZoXVHfC6c58tPptohhqNz0GNmdYQ/https/image.ibb.co/b0Gkwo/Poweredby_640px_Black_Vert_Text.png')
                await ctx.send(embed=embed)
            if arg == 'tenor':
                bro = requests.get("https://api.tenor.com/v1/search?q=" + item + "&key=" + tokens['tenor'] + "&limit=1").json()
                result = bro['results'][0]['media'][0]['tinygif']['url']
                embed = discord.Embed(title='First Result for "' + item + '" on Tenor',
                                      color=discord.Colour.from_rgb(r, g, b))
                embed.set_image(url=result)
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

def setup(client):
    client.add_cog(Fun(client))
