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
        if message.author.bot:
            return
        if message.channel == 892573395273789520:
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
            
            if level < 5:
                xp += random.uniform(1, 3)
                cursor.execute(f"UPDATE levels SET xp = {xp:,.2f} WHERE player = {player}")
            else:
                rand = random.uniform(1, (level//4))
                if rand == 1:
                    xp += random.uniform(1, 3)
                    cursor.execute(f"UPDATE levels SET xp = {xp:,.2f} WHERE player = {player}")
            
            if xp >= 100:
                level += 1
                xp = 0
                cursor.execute(f"UPDATE levels SET level = {level} WHERE player = {player}")
                cursor.execute(f"UPDATE levels SET xp = {xp} WHERE player = {player}")
                await message.channel.send(f'<@{player}> has leveled up to level **{level}**!')

            

            
            
            mydb.commit()

async def setup(bot):
    await bot.add_cog(leveling(bot), guilds=[discord.Object(id=860752406551461909)])