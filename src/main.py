from __future__ import annotations
import os
import logging

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
DEV_GUILD = os.getenv("DEV_GUILD")

logging.basicConfig(level=logging.INFO)


class Bot(commands.Bot):
    def __init__(self) -> None:
        intents = discord.Intents.none()
        intents.guilds = True
        super().__init__(
            command_prefix=commands.when_mentioned,
            intents=intents,
            help_command=None,
            activity=discord.Game(name="Valorant"),
        )

    async def setup_hook(self) -> None:
        await self.load_extension("cogs.core")
        await self.load_extension("cogs.fun")

        if DEV_GUILD and DEV_GUILD.isdigit():
            guild = discord.Object(id=int(DEV_GUILD))
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)

            logging.info(f"Synced commands to DEV_GUILD={DEV_GUILD}")
        else:
            await self.tree.sync()
            logging.info("Synced global commands")

    async def on_ready(self) -> None:
        if self.user:
            logging.info(f"Logged in as {self.user} (ID: {self.user.id})")
        else:
            logging.warning("on_ready called but self.user is None!")


if __name__ == "__main__":
    if not TOKEN:
        raise SystemExit("Set DISCORD_TOKEN in your .env file first!")

    bot = Bot()
    bot.run(TOKEN)
