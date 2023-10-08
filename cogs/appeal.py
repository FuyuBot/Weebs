import discord
from discord import app_commands, TextStyle
from discord.ext import commands
import pymongo
import config
import TOKEN

myclient = pymongo.MongoClient(TOKEN.mongoDB)
mydb = myclient["WeebsHangout"]
mycol = mydb["user_info"]



class appeals(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `appeal.py`")
    
    @app_commands.command(name="appeal", description="Use if you have been punished on the server and would like to appeal your punishment.")
    @app_commands.checks.cooldown(1, 604800, key=lambda i: (i.guild_id, i.user.id))
    @app_commands.describe(type='What is the punishment type?')
    @app_commands.choices(type=[
        discord.app_commands.Choice(name= 'Timeout', value="timeout"),
        discord.app_commands.Choice(name= 'Ban', value="ban"),
        discord.app_commands.Choice(name= 'Warn', value="warn")
    ])
    async def appeal(self, interaction: discord.Interaction, type: discord.app_commands.Choice[str]):
        user = interaction.user.id
        playerDB = mycol.find_one({"_id": user})
        if playerDB == None:
            return await interaction.response.send_message("Unfortunately, you are not in our database.")
        else:
            if playerDB['info']['currently_banned'] == False and playerDB['punishments']['bans'] == [] and playerDB['punishments']['timeouts'] == [] and playerDB['punishments']['warns'] == []:
                return await interaction.response.send_message("You have not been punished on our server.")
            else:
                if type.value == "timeout" and playerDB['punishments']['timeouts'] != []:
                    await interaction.response.send_modal(AppealModal())
                elif type.value == "ban" and playerDB['punishments']['bans'] != []:
                    await interaction.response.send_modal(AppealModal())
                elif type.value == "warn" and playerDB['punishments']['warns'] != []:
                    await interaction.response.send_modal(AppealModal())
                else:
                    if type.value == "timeout" and playerDB['punishments']['timeouts'] == []:
                        return await interaction.response.send_message("You have not been put in timeout.")
                    elif type.value == "ban" and playerDB['punishments']['bans'] == []:
                        return await interaction.response.send_message("You have not been banned.")
                    elif type.value == "warn" and playerDB['punishments']['warns'] == []:
                        return await interaction.response.send_message("You have not been warned.")
    
    @appeal.error
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
                    return await interaction.response.send_message(f"You are on cooldown. Try again in {day} day(s) {hour}:{minutes}:{seconds}.", ephemeral=True)
                    
class AppealModal(discord.ui.Modal, title="Punishment Appeal - A Weeb's Hangout"):
    
    punishReason = discord.ui.TextInput(label="What is your punishment reason?", required=True, placeholder="We will check so don't lie")
    understanding = discord.ui.TextInput(label="Do you understand why you were punished?",style=TextStyle.long, min_length=100, required=True)
    why = discord.ui.TextInput(label="Why should you be unpunished?",style=TextStyle.long, min_length=100, required=True)
    justified = discord.ui.TextInput(label="Do you feel your punishment was justified?", required=True)
    anythingElse = discord.ui.TextInput(label="Anything else?", required=True)
    async def on_submit(self, interaction: discord.Interaction):
        try:    
            user = interaction.user
            appealForum = interaction.client.get_channel(1049868404091273296)
            embed = discord.Embed(
                        title=f"{user}'s appeal",
                        color=discord.Color.red()
            )
            
            
            embed.add_field(name= self.punishReason.label, value= self.punishReason)
            embed.add_field(name= self.understanding.label, value= self.understanding)
            embed.add_field(name= self.why.label, value= self.why)
            embed.add_field(name= self.justified.label, value= self.justified)
            embed.add_field(name= self.anythingElse.label, value= self.anythingElse)
            embed.set_footer(text= f"Applicant's ID: {user.id}")

            await appealForum.create_thread(name=f"{user.name}'s Appeal",embed=embed)
            await interaction.response.send_message("Appeal sent successfully.\n\nPlease note if your appeal has been accepted, one of our staff members will be in contact with you within a week to discuss what will happen next. If this doesn't happen please assume you have been denied and feel free to make an appeal.", ephemeral= True)
        except Exception as e:
            print(e)
async def setup(bot):
    await bot.add_cog(appeals(bot))