from discord.ext import commands
from discord import app_commands


class sync(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.Cog.listener()
    async def on_ready(self):
        print('LOADED: `sync.py`')

    
    @commands.command()
    @commands.has_any_role("*")
    async def sync(self, ctx) -> None:
        try:
            fmt = await ctx.bot.tree.sync()
            print(f"Synced {len(fmt)} commands.")
            return
        except Exception as e:
            print(e)

    @commands.command()
    @commands.has_any_role("*")
    async def syncweebs(self, ctx) -> None:
        if ctx.author.id == 920797181034778655 or ctx.author.id == 155580061888675840:
            try:
                fmt = await ctx.bot.tree.sync(guild=ctx.guild)
                print(f"Synced {len(fmt)} commands.")
                return
            except Exception as e:
                print(e)
        else:
            print("Failed: not sean or jacob.")

async def setup(bot):
    await bot.add_cog(sync(bot))