import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption

class Counting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.current_number = 0
        self.last_user = None
        self.streak = 0
        self.active = False  # Game status

    @nextcord.slash_command(name="count", description="Counting Game commands")
    async def count(self, interaction: Interaction):
        pass  # Group command placeholder

    @count.subcommand(name="start", description="Start the counting game")
    async def start(self, interaction: Interaction):
        if self.active:
            await interaction.response.send_message("⚠️ A counting game is already running!", ephemeral=True)
            return

        self.current_number = 0
        self.last_user = None
        self.streak = 0
        self.active = True

        embed = nextcord.Embed(
            title="🎮 Counting Game Started!",
            description="Start counting from **1** using `/count end <number>`",
            color=nextcord.Color.blurple()
        )
        embed.add_field(name="Streak", value="0", inline=True)
        embed.add_field(name="Next Number", value="1", inline=True)
        embed.set_footer(text="Let's go!")

        await interaction.response.send_message(embed=embed)

    @count.subcommand(
        name="end",
        description="Submit the next number in the counting game"
    )
    async def end(
        self,
        interaction: Interaction,
        number: int = SlashOption(
            name="number",
            description="The number you're submitting",
            required=True
        )
    ):
        if not self.active:
            await interaction.response.send_message("⚠️ No game is running. Use `/count start` to begin!", ephemeral=True)
            return

        if number != self.current_number + 1:
            embed = nextcord.Embed(
                title="❌ Wrong Number!",
                description=f"{interaction.user.mention} ruined the count with **{number}** 😭",
                color=nextcord.Color.red()
            )
            embed.add_field(name="Final Streak", value=str(self.streak), inline=True)
            embed.add_field(name="Restarting", value="Use `/count start` to play again", inline=True)
            embed.set_thumbnail(url=interaction.user.avatar.url if interaction.user.avatar else None)
            await interaction.response.send_message(embed=embed)

            # Reset game
            self.active = False
            self.current_number = 0
            self.last_user = None
            self.streak = 0
            return

        if interaction.user == self.last_user:
            await interaction.response.send_message("⚠️ You can't count twice in a row!", ephemeral=True)
            return

        self.current_number += 1
        self.last_user = interaction.user
        self.streak += 1

        embed = nextcord.Embed(
            title="✅ Correct Count!",
            description=f"{interaction.user.mention} counted **{number}** correctly!",
            color=nextcord.Color.green()
        )
        embed.add_field(name="🔥 Streak", value=str(self.streak), inline=True)
        embed.add_field(name="📈 Next Number", value=str(self.current_number + 1), inline=True)
        embed.set_thumbnail(url=interaction.user.avatar.url if interaction.user.avatar else None)
        embed.set_footer(text="Keep going!")

        await interaction.response.defer()  # Acknowledge first
        message = await interaction.followup.send(embed=embed, wait=True)

        # Add reactions (requires correct permissions)
        try:
            await message.add_reaction("✅")
            await message.add_reaction("❌")
        except nextcord.Forbidden:
            print("Bot lacks permission to add reactions.")

def setup(bot):
    bot.add_cog(Counting(bot))
    print("[Counting] Slash cog loaded successfully.")
