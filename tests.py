import T9
import unittest
import csv
import re

def test_t9():
    t9 = T9.T9()
    words = []
    with open('words.csv',encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            cleaned_row = [col.strip() for col in row]
            row_string = ','.join(cleaned_row)
            split_words = re.split(r'[,\s]+', row_string)
            words.extend([word for word in split_words if word])
    print(words)

class Test_T9(unittest.TestCase):
    def setUp(self):
        self.words = ["aaa", "aba", "aca", "tuv","tuv","tuv","tuv","tuv","tuv", "def", "fed", "efd", "mno","pqrs", "pqrs","qprs"]
        self.T9 = T9.T9()
        for word in self.words:
            self.T9.insert_word(word)

    def test_find_nonexisting_word(self):
        non_existing_word = "999"
        self.assertEqual(self.T9.predict(non_existing_word),[])

    def test_find_existing_word(self):
        non_existing_word = "666"
        self.assertEqual(self.T9.predict(non_existing_word),["mno"])

    def test_find_existing_words(self):
        existing_words = "222"
        self.assertEqual(set(self.T9.predict(existing_words)), set(["aaa", "aba", "aca"]))

    def test_word_appearing_muliple_times(self):
        word = "888"
        self.assertEqual(self.T9.predict(word),["tuv"])

    def test_words_appearing_muliple_times(self):
        word = "7777"
        self.assertEqual(self.T9.predict(word), ["pqrs", "qprs"])

    def test_empty_word(self):
        word = ""
        self.assertEqual(self.T9.predict(word), [])

if __name__ == "__main__":
    unittest.main()









