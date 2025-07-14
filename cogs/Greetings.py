import nextcord
from nextcord.ext import commands
import random

class Greetings(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    # Prefix Command: !nexusbot
    @commands.command(help="Say hello to NexusBot!")
    async def nexusbot(self, ctx):
        embed = nextcord.Embed(
            title="🤖 **Meet NexusBot!**",
            description="Hi there 👋, I am **NexusBot** – your helpful Discord assistant!",
            color=nextcord.Color.blue()
        )
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/4712/4712027.png")
        embed.set_footer(text="Developed with 💙 using Nextcord")
        await ctx.send(embed=embed)

    # Prefix Command: !ping
    @commands.command(help="Get a warm greeting message!")
    async def ping(self, ctx):
        embed = nextcord.Embed(
            title="📡 Need Help?",
            description="Hello! 😄\nI'm here to assist you.\nUse `!help` to see all my commands!\n(Also I have several Slash commands, you can explore them!)",
            color=nextcord.Color.purple()
        )
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/4712/4712040.png")
        embed.set_footer(text="NexusBot at your service!")
        await ctx.send(embed=embed)

    # Event: Member Join
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(1375436330443472928)
        if channel:
            embed = nextcord.Embed(
                title="🎉 Welcome!",
                description=f"Welcome to **{member.guild.name}**, {member.mention}! Hope you have a great time here! 🎉",
                color=nextcord.Color.gold()
            )
            embed.set_thumbnail(url=member.display_avatar.url)
            await channel.send(embed=embed)

    # Event: Member Leave
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(1375436330443472928)
        if channel:
            embed = nextcord.Embed(
                title="😢 Goodbye!",
                description=f"{member.mention} has left the server.",
                color=nextcord.Color.red()
            )
            await channel.send(embed=embed)

    # Unified on_message Event Handler
    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        if message.author.bot:
            return

        msg_lower = message.content.lower()

        # Bot mention logic (only if exact and not a reply)
        if message.content.strip() in [f"<@{self.bot.user.id}>", f"<@!{self.bot.user.id}>"]:
            if message.reference:
                try:
                    ref_msg = await message.channel.fetch_message(message.reference.message_id)
                    if ref_msg.author.id == self.bot.user.id:
                        return  # Ignore replies to the bot itself
                except:
                    return

            guild_name = message.guild.name if message.guild else "NexusBot"

            embed = nextcord.Embed(
                title=f"👑 Welcome to {guild_name.upper()}!",
                description=(
                    f"👋 Hello {message.author.mention}!\n\n"
                    f"🤖 I’m **NexusBot**, your all-in-one server companion for moderation, fun, games, and more.\n\n"
                    f"🔹 Use my commands with the **`!`** prefix\n"
                    f"🔸 Example: **`!ping`**\n"
                    f"🔸 Need help? Just type **`!help`**\n\n"
                    f"🛠️ Dashboard: Coming soon!"
                ),
                color=nextcord.Color.dark_purple()
            )

            avatar_url = (
                self.bot.user.avatar.url
                if self.bot.user.avatar else self.bot.user.default_avatar.url
            )
            embed.set_author(name=self.bot.user.name, icon_url=avatar_url)
            embed.set_thumbnail(url=avatar_url)
            embed.set_footer(text="✨ NexusBot – Making your server legendary!")

            view = nextcord.ui.View()
            view.add_item(nextcord.ui.Button(
                label="➕ Invite NexusBot",
                style=nextcord.ButtonStyle.link,
                url="https://discord.com/oauth2/authorize?client_id=1377525748201685063&scope=bot&permissions=8"
            ))
            view.add_item(nextcord.ui.Button(
                label="🛟 Support Server",
                style=nextcord.ButtonStyle.link,
                url="https://discord.gg/zkwn3ZRaNq"
            ))

            await message.channel.send(embed=embed, view=view)
            return

        # Keyword responses
        if "hello" in msg_lower:
            await message.channel.send(f"Hello {message.author.mention}! How can I assist you today?")
        elif "help" in msg_lower:
            await message.channel.send(f"Hi {message.author.mention}! If you need assistance, feel free to ask!")
        elif "bye" in msg_lower:
            await message.channel.send(f"Goodbye {message.author.mention}! Have a great day! 🌟")

# Setup function to load the cog
def setup(bot):
    bot.add_cog(Greetings(bot))
    print("Greetings cog loaded.")
