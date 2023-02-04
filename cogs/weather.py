import discord
from discord import app_commands
from discord.ext import commands
import config
import json
import requests

class weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `weather.py`")
    
    @app_commands.command(name="weather", description="This is the weather command")
    async def weather(self, interaction: discord.Interaction, city: str, state: str=None, country: str=None):
        try:
            embed = discord.Embed(color=config.color)
            client = interaction.client
            if state == None:
                beforeUrl = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{country}&limit=1&appid={config.openWeatherApiKEY}"
                LATLONGget = requests.get(beforeUrl)
                json_data = json.loads(LATLONGget.text)
                for x in json_data:
                    if x['state']:
                        stateX = x['state']
                        lat = x['lat']
                        lon = x['lon']
                        name = x['name']
                        country = x['country']
                        yes = True
                    else:
                        lat = x['lat']
                        lon = x['lon']
                        name = x['name']
                        country = x['country']
                googleURL = f"https://www.google.com/maps/@{lat},{lon}"
                if yes:
                    embed.set_author(name=f"{name}, {stateX} {country}", url=googleURL, icon_url=client.user.avatar)
                else:
                    embed.set_author(name=f"{name}, {country}", url=googleURL, icon_url=client.user.avatar)
            else:
                beforeUrl = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit=1&appid={config.openWeatherApiKEY}"
            
                LATLONGget = requests.get(beforeUrl)
                json_data = json.loads(LATLONGget.text)
                for x in json_data:
                    lat = x['lat']
                    lon = x['lon']
                    name = x['name']
                    country = x['country']
                    stateX = x['state']
                googleURL = f"https://www.google.com/maps/@{lat},{lon}"
                embed.set_author(name=f"{name}, {stateX} {country}", url=googleURL, icon_url=client.user.avatar)
            urlImperial = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={config.openWeatherApiKEY}&units=imperial"
            urlMetric = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={config.openWeatherApiKEY}&units=metric"
            timeURL = f"https://www.timeapi.io/api/Time/current/coordinate?latitude={lat}&longitude={lon}"
            getTime = requests.get(timeURL)
            time = getTime.json()['time']
            ##### IMPERIAL SYSTEM
            getImperial = requests.get(urlImperial)
            weatherMainTempImperial = getImperial.json()["main"]['temp']
            weatherMainFeelsLikeImperial = getImperial.json()['main']['feels_like']
            weatherMainTempMinImperial = getImperial.json()["main"]['temp_min']
            weatherMainTempMaxImperial = getImperial.json()["main"]['temp_max']
            weatherWindSpeedImperial = getImperial.json()['wind']['speed'] # MPH
            if state != None or country == "US":
                if stateX == "Florida":
                    pass
                else:
                    weatherWindGustImperial = getImperial.json()['wind']['gust'] # MPH
            ##### METRIC SYSTEM
            getMetric = requests.get(urlMetric)
            weatherMainTempMetric = getMetric.json()["main"]['temp']
            weatherMainFeelsLikeMetric = getMetric.json()['main']['feels_like']
            weatherMainTempMinMetric = getMetric.json()["main"]['temp_min']
            weatherMainTempMaxMetric = getMetric.json()["main"]['temp_max']
            weatherWindSpeedMetric = getMetric.json()['wind']['speed'] # KPH
            if state != None or country == "US" :
                if stateX == "Florida":
                    pass
                else:
                    weatherWindGustMetric = getMetric.json()['wind']['gust'] # KPH
            #####
            weatherWeather = getImperial.json()['weather']
            for y in weatherWeather:
                weatherWeatherMain = y['main']
                weatherWeatherDescription = y['description']
                weatherWeatherIcon = y['icon']
            #### 
            weatherMainPressure = getImperial.json()['main']['pressure']
            weatherMainHumidity = getImperial.json()['main']['humidity']
            iconURL = f"http://openweathermap.org/img/wn/{weatherWeatherIcon}@2x.png"
            embed.description = f"Conditions: {weatherWeatherMain}, Description: {weatherWeatherDescription}"
            embed.set_thumbnail(url=iconURL)
            embed.add_field(name="Current Time", value=time)
            embed.add_field(name="Current Temp", value=f"`{weatherMainTempImperial}°F`\n`{weatherMainTempMetric}°C`")
            embed.add_field(name="Feels Like", value=f"`{weatherMainFeelsLikeImperial}°F`\n`{weatherMainFeelsLikeMetric}°C`")
            embed.add_field(name="Min/Max", value=f"`{weatherMainTempMinImperial}°F` - `{weatherMainTempMaxImperial}°F`\n\
                            `{weatherMainTempMinMetric}°C` - `{weatherMainTempMaxMetric}°C`")
            embed.add_field(name="Wind Speed", value=f"`{weatherWindSpeedImperial} MPH`\n`{weatherWindSpeedMetric} KPH`")
            if state != None or country == "US":
                if stateX == "Florida":
                    pass
                else:
                    embed.add_field(name="Wind Gust", value=f"`{weatherWindGustImperial} MPH`\n`{weatherWindGustMetric} KPH`")
            embed.add_field(name="Air Pressure", value=f"`{weatherMainPressure}`", inline=False)
            embed.add_field(name="Humidity", value=f"`{weatherMainHumidity}`", inline=True)

            await interaction.response.send_message(embed=embed, ephemeral=True)
        except Exception as e:
            print(e)

async def setup(bot):
    await bot.add_cog(weather(bot))