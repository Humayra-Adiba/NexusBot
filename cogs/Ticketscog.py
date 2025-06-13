import nextcord
from nextcord.ext import commands
from nextcord import ButtonStyle, PermissionOverwrite
from nextcord.ui import View, Button
import asyncio

class CloseTicketView(View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(label="🔒 Close Ticket", style=ButtonStyle.red, custom_id="close_ticket")
    async def close_ticket(self, button: Button, interaction: nextcord.Interaction):
        await interaction.response.send_message("🔒 Ticket will be closed in 5 seconds...", ephemeral=True)
        await asyncio.sleep(5)
        await interaction.channel.delete(reason="Ticket closed")


class TicketView(View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot

    @nextcord.ui.button(label="🎟️ Create Ticket", style=ButtonStyle.green, custom_id="create_ticket")
    async def create_ticket(self, button: Button, interaction: nextcord.Interaction):
        guild = interaction.guild
        username = interaction.user.name.lower().replace(" ", "-")
        existing_channel = nextcord.utils.get(guild.channels, name=f"ticket-{username}")

        if existing_channel:
            await interaction.response.send_message(f"⚠️ You already have a ticket: {existing_channel.mention}", ephemeral=True)
            return

        overwrites = {
            guild.default_role: PermissionOverwrite(view_channel=False),
            interaction.user: PermissionOverwrite(view_channel=True, send_messages=True, attach_files=True, embed_links=True),
            guild.me: PermissionOverwrite(view_channel=True, send_messages=True)
        }

        category = nextcord.utils.get(guild.categories, name="🎫 Tickets")
        if not category:
            category = await guild.create_category("🎫 Tickets")

        channel = await guild.create_text_channel(
            name=f"ticket-{username}",
            overwrites=overwrites,
            category=category,
            reason="New ticket created"
        )

        await interaction.response.send_message(f"✅ Your ticket has been created: {channel.mention}", ephemeral=True)

        embed = nextcord.Embed(
            title="📩 Ticket Support",
            description="Thank you for reaching out!\n\nPlease explain your issue or question in as much detail as possible. Our team will get back to you shortly.",
            color=nextcord.Color.blurple()
        )
        embed.set_footer(text=f"Opened by {interaction.user}", icon_url=interaction.user.display_avatar.url)
        embed.timestamp = interaction.created_at
        embed.add_field(name="Ticket ID", value=f"#{channel.id}", inline=False)

        await channel.send(content=interaction.user.mention, embed=embed, view=CloseTicketView())


class TicketSystemcog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="setup_ticket",help="Sets up the ticket panel.")
    async def setup_ticket(self, ctx):
        """Sets up the ticket panel (prefix version)"""
        embed = nextcord.Embed(
            title="🎫 Need Support?",
            description="Click the button below to create a support ticket.\nOur team will respond as soon as possible!",
            color=nextcord.Color.green()
        )
        embed.set_footer(text="Ticket System • NexusBot", icon_url=ctx.guild.icon.url if ctx.guild.icon else None)

        view = TicketView(self.bot)
        await ctx.send(embed=embed, view=view)
        await ctx.message.add_reaction("✅")


def setup(bot):
    bot.add_cog(TicketSystemcog(bot))
    print("TicketSystem cog loaded successfully.")