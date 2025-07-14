import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import random

class EmojiCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="emoji", description="Send a random emoji to someone!")
    async def emoji(
        self,
        interaction: Interaction,
        member: nextcord.Member = SlashOption(
            name="user",
            description="The member you want to send a random emoji to",
            required=True
        )
    ):
        emojis = ["😀", "😂", "😍", "🥳", "😎", "😱", "🤖", "👻", "🔥", "🌈", "🎉", "✨", "💩", "👀", "☠️", "🤧", "🥰", "😝", "🤬"]
        chosen = random.choice(emojis)

        embed = nextcord.Embed(
            title="🎭 Emoji Drop!!!",
            description=f"{interaction.user.mention} sent a random emoji to {member.mention}!\n\n **{chosen}**",
            color=nextcord.Color.orange()
        )
        embed.timestamp = interaction.created_at
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(EmojiCommand(bot))
    print("EmojiCommand loaded successfully.")
