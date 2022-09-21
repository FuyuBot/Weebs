try:
    
    import discord
    import random
    from discord.ext import commands
    import mysql.connector
    from config import host, user, password, db


    mydb = mysql.connector.connect(
    host = host,
    user = user,
    password = password,
    database = db
    )

    cursor = mydb.cursor()
    class leveling(commands.Cog):
        def __init__(self, bot: discord.Bot):
            self.bot = bot
        
        @commands.Cog.listener()
        async def on_ready(self):
            print("'leveling.py' successfully loaded!")
        
        @commands.Cog.listener()
        async def on_message(self, message):
            return
            if message.author.bot:
                return
            player = message.author.id
            cursor.execute(f"SELECT player FROM levels WHERE player = {player}")
            playerDB = cursor.fetchall()
            cursor.execute(f"SELECT xp FROM levels WHERE player = {player}")
            xp = cursor.fetchone()
            cursor.execute(f"SELECT level FROM levels WHERE player = {player}")
            level = cursor.fetchone()

            if playerDB == []:
                sql = "INSERT INTO levels (player, level, xp) VALUES (%s, 0, 0)"
                val = (player)
                print(sql)
                print(val)
                cursor.execute(sql, val)
                mydb.commit()
            else:
                if xp == None or level == None:
                    try:
                        
                        cursor.execute("INSERT INTO levels (player, level, xp) VALUES (?, `0`, `0`)", (player))
                        mydb.commit()
                    except:
                        print("2")
                        await message.channel.send('Did not send to the DB, contact staff please.')
                try:
                    xp = xp[0]
                    level = level[0]
                except TypeError:
                    xp = 0
                    level = 0
                
                if level < 5:
                    xp += random.randfloat(1, 3)
                    cursor.execute(f"UPDATE levels SET xp = ? WHERE player = ?", (xp, player))
                else:
                    rand = random.randfloat(1, (level//4))
                    if rand == 1:
                        xp += random.randfloat(1, 3)
                        cursor.execute(f"UPDATE levels SET xp = ? WHERE player = ?", (xp, player))
                
                if xp >= 100:
                    level += 1
                    xp = 0
                    cursor.execute(f"UPDATE levels SET level = ? WHERE player = ?", (level, player))
                    cursor.execute(f"UPDATE levels SET xp = ? WHERE player = ?", (xp, player))
                    await message.channel.send(f'<@{player}> has leveled up to level **{level}**!')
                
                mydb.commit()
    
    def setup(bot):
        bot.add_cog(leveling(bot))

except:
    print("'leveling.py' failed to load.")