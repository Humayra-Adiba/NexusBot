import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import asyncio
import random
from datetime import datetime, timedelta

class Giveaway(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="giveaway", description="🎉 Start a giveaway with prize, winners, and a timer")
    async def giveaway(
        self,
        interaction: Interaction,
        prize: str = SlashOption(description="🎁 Prize for the giveaway"),
        winners: int = SlashOption(description="🏆 Number of winners (1-10)"),
        time: int = SlashOption(description="⌛ Duration value"),
        unit: str = SlashOption(
            name="unit",
            description="⏰ Time unit",
            choices={"minute": "minute", "hour": "hour", "day": "day"}
        )
    ):
        if not (1 <= winners <= 10):
            return await interaction.response.send_message("❌ Number of winners must be between 1 and 10.", ephemeral=True)

        # Convert duration
        unit_seconds = {"minute": 60, "hour": 3600, "day": 86400}
        duration_sec = time * unit_seconds[unit]
        end_time = datetime.now() + timedelta(seconds=duration_sec)
        end_timestamp = int(end_time.timestamp())

        embed = nextcord.Embed(
            title="🎉 GIVEAWAY TIME 🎉 \n",
            description=(
                f"**🎁 Prize:** {prize}\n \n"
                f"**🏆 Winners:** {winners}\n \n"
                f"**⏳ Ends:** <t:{end_timestamp}:R> / <t:{end_timestamp}:F>\n\n \n"
                f"📌 **How to Enter**\nReact with 🎉 to enter the giveaway!\n\n \n"
                f"🔔 Hosted by: {interaction.user.mention}"
            ),
            color=nextcord.Color.magenta()
        )
        embed.set_footer(text="Good luck! • NexusBot 💫")
        embed.timestamp = datetime.utcnow()

        await interaction.response.send_message(embed=embed)
        message = await interaction.original_message()
        await message.add_reaction("🎉")

        # Wait for giveaway duration
        await asyncio.sleep(duration_sec)

        try:
            updated_message = await interaction.channel.fetch_message(message.id)
            users = await updated_message.reactions[0].users().flatten()
            users = [u for u in users if not u.bot]

            if len(users) == 0:
                return await interaction.channel.send("❌ No one joined the giveaway. Cancelled.")

            selected = random.sample(users, min(winners, len(users)))
            winner_mentions = ", ".join(user.mention for user in selected)

            result_embed = nextcord.Embed(
                title="🎊 Giveaway Ended!",
                description=f"**🎁 Prize:** {prize}\n\n🎉 Congratulations to: {winner_mentions}",
                color=nextcord.Color.green()
            )
            result_embed.set_footer(text="Thanks for participating! 🎈")

            await interaction.channel.send(embed=result_embed)

        except Exception as error:
            await interaction.channel.send(f"⚠️ Error during giveaway result: `{error}`")

def setup(bot):
    bot.add_cog(Giveaway(bot))
