import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import random

class HandHold(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="handhold", description="Hold someone's hand warmly!")
    async def handhold(
        self,
        interaction: Interaction,
        user: nextcord.Member = SlashOption(name="user", description="Who are you holding hands with?", required=True)
    ):
        gifs = [
            "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExdnkzaGFlZ3N2dXJham5jcmo3NXV6c2VxNXpkdjI5ZXBmbmxlODltdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/CRWdhM1XgJ7Pi/giphy.gif",
            "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExb3Jqc3gybW0yNzdhNWtvN211YnkwYWZjMGZ3dzQ1bWVhaTN3Nm5iaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Iozpl68qADWOQ/giphy.gif",
            "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjV1MWtsZ3d5aDU4MnVqMThqMTNoa3kyeHRmbjJheDI5dGRnYzZ2NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QXP41W5A32T4UXGbTI/giphy.gif",
            "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZDljbno5OGVwcnlpMDYxazY5YjRuZmZncjd5MXd6YXJoZmNrYTV5biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/mpWQkl5jGLOjjApXUJ/giphy.gif",
            "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExejBmdzVhbmJ5NW5saHo3aDQzZmx5Z2VtNGxsYTl3aHg5c3I0dzcyOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xT1R9F2RCoVNI0bckg/giphy.gif",
        ]
        chosen = random.choice(gifs)
        embed = nextcord.Embed(
            title="❤️ Holding Hands",
            description=f"{interaction.user.mention} is holding hands with {user.mention}! ✨",
            color=nextcord.Color.brand_red()
        )
        embed.set_image(url=chosen)
        await interaction.response.send_message(embed=embed)
        embed.set_footer(text="Hand holding is a beautiful !")
        embed.timestamp = interaction.created_at

def setup(bot):
    bot.add_cog(HandHold(bot))
