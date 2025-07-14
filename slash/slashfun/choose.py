import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import random

class ChooseCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="choose", description="Let the bot choose randomly from your options!")
    async def choose(
        self,
        interaction: Interaction,
        option1: str = SlashOption(name="option1", description="First option", required=True),
        option2: str = SlashOption(name="option2", description="Second option", required=True),
        option3: str = SlashOption(name="option3", description="Third option", required=True),
        option4: str = SlashOption(name="option4", description="Fourth option (optional)", required=False),
        option5: str = SlashOption(name="option5", description="Fifth option (optional)", required=False)
    ):
        # Build list of non-empty options
        options = [opt for opt in [option1, option2, option3, option4, option5] if opt]
        chosen = random.choice(options)

        embed = nextcord.Embed(
            title="🎲 Random Choice",
            description=f"I choose: **{chosen}**",
            color=nextcord.Color.blue()
        )
        embed.set_footer(text=f"Asked by {interaction.user}", icon_url=interaction.user.display_avatar.url)

        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(ChooseCommand(bot))
    print("ChooseCommand loaded successfully.")
