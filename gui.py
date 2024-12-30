import tkinter as tk
import T9
import csv
import re

words = []
try:
    with open('words.csv', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            cleaned_row = [col.strip() for col in row]
            row_string = ','.join(cleaned_row)
            split_words = re.split(r'[,\s]+', row_string)
            words.extend([word for word in split_words if word])
except FileNotFoundError:
    print("Error: words.csv not found.")
    words = []

class NumericKeyboard:

    def __init__(self, master):
        self.master = master
        self.master.title("Numeric Keyboard")

        self.input_string = ""
        self.chosen_word = ""

        self.t9 = T9.T9()
        self.predictions = []
        self.current_prediction_index = -1
        self.rolling_enabled = True

        self.input_entry = tk.Entry(master, font=("Arial", 16), width=20)

        self.input_entry.pack(pady=10)

        self.frame = tk.Frame(master)
        self.frame.pack(pady=10)

        for word in words:
            self.t9.insert_word(word.lower())

        buttons = [
            ("1", ""), ("2", "ABC"), ("3", "DEF"),
            ("4", "GHI"), ("5", "JKL"), ("6", "MNO"),
            ("7", "PQRS"), ("8", "TUV"), ("9", "WXYZ"),
            ("*", ""), ("0", ""), ("#", "")
        ]

        rows_and_cols = {
            0: [0, 0], 1: [0, 1], 2: [0, 2],
            3: [1, 0], 4: [1, 1], 5: [1, 2],
            6: [2, 0], 7: [2, 1], 8: [2, 2],
            9: [3, 0], 10: [3, 1], 11: [3, 2]
        }


        for index, (number, letters) in enumerate(buttons):
            button = tk.Button(
                self.frame,
                text=f"{number} {letters}",
                width=5,
                height=2,
                command=lambda num=number: self.append_character(num)
            )

            button.grid(row=rows_and_cols[index][0], column=rows_and_cols[index][1], padx=5, pady=5)


        self.roll_button = tk.Button(master, text="Roll", command=self.roll)
        self.roll_button.pack(pady=10)

        self.delete_button = tk.Button(master, text="Delete", command=self.delete)
        self.delete_button.pack(pady=10)

        self.save_button = tk.Button(master, text="Save", command=self.save_word)
        self.save_button.pack(pady=10)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=10)

    def append_character(self, num):
        self.input_string += num

        self.input_entry.delete(0, tk.END)
        self.input_entry.insert(0, self.input_string)


    def roll(self):


        self.predictions = self.t9.predict(self.input_string)
        if self.predictions:
            self.current_prediction_index += 1
            if self.current_prediction_index >= len(self.predictions):
                self.current_prediction_index = 0
            self.update_input_entry_with_prediction()

    def update_input_entry_with_prediction(self):
        self.chosen_word = self.predictions[self.current_prediction_index]
        self.input_entry.delete(0, tk.END)
        self.input_entry.insert(0, self.chosen_word)
        self.result_label.config(text=f"Predicted: {self.chosen_word}")

    def delete(self):

        if self.input_string:
            self.input_string = self.input_string[:-1]
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, self.input_string)

    def save_word(self):
        if not self.chosen_word:
            self.result_label.config(text="No word to save.")
            return

        try:
            with open('result.csv', 'a', encoding='utf-8') as result_file:
                result_file.write(self.chosen_word + '\n')
            self.result_label.config(text=f"Saved: {self.chosen_word}")
        except Exception as e:
            self.result_label.config(text=f"Error saving word: {e}")

if words:
    root = tk.Tk()
    app = NumericKeyboard(root)
    root.mainloop()
else:
    print("No words to display.")

