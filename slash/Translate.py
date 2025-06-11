import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
from googletrans import Translator

class Translate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.translator = Translator()

    @nextcord.slash_command(name="translate", description="Translate text into another language")
    async def translate(
        self,
        interaction: Interaction,
        lang: str = SlashOption(description="Target language code (e.g., en, es, fr)"),
        text: str = SlashOption(description="Text to translate")
    ):
        try:
            result = self.translator.translate(text, dest=lang)
            embed = nextcord.Embed(
                title="🌍 Translation",
                color=nextcord.Color.blue()
            )
            embed.add_field(name="Original", value=text, inline=False)
            embed.add_field(name=f"Translated ({lang})", value=result.text, inline=False)
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            await interaction.response.send_message(f"❌ Translation failed: {e}", ephemeral=True)

def setup(bot):
    bot.add_cog(Translate(bot))
    print("[Translate] Cog loaded successfully.")