import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import platform
import psutil
import datetime

class Botstats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = datetime.datetime.now(datetime.timezone.utc)

    def get_uptime(self):
        now = datetime.datetime.now(datetime.timezone.utc)
        delta = now - self.start_time
        days = delta.days
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{days}d {hours}h {minutes}m {seconds}s"

    @nextcord.slash_command(name="ping", description="View bot latency and status")
    async def ping_command(self, interaction: Interaction):
        latency = round(self.bot.latency * 1000)
        uptime = self.get_uptime()
        cpu_usage = psutil.cpu_percent()
        memory = psutil.virtual_memory()
        mem_usage = f"{memory.used // (1024 ** 2)}MB / {memory.total // (1024 ** 2)}MB ({memory.percent}%)"
        python_version = platform.python_version()
        nextcord_version = nextcord.__version__

        embed = nextcord.Embed(
            title="📡 Bot Diagnostics",
            color=nextcord.Color.blurple(),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        embed.set_author(name="NexusBot Status", icon_url=self.bot.user.avatar.url if self.bot.user.avatar else None)
        embed.add_field(name="📶 Latency", value=f"`{latency}ms`", inline=True)
        embed.add_field(name="🔁 Uptime", value=f"`{uptime}`", inline=True)
        embed.add_field(name="🧠 Memory", value=f"`{mem_usage}`", inline=True)
        embed.add_field(name="⚙️ CPU Usage", value=f"`{cpu_usage}%`", inline=True)
        embed.add_field(name="🐍 Python", value=f"`v{python_version}`", inline=True)
        embed.add_field(name="💠 Nextcord", value=f"`v{nextcord_version}`", inline=True)

        embed.set_footer(text="NexusBot | Status Check")
        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name="uptime", description="Check how long the bot has been running")
    async def uptime(self, interaction: Interaction):
        embed = nextcord.Embed(
            title="⏱️ Uptime",
            description=f"`{self.get_uptime()}`",
            color=nextcord.Color.green(),
            timestamp=datetime.datetime.now(datetime.timezone.utc)
        )
        embed.set_footer(text="Bot uptime")
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Botstats(bot))
    print("[Botstats] Cog loaded successfully.")
