import discord
from discord import app_commands
from discord.ext import commands
import pymongo
import config

myclient = pymongo.MongoClient(config.mongoDB)
mydb = myclient["WeebsHangout"]
mycol = mydb["user_info"]

class acceptdeny(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `acceptdeny.py`")
    
    @app_commands.command(name='accept', description="Accept a user's staff application")
    @app_commands.checks.has_any_role("Staff Manager", "Management Team")
    async def accept(self, interaction: discord.Interaction, user: discord.Member):
        player = user.id
        playerDB = mycol.find_one({"_id": player})

        if playerDB['info']['applied'] == False:
            await interaction.response.send_message(f"{user} is not an applicant.", ephemeral= True)
        else:
            mycol.update_one({'_id': player}, {"$set": {"info.applied" : False}})
            mycol.update_one({'_id': player}, {"$set": {"info.staff" : True}})
            acceptMSG = "Congratulations, your application has been accepted! You will be moving on to the next step in the application process.\nA member of our management team will be reaching out to you soon, so be on the lookout for further details. In the meantime, if you haven't already we ask you to please enable 2fa on your discord account. This is needed if you wish to use our punishment commands they are required."
            try:
                await user.send(acceptMSG)
                await interaction.response.send_message("Message sent.")
            except Exception as e:
                print(e)
                await interaction.response.send_message(f"Message did not send.\n{user} may have their DM's disabled.")

    @app_commands.command(name='deny', description="Deny a user's staff application.")
    @app_commands.checks.has_any_role("Staff Manager", "Management Team")
    @app_commands.describe(reason='What is the reason for denial?')
    @app_commands.choices(reason=[
        discord.app_commands.Choice(name= 'Under aged.', value="under_aged"),
        discord.app_commands.Choice(name= 'Not enough detail.', value="not_detailed"),
        discord.app_commands.Choice(name= 'Not enough time.', value="no_time")
    ])
    async def deny(self, interaction: discord.Interaction, user: discord.Member , reason: discord.app_commands.Choice[str]):
        player = user.id
        try:
            val1 = "Unfortunately, your application has been denied.\nPer Discord's TOS, we can not accept any applications of anyone under the age of 13.\nFind more details at: https://discord.com/terms#2."
            val2 = "Unfortunately, your application has been denied.\nWe have decided that your application doesn't meet our criteria. If you still wish to apply, try using more detail in your responses."
            val3 = "Unfortunately, your application has been denied.\nWe have concluded that the amount of time you can contribute does not meet the required amount of time needed.\nIf you believe we can make a compromise, please make a ticket so we can reevaluate your application."
                
            playerDB = mycol.find_one({"_id": player})

            if playerDB['info']['applied'] == False:
                await interaction.response.send_message(f"{user} is not an applicant.", ephemeral= True)
            else:
                mycol.update_one({'_id': player}, {"$set": {"info.applied" : False}})
                mycol.update_one({'_id': player}, {"$set": {"info.staff" : True}})
                if reason.value == "under_aged":
                    try:
                        await user.send(val1)
                        await interaction.response.send_message("Denial message `Under aged` sent.")
                    except Exception as e:
                        print(e)
                        await interaction.response.send_message(f"Message did not send.\n{user} may have their DM's disabled.")
                    mydb.commit()

                elif reason.value == "not_detailed":
                    try:
                        await user.send(val2)
                        await interaction.response.send_message("Denial message `Not enough detail` sent.")
                    except Exception as e:
                        print(e)
                        await interaction.response.send_message(f"Message did not send.\n{user} may have their DM's disabled.")
                    mydb.commit()

                elif reason.value == "no_time":
                    try:
                        await user.send(val3)
                        await interaction.response.send_message("Denial message `Not enough time` sent.")
                    except Exception as e:
                        print(e)
                        await interaction.response.send_message(f"Message did not send.\n{user} may have their DM's disabled.")
                    mydb.commit()
        except Exception as e:
            print(e)

async def setup(bot):
    await bot.add_cog(acceptdeny(bot), guilds=[discord.Object(id=860752406551461909)])