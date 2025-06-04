import nextcord
from nextcord.ext import commands
import random

class Slashcmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="greet", description="Send a greeting message")
    async def greet(self, interaction: nextcord.Interaction):  
        await interaction.response.send_message(f"Hello {interaction.user.mention}! How is your day going?")


    @nextcord.slash_command(name="echo", description="Repeat what you say")
    async def echo(self,interaction: nextcord.Interaction, message: str):
        await interaction.response.send_message(f"You said: {message}")

    

    @nextcord.slash_command(name="roll", description="Roll a dice")
    async def roll(self,interaction: nextcord.Interaction):
        result = random.randint(1, 6)
        await interaction.response.send_message(f"🎲 You rolled a {result}!")


    @nextcord.slash_command(name="userinfo", description="Display your user info")
    async def userinfo(self,interaction: nextcord.Interaction):
        user = interaction.user
        await interaction.response.send_message(
            f"👤 Username: {user.name}\n🆔 ID: {user.id}\n📅 Joined Discord: {user.created_at.strftime('%Y-%m-%d')}"
        )


    @nextcord.slash_command(name="serverinfo", description="Display this server's info")
    async def serverinfo(self,interaction: nextcord.Interaction):
        guild = interaction.guild
        await interaction.response.send_message(
            f"🏠 Server: {guild.name}\n🆔 ID: {guild.id}\n👥 Members: {guild.member_count}"
        )


def setup(bot):
    bot.add_cog(Slashcmd(bot))
    print("Slashcmd cog loaded.")