import discord
from discord import app_commands
from discord.ext import commands
import mysql.connector
from config import host, user, password, db

mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=db
)
cursor = mydb.cursor()


class message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `message.py`")

    @commands.Cog.listener()
    async def on_message(self, message):
        player = message.author.id
        cursor.execute(f"SELECT id FROM messages WHERE id = {player}")
        checkDB = cursor.fetchall()
        if not checkDB:
            return
        else:
            for row in checkDB:
                messageRow = row[0]
                if messageRow == checkDB[0][0]:
                    if message.author.id == int(messageRow):
                        cursor.execute(f"SELECT message FROM messages WHERE id = {player}")
                        messageDB = cursor.fetchall()
                        for msgRow in messageDB:
                            msg = msgRow[0]
                            if msg == messageDB[0][0]:
                                await message.channel.send(msg)
                    else:
                        print("Author did not match ID")

    @app_commands.command(name='message', description="Allows you set a message so that the bot can respond to you whenever you type.")
    @app_commands.checks.has_any_role(895490315174178857) #Special Perms
    async def message(self, interaction: discord.Interaction, msg: str):
        cancel = ['cancel', 'stop']
        if msg not in cancel:
            player = interaction.user.id
            cursor.execute(f"SELECT message FROM messages WHERE id = {player}")
            checkDB = cursor.fetchall()
            if checkDB == []:
                sql = "INSERT INTO messages (id, message) VALUES (%s, %s)"
                val = (player, msg)
                try:
                    cursor.execute(sql, val)
                    mydb.commit()
                    await interaction.response.send_message(f"{interaction.user.mention} I will now send a message after you type.", ephemeral=True)
                except:
                    print("DID NOT SEND TO DB ERROR")
                    print("Message that was sent: " + msg)
                    print("CheckDB response: " + checkDB)
                    await interaction.response.send_message('Did not send to the DB!')
            else:
                await interaction.response.send_message(f'Message already set, please use `/message stop` to clear it and set a new one.', ephemeral=True)
        else:
            player = interaction.user.id
            try:
                cursor.execute(f"DELETE FROM messages WHERE id = {player}")
                mydb.commit()
                await interaction.response.send_message(f"{interaction.user.mention} I will no longer be sending a message after you type.", ephemeral=True)
            except:
                await interaction.response.send_message('Did not send to the DB!')



async def setup(bot):
    await bot.add_cog(message(bot), guilds=[discord.Object(id=860752406551461909)])