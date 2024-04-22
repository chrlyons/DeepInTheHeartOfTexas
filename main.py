import time


class DeepInTheHeartOfTexas:
    LINE_DELAY = 1.5
    VERSE_DELAY = 2.75
    CLAPS = "👏👏👏👏"
    CHORUS = "Deep in the heart of Texas!"

    def __init__(self):
        self.verses = [
            "The stars at night\nAre big and bright",
            "The prairie sky\nIs wide and high",
            "The sage in bloom\nIs like perfume",
            "Reminds me of\nThe one I love",
            "The coyotes wail\nAlong the trail",
            "The rabbits rush\nAround the brush",
            "The stars at night\nAre big and bright",
            "The prairie sky\nIs wide and high",
            "The sage in bloom\nIs like perfume",
            "Reminds me of\nThe one I love"
        ]
        self.current_verse = 0

    @staticmethod
    def next_verse(func):
        def wrapper(self):
            lines = self.verses[self.current_verse].split("\n")
            for line in lines:
                print(f"\033[1;34m{line}\033[0m")
                time.sleep(self.LINE_DELAY)
            print(f"\033[1;31m{self.CLAPS}\n{self.CHORUS}\033[0m\n")
            self.current_verse = (self.current_verse + 1) % len(self.verses)
        return wrapper

    @next_verse
    def next_verse(self):
        pass

    def sing_song(self):
        for _ in range(len(self.verses)):
            self.next_verse()
            time.sleep(self.VERSE_DELAY)


def main():
    yee_haw = DeepInTheHeartOfTexas()
    yee_haw.sing_song()


if __name__ == "__main__":
    main()
