import discord
from discord import app_commands
from discord.ui import Button, View
from discord.ext import commands
import config


requestToJoin = Button(label="Request to Join", style=discord.ButtonStyle.success)
async def requestToJoin_callback(interation: discord.Interaction):
    member = interation.user
    rtj = discord.utils.get(member.guild.roles, id=1043590122895069255)
    if rtj in member.roles:
        await member.remove_roles(rtj)
        return await interation.response.send_message("You have successfully removed `Request to join`.", ephemeral=True)
    else:
        await member.add_roles(rtj)
        return await interation.response.send_message("You have successfully added `Request to join`.", ephemeral=True)

class SelectPronounRoles(discord.ui.Select):
    def __init__(self):
        menu = [
            discord.SelectOption(label="He/Him", description="Gives you the He/Him role."),
            discord.SelectOption(label="She/Her", description="Gives you the She/Her role."),
            discord.SelectOption(label="They/Them", description="Gives you the They/Them role."),
            discord.SelectOption(label="Other", description="Gives you the Other role."),
            discord.SelectOption(label="Ask", description="Gives you the Ask role.")
        ]
        super().__init__(placeholder="Select your role.", max_values=1, min_values=1, options=menu)

    async def callback(self, interaction: discord.Interaction):
        try:
            member = interaction.user
            heHim = discord.utils.get(member.guild.roles, id=1036071311740506166)
            sheHer = discord.utils.get(member.guild.roles, id=1036071316865941594)
            theyThem = discord.utils.get(member.guild.roles, id=1036121053539340318)
            other = discord.utils.get(member.guild.roles, id=1036121656646705162)
            ask = discord.utils.get(member.guild.roles, id=1036071322020741170)
            if self.values[0] == "He/Him":
                if heHim in member.roles:
                    await member.remove_roles(heHim)
                    return await interaction.response.send_message("You have successfully removed the `He/Him` role.", ephemeral=True)
                else:
                    await member.add_roles(heHim)
                    return await interaction.response.send_message("You have successfully added the `He/Him` role.", ephemeral=True)
            elif self.values[0] == "She/Her":
                if sheHer in member.roles:
                    await member.remove_roles(sheHer)
                    return await interaction.response.send_message("You have successfully removed the `She/Her` role.", ephemeral=True)
                else:
                    await member.add_roles(sheHer)
                    return await interaction.response.send_message("You have successfully added the `She/Her` role.", ephemeral=True)
            elif self.values[0] == "They/Them":
                if theyThem in member.roles:
                    await member.remove_roles(theyThem)
                    return await interaction.response.send_message("You have successfully removed the `They/Them` role.", ephemeral=True)
                else:
                    await member.add_roles(theyThem)
                    return await interaction.response.send_message("You have successfully added the `They/Them` role.", ephemeral=True)
            elif self.values[0] == "Other":
                if other in member.roles:
                    await member.remove_roles(other)
                    return await interaction.response.send_message("You have successfully removed the `Other` role.", ephemeral=True)
                else:
                    await member.add_roles(other)
                    return await interaction.response.send_message("You have successfully added the `Other` role.", ephemeral=True)
            elif self.values[0] == "Ask":
                if ask in member.roles:
                    await member.remove_roles(ask)
                    return await interaction.response.send_message("You have successfully removed the `Ask` role.", ephemeral=True)
                else:
                    await member.add_roles(ask)
                    return await interaction.response.send_message("You have successfully added the `Ask` role.", ephemeral=True)
        except Exception as e:
            print(e)

class SelectPronounView(discord.ui.View):
    try:
        def __init__(self, *, timeout=60):
            super().__init__(timeout=timeout)
            self.add_item(SelectPronounRoles())
    except Exception as e:
        print(e)
####### GENERAL ROLES

class SelectGeneralRoles(discord.ui.Select):
    def __init__(self):
        menu = [
                discord.SelectOption(label="Genshin", description="Access to the Genshin channels."),
                discord.SelectOption(label="Not a Weeb", description="If you want to show you aren't a weeb."),
                discord.SelectOption(label="Jzcob Stream Announcements", description="Jzcob's stream announcements."),
                discord.SelectOption(label="New Anime Episodes", description="When new anime episodes come out. (Daily)"),
                discord.SelectOption(label="Server Announcements", description="Discord server announcements"),
                discord.SelectOption(label="Server Updates", description="Discord server announcements"),
                discord.SelectOption(label="Server Events", description="Server event pings")
            ]
        super().__init__(placeholder="Select your role.", max_values=1, min_values=1, options=menu)

    async def callback(self, interaction: discord.Interaction):
        try:
            member = interaction.user
            genshin = discord.utils.get(member.guild.roles, id=910929581605789718)
            notAweeb = discord.utils.get(member.guild.roles, id=865727063327768618)
            jzcobStream = discord.utils.get(member.guild.roles, id=865430630987857921)
            animeEpisodes = discord.utils.get(member.guild.roles, id=927774106554884156)
            serverAnnouncements = discord.utils.get(member.guild.roles, id=865050483189219338)
            serverUpdates = discord.utils.get(member.guild.roles, id=865050484506886164)
            serverEvents = discord.utils.get(member.guild.roles, id=1036071322020741170)
            if self.values[0] == "Genshin":
                if genshin in member.roles:
                    await member.remove_roles(genshin)
                    return await interaction.response.send_message("You have successfully removed the `Genshin Impact` role.", ephemeral=True)
                else:
                    await member.add_roles(genshin)
                    return await interaction.response.send_message("You have successfully added the `Genshin Impact` role.", ephemeral=True)
            elif self.values[0] == "Not a Weeb":
                if notAweeb in member.roles:
                    await member.remove_roles(notAweeb)
                    return await interaction.response.send_message("You have successfully removed the `I am not a weeb` role.", ephemeral=True)
                else:
                    await member.add_roles(notAweeb)
                    return await interaction.response.send_message("You have successfully added the `I am not a weeb` role.", ephemeral=True)
            elif self.values[0] == "Jzcob Stream Announcements":
                if jzcobStream in member.roles:
                    await member.remove_roles(jzcobStream)
                    return await interaction.response.send_message("You have successfully removed the `Jzcob Stream Announcements` role.", ephemeral=True)
                else:
                    await member.add_roles(jzcobStream)
                    return await interaction.response.send_message("You have successfully added the `Jzcob Stream Announcements` role.", ephemeral=True)
            elif self.values[0] == "New Anime Episodes":
                if animeEpisodes in member.roles:
                    await member.remove_roles(animeEpisodes)
                    return await interaction.response.send_message("You have successfully removed the `Episodes` role.", ephemeral=True)
                else:
                    await member.add_roles(animeEpisodes)
                    return await interaction.response.send_message("You have successfully added the `Episodes` role.", ephemeral=True)
            elif self.values[0] == "Server Announcements":
                if serverAnnouncements in member.roles:
                    await member.remove_roles(serverAnnouncements)
                    return await interaction.response.send_message("You have successfully removed the `Announcements` role.", ephemeral=True)
                else:
                    await member.add_roles(serverAnnouncements)
                    return await interaction.response.send_message("You have successfully added the `Announcements` role.", ephemeral=True)
            elif self.values[0] == "Server Updates":
                if serverUpdates in member.roles:
                    await member.remove_roles(serverUpdates)
                    return await interaction.response.send_message("You have successfully removed the `Server Updates` role.", ephemeral=True)
                else:
                    await member.add_roles(serverUpdates)
                    return await interaction.response.send_message("You have successfully added the `Server Updates` role.", ephemeral=True)
            elif self.values[0] == "Server Events":
                if serverEvents in member.roles:
                    await member.remove_roles(serverEvents)
                    return await interaction.response.send_message("You have successfully removed the `Server Events` role.", ephemeral=True)
                else:
                    await member.add_roles(serverEvents)
                    return await interaction.response.send_message("You have successfully added the `Server Events` role.", ephemeral=True)
        except Exception as e:
            print(e)

class SelectGeneralView(discord.ui.View):
    try:
        def __init__(self, *, timeout=60):
            super().__init__(timeout=timeout)
            self.add_item(SelectGeneralRoles())
    except Exception as e:
        print(e)

class SelectGenshinWorldLevel(discord.ui.Select):
    def __init__(self):
        menu = [
            discord.SelectOption(label="World Level 8", description="If you are world level 8."),
            discord.SelectOption(label="World Level 7", description="If you are world level 7."),
            discord.SelectOption(label="World Level 6", description="If you are world level 6."),
            discord.SelectOption(label="World Level 5", description="If you are world level 5."),
            discord.SelectOption(label="World Level 4", description="If you are world level 4."),
            discord.SelectOption(label="World Level 3", description="If you are world level 3."),
            discord.SelectOption(label="World Level 2", description="If you are world level 2."),
            discord.SelectOption(label="World Level 1", description="If you are world level 1."),
        ]
        super().__init__(placeholder="Select your world level.", max_values=1, min_values=1, options=menu)
    async def callback(self, interaction: discord.Interaction):
        try:
            member = interaction.user
            wl8 = discord.utils.get(member.guild.roles, id=1036071227376271390)
            wl7 = discord.utils.get(member.guild.roles, id=1036071267444461641)
            wl6 = discord.utils.get(member.guild.roles, id=1036071270858620938)
            wl5 = discord.utils.get(member.guild.roles, id=1036071272477642782)
            wl4 = discord.utils.get(member.guild.roles, id=1036071279737982996)
            wl3 = discord.utils.get(member.guild.roles, id=1036071285404487720)
            wl2 = discord.utils.get(member.guild.roles, id=1036071289925931008)
            wl1 = discord.utils.get(member.guild.roles, id=1040757164127555684)
            if self.values[0] == "World Level 8":
                if wl8 in member.roles:
                    await member.remove_roles(wl8)
                    return await interaction.response.send_message("You have successfully removed `World Level 8`.", ephemeral=True)
                else:
                    await member.remove_roles(wl8,wl7,wl6,wl5,wl4,wl3,wl2,wl1)
                    await member.add_roles(wl8)
                    return await interaction.response.send_message("You have successfully added `World Level 8`.", ephemeral=True)
            elif self.values[0] == "World Level 7":
                if wl7 in member.roles:
                    await member.remove_roles(wl7)
                    return await interaction.response.send_message("You have successfully removed `World Level 7`.", ephemeral=True)
                else:
                    await member.remove_roles(wl8,wl7,wl6,wl5,wl4,wl3,wl2,wl1)
                    await member.add_roles(wl7)
                    return await interaction.response.send_message("You have successfully added `World Level 7`.", ephemeral=True)
            elif self.values[0] == "World Level 6":
                if wl6 in member.roles:
                    await member.remove_roles(wl6)
                    return await interaction.response.send_message("You have successfully removed `World Level 6`.", ephemeral=True)
                else:
                    await member.remove_roles(wl8,wl7,wl6,wl5,wl4,wl3,wl2,wl1)
                    await member.add_roles(wl6)
                    return await interaction.response.send_message("You have successfully added `World Level 6`.", ephemeral=True)
            elif self.values[0] == "World Level 5":
                if wl5 in member.roles:
                    await member.remove_roles(wl5)
                    return await interaction.response.send_message("You have successfully removed `World Level 5`.", ephemeral=True)
                else:
                    await member.remove_roles(wl8,wl7,wl6,wl5,wl4,wl3,wl2,wl1)
                    await member.add_roles(wl5)
                    return await interaction.response.send_message("You have successfully added `World Level 5`.", ephemeral=True)
            elif self.values[0] == "World Level 4":
                if wl4 in member.roles:
                    await member.remove_roles(wl4)
                    return await interaction.response.send_message("You have succesfully removed `World Level 4`.", ephemeral=True)
                else:
                    await member.remove_roles(wl8,wl7,wl6,wl5,wl4,wl3,wl2,wl1)
                    await member.add_roles(wl4)
                    return await interaction.response.send_message("You have successfully added `World Level 4`.", ephemeral=True)
            elif self.values[0] == "World Level 3":
                if wl3 in member.roles:
                    await member.remove_roles(wl3)
                    return await interaction.response.send_message("You have successfully removed `World Level 3`.", ephemeral=True)
                else:
                    await member.remove_roles(wl8,wl7,wl6,wl5,wl4,wl3,wl2,wl1)
                    await member.add_roles(wl3)
                    return await interaction.response.send_message("You have successfully added `World Level 3`.", ephemeral=True)
            elif self.values[0] == "World Level 2":
                if wl2 in member.roles:
                    await member.remove_roles(wl2)
                    return await interaction.response.send_message("You have successfully removed `World Level 2`.", ephemeral=True)
                else:
                    await member.remove_roles(wl8,wl7,wl6,wl5,wl4,wl3,wl2,wl1)
                    await member.add_roles(wl2)
                    return await interaction.response.send_message("You have successfully added `World Level 2`.", ephemeral=True)
            elif self.values[0] == "World Level 1":
                if wl1 in member.roles:
                    await member.remove_roles(wl1)
                    return await interaction.response.send_message("You have successfully removed `World Level 1`.", ephemeral=True)
                else:
                    await member.remove_roles(wl8,wl7,wl6,wl5,wl4,wl3,wl2,wl1)
                    await member.add_roles(wl1)
                    return await interaction.response.send_message("You have successfully added `World Level 1`.", ephemeral=True)
        except Exception as e:
            print(e)

class ViewGenshinWorldLevel(discord.ui.View):
    try:
        def __init__(self, *, timeout=60):
            super().__init__(timeout=timeout)
            self.add_item(SelectGenshinWorldLevel())
    except Exception as e:
        print(e)

class roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print("LOADED: `roles.py`")
    
    @app_commands.command(name="roles", description="Use this command to get your general roles.")
    @app_commands.checks.has_any_role("Member")
    @app_commands.describe(roles='What type of roles?')
    @app_commands.choices(roles=[
        discord.app_commands.Choice(name= 'Pronouns', value="pronouns"),
        discord.app_commands.Choice(name= 'Server Specific', value="server")
    ])
    async def role(self, interaction: discord.Interaction, roles: discord.app_commands.Choice[str]):
        if roles.value == "pronouns":
            return await interaction.response.send_message(view=SelectPronounView(), ephemeral=True)
        elif roles.value == "server":
            return await interaction.response.send_message(view=SelectGeneralView(), ephemeral=True)
        else:
            return await interaction.response.send_message("You should not have gotten here.")
    
    @app_commands.command(name="genshin-roles", description="Use this command to get your genshin roles.")
    @app_commands.checks.has_any_role("Genshin Impact")
    @app_commands.describe(roles="What type of roles?")
    @app_commands.choices(roles=[
        discord.app_commands.Choice(name= 'World Level', value="worldLevel"),
        discord.app_commands.Choice(name= 'Request to join', value="rtj")
    ])
    async def genshinRole(self, interaction: discord.Interaction, roles: discord.app_commands.Choice[str]):
        if roles.value == "worldLevel":
            return await interaction.response.send_message(view=ViewGenshinWorldLevel(), ephemeral=True)
        elif roles.value == "rtj":
            view = View()
            view.add_item(requestToJoin)
            embed=discord.Embed(color=config.color,title="Request to join",description=f'Please only get this role if you will allow users to join your world or you join their world. This can be for a number of reasons, help with bosses, getting materials for characters/weapons/etc, domains, fishing, anything. Just make sure you are clear when responding to the user that needs help.')
            await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
            requestToJoin.callback = requestToJoin_callback
        else:
            return await interaction.response.send_message("You should not have gotten here.", ephemeral=True)
    

async def setup(bot):
    await bot.add_cog(roles(bot), guilds=[discord.Object(id=860752406551461909)])