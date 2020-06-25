import discord
import random
from discord.ext import commands


class Text(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Text cog is online.")

    @commands.command()
    async def clap(self, ctx, *, text):
        def split(word):
            return list(word)
        a = split(text)
        bruh = []
        for i in a:
            a = i + ' :clap: '
            bruh.append(a)
        await ctx.send(''.join(bruh))

    @commands.command()
    async def doot(self, ctx, *, text):
        def split(word):
            return list(word)
        a = split(text)
        bruh = []
        for i in a:
            a = i + ' :skull: :trumpet: '
            bruh.append(a)
        await ctx.send(''.join(bruh))

    @commands.command()
    async def emojify(self, ctx, *, text):
        text = text.lower()
        bruh = []
        def split(word):
            return list(word)
        a = split(text)
        for i in a:
            if i != ' ':
                a = ':regional_indicator_' + i + ': '
                bruh.append(a)

        await ctx.send(''.join(bruh))

    @commands.command()
    async def greentext(self, ctx, *, text):
        def split(word):
            return list(word)
        a = split(text)
        bruh = []
        for i in a:
            a = i
            bruh.append(a)
        a = (''.join(bruh))
        a = '```css\n' + a + '```'
        await ctx.send(a)

    @commands.command()
    async def imagine(self, ctx, *, text):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        embed = discord.Embed(color=discord.Colour.from_rgb(r, g, b))
        embed.add_field(name='imagining...', value='imagine ' + text)
        embed.set_footer(text='trying hard to imagine, ha?')
        await ctx.send(embed=embed)

    @commands.command()
    async def lenny(self, ctx, *, text):
        await ctx.send('( ͡° ͜ʖ ͡°)')

    @commands.command()
    async def owo(self, ctx, *, text):
        await ctx.send('OwO')

    @commands.command()
    async def partyfrog(self, ctx, *, text):
        def split(word):
            return list(word)
        a = split(text)
        bruh = []
        for i in a:
            a = i + ' :frog: '
            bruh.append(a)
        await ctx.send(''.join(bruh))

    @commands.command()
    async def say(self, ctx, *, text):
        await ctx.send(text + '\n\n-' + ctx.message.author.mention)

    @commands.command()
    async def vaporwave(self, ctx, *, text):
        def split(word):
            return list(word)
        a = split(text)
        bruh = []
        for i in a:
            a = ' ' + i + ' '
            bruh.append(a)
        await ctx.send(''.join(bruh))

    @commands.command()
    async def spoiler(self, ctx, *, text):
        def split(word):
            return list(word)
        a = split(text)
        bruh = []
        for i in a:
            a = '||' + i
            bruh.append(a)
            bruh.append('||')
        await ctx.send(''.join(bruh))

    @commands.command()
    async def code(self, ctx, lang, *, text):
        await ctx.channel.purge(limit=1)
        def split(word):
            return list(word)
        a = split(text)
        bruh = []
        for i in a:
            a = i
            bruh.append(a)
        a = (''.join(bruh))
        a = '```' + lang + '\n' + a + '```'
        await ctx.send(a)


def setup(client):
    client.add_cog(Text(client))
