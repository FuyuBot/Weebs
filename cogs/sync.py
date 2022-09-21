from discord.ext import commands


class sync(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.Cog.listener()
    async def on_ready(self):
        print('LOADED: `sync.py`')

    
    @commands.command()
    async def sync(self, ctx) -> None:
        fmt = await ctx.bot.tree.sync()
        print(f"Synced {len(fmt)} commands.")
        return


async def setup(bot):
    await bot.add_cog(sync(bot))