from __future__ import annotations
import random

import discord
from discord import app_commands
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="echo", description="Echo back your text")
    @app_commands.describe(text="What should I say back?")
    async def echo(self, interaction: discord.Interaction, text: str):
        await interaction.response.send_message(text)

    @app_commands.command(name="roll", description="Roll n dice with m sides")
    @app_commands.describe(n="Number of dices", m="Sides per dice")
    async def roll(self, interaction: discord.Interaction, n: int, m: int) -> None:
        if n <= 0 or m <= 0 or n > 100 or m > 1000:
            await interaction.response.send_message(
                "Please use reasonable values", ephemeral=True
            )

        total: int = sum(random.randint(1, m) for _ in range(n))
        await interaction.response.send_message(
            f"You rolled **{total}** (n={n}, m={m})"
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Fun(bot))
