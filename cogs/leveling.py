import discord
import random
from discord.ext import commands
from discord import app_commands
import mysql.connector
from config import host, user, password, db, color

managementTeam = 860758013731274762
member = 860757567566774322
star = 860760039564378142

mydb = mysql.connector.connect(
host = host,
user = user,
password = password,
database = db
)

class Confirm2(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)
    
    @discord.ui.button(label= "Confirm", style= discord.ButtonStyle.red, custom_id= 'confirmm')
    async def confirm_button2(self, interaction: discord.Interaction, button):
        try:
            cursor.execute(f"DELETE FROM levels")
            await interaction.response.send_message("Levels reset.")
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
        await interaction.response.send_message("Are you sure you would like to\
            reset all of the levels in the server? This action is irreversible.", view=Confirm2())
    
    @app_commands.command(name='level', description="Check what level you are.")
    async def level(self, interaction: discord.Interaction, member: discord.Member=None):
        if member == None:
            player = interaction.user.id
            cursor.execute(f"SELECT level FROM levels WHERE player = {player}")
            level = cursor.fetchone()
            cursor.execute(f"SELECT xp FROM levels WHERE player = {player}")
            xp = cursor.fetchone()
            cursor.execute(f"SELECT player FROM levels WHERE player = {player}")
            playerDB = cursor.fetchall()

            if playerDB == []:
                cursor.execute(f"INSERT INTO levels (player, level, xp) VALUES ({player}, 0, 0)")
                mydb.commit()
                level = level[0]
                xp = xp[0]
                embed = discord.Embed(color=color)
                embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
                embed.add_field(name="__Level__", value=level)
                embed.add_field(name="__XP__", value=f"{xp}/100")
                return await interaction.response.send_message(embed=embed)
            else:
                level = level[0]
                xp = xp[0]
                embed = discord.Embed(color=color)
                embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
                embed.add_field(name="__Level__", value=level)
                embed.add_field(name="__XP__", value=f"{xp}/100")
                return await interaction.response.send_message(embed=embed)
        else:
            player = member.id
            cursor.execute(f"SELECT level FROM levels WHERE player = {player}")
            level = cursor.fetchone()
            cursor.execute(f"SELECT xp FROM levels WHERE player = {player}")
            xp = cursor.fetchone()
            cursor.execute(f"SELECT player FROM levels WHERE player = {player}")
            playerDB = cursor.fetchall()

            if playerDB == []:
                cursor.execute(f"INSERT INTO levels (player, level, xp) VALUES ({player}, 0, 0)")
                mydb.commit()
                level = level[0]
                xp = xp[0]
                embed = discord.Embed(color=color)
                embed.set_author(name=member, icon_url=member.avatar)
                embed.add_field(name="__Level__", value=level)
                embed.add_field(name="__XP__", value=f"{xp}/100")
                return await interaction.response.send_message(embed=embed)
            else:
                level = level[0]
                xp = xp[0]
                embed = discord.Embed(color=color)
                embed.set_author(name=member, icon_url=member.avatar)
                embed.add_field(name="__Level__", value=level)
                embed.add_field(name="__XP__", value=f"{xp}/100")
                return await interaction.response.send_message(embed=embed)

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
                    return
                except:
                    await message.channel.send('Did not send to the DB, contact staff please.')
            try:
                xp = xp[0]
                level = level[0]
            except TypeError:
                xp = 0
                level = 0
            xp += random.uniform(1, 3)
            xpROUND = round(xp, 2)
            cursor.execute(f"UPDATE levels SET xp = {xpROUND} WHERE player = {player}")
            mydb.commit()
            if xp >= 100:
                try:
                    level += 1
                    xp = 0
                    cursor.execute(f"SELECT wallet FROM economy WHERE id = {message.author.id}")
                    wallet = cursor.fetchone()
                    earnings = 10
                    amount = earnings + float(wallet[0])
                    cursor.execute(f"UPDATE economy SET wallet = {amount} WHERE id = {message.author.id}")
                    cursor.execute(f"UPDATE levels SET level = {level} WHERE player = {player}")
                    cursor.execute(f"UPDATE levels SET xp = {xp} WHERE player = {player}")
                    mydb.commit()
                    await message.channel.send(f'<@{player}> has leveled up to level **{level}**!')
                except Exception as e:
                    print(e)
            mydb.commit()

async def setup(bot):
    await bot.add_cog(leveling(bot), guilds=[discord.Object(id=860752406551461909)])