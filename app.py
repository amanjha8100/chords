import os
from dotenv import load_dotenv
from bot import Chords

load_dotenv()


def main():
    bot = Chords()
    bot.run(os.getenv("TOKEN"))


if __name__ == "__main__":
    main()
