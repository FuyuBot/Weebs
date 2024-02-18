import discord
import random
from discord.ext import commands
from discord import app_commands
import config
import TOKEN
import pymongo

managementTeam = 860758013731274762
member = 860757567566774322
star = 860760039564378142

myclient = pymongo.MongoClient(TOKEN.mongoDB)
mydb = myclient["InternationalGang"]
mycol = mydb["user_info"]

limit = [150.0, #1
                    225.0, #2
                    337, #3
                    506, #4
                    759, #5
                    1139, #6
                    1708, #7
                    2562, #8
                    3844, #9
                    5766, #10
                    8649, #11
                    12974, #12
                    19461, #13
                    29192, #14
                    43789, #15
                    65684, #15
                    98526, #16
                    147789, #17
                    221683, #18
                    332525, #19
                    498788, #20
                    748182, #21
                    1122274, #22
                    1683411, #23
                    2525116, #24
                    3787675, #25
                    5681512, #26
                    8522269, #27
                    12783403, #28
                    19175105, #29
                    28762658, #30
                    43143988, #31
                    64715982, #32
                    97073973, #33
                    145610960, #34
                    218416440, #35
                    327624661, #36
                    491436992, #37
                    737155488, #38
                    1105733232, #39
                    1658599848, #40
                    2487899772, #41
                    3731849658, #42
                    5597774487, #43
                    8396661731, #44
                    12594992596, #45
                    18892488895, #46
                    28338733342, #47 
                    42508100014, #48
                    63762150021, #49
                    95643225032] #50


class Confirm(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)
    
    @discord.ui.button(label= "Confirm", style= discord.ButtonStyle.red, custom_id= 'confirmmm')
    async def confirm_button2(self, interaction: discord.Interaction, button):
        try:
            playerDB = mycol.find()
            for x in playerDB:
                mycol.update_one({'_id': x['_id']}, {"$set": {"levels.level": 0}})
                mycol.update_one({'_id': x['_id']}, {"$set": {"levels.xp": 0}})
            await interaction.response.send_message("Levels reset.")
        except Exception as e:
            print(e)

class levelsint(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `leveling.py`")
    
    @app_commands.command(name='reset-levels', description="Resets the XP levels in the server.")
    @app_commands.checks.has_any_role("Jacob")
    async def resetLevels(self, interaction: discord.Interaction):
        await interaction.response.send_message("Are you sure you would like to reset all of the levels in the server? This action is irreversible.", view=Confirm(), ephemeral=True)

    @app_commands.command(name='reset-member-level', description="Resets the XP and levels of a specified user.")
    @app_commands.checks.has_any_role("Jacob")
    async def resetMemberLevel(self, interaction: discord.Interaction, user: discord.Member):
        player = user.id
        mycol.update_one({'_id': player}, {"$set": {"levels.level": 0}})
        mycol.update_one({'_id': player}, {"$set": {"levels.xp": 0}})
        await interaction.response.send_message("Level reset.")
        
    
    @app_commands.command(name='set-member-level', description="Set the level of a specified user.")
    @app_commands.checks.has_any_role("Jacob")
    async def setMemberLevel(self, interaction: discord.Interaction, user: discord.Member, level: int):
        try:
            player = user.id
            if level < 1:
                return await interaction.response.send_message("The number must be greater than 0")
            mycol.update_one({'_id': player}, {"$set": {"levels.level": level}})
            await interaction.response.send_message("Level set.")
        except Exception as e:
            await interaction.response.send_message("<@920797181034778655> There was an error: " + str(e))
    
    @app_commands.command(name='set-member-xp', description="Set the XP of a specified user.")
    @app_commands.checks.has_any_role("Jacob")
    async def setMemberXP(self, interaction: discord.Interaction, user: discord.Member, xp: float):
        try:
            player = user.id
            if xp < 0:
                return await interaction.response.send_message("The number must be greater than 0")
            mycol.update_one({'_id': player}, {"$set": {"levels.xp": xp}})
            await interaction.response.send_message("XP set.")
        except Exception as e:
            await interaction.response.send_message("<@920797181034778655> There was an error: " + str(e))
    
    @app_commands.command(name='add-member-xp', description="Add XP to a specified user.")
    @app_commands.checks.has_any_role("Jacob")
    async def addMemberXP(self, interaction: discord.Interaction, user: discord.Member, xp: float):
        try:
            player = user.id
            if xp < 0:
                return await interaction.response.send_message("The number must be greater than 0")
            playerDB = mycol.find_one({"_id": player})
            currentXP = playerDB['levels']['xp']
            newXP = currentXP + xp
            mycol.update_one({'_id': player}, {"$set": {"levels.xp": newXP}})
            await interaction.response.send_message("XP added.")
        except Exception as e:
            await interaction.response.send_message("<@920797181034778655> There was an error: " + str(e))
    
    @app_commands.command(name='add-member-level', description="Add levels to a specified user.")
    @app_commands.checks.has_any_role("Jacob")
    async def addMemberLevel(self, interaction: discord.Interaction, user: discord.Member, level: int):
        try:
            player = user.id
            if level < 1:
                return await interaction.response.send_message("The number must be greater than 0")
            playerDB = mycol.find_one({"_id": player})
            currentLevel = playerDB['levels']['level']
            newLevel = currentLevel + level
            mycol.update_one({'_id': player}, {"$set": {"levels.level": newLevel}})
            await interaction.response.send_message("Levels added.")
        except Exception as e:
            await interaction.response.send_message("<@920797181034778655> There was an error: " + str(e))
    
    @app_commands.command(name='remove-member-xp', description="Remove XP from a specified user.")
    @app_commands.checks.has_any_role("Jacob")
    async def removeMemberXP(self, interaction: discord.Interaction, user: discord.Member, xp: float):
        try:
            player = user.id
            if xp < 0:
                return await interaction.response.send_message("The number must be greater than 0")
            playerDB = mycol.find_one({"_id": player})
            currentXP = playerDB['levels']['xp']
            newXP = currentXP - xp
            mycol.update_one({'_id': player}, {"$set": {"levels.xp": newXP}})
            await interaction.response.send_message("XP removed.")
        except Exception as e:
            await interaction.response.send_message("<@920797181034778655> There was an error: " + str(e))
    
    @app_commands.command(name='remove-member-level', description="Remove levels from a specified user.")
    @app_commands.checks.has_any_role("Jacob")
    async def removeMemberLevel(self, interaction: discord.Interaction, user: discord.Member, level: int):
        try:
            player = user.id
            if level < 1:
                return await interaction.response.send_message("The number must be greater than 0")
            playerDB = mycol.find_one({"_id": player})
            currentLevel = playerDB['levels']['level']
            newLevel = currentLevel - level
            mycol.update_one({'_id': player}, {"$set": {"levels.level": newLevel}})
            await interaction.response.send_message("Levels removed.")
        except Exception as e:
            await interaction.response.send_message("<@920797181034778655> There was an error: " + str(e))
    
    @app_commands.command(name='list-xp-level', description="List the XP required for each level.")
    async def listXPLevel(self, interaction: discord.Interaction):
        try:
            embed = discord.Embed(title="XP Required for Each Level", color=config.color)
            for x in range(0, 50):
                embed.add_field(name=f"Level {x+1}", value=f"{limit[x]:,.2f}", inline=False)
            return await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(e)

    @app_commands.command(name='level', description="Check what level you are.")
    async def level(self, interaction: discord.Interaction, user: discord.Member=None):
        try:
            if user == None:
                player = interaction.user.id
                playerDB = mycol.find_one({"_id": player})
                xp = playerDB['levels']['xp']
                level = playerDB['levels']['level']
                embed = discord.Embed(color=config.color)
                embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
                embed.add_field(name="__Level__", value=level)
                embed.add_field(name="__XP__", value=f"{xp:,.2f}")
                return await interaction.response.send_message(embed=embed)
            else:
                player = user.id
                playerDB = mycol.find_one({"_id": player})
                xp = playerDB['levels']['xp']
                level = playerDB['levels']['level']
                embed = discord.Embed(color=config.color)
                embed.set_author(name=user, icon_url=user.avatar)
                embed.add_field(name="__Level__", value=level)
                embed.add_field(name="__XP__", value=f"{xp:,.2f}")
                return await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(e)

    @app_commands.command(name="level-leaderboard", description="Displays the leveling leaderboard for everyone in the server.")
    async def levelLeaderboard(self, interaction: discord.Interaction):
        try:
            embed = discord.Embed(title="Level Leaderboard", color=config.color)
            playerDB = mycol.find().sort([("levels.level", -1), ("levels.xp", -1)]).limit(10)
            count = 0
            for x in playerDB:
                count += 1
                user = self.bot.get_user(int(x['_id']))
                xp = x['levels']['xp']
                level = x['levels']['level']
                embed.add_field(name=f"{count}. {user}", value=f"Level: **{level}** | XP: **{xp:,.2f}**", inline=False) 
            return await interaction.response.send_message(embed=embed)
        except Exception as e:
            await interaction.response.send_message("<@920797181034778655> There was an error: " + str(e))

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            badChannels = [892573395273789520,942934115609608213,865107660624756775] #Counting, PokeTwo, Bots
            if message.author.bot:
                return
            if message.channel in badChannels:
                return
            player = message.author.id
            playerDB = mycol.find_one({"_id": player})
            xp = playerDB['levels']['xp']
            level = playerDB['levels']['level']
            xp += random.uniform(1, 3)
            xpROUND = round(xp, 2)
            
            
            
            if xp >= limit[level]:
                level += 1
                wallet =  playerDB['economy']['wallet']
                earnings = level * 10
                amount = earnings + float(wallet)
                mycol.update_one({'_id': player}, {"$set": {"economy.wallet": amount}})
                mycol.update_one({'_id': player}, {"$set": {"levels.level": level}})
                mycol.update_one({'_id': player}, {"$set": {"levels.xp": xp}})
                await message.channel.send(f'<@{player}> has leveled up to level **{level}**!')
            else:
                mycol.update_one({'_id': player}, {"$set": {"levels.xp": xpROUND}})
        except Exception as e:
            print(e)


async def setup(bot):
    await bot.add_cog(levelsint(bot), guilds=[discord.Object(id=config.internationalGang)])
