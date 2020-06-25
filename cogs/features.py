from discord.ext import commands


class Features(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Features cog is online.")

    @commands.command(brief="Pings!")
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')

    @commands.command(brief="Sends the bot invite link.")
    async def server(self, ctx):
        await ctx.send(
            "Here's the invite link: https://discordapp.com/oauth2/authorize?client_id=696185454759903264&scope=bot&permissions=8")
        await ctx.send("https://discord.gg/Gk8vH2M")


    @commands.command(brief="Sends the website.")
    async def website(self, ctx):
        await ctx.send("A message has been sent with the link.")
        await ctx.author.send(
            "https://bit.ly/3cAfbJX")


def setup(client):
    client.add_cog(Features(client))
