import random

from discord.ext import commands


class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="roll",
        help="Simulates rolling dice : '!roll number_of_dice number_of_sides'",
    )
    async def roll(self, ctx, number_of_dice: int, number_of_sides: int):
        dice = [
            str(random.choice(range(1, number_of_sides + 1)))
            for _ in range(int(number_of_dice))
        ]
        await ctx.send(", ".join(dice))
