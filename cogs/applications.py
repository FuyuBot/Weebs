import discord
from discord import app_commands, TextStyle
from discord.ext import commands
import config



class applications(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('LOADED: `applications.py`')

    @app_commands.command(name='apply', description= "Apply to be staff on A Weeb's Hangout.")
    @app_commands.checks.has_any_role("Member")
    async def apply(self, interaction:discord.Interaction):
        try:
            await interaction.response.send_modal(ApplicationModal())
        except Exception as e:
            print(e)

class ApplicationModal(discord.ui.Modal, title= "Staff Application - A Weeb's Hangout"):
    age = discord.ui.TextInput(label= "How old are you?", max_length= 2, required= True)
    languages = discord.ui.TextInput(label= "What languages can you speak fluently?", max_length=200, placeholder= "e.g. English, Spanish, Japanese", required= True)
    whyStaff = discord.ui.TextInput(label= "Why do you want to become a staff member?", style= TextStyle.long, required= True)
    pastExperiences = discord.ui.TextInput(label= "Any past moderation/leadership experience?", style= TextStyle.long, required= True)
    timeDedicate = discord.ui.TextInput(label= "How much time can you lend to the server?", style= TextStyle.long, required= True)
    #send at the end of the message saying we will contact them, and a confirmation message saying it was sent in the channel to close the modal.
    async def on_submit(self, interaction: discord.Interaction):
        
        try:
            userName = interaction.user.name
            userID = interaction.user.id
            applicationLogs = interaction.client.get_channel(1022658693977870377)
            ageToStr = str(self.age) 
            ageToInt = int(ageToStr)
            if ageToInt < 13:
                embed = discord.Embed(
                    title=f"{userName}'s application",
                    color=discord.Color.red()
                )
                embed.add_field(name= self.age.label, value= self.age)
                embed.add_field(name= self.languages.label, value= self.languages)
                embed.add_field(name= self.whyStaff.label, value= self.whyStaff)
                embed.add_field(name= self.pastExperiences.label, value= self.pastExperiences)
                embed.add_field(name= self.timeDedicate.label, value= self.timeDedicate)
                embed.set_footer(text= f"Applicant's ID: {userID}")

                await applicationLogs.send(embed=embed)
                await interaction.response.send_message("Application submitted.\nYou will be contacted soon. Makes sure your privacy settings for direct messages are turned on for A Weeb's Hangout.", ephemeral= True)
            else:
                embed = discord.Embed(
                    title=f"{userName}'s application",
                    color=0x2699C6
                )
                embed.add_field(name= self.age.label, value= self.age)
                embed.add_field(name= self.languages.label, value= self.languages)
                embed.add_field(name= self.whyStaff.label, value= self.whyStaff)
                embed.add_field(name= self.pastExperiences.label, value= self.pastExperiences)
                embed.add_field(name= self.timeDedicate.label, value= self.timeDedicate)
                embed.set_footer(text= f"Applicant's ID: {userID}")

                await applicationLogs.send(embed=embed)
                await interaction.response.send_message("Application submitted.\nYou will be contacted soon. Makes sure your privacy settings for direct messages are turned on for A Weeb's Hangout.", ephemeral= True)


        except Exception as e:
            print(e)
    
async def setup(bot):
    await bot.add_cog(applications(bot), guilds=[discord.Object(id=860752406551461909)])