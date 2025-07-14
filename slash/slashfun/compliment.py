import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import random

class ComplimentCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="compliment", description="Give a sweet compliment to someone")
    async def compliment(
        self,
        interaction: Interaction,
        user: nextcord.Member = SlashOption(name="user", description="User to compliment", required=True)
    ):
        compliments = [
            "You're like sunshine on a rainy day 🌞",
            "You make everything better just by being around 😊",
            "You light up every room you walk into 💫",
            "You're amazing just the way you are 💖",
            "You're one of a kind – truly special 🌟"
            "Your smile is contagious, keep shining! 😄",
            "You have a heart of gold, and it shows in everything you do 💛",
            "Your positivity is like a breath of fresh air 🌬️",
            "You inspire those around you to be better every day 🌈",
            "You have a unique talent for making people feel valued and loved 💕",
            "I admire your strength and resilience in everything you do 💪",
            "I can always feel your kindness and warmth, even from afar 🌹",
            "You have a way of making the world a better place just by being in it 🌍",
            "I wish I could bottle up your energy and share it with everyone! ✨",
            "You have a beautiful soul that shines through in everything you do 🌻",
            "i wish you could see yourself through my eyes, you'd be amazed at how wonderful you are! 👀",
            "Hope you have a fantastic day, because you deserve it! 🌼",
        ]
        chosen = random.choice(compliments)

        embed = nextcord.Embed(
            title="💝 Compliment Delivered!",
            description=f"{user.mention}, {chosen}",
            color=nextcord.Color.magenta()
        )
        embed.set_footer(text=f"From {interaction.user}", icon_url=interaction.user.display_avatar.url)
        embed.timestamp = interaction.created_at
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(ComplimentCommand(bot))
    print("ComplimentCommand loaded successfully.")