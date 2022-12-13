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
    async def shop(self, interaction: discord.Interaction):
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
            shopPage1 = discord.Embed(color=config.color, timestamp=datetime.now(), title="Roles", description="`/purchase` to make a purchase!\nTo equip colors you have purchased `/colors`")
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
        try:
            member = interaction.user
            COLORninja = discord.utils.get(member.guild.roles, id=1050822390952763473)
            COLORgreen = discord.utils.get(member.guild.roles, id=1051199158658285738)
            COLORteal = discord.utils.get(member.guild.roles, id=1051199137326055455)
            COLORblue = discord.utils.get(member.guild.roles, id=1051199127326830654)
            COLORpurple = discord.utils.get(member.guild.roles, id=1051199155470602341)
            COLORred = discord.utils.get(member.guild.roles, id=1051199153029521408)
            COLORorange = discord.utils.get(member.guild.roles, id=1051199144129212496)
            COLORyellow = discord.utils.get(member.guild.roles, id=1051199137024053310)
            COLORwhite = discord.utils.get(member.guild.roles, id=1051199138454310982)
            user = member.id
            player = mycol.find_one({"_id": member.id})
            wallet = player['economy']['wallet']

            if name.lower() == "ninja": #NINJA
                if wallet >= 500000:
                    if player['roles']['ninja'] == False:
                        newAmount = wallet - 500000
                        mycol.update_one({"_id": user}, {"$set": {"economy.wallet": newAmount}})
                        mycol.update_one({"_id": user}, {"$set": {"roles.ninja": True}})
                        return await interaction.response.send_message(f"You have successfully purchased the {COLORninja.mention} role.\n`/colors` to equip it.", ephemeral=True)
                    else:
                        return await interaction.response.send_message("")
                else:
                    return await interaction.response.send_message("You do not have enough money to purchase that.", ephemeral=True)
            elif name.lower() == "green": #GREEN
                if wallet >= 50000:
                    if player['roles']['green'] == False:
                        newAmount = wallet - 50000
                        mycol.update_one({"_id": user}, {"$set": {"economy.wallet": newAmount}})
                        mycol.update_one({"_id": user}, {"$set": {"roles.green": True}})
                        return await interaction.response.send_message(f"You have successfully purchased the {COLORgreen.mention} role.\n`/colors` to equip it.", ephemeral=True)
                else:
                    return await interaction.response.send_message("You already have that role purchased.", ephemeral=True)
            elif name.lower() == "teal": #TEAL
                if wallet >= 50000:
                    if player['roles']['teal'] == False:
                        newAmount = wallet - 50000
                        mycol.update_one({"_id": user}, {"$set": {"economy.wallet": newAmount}})
                        mycol.update_one({"_id": user}, {"$set": {"roles.teal": True}})
                        return await interaction.response.send_message(f"You have successfully purchased the {COLORteal.mention} role.\n`/colors` to equip it.", ephemeral=True)
                else:
                    return await interaction.response.send_message("You already have that role purchased.", ephemeral=True)
            elif name.lower() == "blue": #BLUE
                if wallet >= 50000:
                    if player['roles']['blue'] == False:
                        newAmount = wallet - 50000
                        mycol.update_one({"_id": user}, {"$set": {"economy.wallet": newAmount}})
                        mycol.update_one({"_id": user}, {"$set": {"roles.blue": True}})
                        return await interaction.response.send_message(f"You have successfully purchased the {COLORblue.mention} role.\n`/colors` to equip it.", ephemeral=True)
                else:
                    return await interaction.response.send_message("You already have that role purchased.", ephemeral=True)
            elif name.lower() == "purple": #PURPLE
                if wallet >= 50000:
                    if player['roles']['purple'] == False:
                        newAmount = wallet - 50000
                        mycol.update_one({"_id": user}, {"$set": {"economy.wallet": newAmount}})
                        mycol.update_one({"_id": user}, {"$set": {"roles.purple": True}})
                        return await interaction.response.send_message(f"You have successfully purchased the {COLORpurple.mention} role.\n`/colors` to equip it.", ephemeral=True)
                else:
                    return await interaction.response.send_message("You already have that role purchased.", ephemeral=True)
            elif name.lower() == "red": #RED
                if wallet >= 50000:
                    if player['roles']['red'] == False:
                        newAmount = wallet - 50000
                        mycol.update_one({"_id": user}, {"$set": {"economy.wallet": newAmount}})
                        mycol.update_one({"_id": user}, {"$set": {"roles.red": True}})
                        return await interaction.response.send_message(f"You have successfully purchased the {COLORred.mention} role.\n`/colors` to equip it.", ephemeral=True)
                else:
                    return await interaction.response.send_message("You already have that role purchased.", ephemeral=True)
            elif name.lower() == "orange": #ORANGE
                if wallet >= 50000:
                    if player['roles']['orange'] == False:
                        newAmount = wallet - 50000
                        mycol.update_one({"_id": user}, {"$set": {"economy.wallet": newAmount}})
                        mycol.update_one({"_id": user}, {"$set": {"roles.orange": True}})
                        return await interaction.response.send_message(f"You have successfully purchased the {COLORorange.mention} role.\n`/colors` to equip it.", ephemeral=True)
                else:
                    return await interaction.response.send_message("You already have that role purchased.", ephemeral=True)
            elif name.lower() == "yellow": #YELLOW
                if wallet >= 50000:
                    if player['roles']['yellow'] == False:
                        newAmount = wallet - 50000
                        mycol.update_one({"_id": user}, {"$set": {"economy.wallet": newAmount}})
                        mycol.update_one({"_id": user}, {"$set": {"roles.yellow": True}})
                        return await interaction.response.send_message(f"You have successfully purchased the {COLORyellow.mention} role.\n`/colors` to equip it.", ephemeral=True)
                else:
                    return await interaction.response.send_message("You already have that role purchased.", ephemeral=True)
            elif name.lower() == "white": # WHITE
                if wallet >= 50000:
                    if player['roles']['white'] == False:
                        newAmount = wallet - 50000
                        mycol.update_one({"_id": user}, {"$set": {"economy.wallet": newAmount}})
                        mycol.update_one({"_id": user}, {"$set": {"roles.white": True}})
                        return await interaction.response.send_message(f"You have successfully purchased the {COLORwhite.mention} role.\n`/colors` to equip it.", ephemeral=True)
                else:
                    return await interaction.response.send_message("You already have that role purchased.", ephemeral=True)
            else:
                return await interaction.response.send_message("That was not one of the responses, do `/shop` to see the possible items to purchase.")
        except Exception as e:
            print(e)

    @app_commands.command(name="colors", description="View or set the role color you have.")
    @app_commands.choices(set=[
        discord.app_commands.Choice(name='None', value="none"),
        discord.app_commands.Choice(name='Ninja', value="ninja"),
        discord.app_commands.Choice(name='Green', value="green"),
        discord.app_commands.Choice(name='Teal', value="teal"),
        discord.app_commands.Choice(name='Blue', value="blue"),
        discord.app_commands.Choice(name='Purple', value="purple"),
        discord.app_commands.Choice(name='Red', value="red"),
        discord.app_commands.Choice(name='Orange', value="orange"),
        discord.app_commands.Choice(name='Yellow', value="yellow"),
        discord.app_commands.Choice(name='White', value="white")])
    async def colors(self, interaction: discord.Interaction, set: discord.app_commands.Choice[str]=None):
        try:
            member = interaction.user
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
            playerDB = mycol.find_one({"_id": member.id})
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
            if set == None:
                haveColors = []
                if checkNinja == True: # Ninja
                    haveColors.append(COLORninja.mention)
                if checkGreen == True: # Green
                    haveColors.append(COLORgreen.mention)
                if checkTeal == True: # Teal
                    haveColors.append(COLORteal.mention)
                if checkBlue == True: # Blue
                    haveColors.append(COLORblue.mention)
                if checkPurple == True: # Purple
                    haveColors.append(COLORpurple.mention)
                if checkRed == True: # Red
                    haveColors.append(COLORred.mention)
                if checkOrange == True: # Orange
                    haveColors.append(COLORorange.mention)
                if checkYellow == True: # Yellow
                    haveColors.append(COLORyellow.mention)
                if checkWhite == True: # White
                    haveColors.append(COLORwhite.mention)
                embed = discord.Embed(color=config.color, title="Purchased Colors", description=f", ".join(haveColors))
                return await interaction.response.send_message(embed=embed, ephemeral=True)
            else:
                if set.value == "ninja" and checkNinja == True: #NINJA
                    await member.add_roles(COLORninja)
                    await member.remove_roles(COLORgreen, COLORteal, COLORblue, COLORpurple, COLORred, COLORorange, COLORyellow, COLORwhite)
                    await interaction.response.send_message(f"You have successfully set your color to {COLORninja.mention}.", ephemeral=True)
                elif set.value == "green" and checkGreen == True: #GREEN
                    await member.add_roles(COLORgreen)
                    await member.remove_roles(COLORninja, COLORteal, COLORblue, COLORpurple, COLORred, COLORorange, COLORyellow, COLORwhite)
                    await interaction.response.send_message(f"You have successfully set your color to {COLORgreen.mention}.", ephemeral=True)
                elif set.value == "teal" and checkTeal == True: #TEAL
                    await member.add_roles(COLORteal)
                    await member.remove_roles(COLORninja, COLORgreen, COLORblue, COLORpurple, COLORred, COLORorange, COLORyellow, COLORwhite)
                    await interaction.response.send_message(f"You have successfully set your color to {COLORteal.mention}.", ephemeral=True)
                elif set.value == "blue" and checkBlue == True: #BLUE
                    await member.add_roles(COLORblue)
                    await member.remove_roles(COLORninja, COLORgreen, COLORteal, COLORpurple, COLORred, COLORorange, COLORyellow, COLORwhite)
                    await interaction.response.send_message(f"You have successfully set your color to {COLORblue.mention}.", ephemeral=True)
                elif set.value == "purple" and checkPurple == True: #PURPLE
                    await member.add_roles(COLORpurple)
                    await member.remove_roles(COLORninja, COLORgreen, COLORteal, COLORblue, COLORred, COLORorange, COLORyellow, COLORwhite)
                    await interaction.response.send_message(f"You have successfully set your color to {COLORpurple.mention}.", ephemeral=True)
                elif set.value == "red" and checkRed == True: #RED
                    await member.add_roles(COLORred)
                    await member.remove_roles(COLORninja, COLORgreen, COLORteal, COLORblue, COLORpurple, COLORorange, COLORyellow, COLORwhite)
                    await interaction.response.send_message(f"You have successfully set your color to {COLORred.mention}.", ephemeral=True)
                elif set.value == "orange" and checkOrange == True: #ORANGE
                    await member.add_roles(COLORorange)
                    await member.remove_roles(COLORninja, COLORgreen, COLORteal, COLORblue, COLORpurple, COLORred, COLORyellow, COLORwhite)
                    await interaction.response.send_message(f"You have successfully set your color to {COLORorange.mention}.", ephemeral=True)
                elif set.value == "yellow" and checkYellow == True: #YELLOW
                    await member.add_roles(COLORyellow)
                    await member.remove_roles(COLORninja, COLORgreen, COLORteal, COLORblue, COLORpurple, COLORred, COLORorange, COLORwhite)
                    await interaction.response.send_message(f"You have successfully set your color to {COLORyellow.mention}.", ephemeral=True)
                elif set.value == "white" and checkWhite == True: #WHITE
                    await member.add_roles(COLORwhite)
                    await member.remove_roles(COLORninja, COLORgreen, COLORteal, COLORblue, COLORpurple, COLORred, COLORorange, COLORyellow)
                    await interaction.response.send_message(f"You have successfully set your color to {COLORwhite.mention}.", ephemeral=True)
                elif set.value == "none": #NONE
                    await member.remove_roles(COLORninja, COLORgreen, COLORteal, COLORblue, COLORpurple, COLORred, COLORorange, COLORyellow, COLORwhite)
                    await interaction.response.send_message(f"You have successfully removed your color.", ephemeral=True)
                else:
                    await interaction.response.send_message("How did you get here?")
        except Exception as e:
            print(e)

async def setup(bot):
    await bot.add_cog(shop(bot), guilds=[discord.Object(id=860752406551461909)])