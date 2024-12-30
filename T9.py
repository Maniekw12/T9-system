import Trie

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
            return ['']

        current_digit = sequence[0]
        letters = self.num_to_letters[current_digit]
        rest_of_sequence = sequence[1:]
        rest_combinations = self._generate_combinations(rest_of_sequence)

        combinations = []
        for letter in letters:
            for combination in rest_combinations:
                combinations.append(letter + combination)
        return combinations

    def predict(self, number_sequence):
        # Generate all possible letter combinations for the number sequence
        combinations = self._generate_combinations(number_sequence)
        results = []
        for combination in combinations:
            results.extend(self.trie.starts_with(combination))
        return list(set(results))  # Return unique predictions


