import discord
import random
from discord.ext import commands
from discord import app_commands
import config
import pymongo

managementTeam = 860758013731274762
member = 860757567566774322
star = 860760039564378142

myclient = pymongo.MongoClient(config.mongoDB)
mydb = myclient["WeebsHangout"]
mycol = mydb["user_info"]


class Confirm(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)
    
    @discord.ui.button(label= "Confirm", style= discord.ButtonStyle.red, custom_id= 'confirmmm')
    async def confirm_button2(self, interaction: discord.Interaction, button):
        try:
            player = interaction.user.id
            playerDB = mycol.find()
            for x in playerDB:
                mycol.update_one({'_id': x['_id']}, {"$set": {"levels.level": 0}})
                mycol.update_one({'_id': x['_id']}, {"$set": {"levels.xp": 0}})
            await interaction.response.send_message("Levels reset.")
        except Exception as e:
            print(e)

class levels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `leveling.py`")
    
    @app_commands.command(name='reset-levels', description="Resets the XP levels in the server.")
    @app_commands.checks.has_any_role(managementTeam)
    async def resetLevels(self, interaction: discord.Interaction):
        await interaction.response.send_message("Are you sure you would like to reset all of the levels in the server? This action is irreversible.", view=Confirm(), ephemeral=True)

    @app_commands.command(name='reset-member-level', description="Resets the XP and levels of a specified user.")
    @app_commands.checks.has_any_role(managementTeam)
    async def resetMemberLevel(self, interaction: discord.Interaction, user: discord.Member):
        player = user.id
        mycol.update_one({'_id': player}, {"$set": {"levels.level": 0}})
        mycol.update_one({'_id': player}, {"$set": {"levels.xp": 0}})
        await interaction.response.send_message("Level reset.")
        
    
    @app_commands.command(name='set-member-level', description="Set the level of a specified user.")
    @app_commands.checks.has_any_role(managementTeam)
    async def setMemberLevel(self, interaction: discord.Interaction, user: discord.Member, level: int):
        player = user.id
        if level < 1:
            return await interaction.response.send_message("The number must be greater than 0")
        limit = [150.0, 225.0, 337.5, 506.25, 759.38, 1139.06, 1708.59, 2562.89, 3844.34, 5766.5, 8649.76, 12974.63, 19461.95, 29192.93, 43789.39, 65684.08, 98526.13, 147789.19, 221683.78, 332525.67]
        mycol.update_one({'_id': player}, {"$set": {"levels.level": level}})
        mycol.update_one({'_id': player}, {"$set": {"levels.xp": limit[level - 1]}})
        await interaction.response.send_message("Level set.")

    @app_commands.command(name='level', description="Check what level you are.")
    async def level(self, interaction: discord.Interaction, user: discord.Member=None):
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
            embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
            embed.add_field(name="__Level__", value=level)
            embed.add_field(name="__XP__", value=f"{xp:,.2f}")
            return await interaction.response.send_message(embed=embed)

    @app_commands.command(name="leaderboard", description="Displays the leveling leaderboard for everyone in the server.")
    async def leaderboard(self, interaction: discord.Interaction):
        try:
            embed = discord.Embed(title="Leaderboard", color=config.color)
            playerDB = mycol.find().sort([("levels.level", -1), ("levels.xp", -1)]).limit(10)
            count = 0
            for x in playerDB:
                count += 1
                user = self.bot.get_user(int(x['_id']))
                xp = x['levels']['xp']
                level = x['levels']['level']
                embed.add_field(name=f"{count}. {user.name}", value=f"Level: **{level}** | XP: **{xp:,.2f}**", inline=False) 
            return await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(e)

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
            
            limit = [150.0, 225.0, 337.5, 506.25, 759.38, 1139.06, 1708.59, 2562.89, 3844.34, 5766.5, 8649.76, 12974.63, 19461.95, 29192.93, 43789.39, 65684.08, 98526.13, 147789.19, 221683.78, 332525.67]
            
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
    await bot.add_cog(levels(bot), guilds=[discord.Object(id=860752406551461909)])