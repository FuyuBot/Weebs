import discord
from discord import app_commands
from discord.ext import commands
import config


class members(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `members.py`")

    @app_commands.command(name='member', description="Check someone's information")
    async def member(self, interaction: discord.Interaction, user: discord.Member):
        embed = discord.Embed(
            color=discord.Color.purple()
        )
        embed.set_author(name=f"{user}", icon_url=user.avatar)
        embed.add_field(name="Joined:", value=user.joined_at, inline=False)
        embed.add_field(name="Account Created:", value=user.created_at, inline=False)
        embed.add_field(name="Server Nickname", value=user.nick)
        embed.add_field(name="ID:", value=user.id)
        embed.set_footer(text=config.footer)
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(members(bot))