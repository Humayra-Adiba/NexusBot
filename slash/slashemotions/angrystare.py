import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import random

class AngryStare(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="angrystare", description="Give someone an angry stare!")
    async def angrystare(self, interaction: Interaction,
                member: nextcord.Member = SlashOption(description="User to give an angry stare to", required=True)
    ):
        gifs = [
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTdhd21ieG9xZTZyczljYjh6anIydGxtdWF2cTlmZnhpNWFzZTF1diZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3o7btMCltyDvSgF92E/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTdhd21ieG9xZTZyczljYjh6anIydGxtdWF2cTlmZnhpNWFzZTF1diZlcD12MV9naWZzX3NlYXJjaCZjdD1n/BejdfvEt6eoV2/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTdhd21ieG9xZTZyczljYjh6anIydGxtdWF2cTlmZnhpNWFzZTF1diZlcD12MV9naWZzX3NlYXJjaCZjdD1n/4QxQgWZHbeYwM/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTdhd21ieG9xZTZyczljYjh6anIydGxtdWF2cTlmZnhpNWFzZTF1diZlcD12MV9naWZzX3NlYXJjaCZjdD1n/UYzNgRSTf9X1e/giphy.gif0",
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTdhd21ieG9xZTZyczljYjh6anIydGxtdWF2cTlmZnhpNWFzZTF1diZlcD12MV9naWZzX3NlYXJjaCZjdD1n/UYzNgRSTf9X1e/giphy.gif",
        ]

        gif_url = random.choice(gifs) if gifs else ""
        embed = nextcord.Embed(
            title="Angry Stare!",
            description=f"{interaction.user.mention} gives an angry stare to {member.mention}! 😠",
            color=nextcord.Color.red()
        )
        if gif_url:
            embed.set_image(url=gif_url)
        embed.set_footer(text="That stare could burn holes!")
        embed.timestamp = interaction.created_at
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(AngryStare(bot)) 
