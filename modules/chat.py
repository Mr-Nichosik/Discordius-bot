
import os
import sys
from discord.ext import commands
import random
import config
from utils import clean

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ChatBot(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.channel.id not in config.CHAT_CHANNELS_IDS:
            return
        
        msg = clean(message.content)

        for word in config.HI_WORDS:
            if word in msg:
                await message.channel.send(random.choice(config.ANSWERS))
                break

        for word in config.NICHOSI_WORDS:
            if word in msg:
                await message.channel.send("Ничоси!")
                break

        for word in config.NICHOSI_ATTACK_WORDS:
            if word in msg:
                for i in range(10):
                    await message.channel.send("<:Nichosi_1:823894832068952144>" * 10)
                break

        if msg == "пинг":
            await message.channel.send("понг")
        if msg == "ping":
            await message.channel.send("pong")

async def setup(bot):
    await bot.add_cog(ChatBot(bot))