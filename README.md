# Out-of-context

A discord bot to store and call quotes from a guild.

## To launch it

This bot must have access to message content.

Inside this directory, create a .env file containing:
```
DISCORD_TOKEN=your-bot-token
DISCORD_GUILD=your-guild-name
```

You also must create a out_of_context.txt file (it can be empty).

To run the code:
```bash
python bot.py
```

When successfully launched, it should return:
```
out-of-context has connected to Discord!
guild_name(id: guild_id)
```

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

## Need to add

* Host the discord bot

## Sources

* [how to make a discord bot python](https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-the-developer-portal)
* [working with cog](https://gist.github.com/15696/a1b10f044fbd658ce76ab1f862a1bda2)
* [cog example](https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html)
* [reply](https://stackoverflow.com/questions/69140784/possible-for-discord-bot-to-reply-to-message-that-the-message-calling-the-bot-re)
