import discord
from discord import app_commands
from discord.ext import commands
import random
import config
import pymongo

myclient = pymongo.MongoClient(config.mongoDB)
mydb = myclient["WeebsHangout"]
mycol = mydb["user_info"]

seniorstaff = 865054271857885225
managementTeam = 860758013731274762
staffTeam = 860758014386896926
member = 860757567566774322

class economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `economy.py`")
    
    @app_commands.command(name='balance', description="Check your balance.")
    @app_commands.checks.has_any_role(member, staffTeam, seniorstaff, managementTeam)
    async def balance(self, interaction: discord.Interaction, user: discord.Member=None):
        try:
            if user == None:
                player = interaction.user.id
                playerDB = mycol.find_one({"_id": player})
                wallet = playerDB['economy']['wallet']
                bank = playerDB['economy']['bank']
                embed=discord.Embed(title="Your bank balance", color=config.color)
                embed.set_author(name=f"{interaction.user.name}", icon_url=f"{interaction.user.avatar}")
                embed.add_field(name="Wallet Balance:", value=f"{wallet:,.2f}", inline=True)
                embed.add_field(name="Bank Ballance", value=f"{bank:,.2f}")
                await interaction.response.send_message(embed=embed)
            else:
                if interaction.user.get_role(staffTeam) == "Staff Team" or interaction.user.get_role(seniorstaff) == "Senior Staff" or interaction.user.get_role(managementTeam) == "Management Team":
                    await interaction.response.send_message("Unfortunately you cannot use this command to check someone elses balance.")
                else:
                    player = user.id
                    playerDB = mycol.find_one({"_id": player})
                    wallet = playerDB['economy']['wallet']
                    bank = playerDB['economy']['bank']
                    embed=discord.Embed(title=f"{user.name}'s bank balance", color=config.color)
                    embed.set_author(name=f"{interaction.user.name}", icon_url=f"{interaction.user.avatar}")
                    embed.add_field(name="Wallet Balance:", value=f"{wallet:,.2f}", inline=True)
                    embed.add_field(name="Bank Ballance", value=f"{bank:,.2f}")
                    await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(e)
    
    @app_commands.command(name="baltop", description="Displays the balance leaderboard for everyone in the server.")
    async def baltop(self, interaction: discord.Interaction):
        try:
            x = mycol.find()
            for player in x:
                wallet = player['economy']['wallet']
                bank = player['economy']['bank']
                total = wallet + bank
                user = player['_id']
                mycol.update_one({"_id": user}, {"$set": {"economy.total": total}})

            embed = discord.Embed(title="Balance Leaderboard", color=config.color)
            playerDB = mycol.find().sort([("economy.total", -1)]).limit(10)
            count = 0
            for x in playerDB:
                count += 1
                wallet = x["_id"]
                user = self.bot.get_user(int(x['_id']))
                total = x['economy']['total']
                embed.add_field(name=f"{count}. {user.name}", value=f"Total: **${total:,.2f}**", inline=False) 
            return await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(e)

    @app_commands.command(name='work', description="Earn money by working.")
    @app_commands.checks.cooldown(1, 28800, key=lambda i: (i.guild_id, i.user.id))
    @app_commands.checks.has_any_role(member, staffTeam, seniorstaff, managementTeam)
    async def work(self, interaction: discord.Interaction):
        player = interaction.user.id
        playerDB = mycol.find_one({"_id": player})
        wallet = playerDB['economy']['wallet']
        jobs = ['programmer', 'sales associate', 'cashier']
        try:
            job = random.choice(jobs)
            if job == 'sales associate' or job == 'cashier':
                earnings = random.randint(1, 16)
                amount = earnings + wallet
                mycol.update_one({'_id': player}, {"$set": {"economy.wallet": amount}})
                embed=discord.Embed(description=f"You earned ${earnings} from working!", color=config.color)
                embed.set_author(name=f"{interaction.user.name}", icon_url=f"{interaction.user.avatar}")
                await interaction.response.send_message(embed=embed)
            else:
                earnings = random.randint(20, 30)
                amount = earnings + wallet
                mycol.update_one({'_id': player}, {"$set": {"economy.wallet": amount}})
                embed=discord.Embed(description=f"You earned ${earnings} from working!", color=config.color)
                embed.set_author(name=f"{interaction.user.name}", icon_url=f"{interaction.user.avatar}")
                await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(e)
    @work.error
    async def on_work_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            err = f"{error}"
            n = err[34:-4]
            print(n)
            n = int(n)

            day = n // (24 * 3600)
            
            n = n % (24 * 3600)
            hour = n // 3600

            n %= 3600
            minutes = n // 60

            n %= 60
            seconds = n
            if minutes == 0 and hour == 0:
                return await interaction.response.send_message(f"You are on cooldown. Try again in {seconds} seconds.", ephemeral=True)
            
            return await interaction.response.send_message(f"You are on cooldown. Try again in {hour}:{minutes}:{seconds}.", ephemeral=True)

    @app_commands.command(name="deposit", description="Deposit money into your bank account.")
    @app_commands.checks.has_any_role(member, staffTeam, seniorstaff, managementTeam)
    async def deposit(self, interaction: discord.Interaction, amount: float):
        try:
            player = interaction.user.id
            playerDB = mycol.find_one({"_id": player})
            wallet = playerDB['economy']['wallet']
            bank = playerDB['economy']['bank']
            if wallet == 0:
                return await interaction.response.send_message("You don't have any money to transfer over.", ephemeral=True)
            elif amount == 0:
                return await interaction.response.send_message("You can't transfer $0.", ephemeral=True)
            elif wallet < amount:
                return await interaction.response.send_message("That number is larger then the amount of money you have in your wallet.", ephemeral=True)
            else:
                bankAmount = bank + amount
                walletAmount = wallet - amount
                mycol.update_one({'_id': player}, {"$set": {"economy.wallet": walletAmount}})
                mycol.update_one({'_id': player}, {"$set": {"economy.bank": bankAmount}})
                await interaction.response.send_message(f"You have deposited ${amount:,.2f} into your bank.")
        except Exception as e:
            print(e)
    
    @app_commands.command(name="withdraw", description="Withdraw money from your bank account.")
    @app_commands.checks.has_any_role(member, staffTeam, seniorstaff, managementTeam)
    async def withdraw(self, interaction: discord.Interaction, amount: float):
        try:
            player = interaction.user.id
            playerDB = mycol.find_one({"_id": player})
            wallet = playerDB['economy']['wallet']
            bank = playerDB['economy']['bank']
            if bank == 0:
                return await interaction.response.send_message("You don't have any money to transfer over.", ephemeral=True)
            elif amount == 0:
                return await interaction.response.send_message("You can't transfer $0.", ephemeral=True)
            elif bank < amount:
                return await interaction.response.send_message("That number is larger then the amount of money you have in your bank.", ephemeral=True)
            else:
                bankAmount = bank - amount
                walletAmount = wallet + amount
                mycol.update_one({'_id': player}, {"$set": {"economy.wallet": walletAmount}})
                mycol.update_one({'_id': player}, {"$set": {"economy.bank": bankAmount}})
                await interaction.response.send_message(f"You have withdrawn ${amount:,.2f} from your bank.")
        except Exception as e:
            print(e)
    
    @app_commands.command(name="add-money", description="Adds money to a user.")
    @app_commands.checks.has_role(managementTeam)
    async def addMoney(self, interaction: discord.Interaction, user: discord.Member, amount: float):
        try:
            player = user.id
            playerDB = mycol.find_one({"_id": player})
            wallet = playerDB['economy']['wallet']
            addAmount = wallet + amount
            mycol.update_one({'_id': player}, {"$set": {"economy.wallet": addAmount}})
            await interaction.response.send_message(f"Added ${amount:,.2f} to {user.name}'s wallet.")
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
    async def removeMoney(self, interaction: discord.Interaction, user: discord.Member, where: discord.app_commands.Choice[str], amount: float=None):
        try:
            player = user.id
            playerDB = mycol.find_one({"_id": player})
            wallet = playerDB['economy']['wallet']
            bank = playerDB['economy']['bank']
            if amount == 0:
                return await interaction.response.send_message("You can't remove nothing.")
            if where.name != "All" and amount == None:
                return await interaction.response.send_message("Please put in an amount.")
            if where.name == "Wallet":
                removeAmount = wallet - amount
                mycol.update_one({'_id': player}, {"$set": {"economy.wallet": removeAmount}})
                await interaction.response.send_message(f"Removed ${amount} from {user.name}'s wallet.")
            elif where.name == "Bank":
                removeAmount = bank - amount
                mycol.update_one({'_id': player}, {"$set": {"economy.bank": removeAmount}})
                await interaction.response.send_message(f"Removed ${amount} from {user.name}'s bank.")
            elif where.name == "All":
                mycol.update_one({'_id': player}, {"$set": {"economy.wallet": 0}})
                mycol.update_one({'_id': player}, {"$set": {"economy.bank": 0}})
                await interaction.response.send_message(f"Removed all money from {user.name}.")
            else:
                return await interaction.response.send_message("That was not one of the options.")
        except Exception as e:
            print(e)
    
    @app_commands.command(name="pay", description="Pay some money to another user")
    @app_commands.checks.has_any_role(member, staffTeam, seniorstaff, managementTeam)
    async def pay(self, interaction: discord.Interaction, user: discord.Member, amount: int):
        try:
            author = interaction.user.id
            member = user.id
            authorDB = mycol.find_one({"_id": author})
            memberDB = mycol.find_one({"_id": member})
            authorWallet = authorDB['economy']['wallet']
            memberWallet = memberDB['economy']['wallet']
            if authorWallet == 0:
                return await interaction.response.send_message("You have no money in your wallet to send over.")
            elif authorWallet < amount:
                return await interaction.response.send_message("You don't have that amount of money.")
            else:
                removeAmount = authorWallet - amount
                addAmount = memberWallet + amount
                mycol.update_one({'_id': author}, {"$set": {"economy.wallet": removeAmount}})
                mycol.update_one({'_id': member}, {"$set": {"economy.wallet": addAmount}})
                return await interaction.response.send_message(f"You have payed {user.mention} ${amount}.")
        except Exception as e:
            print(e)
    
    @app_commands.command(name="steal", description="Attempt to steal money from someone!")
    @app_commands.checks.cooldown(1, 6000, key=lambda i: (i.guild_id, i.user.id))
    async def steal(self, interaction: discord.Interaction, user: discord.Member):
        try:
            author = interaction.user.id
            member = user.id
            authorDB = mycol.find_one({"_id": author})
            memberDB = mycol.find_one({"_id": member})
            authorWallet = authorDB['economy']['wallet']
            memberWallet = memberDB['economy']['wallet']
            if user.id == interaction.user.id:
                return await interaction.response.send_message(f"You can not steal from yourself.")
            elif user.id == 926163269503299695:
                return await interaction.response.send_message(f"You can not steal from me!")
            else:
                ranNum = random.randint(1,2)
                if ranNum == 1:
                    if memberWallet == 0:
                        return await interaction.response.send_message(f"Unfortunately, {member.mention} did not have any money on them to steal.")
                    else:
                        stealPercent = round(random.uniform(0,0.5), 2)
                        stealAmount = memberWallet*stealPercent
                        newBalance = round(memberWallet - stealAmount, 2)
                        authorNewBalance = round(authorWallet + stealAmount, 2)
                        mycol.update_one({'_id': author}, {"$set": {"economy.wallet": authorNewBalance}})
                        mycol.update_one({'_id': member}, {"$set": {"economy.wallet": newBalance}})
                        return await interaction.response.send_message(f"<@{interaction.user.id}>, you have stolen ${stealAmount:,.2f} from <@{user.id}>.")
                else:
                    return await interaction.response.send_message("The attempt to steal money failed.")
        except Exception as e:
            print(e)
    @steal.error
    async def on_steal_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            err = f"{error}"
            n = err[34:-4]
            print(n)
            n = int(n)

            day = n // (24 * 3600)
            
            n = n % (24 * 3600)
            hour = n // 3600

            n %= 3600
            minutes = n // 60

            n %= 60
            seconds = n
            if minutes == 0 and hour == 0:
                return await interaction.response.send_message(f"You are on cooldown. Try again in {seconds} seconds.", ephemeral=True)
            
            return await interaction.response.send_message(f"You are on cooldown. Try again in {hour}:{minutes}:{seconds}.", ephemeral=True)
    
    @app_commands.command(name="daily-income", description="Use this command to claim your daily income.")
    @app_commands.checks.has_any_role("Member")
    @app_commands.checks.cooldown(1, 86400, key=lambda i: (i.guild_id, i.user.id))
    async def dailyIncome(self, interaction: discord.Interaction):
        try:
            player = interaction.user.id
            playerDB = mycol.find_one({"_id": player})
            wallet = playerDB['economy']['wallet']
            earnings = 250
            amount = wallet + earnings
            mycol.update_one({'_id': player}, {"$set": {"economy.wallet": amount}})
            return await interaction.response.send_message(f"You claimed your daily income, you can claim it again in 1 day!", ephemeral=True)
        except Exception as e:
            print(e)
    @dailyIncome.error
    async def on_dailyIncome_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            err = f"{error}"
            n = err[34:-4]
            print(n)
            n = int(n)

            day = n // (24 * 3600)
            
            n = n % (24 * 3600)
            hour = n // 3600

            n %= 3600
            minutes = n // 60

            n %= 60
            seconds = n
            if minutes == 0 and hour == 0:
                return await interaction.response.send_message(f"You are on cooldown. Try again in {seconds} seconds.", ephemeral=True)
            
            return await interaction.response.send_message(f"You are on cooldown. Try again in {hour}:{minutes}:{seconds}.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(economy(bot), guilds=[discord.Object(id=860752406551461909)])