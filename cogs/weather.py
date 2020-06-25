import json
import requests
from discord.ext import commands

global tokens
with open('tokens.json', 'r') as l:
    tokens = json.load(l)

class Weather(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Weather cog is online.")

    @commands.command(aliases=['Weather'], brief="Checks the temperature of a place!")
    async def weather(self, ctx, *, place):
        api_adress = ' http://api.openweathermap.org/data/2.5/weather?appid=' + tokens['weather'] + '&q='
        url = api_adress + place
        results = requests.get(url).json()
        formatted_data = results['weather'][0]['main']
        if formatted_data == 'Rain':
            await ctx.send("It is raining outside")
        elif formatted_data == 'Clouds':
            await ctx.send("It is cloudy outside")
        elif formatted_data == 'Clear':
            await ctx.send("It is clear outside")
        elif formatted_data == 'Haze':
            await ctx.send("It is Hazy outside")
        elif formatted_data == 'Thunderstorm':
            await ctx.send("It is very rainy with lightning")
        elif formatted_data == 'Snow':
            await ctx.send("It is snowing outside")
        elif formatted_data == 'Mist':
            await ctx.send("It is misty outside")

    @commands.command(aliases=['Temperature', 'temp'], brief="Checks the temperature of a place!")
    async def temperature(self, ctx, *, place):
        api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=' + tokens['weather'] + '&units=imperial'
        url = api_address + '&q=' + place
        results = requests.get(url).json()
        formatted_data = results['main']['temp']
        await ctx.send(str(round(formatted_data)) + ' degrees F')

    @commands.command(aliases=['Humidity'])
    async def humidity(self, ctx, *, place):
        api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=' + tokens['weather'] + '&q='
        url = api_address + place
        results = requests.get(url).json()
        formatted_data = results['main']['humidity']
        await ctx.send(str(formatted_data) + '%')

    @commands.command(aliases=['Wind'])
    async def wind(self, ctx, *, place):
        api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=' + tokens['weather'] + '&units=imperial'
        url = api_address + '&q=' + place
        results = requests.get(url).json()
        wind_speed = results['wind']['speed']
        await ctx.send(str(wind_speed) + 'mph')

    @commands.command(aliases=['tempfeels', 'Temp_feel'])
    async def temp_feel(self, ctx, *, place):
        api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=' + tokens['weather'] + '&units=imperial'
        url = api_address + '&q=' + place
        results = requests.get(url).json()
        formatted_data = results['main']['feels_like']
        await ctx.send(str(round(formatted_data)) + '°F')


def setup(client):
    client.add_cog(Weather(client))