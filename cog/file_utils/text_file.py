import mmap


def count_quotes(filename):
    with open(filename, "r+") as f:
        buf = mmap.mmap(f.fileno(), 0)
        lines = 0
        readline = buf.readline
        while readline():
            lines += 1
        return lines


def get_quote(filename, number):
    with open(filename, "r") as file:
        for count, quote in enumerate(file):
            if count == number - 1:
                return quote
    return None


def read_quotes(filename):
    response = ""
    with open(filename, "r") as file:
        for count, quote in enumerate(file):
            response += str(count + 1) + ": " + quote
    return response


def write_quote(sentence, message, filename):
    count = count_quotes(filename)
    quote = (
        '"'
        + sentence
        + '", '
        + message.author.display_name
        + ", "
        + message.created_at.strftime("%d/%m/%Y, %H:%M:%S")
        + "\n"
    )
    with open(filename, "a") as file:
        file.write(quote)
    return count, quote
