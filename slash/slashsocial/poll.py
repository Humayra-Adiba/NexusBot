import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption

class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="poll", description="Create a poll with three options")
    async def poll(
        self,
        interaction: Interaction,
        question: str = SlashOption(description="Poll question"),
        option1: str = SlashOption(description="First option"),
        option2: str = SlashOption(description="Second option"),
        option3: str = SlashOption(description="Third option")
    ):
        embed = nextcord.Embed(
            title="📊 New Poll!",
            description=(
                f"**{question}**\n\n \n"
                f"1️⃣ {option1}\n \n"
                f"2️⃣ {option2}\n \n"
                f"3️⃣ {option3} \n \n"
            ),
            color=nextcord.Color.purple()
        )
        embed.set_footer(text=f"Poll created by {interaction.user.display_name}")
        embed.timestamp = interaction.created_at

        await interaction.response.send_message(embed=embed)
        message = await interaction.original_message()

        await message.add_reaction("1️⃣")
        await message.add_reaction("2️⃣")
        await message.add_reaction("3️⃣")

def setup(bot):
    bot.add_cog(Poll(bot))
