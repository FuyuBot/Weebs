import discord
import random
from discord.ext import commands
from discord import app_commands
import mysql.connector
from config import host, user, password, db

managementTeam = 892573395273789520
member = 860757567566774322
star = 860760039564378142

mydb = mysql.connector.connect(
host = host,
user = user,
password = password,
database = db
)

class Confirm(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)
    
    @discord.ui.button(label= "Confirm", style= discord.ButtonStyle.red, custom_id= 'confirm')
    async def confirm_button(self, interaction: discord.Interaction, button):
        try: 
            cursor.execute(f"DELETE * FROM levels WHERE")
            interaction.response.send_message("Levels reset.")
        except Exception as e:
            print(e)

cursor = mydb.cursor()
class leveling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `leveling.py`")

    @app_commands.command(name='reset-levels', description="Resets the XP levels in the server.")
    @app_commands.checks.has_any_role(managementTeam)
    async def resetLevels(self, interaction: discord.Interaction):
        try:
            await interaction.response.send_message("Are you sure you would like to reset all of the levels in the server? This action is irreversible.", view=Confirm())
        except Exception as e:
            print

    @commands.Cog.listener()
    async def on_message(self, message):
        badChannels = [892573395273789520,942934115609608213,865107660624756775] #Counting, PokeTwo, Bots
        if message.author.bot:
            return
        if message.channel in badChannels:
            return
        player = message.author.id
        cursor.execute(f"SELECT player FROM levels WHERE player = {player}")
        playerDB = cursor.fetchall()
        cursor.execute(f"SELECT xp FROM levels WHERE player = {player}")
        xp = cursor.fetchone()
        cursor.execute(f"SELECT level FROM levels WHERE player = {player}")
        level = cursor.fetchone()

        if playerDB == []:
            cursor.execute(f"INSERT INTO levels (player, level, xp) VALUES ({player}, 0, 0)")
            mydb.commit()
        else:
            if xp == None or level == None:
                try:
                    
                    cursor.execute(f"INSERT INTO levels (player, level, xp) VALUES ({player}, 0, 0)")
                    mydb.commit()
                except:
                    await message.channel.send('Did not send to the DB, contact staff please.')
            try:
                xp = xp[0]
                level = level[0]
            except TypeError:
                xp = 0
                level = 0
            
            xp += random.uniform(99, 100)
            cursor.execute(f"UPDATE levels SET xp = {xp:,.2f} WHERE player = {player}")
            
            if xp >= 100:
                level += 1
                xp = 0
                cursor.execute(f"SELECT wallet FROM economy WHERE id = {message.user.id}")
                wallet = cursor.fetchone()
                earnings = 10
                amount = earnings + int(wallet[0])
                cursor.execute(f"UPDATE economy SET wallet = {amount} WHERE id = {message.user.id}")
                cursor.execute(f"UPDATE levels SET level = {level} WHERE player = {player}")
                cursor.execute(f"UPDATE levels SET xp = {xp} WHERE player = {player}")
                await message.channel.send(f'<@{player}> has leveled up to level **{level}**!')

                level10 = discord.utils.get(user.guild.roles, id=865727060861386792)
                level20 =discord.utils.get(user.guild.roles, id=865727060172603433)
                level30 =discord.utils.get(user.guild.roles, id=865727059299795005)
                level40 =discord.utils.get(user.guild.roles, id=865722681139527681)
                level50 =discord.utils.get(user.guild.roles, id=865430631944290334)
                level60 =discord.utils.get(user.guild.roles, id=927774106554884156)
                level70 =discord.utils.get(user.guild.roles, id=1034276120876548126)
                level80 =discord.utils.get(user.guild.roles, id=1027388421834031204)
                level90 =discord.utils.get(user.guild.roles, id=1034276482509451284)
                level100 =discord.utils.get(user.guild.roles, id=1034276484556275742)

                if level == 10:
                    await user.add_roles(level10)
                elif level == 20:
                    await user.add_roles(level20)
                elif level == 30:
                    await user.add_roles(level30)
                elif level == 40:
                    await user.add_roles(level40)
                elif level == 50:
                    await user.add_roles(level50)
                elif level == 60:
                    await user.add_roles(level60)
                elif level == 70:
                    await user.add_roles(level70)
                elif level == 80:
                    await user.add_roles(level80)
                elif level == 90:
                    await user.add_roles(level90)
                elif level == 100:
                    await user.add_roles(level100)
                
            
            mydb.commit()

async def setup(bot):
    await bot.add_cog(leveling(bot), guilds=[discord.Object(id=860752406551461909)])