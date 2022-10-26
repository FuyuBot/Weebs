import discord
from discord import app_commands
from discord.ext import commands
from bs4 import BeautifulSoup
import json
import requests

admin = 860758015011586069
management = 860758013731274762

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 OPR/91.0.4516.72'
        }
'''
class ReadRss:
    def __init__(self, rss_url, headers):
        self.url = rss_url
        self.headers = headers
        try:
            self.r = requests.get(rss_url, headers=self.headers)
            self.status_code = self.r.status_code
        except Exception as e:
            print('Error fetching the URL: ', rss_url)
            print(e)
        try:
            self.soup = BeautifulSoup(self.r.text, 'lxml')
        except Exception as e:
            print('Could not parse the xml: ', self.url)
        
        self.articles = self.soup.findAll('item')
        self.articles_dicts = [{'title':a.find('title').text,'link':a.link.next_sibling.replace('\n','').replace('\t',''),'description':a.find('description').text,'pubdate':a.find('pubdate').text} for a in self.articles]
        self.urls = [d['link'] for d in self.articles_dicts if 'link' in d]
        self.titles = [d['title'] for d in self.articles_dicts if 'title' in d]
        self.descriptions = [d['category'] for d in self.articles_dicts if 'category' in d]
        self.pub_dates = [d['pubdate'] for d in self.articles_dicts if 'pubdate' in d]
'''

class seasonalAnime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    
    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `seasonalAnime.py`")
        
async def setup(bot):
    await bot.add_cog(seasonalAnime(bot), guilds=[discord.Object(id=860752406551461909)])