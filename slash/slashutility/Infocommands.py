import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import datetime
import platform
import psutil
import time

start_time = time.time()

class InfoCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="userinfo", description="Display user info")
    async def userinfo(self, interaction: Interaction, user: nextcord.Member = SlashOption(required=False, description="Select a user")):
        user = user or interaction.user
        embed = nextcord.Embed(title="👤 User Info", color=nextcord.Color.blue())
        embed.set_thumbnail(url=user.display_avatar.url)
        embed.add_field(name="Username", value=user.name, inline=True)
        embed.add_field(name="User ID", value=user.id, inline=True)
        embed.add_field(name="Joined Discord", value=user.created_at.strftime("%Y-%m-%d"), inline=False)
        embed.add_field(name="Joined Server", value=user.joined_at.strftime("%Y-%m-%d") if user.joined_at else "Unknown", inline=False)
        embed.set_footer(text=f"Requested by {interaction.user.name}", icon_url=interaction.user.display_avatar.url)
        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name="serverinfo", description="Display server info")
    async def serverinfo(self, interaction: Interaction):
        guild = interaction.guild
        embed = nextcord.Embed(title="🏠 Server Info", color=nextcord.Color.green())
        embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
        embed.add_field(name="Server Name", value=guild.name, inline=True)
        embed.add_field(name="Server ID", value=guild.id, inline=True)
        embed.add_field(name="Members", value=guild.member_count, inline=True)
        embed.add_field(name="Roles", value=len(guild.roles), inline=True)
        embed.add_field(name="Created On", value=guild.created_at.strftime("%Y-%m-%d"), inline=False)
        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name="roles", description="List all server roles")
    async def roles(self, interaction: Interaction):
        roles = [role.name for role in interaction.guild.roles if role.name != "@everyone"]
        roles_display = ", ".join(roles) if roles else "No roles found."
        embed = nextcord.Embed(title="📜 Server Roles", description=roles_display[:4000], color=nextcord.Color.orange())
        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name="avatar", description="Display a user's avatar")
    async def avatar(self, interaction: Interaction, user: nextcord.Member = SlashOption(required=False, description="Select a user")):
        user = user or interaction.user
        embed = nextcord.Embed(title=f"{user.name}'s Avatar", color=nextcord.Color.blurple())
        embed.set_image(url=user.display_avatar.url)
        await interaction.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(InfoCommands(bot))

