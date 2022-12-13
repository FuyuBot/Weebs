import discord
from discord import app_commands
from discord.ui import Button, View
from discord.ext import commands
from datetime import datetime
import config
import pymongo

myclient = pymongo.MongoClient(config.mongoDB)
mydb = myclient["WeebsHangout"]
mycol = mydb["user_info"]
pageNum = 1

async def rolesPageButton_callback(interaction: discord.Interaction):
    rolesPageButton.disabled = False
    #previousPageButton.disabled = False
    #nextPageButton.disabled = False
    #lastPageButton.disabled = False
    member = interaction.user
    playerDB = mycol.find_one({"_id": member.id})
    #### COLORS
    COLORninja = discord.utils.get(member.guild.roles, id=1050822390952763473)
    COLORgreen = discord.utils.get(member.guild.roles, id=1051199158658285738)
    COLORteal = discord.utils.get(member.guild.roles, id=1051199137326055455)
    COLORblue = discord.utils.get(member.guild.roles, id=1051199127326830654)
    COLORpurple = discord.utils.get(member.guild.roles, id=1051199155470602341)
    COLORred = discord.utils.get(member.guild.roles, id=1051199153029521408)
    COLORorange = discord.utils.get(member.guild.roles, id=1051199144129212496)
    COLORyellow = discord.utils.get(member.guild.roles, id=1051199137024053310)
    COLORwhite = discord.utils.get(member.guild.roles, id=1051199138454310982)
    #COLORextra = discord.utils.get(member.guild.roles, id=1051199150101897216)
    ### CHECK DB
    checkNinja = playerDB['roles']['ninja']
    checkGreen = playerDB['roles']['green']
    checkTeal = playerDB['roles']['teal']
    checkBlue = playerDB['roles']['blue']
    checkPurple = playerDB['roles']['purple']
    checkRed = playerDB['roles']['red']
    checkOrange = playerDB['roles']['orange']
    checkYellow = playerDB['roles']['yellow']
    checkWhite = playerDB['roles']['white']
    #checkExtra = playerDB['roles']['extra']

    if checkNinja != True: # Ninja
        priceNinja = "$500,000"
    else:
        priceNinja = "Purchased"
    if checkGreen != True: # Green
        priceGreen = "$50,000"
    else:
        priceGreen = "Purchased"
    if checkTeal!= True: # Teal
        priceTeal = "$50,000"
    else:
        priceTeal = "Purchased"
    if checkBlue != True: # Blue
        priceBlue = "$50,000"
    else:
        priceBlue = "Purchased"
    if checkPurple != True: # Purple
        pricePurple = "$50,000"
    else:
        pricePurple = "Purchased"
    if checkRed != True: # Red
        priceRed = "$50,000"
    else:
        priceRed = "Purchased"
    if checkOrange != True: # Orange
        priceOrange = "$50,000"
    else:
        priceOrange = "Purchased"
    if checkYellow != True: # Yellow
        priceYellow = "$50,000"
    else:
        priceYellow = "Purchased"
    if checkWhite != True: # White
        priceWhite = "$50,000"
    else:
        priceWhite = "Purchased"
    #if checkExtra != True: # Extra
    #    priceExtra = "$50,000"
    #else:
    #    priceExtra = "Purchased"
    ####EMBEDS
    shopPage1 = discord.Embed(color=config.color, timestamp=datetime.now(), title="Roles", description="`/purchase` to make a purchase!\nTo equip colors you have purchased `/color`")
    shopPage1.set_author(name="Server Shop • Page 1")
    shopPage1.set_thumbnail(url=interaction.guild.icon)
    shopPage1.set_footer(text=config.footer)
    shopPage1.add_field(name=f"{COLORninja.name}", value=f"{priceNinja}\n{COLORninja.mention}")
    shopPage1.add_field(name=f"{COLORgreen.name}", value=f"{priceGreen}\n{COLORgreen.mention}")
    shopPage1.add_field(name=f"{COLORteal.name}", value=f"{priceTeal}\n{COLORteal.mention}")
    shopPage1.add_field(name=f"{COLORblue.name}", value=f"{priceBlue}\n{COLORblue.mention}")
    shopPage1.add_field(name=f"{COLORpurple.name}", value=f"{pricePurple}\n{COLORpurple.mention}")
    shopPage1.add_field(name=f"{COLORred.name}", value=f"{priceRed}\n{COLORred.mention}")
    shopPage1.add_field(name=f"{COLORorange.name}", value=f"{priceOrange}\n{COLORorange.mention}")
    shopPage1.add_field(name=f"{COLORyellow.name}", value=f"{priceYellow}\n{COLORyellow.mention}")
    shopPage1.add_field(name=f"{COLORwhite.name}", value=f"{priceWhite}\n{COLORwhite.mention}")
    #shopPage1.add_field(name=f"{COLORextra.name}", value=f"{priceExtra}\n{COLORextra.mention}")
    #view = View()
    #view.add_item(rolesPageButton)
    #view.add_item(previousPageButton)
    #view.add_item(whatPageButton)
    #view.add_item(nextPageButton)
    #view.add_item(lastPageButton)
    await interaction.response.send_message(embed=shopPage1, ephemeral=True)
    #rolesPageButton.callback = rolesPageButton_callback
    #previousPageButton.callback = previousPageButton_callback
    #nextPageButton.callback = nextPageButton_callback
    #lastPageButton.callback = lastPageButton_callback
async def previousPageButton_callback(interaction: discord.Interaction):
    return
async def nextPageButton_callback(interaction: discord.Interaction):
    return
async def lastPageButton_callback(interaction: discord.Interaction):
    return
rolesPageButton = Button(label="Color Roles", style=discord.ButtonStyle.primary)
#previousPageButton = Button(label="Previous Page", style=discord.ButtonStyle.success)
#whatPageButton = Button(label=f"What Page", style=discord.ButtonStyle.gray, disabled=True)
#nextPageButton = Button(label="Next Page", style=discord.ButtonStyle.success)
#lastPageButton = Button(label="Last Page", style=discord.ButtonStyle.primary)

class shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `shop.py`")

    @app_commands.command(name="shop", description="View the server shop!")
    async def shop(self, interaction: discord.Interaction, page: int=None):
        try:
            member = interaction.user
            playerDB = mycol.find_one({"_id": member.id})
            #### COLORS
            COLORninja = discord.utils.get(member.guild.roles, id=1050822390952763473)
            COLORgreen = discord.utils.get(member.guild.roles, id=1051199158658285738)
            COLORteal = discord.utils.get(member.guild.roles, id=1051199137326055455)
            COLORblue = discord.utils.get(member.guild.roles, id=1051199127326830654)
            COLORpurple = discord.utils.get(member.guild.roles, id=1051199155470602341)
            COLORred = discord.utils.get(member.guild.roles, id=1051199153029521408)
            COLORorange = discord.utils.get(member.guild.roles, id=1051199144129212496)
            COLORyellow = discord.utils.get(member.guild.roles, id=1051199137024053310)
            COLORwhite = discord.utils.get(member.guild.roles, id=1051199138454310982)
            #COLORextra = discord.utils.get(member.guild.roles, id=1051199150101897216)
            ### CHECK DB
            checkNinja = playerDB['roles']['ninja']
            checkGreen = playerDB['roles']['green']
            checkTeal = playerDB['roles']['teal']
            checkBlue = playerDB['roles']['blue']
            checkPurple = playerDB['roles']['purple']
            checkRed = playerDB['roles']['red']
            checkOrange = playerDB['roles']['orange']
            checkYellow = playerDB['roles']['yellow']
            checkWhite = playerDB['roles']['white']
            #checkExtra = playerDB['roles']['extra']

            if checkNinja != True: # Ninja
                priceNinja = "$500,000"
            else:
                priceNinja = "Purchased"
            if checkGreen != True: # Green
                priceGreen = "$50,000"
            else:
                priceGreen = "Purchased"
            if checkTeal!= True: # Teal
                priceTeal = "$50,000"
            else:
                priceTeal = "Purchased"
            if checkBlue != True: # Blue
                priceBlue = "$50,000"
            else:
                priceBlue = "Purchased"
            if checkPurple != True: # Purple
                pricePurple = "$50,000"
            else:
                pricePurple = "Purchased"
            if checkRed != True: # Red
                priceRed = "$50,000"
            else:
                priceRed = "Purchased"
            if checkOrange != True: # Orange
                priceOrange = "$50,000"
            else:
                priceOrange = "Purchased"
            if checkYellow != True: # Yellow
                priceYellow = "$50,000"
            else:
                priceYellow = "Purchased"
            if checkWhite != True: # White
                priceWhite = "$50,000"
            else:
                priceWhite = "Purchased"
            #if checkExtra != True: # Extra
            #    priceExtra = "$50,000"
            #else:
            #    priceExtra = "Purchased"
            ####EMBEDS
            shopPage1 = discord.Embed(color=config.color, timestamp=datetime.now(), title="Roles", description="`/purchase` to make a purchase!\nTo equip colors you have purchased `/color`")
            shopPage1.set_author(name="Server Shop • Page 1")
            shopPage1.set_thumbnail(url=interaction.guild.icon)
            shopPage1.set_footer(text=config.footer)
            shopPage1.add_field(name=f"{COLORninja.name}", value=f"{priceNinja}\n{COLORninja.mention}")
            shopPage1.add_field(name=f"{COLORgreen.name}", value=f"{priceGreen}\n{COLORgreen.mention}")
            shopPage1.add_field(name=f"{COLORteal.name}", value=f"{priceTeal}\n{COLORteal.mention}")
            shopPage1.add_field(name=f"{COLORblue.name}", value=f"{priceBlue}\n{COLORblue.mention}")
            shopPage1.add_field(name=f"{COLORpurple.name}", value=f"{pricePurple}\n{COLORpurple.mention}")
            shopPage1.add_field(name=f"{COLORred.name}", value=f"{priceRed}\n{COLORred.mention}")
            shopPage1.add_field(name=f"{COLORorange.name}", value=f"{priceOrange}\n{COLORorange.mention}")
            shopPage1.add_field(name=f"{COLORyellow.name}", value=f"{priceYellow}\n{COLORyellow.mention}")
            shopPage1.add_field(name=f"{COLORwhite.name}", value=f"{priceWhite}\n{COLORwhite.mention}")
            #shopPage1.add_field(name=f"{COLORextra.name}", value=f"{priceExtra}\n{COLORextra.mention}")
            
            #rolesPageButton.disabled = False
            #view = View()
            #view.add_item(rolesPageButton)
            #view.add_item(previousPageButton)
            #view.add_item(whatPageButton)
            #view.add_item(nextPageButton)
            #view.add_item(lastPageButton)
            await interaction.response.send_message(embed=shopPage1, ephemeral=True)
            #rolesPageButton.callback = rolesPageButton_callback
            #previousPageButton.callback = previousPageButton_callback
            #nextPageButton.callback = nextPageButton_callback
            #lastPageButton.callback = lastPageButton_callback

        except Exception as e:
            print(e)
    
    @app_commands.command(name="purchase", description="Purchase something from the shop")
    async def purchase(self, interaction: discord.Interaction, name: str):
        member = interaction.user
        player = mycol.find_one({"_id": member.id})
        wallet = player['economy']['wallet']
        bank = player['economy']['bank']
        total = wallet + bank
        user = player['_id']
        mycol.update_one({"_id": user}, {"$set": {"economy.total": total}})
        total = player['economy']['total']
        print(total)
        if name.lower() == "ninja" and total >= 500000:
            
            return await interaction.response.send_message("Success!")
        elif name.lower() == "green" and total == 50000:
            return
        else:
            return await interaction.response.send_message("You did not have enough money.")

        
        
        
        
        
        
        
        return await interaction.response.send_message("WIP", ephemeral=True)

async def setup(bot):
    await bot.add_cog(shop(bot), guilds=[discord.Object(id=860752406551461909)])