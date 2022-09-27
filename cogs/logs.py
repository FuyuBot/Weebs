from re import T
import discord
from discord import app_commands
from discord.ext import commands


class logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `logs.py`")
    
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        try:
            embed = discord.Embed(color=0x2699C6)
            embed.set_author(name=message.author, icon_url=message.author.avatar)
            embed.add_field(name=f'Messaged Deleted in #{message.channel.name}', value=message.content)
            embed.set_footer(text=f"User's ID: {message.author.id}")
            logsChannel = self.bot.get_channel(865073643553423360)
            await logsChannel.send(embed=embed)
        except Exception as e:
            print(e)
    
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        try:
            embed = discord.Embed(title=f'Messaged Edited in #{before.channel.name}',color=0x2699C6)
            embed.set_author(name=before.author, icon_url=before.author.avatar)
            embed.add_field(name=f'Before', value=before.content)
            embed.add_field(name=f'After', value=after.content)
            embed.set_footer(text=f"User's ID: {before.author.id}")
            logsChannel = self.bot.get_channel(865073643553423360)
            await logsChannel.send(embed=embed)
        except Exception as e:
            print(e)

async def setup(bot):
    await bot.add_cog(logs(bot))