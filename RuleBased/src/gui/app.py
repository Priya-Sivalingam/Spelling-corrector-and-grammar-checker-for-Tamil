import tkinter as tk
from tkinter import messagebox
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import necessary data and functions
from data.verb_conjugations import verb_forms
from data.gender_mapping import gender_map
from data.tense_mapping import tense_map
from utils.parser import parse_sentence
from utils.corrector import correct_grammar

# Reverse mapping for conjugated verbs
conjugation_to_base = {
    conjugation: base_verb
    for base_verb, tenses in verb_forms.items()
    for tense, genders in tenses.items()
    for conjugation in genders.values()
}

# Function to handle grammar correction
def correct_sentence():
    # Get input sentence
    input_text = input_field.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showerror("Error", "Please enter a sentence.")
        return

    # Parse the sentence
    subject, tense, verb, tense_indicator = parse_sentence(input_text, gender_map, tense_map, conjugation_to_base)

    # Correct grammar
    corrected_sentence = correct_grammar(subject, tense, verb, gender_map, verb_forms, conjugation_to_base, tense_indicator)

    # Display corrected sentence
    if "Error" in corrected_sentence:
        corrected_label.config(text=f"Error: {corrected_sentence}", fg="red")
    else:
        corrected_label.config(text=f"Corrected Sentence: {corrected_sentence}", fg="green")

# Function to clear the input and output
def clear_text():
    input_field.delete("1.0", tk.END)
    corrected_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Tamil Grammar Corrector")
root.geometry("500x400")

# Add a title label
title_label = tk.Label(root, text="Tamil Grammar Corrector", font=("Arial", 18, "bold"), fg="blue")
title_label.pack(pady=10)

# Add an input field
input_label = tk.Label(root, text="Enter a Tamil sentence with grammatical errors:", font=("Arial", 12))
input_label.pack(pady=5)
input_field = tk.Text(root, height=5, width=50, font=("Arial", 12))
input_field.pack(pady=5)

# Add a Correct button
correct_button = tk.Button(root, text="Correct Sentence", font=("Arial", 12, "bold"), bg="green", fg="white", command=correct_sentence)
correct_button.pack(pady=10)

# Add a Clear button
clear_button = tk.Button(root, text="Clear", font=("Arial", 12), bg="red", fg="white", command=clear_text)
clear_button.pack(pady=5)

# Add a label to display the corrected sentence
corrected_label = tk.Label(root, text="", font=("Arial", 12), wraplength=400)
corrected_label.pack(pady=10)

# Run the application
root.mainloop()
