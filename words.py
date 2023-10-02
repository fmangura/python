def print_upper_words(words):
    """Given a list of words, convert all words to uppercase"""

    for word in words:
        print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])

def print_upper_words_2(words):
    """Print words that start with.."""

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

def print_upper_words_3(words, must_start_with):
    """Print words that have passed in letters"""

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break