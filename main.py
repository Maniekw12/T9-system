import T9


def test_t9():
    t9 = T9.T9()

    # Wstawiamy słowa do Trie
    words = [
        'hello', 'hi', 'happy', 'hey', 'help', 'hike', 'hero', 'hill',
        'apple', 'ball', 'cat', 'dog', 'elephant', 'fish', 'goat', 'hat', 'ice', 'joke', 'kite', 'love', 'moon',
        'night', 'ocean', 'pizza', 'queen', 'rain', 'sun', 'tree', 'umbrella', 'victory', 'water', 'x-ray', 'yellow',
        'zebra',
        'book', 'car', 'dance', 'egg', 'friend', 'garden', 'house', 'island', 'jump', 'key', 'lamp', 'music', 'nose',
        'open',
        'pen', 'quiet', 'river', 'star', 'tea', 'under', 'voice', 'window', 'yes', 'zero', 'adventure', 'beach',
        'cloud',
        'dolphin', 'energy', 'family', 'game', 'holiday', 'idea', 'jelly', 'kangaroo', 'lion', 'mountain', 'notebook',
        'orange',
        'pencil', 'question', 'robot', 'snow', 'tiger', 'unicorn', 'vase', 'wind', 'xylophone', 'yawn', 'zipper', 'art',
        'bees', 'castle', 'diamond', 'earth', 'feather', 'guitar', 'honey', 'island', 'joy', 'koala', 'lemon', 'mirror',
        'necklace', 'octopus', 'piano', 'queen', 'rainbow', 'sunflower', 'travel', 'universe', 'vacation', 'whale',
        'xenon',
        'yogurt', 'zigzag', 'balloon', 'carrot', 'drum', 'engine', 'feast', 'glove', 'helicopter', 'internet', 'jungle',
        'kangaroo',"l",
    ]

    for word in words:
        t9.insert_word(word)

    while True:
        print("  1      2      3  ")
        print("       ABC    DEF ")
        print("  4      5      6  ")
        print(" GHI    JKL    MNO ")
        print("  7      8      9  ")
        print(" PQRS   TUV   WXYZ ")
        print("  *      0      #  ")
        game = input("Wpisz literki: ")

        if game == "q":
            break
        else:
            predictions = t9.predict(game)
            print(predictions)


test_t9()

