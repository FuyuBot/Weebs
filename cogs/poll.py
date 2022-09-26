import discord
from discord import app_commands
from discord.ext import commands
import config

moderator = 860758015959498763
seniormoderator = 860758015585812480
seniorstaff = 865054271857885225
managementTeam = 860758013731274762

class poll(commands.Cog):
    def __int__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print('LOADED: `poll.py`')

    @app_commands.command(name='poll', description='Start a Poll.')
    @app_commands.checks.has_any_role(moderator,seniormoderator,seniorstaff,managementTeam)
    async def poll(self, interaction: discord.Interaction, title: str, option1: str, option2: str, option3: str=None, option4: str=None):
        user = interaction.user
        message = interaction.message
        embed = discord.Embed(
            title=f'{title}'
        )
        embed.add_field(name=':one:', value=option1)
        embed.add_field(name=':two:', value=option2)
        if option3 is not None:
            embed.add_field(name=':three:', value=option3)

        if option4 is not None:
            embed.add_field(name=':four:', value=option4)
        embed.set_footer(text=config.footer)

        await interaction.response.send_message(embed=embed)

        async for message in interaction.channel.history():
            if not message.embeds:
                continue
            if message.embeds[0].title == embed.title and message.embeds[0].colour == embed.colour:
                msg = message
                break
            
        await msg.add_reaction("1️⃣")
        await msg.add_reaction("2️⃣")
        if option3 is not None:
            await msg.add_reaction("3️⃣")
        if option4 is not None:
            await msg.add_reaction("4️⃣")



async def setup(bot):
    await bot.add_cog(poll(bot), guilds=[discord.Object(id=860752406551461909)])