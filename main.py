import Trie
import T9


def test_t9():
    t9 = T9.T9()

    # Wstawiamy słowa do Trie
    words = ['hello', 'hi', 'happy', 'hey', 'help', 'hike', 'hero', 'hill']
    for word in words:
        t9.insert_word(word)

    # Testujemy dla numeru "44"
    print("Test dla numeru '44':")
    predictions = t9.predict("44")
    print(predictions)

    # Testujemy dla numeru "4357" (może odpowiadać np. "help")
    print("Test dla numeru '4357':")
    predictions = t9.predict("4357")
    print(predictions)

# Uruchomienie testu
test_t9()

