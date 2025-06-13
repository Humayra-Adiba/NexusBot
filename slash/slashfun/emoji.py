import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import random

class EmojiCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="emoji", description="Get a random emoji")
    async def emoji(self, interaction: Interaction):
        emojis = ["😀", "😂", "😍", "🥳", "😎", "😱", "🤖", "👻", "🔥", "🌈", "🎉", "✨", "💩", "👀", "☠️", "🤧", "🥰","😝","🤬"]
        chosen = random.choice(emojis)

        embed = nextcord.Embed(
            title="🎭 Random Emoji",
            description=f"Here’s one for you: **{chosen}**",
            color=nextcord.Color.orange()
        )
        embed.set_footer(text=f"Given by {interaction.user}", icon_url=interaction.user.display_avatar.url)
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(EmojiCommand(bot))
    print("EmojiCommand loaded successfully.")