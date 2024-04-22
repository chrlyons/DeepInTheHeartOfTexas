# Deep in the Heart of Texas!

This Python script plays the song "Deep in the Heart of Texas" in the console. The song is broken down into verses, and each verse is printed line by line with a slight delay between lines and a longer delay between verses. The script uses decorators and ANSI escape codes to enhance the output and make it more visually appealing.

## Prerequisites

- Python 3.x

## How to Run

1. Save the script to a file with a `.py` extension (e.g., `deep_in_the_heart_of_texas.py`).

2. Open a terminal or command prompt and navigate to the directory where the script is saved.

3. Run the script using the following command:

4. The song will start playing in the console, with each verse printed line by line and a delay between verses.

## Code Structure

The script consists of the following components:

- `DeepInTheHeartOfTexas` class:
- `__init__` method: Initializes the verses and the current verse index.
- `next_verse` decorator: Decorates the `next_verse` method to handle the printing of each verse line by line with a delay and adds the claps and chorus after each verse.
- `next_verse` method: An empty method decorated by `next_verse` decorator.
- `sing_song` method: Iterates over the verses and calls `next_verse` to sing the entire song.

- `main` function:
- Creates an instance of the `DeepInTheHeartOfTexas` class.
- Calls the `sing_song` method to play the entire song.

- Constants:
- `LINE_DELAY`: The delay (in seconds) between each line within a verse.
- `VERSE_DELAY`: The delay (in seconds) between verses.
- `CLAPS`: The clap emojis printed after each verse.
- `CHORUS`: The chorus line printed after each verse.

## Customization

You can customize the script by modifying the following:

- `verses`: Update the list of verses in the `__init__` method of the `DeepInTheHeartOfTexas` class to change the lyrics of the song.
- `LINE_DELAY` and `VERSE_DELAY`: Adjust the delay values to change the pacing of the song.
- `CLAPS` and `CHORUS`: Modify the clap emojis and chorus line to suit your preferences.
- ANSI escape codes: Change the color codes (`\033[1;34m` and `\033[1;32m`) to use different colors for the verses and chorus.

## Dependencies

The script does not have any external dependencies. It only uses the built-in `time` module for adding delays.

## License

This script is released under the [MIT License](https://opensource.org/licenses/MIT).

Feel free to use, modify, and distribute the script as per the terms of the license.
