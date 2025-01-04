# Implementacja Systemu T9

## Wprowadzenie

T9 predictive text to system używany w klawiaturach 4x3, który umożliwia szybkie wprowadzanie tekstu na urządzeniach z ograniczoną liczbą klawiszy. System ten przewiduje, jakie słowa użytkownik chce wpisać, na podstawie kolejności naciśniętych klawiszy i predefiniowanego słownika. Struktura całego systemu opiera się na strukturze danych Trie.

## Struktura Trie
struktura Trie to struktura danych, która przechowuje kolekcję łańcuchów znaków w sposób hierarchiczny, umożliwiając efektywne przeszukiwanie i przechowywanie danych opartych na prefiksach.

## Opis działania

1. **Struktura klawiatury**:
   - Klawiatura 4x3 zawiera klawisze numeryczne od `2` do `9`, gdzie każdemu klawiszowi przypisane są odpowiednie litery:
     - `2`: A, B, C
     - `3`: D, E, F
     - `4`: G, H, I
     - `5`: J, K, L
     - `6`: M, N, O
     - `7`: P, Q, R, S
     - `8`: T, U, V
     - `9`: W, X, Y, Z

## Mechanizm Przewidywania

### Wprowadzanie Danych

- Użytkownik wpisuje ciąg cyfr odpowiadających literom słowa na klawiaturze numerycznej.

### Przeszukiwanie Słownika

- System przeszukuje słownik w poszukiwaniu możliwych słów zgodnych z podanym ciągiem cyfr.
- Słownik jest reprezentowany przez plik `words.csv`, który zawiera wszystkie dostępne słowa.

### Przeglądanie Predykcji

- Użytkownik może korzystać z przycisku **"Roll"**, aby przeglądać kolejne przewidziane słowa.

### Zapisywanie Wyników

- Po wybraniu odpowiedniego słowa poprzez przycisk **save**, system zapisuje je do pliku `result.csv`.
- Plik `result.csv` przechowuje wszystkie zapisane **słowa**, umożliwiając późniejszą analizę lub wykorzystanie.

---

## Struktura Plików

- **`words.csv`**: Zawiera listę wszystkich dostępnych słów używanych przez system do predykcji.
- **`result.csv`**: Przechowuje zapisane przez użytkownika słowa.
- **`tests.py`**: Zawiera testy do programu.
- **`Trie.py`**: Zawiera implementację struktury danych Trie.
- **`gui.py`**: Zawiera implementację interfejsu użytkownika.


## Struktura Plików
   - Wprowadzenie ciągu cyfr `43556` może zwrócić (jeśli dane słowo jest w słowniku):
     - `HELLO`
  - Wprowadzenie ciągu cyfr `222` może zwrócić:
     - `aaa`
     - `aca`
     - `aba`
---


## Implementacja 
### Plik ze strukturą Trie

1) Konstruktor w klasie `TrieNode`:
    - **Opis**: Konstruktor inicjalizuje nowy węzeł w strukturze Trie.
    - **`self.children`**: Słownik przechowujący odwołania do dzieci danego węzła.
    - **`self.word_end`**: Flaga logiczna oznaczająca, czy węzeł kończy słowo.

2) Konstruktor w klasie `Trie`:
    - **Opis**: Konstruktor inicjalizuje obiekt `Trie`.
    - **`self.root`**: Korzeń drzewa Trie, będący instancją klasy `TrieNode`.

3) Metoda `insert_key(self, word: str) -> None`:
    - **Opis**: Dodaje nowe słowo do struktury Trie.
    - **Działanie**:
        1. Rozpoczyna od korzenia (`self.root`).
        2. Iteruje po każdej literze słowa.
        3. Jeśli litera nie istnieje w bieżącym węźle (`curr.children`), tworzy nowy węzeł i dodaje go jako dziecko.
        4. Po przetworzeniu wszystkich liter oznacza ostatni węzeł jako koniec słowa (`word_end = True`).

4) Metoda `search(self, node: TrieNode, prefix: str, result: list)`:
    - **Opis**: Metoda ta sprawdza, czy dany węzeł w strukturze Trie oznacza koniec słowa. Jeśli tak, dodaje odpowiadający mu prefiks (czyli dotychczas zbudowane słowo) do listy wyników.


5) Metoda `starts_with(self, prefix: str) -> list`:
    - **Opis**: Zwraca listę słów zaczynających się od danego prefiksu.
    - **Działanie**:
        1. Przeszukuje Trie, poruszając się po literach prefiksu, zaczynając od korzenia (`self.root`).
        2. Jeśli którakolwiek litera nie istnieje w Trie, zwraca pustą listę (prefiks nie istnieje).
        3. Po dotarciu do węzła kończącego prefiks wywołuje metodę search, aby zebrać wszystkie słowa zaczynające się od tego węzła.
        4. Zwraca listę result, która zawiera wszystkie znalezione słowa.
---
### Plik ze strukturą T9

1) Konstruktor w klasie `T9`:
    - **Opis**: Konstruktor inicjalizuje obiekt klasy `T9`.
    - **Atrybuty**:
        - `num_to_letters`: Słownik mapujący cyfry (`2-9`) na odpowiadające im litery alfabetu (zgodnie z tradycyjnym układem T9).
        - `trie`: Instancja klasy `Trie`, używana do przechowywania słów i wykonywania operacji wyszukiwania.


2) Metoda `insert_word(self, word: str) -> None`:
    - **Opis**: Dodaje słowo do struktury `Trie`.


3) Metoda `_generate_combinations(self, sequence: str) -> list`:
    - **Opis**: Generuje wszystkie możliwe kombinacje liter dla podanej sekwencji cyfr.
    - **Zwraca**: Lista wszystkich możliwych kombinacji liter odpowiadających podanemu ciągowi cyfr.

4) Metoda `predict(self, number_sequence: str) -> list`:
    - **Opis**: Przewiduje słowa na podstawie podanego ciągu cyfr.
    - **Parametry**:
        - `number_sequence`: Ciąg cyfr reprezentujący słowo.
    - **Zwraca**: Lista unikalnych słów pasujących do kombinacji liter wynikających z podanego ciągu cyfr.
5) Metoda  `predict(self, number_sequence: str) -> list`:
    - **Opis**: Zwraca listę słów zaczynających się od danego prefiksu.
    - **Działanie**:
        1. Tworzy wszystkie możliwe kombinacje słow na podstawie podanego ciągu cyfr.
        2. Poszukuje słow, znajdujących się w trie, które znajdują się w wygenerowanych kombinacjach
        3. Zwraca listę result, która zawiera wszystkie znalezione predykcje.

---
### Plik z implementacją interfejsu użytkownika
Interfejs użytkownika został zaimplementowany przy użyciu biblioteki `tkinter`. Poniżej znajduje się opis jego funkcjonalności.

## Funkcjonalności interfejsu:

1. **Pole wprowadzania:**
   - Umożliwia użytkownikowi wpisywanie ciągu cyfr, które są przetwarzane w celu przewidzenia odpowiadających im słów.

2. **Klawiatura numeryczna:**
   - Symuluje klawiaturę T9 z przyciskami numerycznymi (`1-9`, `0`, `*`, `#`).
   - Przyciski są oznaczone odpowiednimi literami, zgodnie z tradycyjnym układem T9.

3. **Przycisk "Roll":**
   - Pozwala na przeglądanie kolejnych przewidywań dla wprowadzonego ciągu cyfr.

4. **Przycisk "Delete":**
   - Usuwa ostatni wprowadzony znak z ciągu cyfr.

5. **Przycisk "Save":**
   - Zapisuje wybrane słowo do pliku `result.csv`.

6. **Etykieta wyniku:**
   - Wyświetla aktualnie wybrane słowo lub komunikaty informacyjne.

### Testy

Poniżej znajduje się opis testów jednostkowych, które zostały zaimplementowane w celu sprawdzenia funkcjonalności klasy `T9`.

### Opis testów:

1. **test_find_nonexisting_word**
   - **Opis:** Sprawdza, czy metoda `predict` zwraca pustą listę, gdy szukane słowo nie istnieje w słowniku.

2. **test_find_existing_word**
   - **Opis:** Sprawdza, czy metoda `predict` zwraca poprawne słowo na podstawie wprowadzonego ciągu cyfr.

3. **test_find_existing_words**
   - **Opis:** Weryfikuje, czy metoda `predict` zwraca wszystkie pasujące słowa dla danego ciągu cyfr.

4. **test_word_appearing_multiple_times**
   - **Opis:** Sprawdza, czy metoda `predict` zwraca unikalne słowo, które pojawia się wielokrotnie w słowniku.

5. **test_words_appearing_multiple_times**
   - **Opis:** Weryfikuje, czy metoda `predict` zwraca poprawną liczbę unikalnych słów, które pojawiają się wielokrotnie w słowniku.

6. **test_empty_word**
   - **Opis:** Sprawdza, czy metoda `predict` zwraca pustą listę, gdy wprowadzone słowo jest puste.


### Podsumowanie
Testy pokrywają kluczowe funkcjonalności klasy `T9`, takie jak przewidywanie słów na podstawie ciągu cyfr, obsługa przypadków brzegowych (np. brak wyników, puste wejście), a także zapewnienie, że zwracane są poprawne i unikalne słowa. Każdy test sprawdza inną funkcjonalność metody `predict`, co pozwala na kompleksowe przetestowanie działania klasy.




