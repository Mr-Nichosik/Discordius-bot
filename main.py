
import config
import asyncio
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=config.PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as #{bot.user.id} - {bot.user.name}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return  # игнорируем — если написали /чтототакое чего нет
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("у тебя нет прав :/")

async def main():
    async with bot:
        await bot.load_extension("modules.moderation")
        await bot.load_extension("modules.chat")
        await bot.load_extension("modules.roles")
        await bot.start(config.TOKEN)

if __name__ == "__main__":
    asyncio.run(main())