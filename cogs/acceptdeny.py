import discord
from discord import app_commands
from discord.ext import commands

class acceptdeny(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `acceptdeny.py`")
    
    @app_commands.command(name='deny', description="Deny a user's staff application.")
    @app_commands.checks.has_any_role("Staff Manager", "Management Team")
    @app_commands.describe(reason='What is the reason for denial?')
    @app_commands.choices(reason=[
        discord.app_commands.Choice(name= 'Under aged.', value=""),
        discord.app_commands.Choice(name= 'Not enough detail.', value=""),
        discord.app_commands.Choice(name= 'Not enough time.', value="")
    ])
    async def deny(self, interaction: discord.Interaction, user: discord.Member , reason: discord.app_commands.Choice[str]):
        
        val1 = "Unfortunately, your application has been denied.\nPer Discord's TOS, we can not accept any applications of anyone under the age of 13.\nFind more details at: https://discord.com/terms#2."
        val2 = "Unfortunately, your application has been denied.\nWe have decided that your application doesn't meet our criteria. If you still wish to apply, try using more detail in your responses."
        val3 = "Unfortunately, your application has been denied.\nWe have concluded that the amount of time you are able to contribute does not meet the required amount of time needed.\nIf you believe we can make a compromise, please make a ticket so we can reevaluate your application."
            
        if reason.name == "Under aged.":
            try:
                await user.send(val1)
                sent = True
            except Exception as e:
                print(e)
            if sent != True:
                await interaction.response.send_message("Message did not send.")
            else: 
                await interaction.response.send_message("Message sent.")
        elif reason.name == "Not enough detail.":
            try:
                await user.send(val2)
                sent = True
            except Exception as e:
                print(e)
            if sent != True:
                await interaction.response.send_message("Message did not send.")
            else: 
                await interaction.response.send_message("Message sent.")
        elif reason.name == "Not enough time.":
            try:
                await user.send(val3)
                sent = True
            except Exception as e:
                print(e)
            if sent != True:
                await interaction.response.send_message("Message did not send.")
            else: 
                await interaction.response.send_message("Message sent.")

async def setup(bot):
    await bot.add_cog(acceptdeny(bot), guilds=[discord.Object(id=860752406551461909)])