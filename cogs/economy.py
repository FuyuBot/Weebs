from ast import Not
import discord
from discord import app_commands
from discord.ext import commands
import random
import mysql.connector
from config import host, user, password, db

seniorstaff = 865054271857885225
managementTeam = 860758013731274762
staffTeam = 860758014386896926
member = 860757567566774322

mydb = mysql.connector.connect(
host = host,
user = user,
password = password,
database = db
)
cursor = mydb.cursor()
class economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `economy.py`")
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot: return
        
        user = message.author
        cursor.execute(f"SELECT id FROM economy WHERE id = {user.id}")
        userDB = cursor.fetchone()
        if userDB is None:
            cursor.execute(f"INSERT INTO economy (id, wallet, bank) VALUES ({user.id}, 0, 0)")
        else: return
        mydb.commit()
    
    @app_commands.command(name='balance', description="Check your balance.")
    @app_commands.checks.has_any_role(member, staffTeam, seniorstaff, managementTeam)
    async def balance(self, interaction: discord.Interaction , member: discord.Member=None):
        try:
            if member == None:
                cursor.execute(f"SELECT id FROM economy WHERE id = {interaction.user.id}")
                userDB = cursor.fetchone()
                if userDB is None:
                    cursor.execute(f"INSERT INTO economy (id, wallet, bank) VALUES ({interaction.user.id}, 0, 0)")
                    mydb.commit()
                    cursor.execute(f"SELECT wallet, bank FROM economy WHERE id = {interaction.user.id}")
                    bal = cursor.fetchone()
                    try:
                        wallet = bal[0]
                        bank = bal[1]
                    except:
                        wallet = 0
                        bank = 0
                    
                    embed=discord.Embed(title="Your bank balance", color=0x2699C6)
                    embed.set_author(name=f"{interaction.user.name}", icon_url=f"{interaction.user.avatar}")
                    embed.add_field(name="Wallet Balance:", value=f"{wallet}", inline=True)
                    embed.add_field(name="Bank Ballance", value=f"{bank}")

                    await interaction.response.send_message(embed=embed)
                else:
                    mydb.reconnect()
                    cursor.execute(f"SELECT wallet, bank FROM economy WHERE id = {interaction.user.id}")
                    
                    bal = cursor.fetchone()
                    try:
                        wallet = bal[0]
                        bank = bal[1]
                    except:
                        wallet = 0
                        bank = 0
                    
                    embed=discord.Embed(title="Your bank balance", color=0x2699C6)
                    embed.set_author(name=f"{interaction.user.name}", icon_url=f"{interaction.user.avatar}")
                    embed.add_field(name="Wallet Balance:", value=f"{wallet}", inline=True)
                    embed.add_field(name="Bank Ballance", value=f"{bank}")

                    await interaction.response.send_message(embed=embed)

            else:
                if interaction.user.get_role(staffTeam) == "Staff Team" or interaction.user.get_role(seniorstaff) == "Senior Staff" or interaction.user.get_role(managementTeam) == "Management Team":
                    await interaction.response.send_message("Unfortunately you cannot use this command to check someone elses balance.")
                else:
                    cursor.execute(f"SELECT id FROM economy WHERE id = {member.id}")
                    userDB = cursor.fetchone()
                    if userDB is None:
                        cursor.execute(f"INSERT INTO economy (id, wallet, bank) VALUES ({member.id}, 0, 0)")
                        mydb.commit()
                        mydb.reconnect()
                        cursor.execute(f"SELECT wallet, bank FROM economy WHERE id = {member.id}")
                        bal = cursor.fetchone()
                        try:
                            wallet = bal[0]
                            bank = bal[1]
                        except:
                            wallet = 0
                            bank = 0
                        
                        embed=discord.Embed(title=f"{member.name}'s bank balance", color=0x2699C6)
                        embed.set_author(name=f"{interaction.user.name}", icon_url=f"{interaction.user.avatar}")
                        embed.add_field(name="Wallet Balance:", value=f"{wallet}", inline=True)
                        embed.add_field(name="Bank Ballance", value=f"{bank}")

                        await interaction.response.send_message(embed=embed)
                    else:
                        mydb.reconnect()
                        cursor.execute(f"SELECT wallet, bank FROM economy WHERE id = {member.id}")
                        
                        bal = cursor.fetchone()
                        try:
                            wallet = bal[0]
                            bank = bal[1]
                            print("it can see the balance from the db")
                        except:
                            wallet = 0
                            bank = 0
                            print("did not read the balance from the db")
                        
                        embed=discord.Embed(title=f"{member.name}'s bank balance", color=0x2699C6)
                        embed.set_author(name=f"{interaction.user.name}", icon_url=f"{interaction.user.avatar}")
                        embed.add_field(name="Wallet Balance:", value=f"{wallet}", inline=True)
                        embed.add_field(name="Bank Ballance", value=f"{bank}")

                        await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(e)
    @app_commands.command(name='work', description="Check your balance.")
    @app_commands.checks.has_any_role(member, staffTeam, seniorstaff, managementTeam)
    async def work(self, interaction: discord.Interaction):
        earnings = random.randint(1, 5)
        cursor.execute(f"SELECT id FROM economy WHERE id = {interaction.user.id}")
        userDB = cursor.fetchone()
        if userDB is None:
            cursor.execute(f"INSERT INTO economy (id, wallet, bank) VALUES ({interaction.user.id}, 0, 0)")
            mydb.commit()
            cursor.execute(f"SELECT wallet FROM economy WHERE id = {interaction.user.id}")
            wallet = cursor.fetchone()
            cursor.execute(f"UPDATE economy SET wallet {earnings + wallet} WHERE id = {interaction.user.id}")

            try:
                wallet = wallet[0]
            except:
                wallet = 0
            
            embed=discord.Embed(title=f"You earned ${earnings} from working!", color=0x2699C6)
            embed.set_author(name=f"{interaction.user.name}", icon_url=f"{interaction.user.avatar}")

            await interaction.response.send_message(embed=embed)
        else:
            try:
                cursor.execute(f"INSERT INTO economy (id, wallet, bank) VALUES ({interaction.user.id}, 0, 0)")
                mydb.commit()
                cursor.execute(f"SELECT wallet FROM economy WHERE id = {interaction.user.id}")
                wallet = cursor.fetchone()
                cursor.execute(f"UPDATE economy SET wallet {earnings + wallet} WHERE id = {interaction.user.id}")

                try:
                    wallet = wallet[0]
                except:
                    wallet = 0
                
                embed=discord.Embed(title=f"You earned ${earnings} from working!", color=0x2699C6)
                embed.set_author(name=f"{interaction.user.name}", icon_url=f"{interaction.user.avatar}")

                await interaction.response.send_message(embed=embed)
            except Exception as e:
                print(e)

        mydb.commit()

async def setup(bot):
    await bot.add_cog(economy(bot), guilds=[discord.Object(id=860752406551461909)])