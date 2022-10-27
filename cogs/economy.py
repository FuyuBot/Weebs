from ast import Not
import discord
from discord import app_commands
from discord.ext import commands
import random
import mysql.connector
from config import host, user, password, db
import math

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
                    embed.add_field(name="Bank Ballance:", value=f"{bank}")

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
                        embed.add_field(name="Bank Ballance:", value=f"{bank}")

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
                        embed.add_field(name="Bank Ballance:", value=f"{bank}")

                        await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(e)

    @app_commands.command(name='work', description="Earn money by working.")
    @app_commands.checks.has_any_role(member, staffTeam, seniorstaff, managementTeam)
    async def work(self, interaction: discord.Interaction):
        try:
            earnings = random.randint(1, 5)
            cursor.execute(f"SELECT id FROM economy WHERE id = {interaction.user.id}")
            userDB = cursor.fetchone()
            if userDB is None:
                cursor.execute(f"INSERT INTO economy (id, wallet, bank) VALUES ({interaction.user.id}, 0, 0)")
                mydb.commit()
                cursor.execute(f"SELECT wallet FROM economy WHERE id = {interaction.user.id}")
                wallet = cursor.fetchone()
                amount = earnings + int(wallet[0])
                cursor.execute(f"UPDATE economy SET wallet = {amount} WHERE id = {interaction.user.id}")

                try:
                    wallet = wallet[0]
                except:
                    wallet = 0
                
                embed=discord.Embed(description=f"You earned ${earnings} from working!", color=0x2699C6)
                embed.set_author(name=f"{interaction.user.name}", icon_url=f"{interaction.user.avatar}")

                await interaction.response.send_message(embed=embed)
            else:
                try:
                    cursor.execute(f"SELECT wallet FROM economy WHERE id = {interaction.user.id}")
                    wallet = cursor.fetchone()
                    amount = earnings + int(wallet[0])
                    cursor.execute(f"UPDATE economy SET wallet = {amount} WHERE id = {interaction.user.id}")
                    mydb.commit()
                    try:
                        wallet = wallet[0]
                    except:
                        wallet = 0
                    
                    embed=discord.Embed(description=f"You earned ${earnings} from working!", color=0x2699C6)
                    embed.set_author(name=f"{interaction.user.name}", icon_url=f"{interaction.user.avatar}")

                    await interaction.response.send_message(embed=embed)
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)

    @app_commands.command(name="deposit", description="Deposit money into your bank account.")
    @app_commands.checks.has_any_role(member, staffTeam, seniorstaff, managementTeam)
    async def deposit(self, interaction: discord.Interaction, amount: int):
        try:
            cursor.execute(f"SELECT * FROM economy WHERE ID = {interaction.user.id}")
            data = cursor.fetchone()
            if data is None:
                cursor.execute(f"INSERT INTO economy (id, wallet, bank) VALUES ({interaction.user.id}, 0, 0)")
                mydb.commit()
                return await interaction.response.send_message("Your account has just been created. You have no money to deposit.", ephemeral=True)
                
            else:
                try:
                    wallet = int(data[1])
                    bank = int(data[2])
                except Exception as e:
                    await interaction.response.send_message("There was an error.")
                    print(e)
                
                if wallet == 0:
                    return await interaction.response.send_message("You don't have any money to transfer over.", ephemeral=True)
                elif amount == 0:
                    return await interaction.response.send_message("You can't transfer $0.", ephemeral=True)
                elif wallet < amount:
                    return await interaction.response.send_message("That number is larger then the amount of money you have in your wallet.", ephemeral=True)
                else:
                    bankAmount = bank + amount
                    walletAmount = wallet - amount
                    cursor.execute(f"UPDATE economy SET bank = {bankAmount} WHERE id = {interaction.user.id}")
                    cursor.execute(f"UPDATE economy SET wallet = {walletAmount} WHERE id = {interaction.user.id}")
                    mydb.commit()
                    await interaction.response.send_message(f"You have deposited ${amount} into your bank.")
                    
        except Exception as e:
            print(e)
    
    @app_commands.command(name="withdraw", description="Withdraw money from your bank account.")
    @app_commands.checks.has_any_role(member, staffTeam, seniorstaff, managementTeam)
    async def withdraw(self, interaction: discord.Interaction, amount: int):
        cursor.execute(f"SELECT * FROM economy WHERE ID = {interaction.user.id}")
        data = cursor.fetchone()
        if data is None:
            cursor.execute(f"INSERT INTO economy (id, wallet, bank) VALUES ({interaction.user.id}, 0, 0)")
            mydb.commit()
            return await interaction.response.send_message("Your account has just been created. You have no money to withdraw.", ephemeral=True)
            
        else:
            try:
                wallet = int(data[1])
                bank = int(data[2])
            except Exception as e:
                await interaction.response.send_message("There was an error.")
                print(e)
            
            if bank == 0:
                return await interaction.response.send_message("You don't have any money to transfer over.", ephemeral=True)
            elif amount == 0:
                return await interaction.response.send_message("You can't transfer $0.", ephemeral=True)
            elif bank < amount:
                return await interaction.response.send_message("That number is larger then the amount of money you have in your bank.", ephemeral=True)
            else:
                bankAmount = bank - amount
                walletAmount = wallet + amount
                cursor.execute(f"UPDATE economy SET bank = {bankAmount} WHERE id = {interaction.user.id}")
                cursor.execute(f"UPDATE economy SET wallet = {walletAmount} WHERE id = {interaction.user.id}")
                await interaction.response.send_message(f"You have withdrawn ${amount} from your bank.")
                mydb.commit()

    @app_commands.command(name="add-money", description="Adds money to a user.")
    @app_commands.checks.has_role(managementTeam)
    async def addMoney(self, interaction: discord.Interaction, member: discord.Member, amount: int):
        try:
            cursor.execute(f"SELECT * FROM economy WHERE id = {member.id}")
            userDB = cursor.fetchone()
            if userDB is None:
                cursor.execute(f"INSERT INTO economy (id, wallet, bank) VALUES ({member.id}, 0, 0)")
                mydb.commit()
                mydb.reconnect()
                await interaction.response.send_message(f"{member} did not have an account before, creating one now. Please input the command again.", ephemeral=True)
            else:
                addAmount = int(userDB[1]) + amount
                cursor.execute(f"UPDATE economy SET wallet = {addAmount} WHERE id = {member.id}")
                mydb.commit()

                await interaction.response.send_message(f"Added ${amount} to {member.name}'s wallet.")
        except Exception as e:
            print(e)
            
    @app_commands.command(name="remove-money", description="Adds money to a user.")
    @app_commands.checks.has_role(managementTeam)
    @app_commands.describe(where='Which account?')
    @app_commands.choices(where=[
        discord.app_commands.Choice(name= 'Wallet', value="1"),
        discord.app_commands.Choice(name= 'Bank', value="2"),
        discord.app_commands.Choice(name= 'All', value="3")
    ])
    async def removeMoney(self, interaction: discord.Interaction, member: discord.Member, where: discord.app_commands.Choice[str], amount: int=None):
        try:
            cursor.execute(f"SELECT * FROM economy WHERE id = {member.id}")
            userDB = cursor.fetchone()
            print(where.name)
            if userDB is None:
                cursor.execute(f"INSERT INTO economy (id, wallet, bank) VALUES ({member.id}, 0, 0)")
                mydb.commit()
                return await interaction.response.send_message(f"{member} did not have an account before, creating one now.")
            else:
                if amount == 0:
                    return await interaction.response.send_message("You can't remove nothing.")
                if where.name != "All" and amount == None:
                    return await interaction.response.send_message("Please put in an amount.")
                if where.name == "Wallet":
                    removeAmount = int(userDB[1]) - amount
                    cursor.execute(f"UPDATE economy SET wallet = {removeAmount} WHERE id = {member.id}")
                    mydb.commit()
                    await interaction.response.send_message(f"Removed ${amount} from {member.name}'s wallet.")
                elif where.name == "Bank":
                    removeAmount = int(userDB[2]) - amount
                    cursor.execute(f"UPDATE economy SET wallet = {removeAmount} WHERE id = {member.id}")
                    mydb.commit()
                    await interaction.response.send_message(f"Removed ${amount} from {member.name}'s bank.")
                elif where.name == "All":
                    cursor.execute(f"UPDATE economy SET wallet = 0 WHERE id = {member.id}")
                    cursor.execute(f"UPDATE economy SET bank = 0 WHERE id = {member.id}")
                    mydb.commit()
                    await interaction.response.send_message(f"Removed all money from {member.name}.")
                else:
                    return await interaction.response.send_message("That was not one of the options.")
        except Exception as e:
            print(e)
    
    @app_commands.command(name="pay", description="Pay some money to another user")
    @app_commands.checks.has_any_role(member, staffTeam, seniorstaff, managementTeam)
    async def pay(self, interaction: discord.Interaction, member: discord.Member, amount: int):
        try:
            cursor.execute(f"SELECT * FROM economy WHERE id = {interaction.user.id}")
            userMoney = cursor.fetchone()
            cursor.execute(f"SELECT * FROM economy WHERE id = {member.id}")
            memberMoney = cursor.fetchone()
            if userMoney is None:
                cursor.execute(f"INSERT INTO economy (id, wallet, bank) VALUES ({interaction.user.id}, 0, 0)")
                mydb.commit()
                return await interaction.response.send_message("Your account has just been created. You have no money to pay.", ephemeral=True)
            elif memberMoney is None:
                cursor.execute(f"INSERT INTO economy (id, wallet, bank) VALUES ({member.id}, 0, 0)")
                mydb.commit()
                return await interaction.response.send_message(f"{member} did not have an account before, creating one now.")
            else:
                userWallet = int(userMoney[1])
                memberWallet = int(memberMoney[1])
                if userWallet == 0:
                    return await interaction.response.send_message("You have no money in your wallet to send over.")
                elif userWallet < amount:
                    return await interaction.response.send_message("You don't have that amount of money.")
                else:
                    removeAmount = userWallet - amount
                    addAmount = memberWallet + amount
                    cursor.execute(f"UPDATE economy SET wallet = {removeAmount} WHERE id = {interaction.user.id}")
                    cursor.execute(f"UPDATE economy SET wallet = {addAmount} WHERE id = {member.id}")
                    mydb.commit()
                    return await interaction.response.send_message(f"You have payed {member.mention} ${amount}.")
        except Exception as e:
            print(e)
    
    @app_commands.command(name="steal", description="Attempt to steal money from someone!")
    @app_commands.checks.has_any_role(managementTeam)
    @app_commands.checks.cooldown(1, 10, key=lambda i: (i.guild_id, i.user.id))
    async def steal(self, interaction: discord.Interaction, member: discord.Member):
        try:
            if member.id == interaction.user.id:
                return await interaction.response.send_message(f"You can not steal from yourself.")
            elif member.id == 926163269503299695:
                return await interaction.response.send_message(f"You can not steal from me!")
            else:
                ranNum = random.randint(1,2)
                if ranNum == 1:
                    cursor.execute(f"SELECT wallet FROM economy WHERE id = {interaction.user.id}")
                    authorMoney = cursor.fetchone()
                    cursor.execute(f"SELECT wallet FROM economy WHERE id = {member.id}")
                    memberMoney = cursor.fetchone()
                    if memberMoney is None:
                        return await interaction.response.send_message(f"Unfortunately, {member.mention} did not have any money on them to steal.")
                    else:
                        wallet = int(memberMoney[0]) #Getting the wallet balance from the user and making it an int.
                        authorWallet = int(authorMoney[0]) #Getting the wallet balance from the author.
                        stealPercent = round(random.uniform(0,1), 2)#Getting a percentage of what to get from the user.
                        stealAmount = wallet*stealPercent#Getting the amount being stolen from the user.
                        newBalance = wallet - stealAmount
                        authorNewBalance = authorWallet + stealAmount
                        cursor.execute(f"UPDATE economy SET wallet = {newBalance:,.2f} WHERE id = {member.id}")
                        cursor.execute(f"UPDATE economy SET wallet = {authorNewBalance:,.2f} WHERE id = {interaction.user.id}")
                        mydb.commit()
                        return await interaction.response.send_message(f"<@{interaction.user.id}>, you have stolen ${stealAmount:,.2f} from <@{member.id}>.")
                else:
                    return await interaction.response.send_message("The attempt to steal money failed.")
        except Exception as e:
            print(e)
    @steal.error
    async def on_steal_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            return await interaction.response.send_message(str(error))
async def setup(bot):
    await bot.add_cog(economy(bot), guilds=[discord.Object(id=860752406551461909)])