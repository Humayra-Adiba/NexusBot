import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
from datetime import datetime

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="countdown", description="Create a countdown to an event")
    async def countdown(
        self,
        interaction: Interaction,
        event: str = SlashOption(description="Event name"),
        date: str = SlashOption(description="Date in YYYY-MM-DD format")
    ):
        try:
            event_date = datetime.strptime(date, "%Y-%m-%d")
            now = datetime.now()

            if event_date < now:
                await interaction.response.send_message("The date has already passed!", ephemeral=True)
                return

            delta = event_date - now
            days = delta.days
            hours, remainder = divmod(delta.seconds, 3600)
            minutes = remainder // 60

            embed = nextcord.Embed(title="⏳ Countdown", color=0x00FFFF)
            embed.add_field(name="Event", value=event, inline=False)
            embed.add_field(name="Time Left", value=f"{days} days, {hours} hours, {minutes} minutes", inline=False)
            embed.set_footer(text=f"Countdown to {event} on {event_date.strftime('%Y-%m-%d')}")
            embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/2662/2662503.png")
            embed.timestamp = interaction.created_at
            await interaction.response.send_message(embed=embed)
        except ValueError:
            await interaction.response.send_message("Invalid date format. Use YYYY-MM-DD.", ephemeral=True)





def setup(bot):
    bot.add_cog(Utility(bot))
    print("Utility cog loaded.")