import mmap
import random

from discord.ext import commands

from quotes import BROOKLYN_99_QUOTES, PRIORY_OF_THE_ORANGE_TREE_QUOTES


def mapcount(filename):
    with open(filename, "r+") as f:
        buf = mmap.mmap(f.fileno(), 0)
        lines = 0
        readline = buf.readline
        while readline():
            lines += 1
        return lines


def write_quote(sentence, message, filename):
    count = mapcount(filename)
    with open(filename, "a") as file:
        quote = (
            '"'
            + sentence
            + '", '
            + message.author.display_name
            + ", "
            + message.created_at.strftime("%d/%m/%Y, %H:%M:%S")
        )
        file.write(quote + "\n")
    return count, quote


def get_line(filename, number):
    with open(filename, "r") as file:
        for count, line in enumerate(file):
            if count == number - 1:
                return line
    return None


class Quotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.content == "99!":
            response = random.choice(BROOKLYN_99_QUOTES)
            await message.channel.send(response)

    @commands.command(
        name="priory",
        help="Responds with a random quote from the Priory of the Orange Tree",
    )
    async def priory_orange_tree(self, ctx):
        response = random.choice(PRIORY_OF_THE_ORANGE_TREE_QUOTES)
        await ctx.send(response)

    @commands.command(
        name="feed",
        help="Store the message to later use it for the serve command: '!feed quote' or '!feed' as a reply to the quote",
    )
    async def feed(self, ctx, arg=None):
        quote = ""
        reference = ctx.message.reference
        if reference is None:
            if arg is None:
                return await ctx.send(
                    "You did not reply to any message or write a sentence (nothing to add)"
                )
            else:
                count, quote = write_quote(arg, ctx.message, "out_of_context.txt")
        else:
            count, quote = write_quote(
                reference.resolved.content, reference.resolved, "out_of_context.txt"
            )
        await ctx.send(str(count + 1) + ": " + quote)

    @commands.command(
        name="menu",
        help="Gets all stored custom quotes",
    )
    async def menu(self, ctx):
        response = ""
        with open("out_of_context.txt", "r") as file:
            for count, line in enumerate(file):
                response += str(count + 1) + ": " + line
        if response == "":
            response = "No quote"
        await ctx.send(response)

    @commands.command(
        name="serve",
        help="Responds with the custom quote corresponding to the number: '!serve quote_number'",
    )
    async def serve(self, ctx, arg: int):
        quote = get_line("out_of_context.txt", arg)
        if quote is None:
            await ctx.send("No quote with this number")
        await ctx.send(quote)

    @commands.command(
        name="random",
        help="Responds with a random quote",
    )
    async def random(self, ctx):
        count = mapcount("out_of_context.txt")
        number = random.randint(1, count)
        quote = get_line("out_of_context.txt", number)
        await ctx.send(quote)


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


async def setup(bot):
    await bot.add_cog(Quotes(bot))
    await bot.add_cog(Utils(bot))
