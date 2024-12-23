import discord
from discord import app_commands, TextStyle
from discord.ext import commands
import pymongo
import config
import TOKEN

myclient = pymongo.MongoClient(TOKEN.mongoDB)
mydb = myclient["WeebsHangout"]
mycol = mydb["user_info"]
botCol = mydb["bot_info"]


class applications(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('LOADED: `applications.py`')
    
    @app_commands.command(name='toggle-applications', description="Enable/Disable applications")
    @app_commands.checks.has_any_role("Management Team")
    @app_commands.describe(toggle='What would you like to toggle it to?')
    @app_commands.choices(toggle=[
        discord.app_commands.Choice(name= 'On', value="true"),
        discord.app_commands.Choice(name= 'Off', value="false")
    ])
    async def toggleApps(self, interaction: discord.Interaction, toggle: discord.app_commands.Choice[str]):
        try:
            announcements = interaction.client.get_channel(865057220047798303)
            botDB = botCol.find_one({"_id": 926163269503299695})
            if toggle.value == "true":
                if botDB['application-status'] == True:
                    return await interaction.response.send_message("Applications are already enabled.", ephemeral=True)
                else:
                    botCol.update_one({"_id": 926163269503299695}, {"$set": {"application-status": True}})
                    await interaction.response.send_message("Applications have been `Enabled`.")
                    return await announcements.send("<@&865050483189219338>\n\nApplications have been `ENABLED` by the Management Team!")
            else:
                if botDB['application-status'] == False:
                    return await interaction.response.send_message("Applications are already disabled.", ephemeral=True)
                else:
                    botCol.update_one({"_id": 926163269503299695}, {"$set": {"application-status": False}})
                    await interaction.response.send_message("Applications have been `Disabled`.")
                    return await announcements.send("<@&865050483189219338>\n\nApplications have been `DISABLED` by the Management Team, when they get enabled again there will be another announcement.")
        except Exception as e:
            print(e)

    @app_commands.command(name='apply', description= "Apply to be staff on A Weeb's Hangout.")
    @app_commands.checks.cooldown(1, 604800, key=lambda i: (i.guild_id, i.user.id))
    @app_commands.checks.has_any_role("Member")
    async def apply(self, interaction:discord.Interaction):
        player = interaction.user.id
        try:
            playerDB = mycol.find_one({"_id": player})
            botDB = botCol.find_one({"_id": 926163269503299695})
            if playerDB['info']['applied'] == True:
                await interaction.response.send_message(f"{player} you have already applied.", ephemeral= True)
            else:
                if botDB['application-status'] == True:
                    await interaction.response.send_modal(ApplicationModal())
                else:
                    await interaction.response.send_message("Unforuntely applications are currently disabled. There will be announcement in <#865057220047798303> when they are reenabled.", ephemeral=True)
        except Exception as e:
            print(e)
    
    @apply.error
    async def on_work_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            err = f"{error}"
            n = err[34:-4]
            print(n)
            n = int(n)

            day = n // (24 * 3600)
            
            n = n % (24 * 3600)
            hour = n // 3600

            n %= 3600
            minutes = n // 60

            n %= 60
            seconds = n
            if minutes == 0 and hour == 0:
                return await interaction.response.send_message(f"You are on cooldown. Try again in {seconds} seconds.", ephemeral=True)
            else:
                if day != 0:
                    return await interaction.response.send_message(f"You are on cooldown. Try again in {day} day(s) {hour}:{minutes}:{seconds}.", ephemeral=True)
                else:
                    return await interaction.response.send_message(f"You are on cooldown. Try again in {hour}:{minutes}:{seconds}.", ephemeral=True)

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
            applicationForum = interaction.client.get_channel(1047376618051620984)
            ageToStr = str(self.age) 
            ageToInt = int(ageToStr)
            mycol.update_one({'_id': userID}, {"$set": {"info.applied" : True}})
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
                

                await applicationForum.create_thread(name=f"{userName}'s application", embed=embed)
                await interaction.response.send_message("Application submitted.\nYou will be contacted soon. Makes sure your privacy settings for direct messages are turned on for A Weeb's Hangout.", ephemeral= True)
            else:
                embed = discord.Embed(
                    title=f"{userName}'s application",
                    color=config.color
                )
                embed.add_field(name= self.age.label, value= self.age)
                embed.add_field(name= self.languages.label, value= self.languages)
                embed.add_field(name= self.whyStaff.label, value= self.whyStaff)
                embed.add_field(name= self.pastExperiences.label, value= self.pastExperiences)
                embed.add_field(name= self.timeDedicate.label, value= self.timeDedicate)
                embed.set_footer(text= f"Applicant's ID: {userID}")

                await applicationForum.create_thread(name=f"{userName}'s application", embed=embed)
                await interaction.response.send_message("Application submitted.\nYou will be contacted soon. Makes sure your privacy settings for direct messages are turned on for A Weeb's Hangout.", ephemeral= True)
        except Exception as e:
            print(e)
    
async def setup(bot):
    await bot.add_cog(applications(bot), guilds=[discord.Object(id=860752406551461909)])