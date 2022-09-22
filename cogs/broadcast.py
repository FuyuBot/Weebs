import discord
from discord import app_commands
from discord.ext import commands

class broadcast(commands.Cog):
    def __init__(self, bot): 
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"LOADED: `broadcast.py`")


    @app_commands.command(name='broadcast', description="Send a message to any channel on the server.")
    @app_commands.describe(channel= "The channel id of the channel you would like to send your message.", title= "Title of the message you want to send.",msg= "The message you would like to send")
    @app_commands.checks.has_any_role('Management Team')
    async def broadcast(self, interaction: discord.Interaction, channel: discord.TextChannel, title: str, msg: str):
        sendChannel = interaction.client.get_channel(channel.id)
        embed = discord.Embed(
            title=f'{title}',
            description=f'{msg}'
        )
        await sendChannel.send(embed=embed)
        await interaction.response.send_message(f"Message sent to {channel}.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(broadcast(bot))