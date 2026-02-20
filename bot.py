import discord
from discord.ext import commands

import os
TOKEN = os.getenv("TOKEN")
ROLE_NAME = "EVsiurek"

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

class VerifyView(discord.ui.View):
    @discord.ui.button(label="Zweryfikuj się", style=discord.ButtonStyle.green)
    async def verify_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        role = discord.utils.get(interaction.guild.roles, name=ROLE_NAME)

        if role is None:
            await interaction.response.send_message("Rola nie istnieje!", ephemeral=True)
            return

        if role in interaction.user.roles:
            await interaction.response.send_message("Już jesteś zweryfikowany!", ephemeral=True)
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message("Weryfikacja zakończona ✅", ephemeral=True)

@bot.event
async def on_ready():
    print(f"Zalogowano jako {bot.user}")

@bot.command()
async def weryfikacja(ctx):
    embed = discord.Embed(
        title="Weryfikacja",
        description="Kliknij przycisk poniżej aby uzyskać dostęp do serwera.",
        color=discord.Color.green()
    )
    await ctx.send(embed=embed, view=VerifyView())

bot.run(TOKEN) 