# Out-of-context

A discord bot to store and call quotes from a guild.

## What does it do?

It can react to things happening on the guild, and has specific commands.

### Reactions

```
Guild member sent exaclty the message "99!":
  Responds with a random quote from Brooklyn 99
An error happened in response to a command:
  Responds with the error message
```

### Commands

```
Quotes:
  !feed                                         Store the message to later use it for the serve command: '!feed quote' or '!feed' as a reply to the quote
  !menu                                         Gets all stored custom quotes
  !serve quote_number                           Responds with the custom quote corresponding to the number
  !priory                                       Responds with a random quote from the Priory of the Orange Tree
  !random                                       Responds with a random quote from the custom quotes
Utils:
  !roll number_of_dice number_of_sides          Simulates rolling dice
​No Category:
  !help                                         Shows this message

Type !help command for more info on a command.
You can also type !help category for more info on a category.
```

## To launch it

This bot must have access to message content.

Inside this directory, create a `.env` file containing:
```
DISCORD_TOKEN=your-bot-token
DISCORD_GUILD=your-guild-name
```
For more info on how to get those variables: [how to make a discord bot in the developer portal](https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-the-developer-portal).

To install dependencies:
```bash
pip install -r requirements.txt
```

To run the code:
```bash
python bot.py
```

When successfully launched, it should return:
```
out-of-context has connected to Discord!
guild_name(id: guild_id)
```

### Storing quotes

You can either use a text file or a Google Doc.

#### Text file

Create a `out_of_context.txt` file (it can be empty). The main drawback is that if the bot is launched on multiple server, the text file must be transfered each time.

#### Google Doc

Add a credentials.json from Google For Developers (ID client OAuth 2.0).

Must also add `GOOGLE_DOCUMENT_ID=your-document-id` to the `.env` file.

More details for the setup on [Google Docs - Python: quickstart](https://developers.google.com/docs/api/quickstart/python?hl=fr).

## Need to add

* Host the discord bot

## Sources

* [How to make a discord bot python](https://realpython.com/how-to-make-a-discord-bot-python/)
* [Working with cog](https://gist.github.com/15696/a1b10f044fbd658ce76ab1f862a1bda2)
* [Cog example](https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html)
* [Deal with replies](https://stackoverflow.com/questions/69140784/possible-for-discord-bot-to-reply-to-message-that-the-message-calling-the-bot-re)
* [Google Docs - Python: quickstart](https://developers.google.com/docs/api/quickstart/python?hl=fr)
* [Inserting in Google Doc with Python](https://gist.github.com/mattroz/e3cf49ce41da355ba245ddd7f33e681d)
