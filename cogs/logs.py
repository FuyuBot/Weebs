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
    async def on_message_edit(self, before, after):
        try:
            embed = discord.Embed(
                title=f"edited their message.",
                color=0x2699C6
            )
            embed.add_field(name='Before', value=before)
            embed.add_field(name='After', value=after)
            logsChannel = self.bot.get_channel(865073673668526080)
            await logsChannel.send(embed=embed)
        except Exception as e:
            print(e)

async def setup(bot):
    await bot.add_cog(logs(bot))