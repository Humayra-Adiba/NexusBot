import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption, Permissions

class ClearCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="clear", description="Delete a number of messages from the channel (Mods/Admin only)")
    async def clear(
        self,
        interaction: Interaction,
        amount: int = SlashOption(
            name="amount",
            description="Number of messages to delete (max 100)",
            required=True
        )
    ):
        # Check if user is the server owner
        is_owner = interaction.user.id == interaction.guild.owner_id
        # Check if user has manage_messages permission
        has_permission = interaction.channel.permissions_for(interaction.user).manage_messages

        if not (has_permission or is_owner):
            await interaction.response.send_message(
                "❌ Only moderators, admins, or the server owner can use this command.",
                ephemeral=True
            )
            return

        if amount < 1 or amount > 100:
            await interaction.response.send_message("❌ Please enter a number between 1 and 100.", ephemeral=True)
            return

        await interaction.channel.purge(limit=amount)

        embed = nextcord.Embed(
            title="🧹 Messages Cleared",
            description=f"Successfully deleted **{amount}** messages in {interaction.channel.mention}.",
            color=nextcord.Color.red()
        )
        embed.set_footer(text=f"Action by {interaction.user}", icon_url=interaction.user.display_avatar.url)

        await interaction.response.send_message(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(ClearCommand(bot))
    print("ClearCommand loaded successfully.")