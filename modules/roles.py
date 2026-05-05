
import discord
from discord.ext import commands
import config

class Roles(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.channel_id != config.ROLES_CHANNEL_ID:
            return
        if payload.message_id != config.ROLES_MESSAGE_ID:
            return
        
        guild = self.bot.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        emoji = str(payload.emoji)

        if emoji not in config.ROLES:
            return

        if len(member.roles) >= config.MAX_ROLES:
            channel: discord.TextChannel = self.bot.get_channel(payload.channel_id)
            message = await channel.fetch_message(config.ROLES_MESSAGE_ID)
            await message.remove_reaction(emoji, member)

            text_channel: discord.TextChannel = self.bot.get_channel(config.CHAT_CHANNELS_IDS[0])
            await text_channel.send(f"{member.mention}, у тебя уже максимум ролей ({config.MAX_ROLES})")
            return
        
        role = guild.get_role(config.ROLES[emoji]) # достём объект роли по её ID из конфига
        await member.add_roles(role)

        print(f"Added {role.name} to #{member.id} - {member.display_name}")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.channel_id != config.ROLES_CHANNEL_ID:
            return
        if payload.message_id != config.ROLES_MESSAGE_ID:
            return
        
        guild = self.bot.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        emoji = str(payload.emoji)

        if emoji not in config.ROLES:
            return
        
        role = guild.get_role(config.ROLES[emoji])
        await member.remove_roles(role)

        print(f"Removed {role.name} from #{member.id} - {member.display_name}")

async def setup(bot):
    await bot.add_cog(Roles(bot))