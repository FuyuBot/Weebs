import discord
from discord import app_commands
from discord.ext import commands
from discord.utils import get
import config

class RequestModal(discord.ui.Modal, title="Request to join Form"):
    genshinName = discord.ui.TextInput(label="What is your name in Genshin?", required=True, )
    worldLevel = discord.ui.TextInput(label="What is your World Level?", required=True)
    '''menu = [
        discord.SelectOption(label="Domains", description="If you want to join because you want help with domains."),
        discord.SelectOption(label="Materials", description="If you want to steal some materials from someone."),
        discord.SelectOption(label="Bosses", description="If you would like help with bosses."),
        discord.SelectOption(label="Fishing", description="If you would like to fish in someone else's world.")
    ]
    reason = discord.ui.Select(options=menu, max_values=1)'''
    reason = discord.ui.TextInput(label="Why would you like to join?", placeholder="Electro Regisvine, Pryo Hypostasis, etc", required=True)
    async def on_submit(self, interaction: discord.Interaction):
        try:
            channel = interaction.client.get_channel(865681786877378630)
            user = interaction.user

            embed = discord.Embed(color=config.color, title=f"{user}")
            embed.add_field(name="__Genshin Name:__", value=self.genshinName, inline=True)
            embed.add_field(name="__World Level:__", value=self.worldLevel, inline=True)
            embed.add_field(name="__Requesting:__", value=self.reason, inline=False)

            await interaction.response.send_message("Successfully opened the request-to-join form.", ephemeral=True)
            await channel.send(embed=embed)
        except Exception as e:
            print(e)

class genshin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `genshin.py`")
    
    @app_commands.command(name="request-to-join", description="You can use this command to ask other members about joining their world.")
    @app_commands.checks.cooldown(1, 86400, key=lambda i: (i.guild_id, i.user.id))
    async def requestToJoin(self, interaction: discord.Interaction):
        try:
            return await interaction.response.send_modal(RequestModal())
        except Exception as e:
            print(e)
    @requestToJoin.error
    async def on_request_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
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

    @app_commands.command(name="genshin-birthdays", description="Sends the genshin birthdays")
    @app_commands.checks.has_any_role("Management Team")
    async def genshinBirthday(self, interaction: discord.Interaction, channel: discord.TextChannel):
        sendChannel = interaction.client.get_channel(channel.id)
        springBirthdays = discord.Embed(color=0x2cab44, title="Spring Birthdays")
        summerBirthdays = discord.Embed(color=0xd12c2c, title="Summer Birthdays")
        fallBirthdays = discord.Embed(color=0xd45815, title="Fall Birthdays")
        winterBirthdays = discord.Embed(color=0x1dd1de, title="Winter Birthdays")
        dendro = get(interaction.guild.emojis, name="dendro")
        electro = get(interaction.guild.emojis, name="electro")
        cryo = get(interaction.guild.emojis, name="cryo")
        geo = get(interaction.guild.emojis, name="geo")
        pyro = get(interaction.guild.emojis, name="pyro")
        anemo = get(interaction.guild.emojis, name="anemo")
        hydro = get(interaction.guild.emojis, name="hydro")


        springBirthdays.set_thumbnail(url="https://media.discordapp.net/attachments/587673289560817858/810288620799918140/Spring.png")
        springBirthdays.add_field(name="January", value=f"\
            03 {anemo} Wanderer\n\
            09 {pyro} Thoma\n\
            18 {cryo} Diona\n\
            24 {cryo} Rosaria", inline=False)
        springBirthdays.add_field(name="February", value=f"\
            11 {dendro} Alhaitham\n\
            14 {electro} Beidou\n\
            22 {hydro} Sangonomiya Kokomi\n\
            29 {pyro} Bennett", inline=False)
        springBirthdays.add_field(name="March", value=f"\
            03 {cryo} Qiqi\n\
            06 {dendro} Yaoyao\n\
            10 {cryo} Shenhe\n\
            14 {anemo} Jean\n\
            21 {geo} Noelle\n\
            26 {hydro} Kamisato Ayato", inline=False)
        
        summerBirthdays.set_thumbnail(url="https://media.discordapp.net/attachments/587673289560817858/823227504059875378/Summer.png")
        summerBirthdays.add_field(name="April", value=f"\
            17 {anemo} Xiao\n\
            20 {hydro} Yelan\n\
            30 {pyro} Diluc", inline=False)
        summerBirthdays.add_field(name="May", value=f"\
            03 {hydro} Candace\n\
            08 {dendro} Collei\n\
            18 {geo} Gourou\n\
            21 {geo} Yun Jin\n\
            27 {electro} Fischl", inline=False)
        summerBirthdays.add_field(name="June", value=f"\
            01 {geo} Arataki Itto\n\
            09 {electro} Lisa\n\
            16 {anemo} Venti\n\
            21 {pyro} Yoimiya\n\
            23 {electro} Cyno\n\
            26 {electro} Raiden Shogun\n\
            27 {electro} Yae Miko", inline=False)

        fallBirthdays.set_thumbnail(url="https://media.discordapp.net/attachments/587673289560817858/810288618621894656/AUTUMN.png")
        fallBirthdays.add_field(name="July", value=f"\
            05 {hydro} Barbara\n\
            14 {electro} Kujou Sara\n\
            15 {pyro} Hu tao\n\
            20 {hydro} Tartaglia\n\
            24 {anemo} Shikanoin Heizou\n\
            27 {pyro} Klee | {electro} Kuki Shinobu\n\
            28 {pyro} Yanfei", inline=False)
        fallBirthdays.add_field(name="August", value=f"\
            10 {pyro} Amber\n\
            20 {anemo} Faruzan\n\
            26 {geo} Ningguang\n\
            31 {hydro} Mona", inline=False)
        fallBirthdays.add_field(name="September", value=f"\
            07 {cryo} Chongyun\n\
            09 {electro} Razor\n\
            13 {geo} Albedo\n\
            28 {cryo} Kamisato Ayaka", inline=False)

        winterBirthdays.set_thumbnail(url="https://media.discordapp.net/attachments/587673289560817858/823227333733253140/Winter.png")
        winterBirthdays.add_field(name="October", value=f"\
            09 {hydro} Xingqiu\n\
            16 {pyro} Xinyan\n\
            19 {anemo} Sayu\n\
            25 {cryo} Eula\n\
            27 {dendro} Nahida\n\
            29 {anemo} Kaedehara Kazuha", inline=False)
        winterBirthdays.add_field(name="November", value=f"\
            02 {pyro} Xiangling\n\
            20 {electro} Keqing\n\
            26 {anemo} Sucrose\n\
            30 {cryo} Kaeya", inline=False)
        winterBirthdays.add_field(name="December", value=f"\
            02 {cryo} Ganyu\n\
            03 {hydro} Nilou\n\
            19 {cryo} Layla\n\
            21 {electro} Dori\n\
            29 {dendro} Tighnari\n\
            31 {geo} Zhongli", inline=False)
        
        await sendChannel.send(embed=springBirthdays)
        await sendChannel.send(embed=summerBirthdays)
        await sendChannel.send(embed=fallBirthdays)
        await sendChannel.send(embed=winterBirthdays)
    
    @app_commands.command(name="genshin-code", description="Send a genshin code in the genshin codes channel.")
    @app_commands.checks.has_any_role("Senior Moderator", "Senior Staff", "Genshin Codes")
    async def genshinCodes(self, interaction: discord.Interaction, code: str):
        try:
            channel = interaction.client.get_channel(1050114033564520539)
            embed = discord.Embed(title=f"`{code}`", color=0x26c662)
            embed.set_author(icon_url=interaction.user.avatar, name=interaction.user)
            await channel.send("<@&910929581605789718>", embed=embed)
            return await interaction.response.send_message("Sent successfully.", ephemeral=True)
        except Exception as e:
            print(e)


        
async def setup(bot):
    await bot.add_cog(genshin(bot), guilds=[discord.Object(id=config.weebsHangout)])