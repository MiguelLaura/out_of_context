import os.path

from dotenv import load_dotenv


load_dotenv()
DOCUMENT_ID = os.getenv("GOOGLE_DOCUMENT_ID")

FILENAME = "out_of_context.txt"

BROOKLYN_99_QUOTES = [
    "I'm the human form of the 💯 emoji.",
    "Bingpot!",
    (
        "Cool. Cool cool cool cool cool cool cool, "
        "no doubt no doubt no doubt no doubt."
    ),
]

PRIORY_OF_THE_ORANGE_TREE_QUOTES = [
    "No woman should be made to fear that she was not enough.",
    "I would live alone for fifty years to have one day with you.",
    "All the world is a cage in a young girl's eyes.",
    "When history fails to shed light on the truth, myth creates its own.",
    (
        "I do not sleep because I am not only afraid of the monsters at my door, "
        "but also of the monsters my own mind can conjure. "
        "The ones that live within."
    ),
]
