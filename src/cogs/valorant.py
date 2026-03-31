from __future__ import annotations

import discord
from discord import app_commands
from discord.ext import commands


class Valorant(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="echo", description="Echo back your text")
    @app_commands.describe(text="What should I say back?")
    async def echo(self, interaction: discord.Interaction, text: str):
        await interaction.response.send_message(text)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Valorant(bot))
