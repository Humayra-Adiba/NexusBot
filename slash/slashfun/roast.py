import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import random

class RoastCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="roast", description="Lightly roast a user (for fun!)")
    async def roast(
        self,
        interaction: Interaction,
        user: nextcord.Member = SlashOption(name="user", description="User to roast", required=True)
    ):
        roasts = [
            "You're like a cloud. When you disappear, it's a beautiful day.",
            "If I had a dollar for every smart thing you said, I'd be broke.",
            "You're not stupid; you just have bad luck thinking.",
            "I'd explain it to you, but I left my English-to-Dingbat dictionary at home.",
            "You're like a software update… nobody wants you, but we have to deal with you. 💾",
            "You're not useless. You can always serve as a bad example. 😬",
            "You have something on your chin… no, the third one down. 😅",
            "You're as sharp as a butter knife. 🔪🧈",
            "If I had a nickel for every brain cell you had, I’d have 5 cents. 🧠💸",
            "You're the reason the gene pool needs a lifeguard. 🧬🏊‍♂️",
            "You're like a puzzle with half the pieces missing. 🧩🤷",
            "You're proof that even evolution takes a break sometimes. 🧬😴",
            "Your secrets are always safe with me. I never even listen. 🙉📵",
            "You're like a cloud ☁️ — when you go away, it's a beautiful day. 🌞",
            "You bring everyone so much joy… when you log off. 👋💻",
            "You're slower than a snail riding a turtle through peanut butter. 🐌🐢🥜",
            "You have something on your face… oh, it's just failure. 😬💀",
            "You should wear a watch on both wrists. One for each personality. ⌚😵",
            "You're like Wi-Fi. Everyone complains when you're around. 📶🚫",
            "You're about as helpful as a screen door on a submarine. 🚪🌊",
            "You're not annoying… you’re just the audio version of a headache. 🔊🤕",
            "You're like a cloud of lag in a Discord call. 📞🐢",
            "You're the human version of a typo. 📝❌",
            "You're not the brightest LED in the keyboard. ⌨️💡",
            "You're the kind of person who claps when the plane lands. 🛬👏",
            "Your brain’s Wi-Fi signal must be weak. No connection found. 📡❌",
            "You could trip over a wireless signal. 📶😵‍💫"
        ]
        chosen = random.choice(roasts)

        embed = nextcord.Embed(
            title="🔥 Roast Time!",
            description=f"{user.mention}, {chosen}",
            color=nextcord.Color.red()
        )
        embed.set_footer(text=f"Roasted by {interaction.user}", icon_url=interaction.user.display_avatar.url)
        embed.timestamp = interaction.created_at
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(RoastCommand(bot))
    print("RoastCommand loaded successfully.")