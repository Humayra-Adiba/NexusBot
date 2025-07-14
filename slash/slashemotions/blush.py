import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import random

class Blush(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="blush", description="Blushed at someone with love!")
    async def blush(
        self,
        interaction: Interaction,
        user: nextcord.Member = SlashOption(name="user", description="Who are you blushing with?", required=True)
    ):
        gifs = [
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGZwcDljdmdzZjBnemcwNHhkemNpMGxjNGQyeG90OGU0eGh0eXltbSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/4A9uYkyko4rSw/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGZwcDljdmdzZjBnemcwNHhkemNpMGxjNGQyeG90OGU0eGh0eXltbSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/HPI9m7McNPGN2/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGZwcDljdmdzZjBnemcwNHhkemNpMGxjNGQyeG90OGU0eGh0eXltbSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/2RFqpNVScIWE8/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGZwcDljdmdzZjBnemcwNHhkemNpMGxjNGQyeG90OGU0eGh0eXltbSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/8iCAkwYQW3dzx64nvP/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdGZwcDljdmdzZjBnemcwNHhkemNpMGxjNGQyeG90OGU0eGh0eXltbSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/PR3wumHIdsBhu/giphy.gif",
        ]
        chosen = random.choice(gifs)
        embed = nextcord.Embed(
            title="💫 Blushing Time!",
            description=f"{interaction.user.mention} lovingly blushed with {user.mention}! 🥰",
            color=nextcord.Color.red()
        )
        embed.set_image(url=chosen)
        await interaction.response.send_message(embed=embed)
        embed.set_footer(text="Blushing is a sign of affection!")
        embed.timestamp = interaction.created_at

def setup(bot):
    bot.add_cog(Blush(bot))
