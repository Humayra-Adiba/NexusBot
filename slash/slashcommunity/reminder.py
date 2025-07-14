import nextcord
from nextcord.ext import commands, tasks
from nextcord import Interaction, SlashOption
import asyncio
import re

class Reminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def parse_time(self, time_str):
        match = re.match(r"(\d+)([smhd])", time_str.lower())
        if not match:
            return None
        value, unit = match.groups()
        multiplier = {"s": 1, "m": 60, "h": 3600, "d": 86400}
        return int(value) * multiplier[unit]

    @nextcord.slash_command(name="remind", description="Set a reminder")
    async def remind(
        self,
        interaction: Interaction,
        time: str = SlashOption(description="When to remind (e.g., 10s, 5m, 2h)"),
        message: str = SlashOption(description="Reminder message")
    ):
        seconds = self.parse_time(time)
        if seconds is None or seconds <= 0:
            await interaction.response.send_message("❌ Invalid time format. Use like `10s`, `5m`, `2h`, or `1d`.", ephemeral=True)
            return

        await interaction.response.send_message(f"⏳ Reminder set! I will remind you in `{time}`.")

        await asyncio.sleep(seconds)
        try:
            await interaction.user.send(f"🔔 Reminder: {message}")
        except nextcord.Forbidden:
            await interaction.followup.send(f"🔔 Reminder: {message}", ephemeral=True)

def setup(bot):
    bot.add_cog(Reminder(bot))
    print("[Reminder] Cog loaded successfully.")