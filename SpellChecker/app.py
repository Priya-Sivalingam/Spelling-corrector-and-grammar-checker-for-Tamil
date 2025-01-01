from flask import Flask, request, render_template
from spellchecker import SpellChecker
from typing import List

app = Flask(__name__)

def load_words(file_path: str) -> List[str]:
    with open(file_path, 'r', encoding='utf-8') as file: 
        return [line.strip() for line in file.readlines()]
    
correct_words = load_words('../Dataset/processed_words.txt')
spell_checker = SpellChecker(correct_words)


@app.route("/", methods=["GET", "POST"])
def home():
    corrected_sentence = ""
    suggestions_list = []

    if request.method == "POST":
        user_input = request.form.get("sentence")
        corrected_sentence = spell_checker.correct(user_input)

        suggestions_list = {
            word: spell_checker.suggestions(word)
            for word in user_input.split()
        }

    return render_template("index.html", corrected_sentence=corrected_sentence, suggestions=suggestions_list)

if __name__ == "__main__":
    app.run(debug=True)
