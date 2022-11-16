import discord
from discord import app_commands, TextStyle, TextInput
from discord.ext import commands
import config


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
            #await interaction.response.send_message(str(error), ephemeral=True)
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
            
            if hour != 0:
                return await interaction.response.send_message(f"You are on cooldown. Try again in {hour} hours, {minutes} minute(s) and {seconds} seconds.", ephemeral=True)
            elif hour == 1:
                return await interaction.response.send_message(f"You are on cooldown. Try again in {hour} hour, {minutes} minute(s) and {seconds} seconds.", ephemeral=True)

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
    reason = discord.ui.TextInput(label="Why would you like to join?", placeholder="Domains, Materials, Bosses, Fishing", required=True)
    async def on_submit(self, interaction: discord.Interaction):
        try:
            channel = interaction.client.get_channel(865681786877378630)
            user = interaction.user

            embed = discord.Embed(color=config.color, title=f"{user} is requesting to join a world.")
            embed.add_field(name="__Genshin Name:__", value=self.genshinName, inline=True)
            embed.add_field(name="__World Level:__", value=self.worldLevel, inline=True)
            embed.add_field(name="__Requesting:__", value=self.reason, inline=False)
            print(self.genshinName)
            print(self.worldLevel)
            print(self.reason)
            print(self.reasonExplained)

            await interaction.response.send_message("Successfully opened the request-to-join form.", ephemeral=True)
            await channel.send(embed=embed)
        except Exception as e:
            print(e)

async def setup(bot):
    await bot.add_cog(genshin(bot), guilds=[discord.Object(id=config.weebsHangout)])
