import Trie
from itertools import product

class T9:

    def __init__(self):
        self.num_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        self.trie = Trie.Trie()

    def insert_word(self, word):
        self.trie.insert_key(word)

    def _generate_combinations(self,sequence):
        if not sequence:
            return []

        letters_for_digits = []
        for digit in sequence:
            for digit in self.num_to_letters:
                letters_for_digits.append(self.num_to_letters[digit])

        if not letters_for_digits:
            return []
###############################################
        # Produkt kartezjański liter dla każdej cyfry (wszystkie możliwe kombinacje)
        all_combinations = product(*letters_for_digits)

        # Połącz każdą krotkę w pojedynczy string
        result = [''.join(combination) for combination in all_combinations]
##############################################
    def predict(self, number_sequence):
        # Generate all possible letter combinations for the number sequence
        def generate_combinations(sequence):
            if not sequence:
                return ['']

            current_digit = sequence[0]
            letters = self.num_to_letters[current_digit]
            rest_of_sequence = sequence[1:]
            rest_combinations = generate_combinations(rest_of_sequence)

            combinations = []
            for letter in letters:
                for combination in rest_combinations:
                    combinations.append(letter + combination)
            return combinations

        combinations = generate_combinations(number_sequence)
        results = []
        for combination in combinations:
            results.extend(self.trie.starts_with(combination))
        return list(set(results))  # Return unique predictions
