import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member
import datetime

class Greet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.birthdays = {}  # Format: {user_id: "MM-DD"}

    @nextcord.slash_command(name="greet", description="Send a greeting message")
    async def greet(self, interaction: Interaction):  
        embed = nextcord.Embed(
            title="👋 Greetings!",
            description=f"Hello {interaction.user.mention}! Hope you're having a great day!",
            color=nextcord.Color.green()
        )
        embed.set_thumbnail(url=interaction.user.display_avatar.url)
        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name="echo", description="Repeat what you say")
    async def echo(self, interaction: Interaction, message: str):
        embed = nextcord.Embed(
            title="🗣 Echo",
            description=f"You said: `{message}`",
            color=nextcord.Color.blurple()
        )
        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name="set_birthday", description="Set your birthday (MM-DD)")
    async def set_birthday(self, interaction: Interaction, date: str):
        try:
            datetime.datetime.strptime(date, "%m-%d") 
            self.birthdays[interaction.user.id] = date
            await interaction.response.send_message(f"🎉 Birthday set to `{date}`!")
        except ValueError:
            await interaction.response.send_message("❌ Please use the format MM-DD (e.g. `06-15`).")


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        # Auto-reply when bot is mentioned
        if self.bot.user.mentioned_in(message):
            await message.channel.send(f"👋 Hello {message.author.mention}, how can I help you?")

        # Birthday check
        today = datetime.datetime.now().strftime("%m-%d")
        for user_id, bday in self.birthdays.items():
            if bday == today:
                user = self.bot.get_user(user_id)
                if user:
                    await message.channel.send(f"🎂 Happy Birthday {user.mention}!")

def setup(bot):
    bot.add_cog(Greet(bot))
