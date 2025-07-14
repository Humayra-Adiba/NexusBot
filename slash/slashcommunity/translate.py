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
            embed.set_footer(text=f"Translated from {result.src} to {lang} using Google Translate API ✨ NexusBot")
            embed.set_thumbnail(url="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=facearea&w=256&q=80")
            embed.timestamp = interaction.created_at
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            await interaction.response.send_message(f"❌ Translation failed: {e}", ephemeral=True)

def setup(bot):
    bot.add_cog(Translate(bot))
    print("[Translate] Cog loaded successfully.")


