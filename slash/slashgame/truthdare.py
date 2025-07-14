import random
import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption

class TruthDare(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.truths = [
            "What’s a secret you’ve never told anyone?",
            "Have you ever lied in this server?",
            "What’s your most embarrassing memory?",
            "Who’s your secret crush?",
            "If you could change one thing about yourself, what would it be?",
            "What’s the most ridiculous thing you’ve ever done?",
            "Did you ever love anyone? 👀",
            "What’s the biggest lie you’ve ever told?",
            "Do you have any crush in present?",
            "Do you like someone in this server?",
            "What’s the most embarrassing thing you’ve done in front of someone you like?",
            "Have you ever had a crush on a teacher? 👀",
            "What’s a secret talent you have… or think you have?"
            "What’s the most embarrassing thing you’ve done in public?",
            "What’s the most embarrassing thing you’ve done in front of your crush?",
            "What’s the most embarrassing thing you’ve done in front of your friends?",
            "What’s the most embarrassing thing you’ve done in front of your family?",
            "Who is the person you would never want to see again?",
            "How many crushes have you had in your life?",
            "when was the last time you cried and why?",
            "Where do you see yourself in 5 years?",
            "Do you have ever hugged someone ?",
            "Do you have ever kissed someone ?",
            "Do you ever hold hands with someone ?",
            "Do you wanna marry in this time?",
        ]

        self.dares = [
            "Send a heart emoji to someone random in the server ❤️",
            "Say 'I like you' to the person you like",
            "Pretend to be a cat for 1 minute in voice chat 🐱",
            "Show your DMs to the server (screenshot) 📸",
            "Reveal your face in this server (photo) ☠️",
            "Change your nickname to 'Pickle' for 10 minutes 🥒",
            "Do 10 push-ups and share a video proof 💪",
            "Send a voice message saying 'I like you' to the person you like 💌",
            "Share a funny meme in the server 😂",
            "Do an impression of your favorite character for 30 seconds 🎭",
            "Come Vc and sing a song of your choice 🎤",
            "Send your most worst handwriting in the server 🤳",
            "Act like a robot for 2 minutes in VC or messages. 🤖"
            "Come vc , share your screen and show your facebook profile here📱",
            "Come vc , share your screen and show your instagram profile here📱",
            "Come vc , share your screen and show your twitter profile here📱",
            "Come vc and open your camera and show your room to the server 🏠",
            "Show your messenger inbox to the server (screenshot) 📸",
            "Show your instagram inbox to the server (screenshot) 📸",
            "Share your most embarrassing photo in the server (screenshot) 📸",
        ]

    @nextcord.slash_command(
        name="truthdare",
        description="Play Truth or Dare!",
    )
    async def truthdare(
        self,
        interaction: Interaction,
        choice: str = SlashOption(
            name="choice",
            description="Pick Truth or Dare",
            choices=["truth", "dare"]
        )
    ):
        # Pick question or dare
        content = random.choice(self.truths if choice == "truth" else self.dares)

        # Create Embed
        embed = nextcord.Embed(
            title="🎲 Truth or Dare \n",
            description=f"**{choice.capitalize()} Challenge ☠️** \n",
            color=nextcord.Color.purple()
        )
        embed.add_field(name="🔥 **Your Task** 🔥", value=content, inline=False)
        embed.set_footer(text=f"Requested by {interaction.user}", icon_url=interaction.user.avatar.url if interaction.user.avatar else None)
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2662/2662503.png")
        embed.timestamp = interaction.created_at
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(TruthDare(bot))
    print("[TruthDare] Cog loaded successfully.")