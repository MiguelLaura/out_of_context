import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from cog.quotes import Quotes
from cog.utils import Utils


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")


class CustomBot(commands.Bot):
    async def setup_hook(self):
        await self.add_cog(Quotes(self))
        await self.add_cog(Utils(self))

    async def on_ready(self):
        print(f"{self.user.name} has connected to Discord!")

        guild = discord.utils.get(self.guilds, name=GUILD)
        print(f"{guild.name} (id: {guild.id})")

    async def on_command_error(self, ctx, error):
        await ctx.send(error)


if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True

    bot = CustomBot(command_prefix="!", intents=intents)

    bot.run(TOKEN)
