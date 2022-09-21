import discord
import requests
import typing
import asyncio
#import mysql.connector
from discord.ext import commands
from discord.ext.commands import bot
from discord.utils import get

client = commands.Bot(command_prefix = '.')
loop = asyncio.get_event_loop()
bot = client
client.remove_command('help')

@client.event 
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="for .help"))
    print('Bot is Ready!')
    #channel = client.get_channel(719712444632662117)
    #await channel.send('Type `.verify (MC Name)` to be verified.')


@client.command()
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.green()
    )

    embed.set_author(name="Majikku Server Help Command!")
    embed.set_footer(text='Bot created by Jzcob#1226 and Sezn#6554')
    embed.add_field(name="reverify", value="This command is used to update your name and to get the `Magician` role if you join the Guild.", inline=False)
    embed.add_field(name="namehistory", value="This command is used to show someone's minecraft name histroy.", inline=False)
    embed.add_field(name="hplevel", value="This command is used to show someone's level on Hypixel.", inline=False)
    #embed.add_field(name="Ban", value="This command is used to ban people.", inline=False)
    #embed.add_field(name="Unban", value="This command is used to unban people.", inline=False)
    #embed.add_field(name="Mute", value="This command is used to mute people.", inline=False)
    #embed.add_field(name="Unmute", value="This command is used to unmute people.", inline=False)

    await ctx.send(embed=embed)

@client.command()
async def namehistory(ctx, name):
    url = 'https://api.hypixel.net/player?key=a5552599-a08b-4f2a-aec7-dbac394f07ff&name={name}'
    response = requests.get(url)
    names = response.json()['player']['knownAliases']
    full_string = ', '.join([str(elem) for elem in names]) 

    embed = discord.Embed(
        color = discord.Color.green()
    )

    embed.add_field(name='Names', value=full_string)
    await ctx.send(embed=embed)

@client.command()
async def hplevel(ctx, name):
    embed = discord.Embed(
        colour = discord.Colour.green()
    )

    embed.set_image(url=f'https://gen.plancke.io/exp/{name}.png')
    await ctx.send(embed=embed)

@client.command(pass_context=True)
@commands.has_role('Unverified')
async def verify(ctx, nickname):
    member = ctx.message.author
    channel = client.get_channel(719712446629150770)
    UUIDURL = f"https://api.mojang.com/users/profiles/minecraft/{nickname}"
    response = requests.get(UUIDURL)
    MCuuid = response.json()['id']
    url = 'https://api.hypixel.net/guild?key=a5552599-a08b-4f2a-aec7-dbac394f07ff&id=5744ee240cf2655761ae8e19'
    uuidlist = []
    guildreq = requests.get(url)
    uuids = guildreq.json()['guild']['members']
    hypixelAPI = f'https://api.hypixel.net/player?key=e740f9ee-b28e-4aab-8967-b43319123151&uuid={MCuuid}'
    namereq = requests.get(hypixelAPI)
    displayname = displaynameGet.json()['player']['displayname']
    for uuid in uuids:
        uuidlist.append(uuid['uuid']) 
    verified = discord.utils.get(member.guild.roles, name="Verified")
    unverified = discord.utils.get(member.guild.roles, name="Unverified")
    if MCuuid in uuidlist:
        await channel.send(f'``{nickname}`` has joined the server.')
        await ctx.send(f'Welcome {nickname} to the Majikku Guild discord server!')
        await member.add_roles(verified)
        await member.remove_roles(unverified)
        magician = discord.utils.get(member.guild.roles, name="Magician")
        await member.add_roles(magician)
        await member.edit(nick= displayname)
    else:
        await member.add_roles(verified)
        await member.remove_roles(unverified)
        await ctx.send(f"`{nickname}` has joined the server.")
        await ctx.send(f'Welcome {nickname} to the Majikku Guild discord server!')
        await member.edit(nick= displayname)

@client.command(pass_context=True)
@commands.has_role('Verified')
async def reverify(ctx, nickname):
    member = ctx.message.author
    UUIDURL = f"https://api.mojang.com/users/profiles/minecraft/{nickname}"
    response = requests.get(UUIDURL)
    MCuuid = response.json()['id']
    GUILDurl = "https://api.hypixel.net/guild?key=a5552599-a08b-4f2a-aec7-dbac394f07ff&id=5744ee240cf2655761ae8e19"
    GUILDres = requests.get(GUILDurl)
    hypixelAPI = f'https://api.hypixel.net/player?key=e740f9ee-b28e-4aab-8967-b43319123151&uuid={MCuuid}'
    namereq = requests.get(hypixelAPI)
    displayname = displaynameGet.json()['player']['displayname']
    if MCuuid.encode() in GUILDres.content:
        await ctx.send(f"``{nickname}``, you're role has been updated!")
        magician = discord.utils.get(member.guild.roles, name="Magician")
        await member.add_roles(magician)
        await member.edit(nick= displayname)
    else:
        await ctx.send(f"`{nickname}`, your roles are already up-to-date!")
        magician = discord.utils.get(member.guild.roles, name="Magician")
        await member.remove_roles(magician)
        await member.edit(nick= displayname)

key = 'e740f9ee-b28e-4aab-8967-b43319123151'
@client.command(pass_context=True)
@commands.has_role('Guild Management')
async def guild(ctx, name):
    member = ctx.message.author
    UUIDURL = f"https://api.mojang.com/users/profiles/minecraft/{name}"
    response = requests.get(UUIDURL)
    MCuuid = response.json()['id']
    GUILDurl = "https://api.hypixel.net/guild?key=a5552599-a08b-4f2a-aec7-dbac394f07ff&id=5744ee240cf2655761ae8e19"
    GUILDres = requests.get(GUILDurl)
    hypixelAPI = f'https://api.hypixel.net/player?key=e740f9ee-b28e-4aab-8967-b43319123151&uuid={MCuuid}'
    namereq = requests.get(hypixelAPI)
    displayname = namereq.json()['player']['displayname']
    if MCuuid.encode() in GUILDres.content:
        await ctx.send(f"``{name}`` is in the guild")
    else:
        await ctx.send(f"`{name}` is no longer in the guild.")



#@client.command()
#@commands.has_permissions(ban_members=True)
#async def ban(ctx, name: discord.Member=None, *, reason=None):
#    a = str(name)
#    b = str(reason)
#    mydb = mysql.connector.connect(host= 'na01-sql.pebblehost.com', user= "customer_123145_punishments", password= "DYf2Rz7CrCPC1GieGwV#", database= 'customer_123145_punishments')
#    mycursor = mydb.cursor()
#    staff = ctx.message.author
#    if name == None:
#        await ctx.send("You need to specify who you want to ban and give a reason.")
#        return
#    if reason == None:
#        await ctx.send("You need a reason to ban this person.")
#    else:    
#        await name.send(f'You have been banned for `{reason}.`')
#        await ctx.send(f'**{name}** has been banned by **{staff}** for the reason `{reason}.`')
#        await name.ban(reason=reason)
#        sql = "INSERT INTO Bans (name, date, reason) VALUES (%s, NOW(), %s)"
#        val = [(a, b)]
#        mycursor.executemany(sql, val)
#        mydb.commit()

#@client.command()
#@commands.has_permissions(ban_members=True)
#async def unban(ctx, *, member=None):
#    a = str(member)
#    mydb = mysql.connector.connect(host= 'na01-sql.pebblehost.com', user= "customer_123145_punishments", password= "DYf2Rz7CrCPC1GieGwV#", database= 'customer_123145_punishments')
#    mycursor = mydb.cursor()
#    banned_users = await ctx.guild.bans()
#    member_name, member_discriminator = member.split('#')
#    if member == None:
#        await ctx.send("You need to specify who you want to unban.")   
#    else:    
#        for ban_entry in banned_users:
#            user = ban_entry.user
#            if (user.name, user.discriminator) == (member_name, member_discriminator):
#                await ctx.guild.unban(user)
#                await ctx.send(f"{member} was unbanned.")
#                sql = "DELETE FROM Bans WHERE Name = %s"
#                val = [(a)]
#                mycursor.execute(sql, val)
#                mydb.commit()
#                return
#        else:
#            await ctx.send(f"{member} is not banned.")
    

#@client.command()
#@commands.has_permissions(manage_messages=True)
#async def mute(ctx, name: discord.Member=None, *, reason=None):
#    a = str(name)
#    b = str(reason)
#    mydb = mysql.connector.connect(host= 'na01-sql.pebblehost.com', user= "customer_123145_punishments", password= "DYf2Rz7CrCPC1GieGwV#", database= 'customer_123145_punishments')
#    mycursor = mydb.cursor()
#    muted = discord.utils.get(name.guild.roles, name="Muted")
#    if name == None:
#        await ctx.send("You need to specify who you want to mute and give a reason.")
#    if reason == None:
#        await ctx.send("You need a reason to mute this person.")
#    else:    
#        await name.add_roles(muted)
#        await ctx.send(f"{name} was muted.")
#        sql = "INSERT INTO Bans (name, date, reason) VALUES (%s, NOW(), %s)"
#        val = [(a, b)]
#        mycursor.executemany(sql, val)
#        mydb.commit()

#@client.command()
#@commands.has_permissions(manage_messages=True)
#async def unmute(ctx, name=None):
#    if name == None:
#        await ctx.send("You need to specify who you want to unmute.")
#    else:
#        a= str(name)
#        mydb = mysql.connector.connect(host= 'na01-sql.pebblehost.com', user= "customer_123145_punishments", password= "DYf2Rz7CrCPC1GieGwV#", database= 'customer_123145_punishments')
#        mycursor = mydb.cursor()
#        muted = discord.utils.get(name.guild.roles, name="Muted")
#        await name.remove_roles(muted)
#        sql = "DELETE FROM Mutes WHERE Name = %s"
#        val = [(a)]
#        mycursor.execute(sql, val)
#        mydb.commit()

client.run('')