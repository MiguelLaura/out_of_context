import random

from discord.ext import commands

from cog.constants import (
    DOCUMENT_ID,
    BROOKLYN_99_QUOTES,
    PRIORY_OF_THE_ORANGE_TREE_QUOTES,
)
from cog.file_utils.google_doc import get_quote, count_quotes, read_quotes, write_quote


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
                count, quote = write_quote(arg, ctx.message, DOCUMENT_ID)
        else:
            count, quote = write_quote(
                reference.resolved.content, reference.resolved, DOCUMENT_ID
            )
        await ctx.send(str(count + 1) + ": " + quote)

    @commands.command(
        name="menu",
        help="Gets all stored custom quotes",
    )
    async def menu(self, ctx):
        response = read_quotes(DOCUMENT_ID)
        if response == "":
            response = "No quote"
        await ctx.send(response)

    @commands.command(
        name="serve",
        help="Responds with the custom quote corresponding to the number: '!serve quote_number'",
    )
    async def serve(self, ctx, arg: int):
        quote = get_quote(DOCUMENT_ID, arg)
        if quote is None:
            await ctx.send("No quote with this number")
        await ctx.send(quote)

    @commands.command(
        name="random",
        help="Responds with a random quote",
    )
    async def random(self, ctx):
        count = count_quotes(DOCUMENT_ID)
        number = random.randint(1, count)
        quote = get_quote(DOCUMENT_ID, number)
        await ctx.send(quote)
