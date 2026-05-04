
import os
import sys
from discord.ext import commands
import config

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clear(self, ctx, amount: int):
        if amount > 15:
            await ctx.send("свыше 15 сообщений за раз не удалить :/")
            return
        
        # вторую часть поправить позже
        if (ctx.author.top_role.id not in config.PRIVILEGED_ROLES_IDS) or (ctx.author.top_role.id in config.BAD_ROLES_IDS):
            await ctx.send("у тебя нет прав :/")
            return
        
        await ctx.channel.purge(limit=amount)
        print(f"Deleted {amount} messages in #{ctx.channel}")
    
    @clear.error
    async def clear_error(self, ctx, error):
        await ctx.send("укажи число")
        print(f"Clear command error: {error}")
    
async def setup(bot):
    await bot.add_cog(Moderation(bot))