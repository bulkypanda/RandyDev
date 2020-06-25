import discord
import random
import re
from discord.ext import commands
import aiohttp
import io


class Images(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Images cog is online.")

    """@commands.command(brief="Prison")
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
            await ctx.send(embed=show_avatar)"""

    @commands.command(brief="blur")
    async def blur(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        API = '{}'.format(member.avatar_url)
        results = ('https://some-random-api.ml/beta/blur?avatar=' + API)
        final = re.sub('webp', 'png', results)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        show_avatar = discord.Embed(
            color=discord.Colour.from_rgb(r, g, b)
        )
        show_avatar.set_image(url=final)
        await ctx.send(embed=show_avatar)

    @commands.command(brief="blurple")
    async def blurple(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        API = '{}'.format(member.avatar_url)
        results = ('https://some-random-api.ml/beta/blurple?avatar=' + API)
        final = re.sub('webp', 'png', results)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        show_avatar = discord.Embed(
            color=discord.Colour.from_rgb(r, g, b)
        )
        show_avatar.set_image(url=final)
        await ctx.send(embed=show_avatar)

    @commands.command(brief="glass")
    async def glass(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        API = '{}'.format(member.avatar_url)
        results = ('https://some-random-api.ml/beta/glass?avatar=' + API)
        final = re.sub('webp', 'png', results)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        show_avatar = discord.Embed(
            color=discord.Colour.from_rgb(r, g, b)
        )
        show_avatar.set_image(url=final)
        await ctx.send(embed=show_avatar)

    @commands.command(brief="pixelate")
    async def pixelate(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        API = '{}'.format(member.avatar_url)
        results = ('https://some-random-api.ml/beta/pixelate?avatar=' + API)
        final = re.sub('webp', 'png', results)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        show_avatar = discord.Embed(
            color=discord.Colour.from_rgb(r, g, b)
        )
        show_avatar.set_image(url=final)
        await ctx.send(embed=show_avatar)

    @commands.command(brief="spin")
    async def spin(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        API = '{}'.format(member.avatar_url)
        results = ('https://some-random-api.ml/beta/spin?avatar=' + API)
        final = re.sub('webp', 'png', results)
        async with aiohttp.ClientSession().get(final) as r:
            data = io.BytesIO(await r.read())  # getting an image
            await ctx.send(file=discord.File(data, 'spin.gif'))

    @commands.command(brief="sepia")
    async def sepia(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        API = '{}'.format(member.avatar_url)
        results = ('https://some-random-api.ml/beta/sepia?avatar=' + API)
        final = re.sub('webp', 'png', results)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        show_avatar = discord.Embed(
            color=discord.Colour.from_rgb(r, g, b)
        )
        show_avatar.set_image(url=final)
        await ctx.send(embed=show_avatar)

    @commands.command(brief="wasted")
    async def wasted(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        API = '{}'.format(member.avatar_url)
        results = ('https://some-random-api.ml/beta/wasted?avatar=' + API)
        final = re.sub('webp', 'png', results)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        show_avatar = discord.Embed(
            color=discord.Colour.from_rgb(r, g, b)
        )
        show_avatar.set_image(url=final)
        await ctx.send(embed=show_avatar)

    @commands.command(brief="invert")
    async def invert(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        API = '{}'.format(member.avatar_url)
        results = ('https://some-random-api.ml/beta/invert?avatar=' + API)
        final = re.sub('webp', 'png', results)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        show_avatar = discord.Embed(
            color=discord.Colour.from_rgb(r, g, b)
        )
        show_avatar.set_image(url=final)
        await ctx.send(embed=show_avatar)

    @commands.command(brief="triggered")
    async def triggered(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        API = '{}'.format(member.avatar_url)
        results = ('https://some-random-api.ml/beta/triggered?avatar=' + API)
        final = re.sub('webp', 'png', results)
        async with aiohttp.ClientSession().get(final) as r:
            data = io.BytesIO(await r.read())  # getting an image
            await ctx.send(file=discord.File(data, 'triggered.gif'))


def setup(client):
    client.add_cog(Images(client))
