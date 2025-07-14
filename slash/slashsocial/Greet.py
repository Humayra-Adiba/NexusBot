import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import datetime

class Greet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.birthdays = {}  # Stores user_id -> MM-DD strings

    @nextcord.slash_command(name="greet", description="Send a greeting message")
    async def greet(self, interaction: Interaction):  
        embed = nextcord.Embed(
            title="👋 Greetings!",
            description=f"Hello {interaction.user.mention}! Hope you're having a great day!",
            color=nextcord.Color.green()
        )
        embed.set_thumbnail(url=interaction.user.display_avatar.url)
        embed.set_footer(text="Greeting from your friendly bot!")
        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name="echo", description="Repeat what you say")
    async def echo(self, interaction: Interaction, message: str = SlashOption(description="What do you want me to say?")):
        embed = nextcord.Embed(
            title="🗣 Echo",
            description=f"You said: `{message}`",
            color=nextcord.Color.blurple()
        )
        embed.set_footer(text=f"Requested by {interaction.user.name}", icon_url=interaction.user.display_avatar.url)
        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name="set_birthday", description="Set your birthday (MM-DD)")
    async def set_birthday(self, interaction: Interaction, date: str = SlashOption(description="Your birthday (MM-DD)")):
        try:
            datetime.datetime.strptime(date, "%m-%d") 
            self.birthdays[interaction.user.id] = date
            await interaction.response.send_message(f"🎉 Birthday set to `{date}`!")
        except ValueError:
            await interaction.response.send_message("❌ Please use the format MM-DD (e.g. `06-15`).")

    @nextcord.slash_command(name="check_birthdays", description="Check if today is anyone's birthday")
    async def check_birthdays(self, interaction: Interaction):
        today = datetime.datetime.now().strftime("%m-%d")
        sent = False
        for user_id, bday in self.birthdays.items():
            if bday == today:
                user = self.bot.get_user(user_id)
                if user:
                    await interaction.channel.send(f"🎂 Happy Birthday {user.mention}!")
                    sent = True
        if not sent:
            await interaction.response.send_message("🎈 No birthdays today.")
        else:
            await interaction.response.send_message("✅ Birthday messages sent.")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        # Auto-reply when bot is mentioned
        if self.bot.user.mentioned_in(message):
            await message.channel.send(f"👋 Hello {message.author.mention}, how can I help you?")

        # Automatic birthday wishes
        today = datetime.datetime.now().strftime("%m-%d")
        for user_id, bday in self.birthdays.items():
            if bday == today:
                user = self.bot.get_user(user_id)
                if user:
                    await message.channel.send(f"🎂 Happy Birthday {user.mention}!")



    @nextcord.slash_command(name="say", description="Make the bot say something")
    async def say(
        self,
        interaction: Interaction,
        message: str = SlashOption(
            name="message",
            description="What should the bot say?",
            required=True
        ),
    ):
        embed = nextcord.Embed(
            title="🗣️ Message from the Bot...... ",
            description=message,
            color=nextcord.Color.purple()
        )
        embed.set_footer(text="*from your friendly bot*", icon_url=self.bot.user.display_avatar.url)
        embed.timestamp = datetime.datetime.utcnow()
        await interaction.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(Greet(bot))
