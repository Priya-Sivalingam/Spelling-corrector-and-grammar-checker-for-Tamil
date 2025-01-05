import tkinter as tk
from tkinter import ttk, messagebox
import json
from nltk.translate.bleu_score import sentence_bleu


# Load the rules from JSON files
def load_rules_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


subject_verb_rules = load_rules_from_file("subject_verb_rules.json")
tense_rules = load_rules_from_file("File_tense_rules.json")


# Grammar Corrector Functions
def tokenize_sentence(sentence):
    return sentence.split()


def check_subject_verb_agreement(sentence, subject_verb_rules):
    tokens = tokenize_sentence(sentence)
    if len(tokens) > 1 and tokens[0] in subject_verb_rules:
        expected_verb = subject_verb_rules[tokens[0]]
        if tokens[1] != expected_verb:
            corrected_sentence = sentence.replace(tokens[1], expected_verb)
            return corrected_sentence
    return sentence


def check_tense_agreement(sentence, tense_rules):
    tokens = tokenize_sentence(sentence)
    if len(tokens) > 1 and tokens[0] in tense_rules:
        subject = tokens[0]
        verb = tokens[1]

        for tense, correct_verb in tense_rules[subject].items():
            if verb == correct_verb:
                return sentence  # Already correct

        expected_verb = tense_rules[subject]["past"]  # Default to past for correction
        corrected_sentence = sentence.replace(verb, expected_verb)
        return corrected_sentence
    return sentence


def grammar_corrector(sentence, subject_verb_rules, tense_rules):
    corrected_sentence = check_subject_verb_agreement(sentence, subject_verb_rules)
    corrected_sentence = check_tense_agreement(corrected_sentence, tense_rules)
    return corrected_sentence


def calculate_char_bleu_score(predicted_sentence, reference_sentence):
    reference = [list(reference_sentence)]
    predicted = list(predicted_sentence)
    return sentence_bleu(reference, predicted)


# GUI Implementation
def process_input():
    input_sentence = input_entry.get()

    if not input_sentence:
        messagebox.showerror("Error", "Please enter an input sentence.")
        return

    # Correct the sentence
    corrected_sentence = grammar_corrector(input_sentence, subject_verb_rules, tense_rules)
    
    # Calculate BLEU score comparing input to corrected sentence
    bleu_score = calculate_char_bleu_score(corrected_sentence, input_sentence)

    # Display the results
    corrected_output.set(corrected_sentence)
    bleu_output.set(f"{bleu_score:.4f}")


# Create the Tkinter Window
root = tk.Tk()
root.title("Tamil Grammar Corrector")
root.geometry("500x250")

# Input Section
ttk.Label(root, text="Input Sentence:").pack(pady=5)
input_entry = ttk.Entry(root, width=50)
input_entry.pack()

# Process Button
process_button = ttk.Button(root, text="Correct Sentence", command=process_input)
process_button.pack(pady=10)

# Output Section
ttk.Label(root, text="Corrected Sentence:").pack(pady=5)
corrected_output = tk.StringVar()
corrected_label = ttk.Label(root, textvariable=corrected_output, foreground="green")
corrected_label.pack()

ttk.Label(root, text="Character-Level BLEU Score:").pack(pady=5)
bleu_output = tk.StringVar()
bleu_label = ttk.Label(root, textvariable=bleu_output, foreground="blue")
bleu_label.pack()

# Run the GUI Loop
root.mainloop()
