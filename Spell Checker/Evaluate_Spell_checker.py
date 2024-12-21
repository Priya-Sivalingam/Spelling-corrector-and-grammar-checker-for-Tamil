# evaluate_spell_checker.py

import csv
from spellchecker import SpellChecker, lev

# Evaluation function
def evaluate_spell_checker(spell_checker, test_data_file):
    correct_count = 0
    total_count = 0

    # Read the test data
    with open(test_data_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            misspelled_word = row['Misspelled']
            correct_word = row['Correct']

            # Get the spell checker's suggestions
            corrections = spell_checker.correct()  # Get corrected results

            # Get the suggestions for the misspelled word
            suggestions = corrections.get(misspelled_word, [misspelled_word])
            
            # Remove duplicates by converting to a set
            unique_suggestions = list(set(suggestions))

            # Compute Levenshtein distance for each unique suggestion and pick the best
            lev_scores = [(suggestion, lev(misspelled_word, suggestion)) for suggestion in unique_suggestions]
            lev_scores.sort(key=lambda x: x[1])  # Sort by Levenshtein score (lower is better)

            # Best suggestion is the one with the lowest Levenshtein distance
            best_suggestion = lev_scores[0][0]

            # Compare the best suggestion with the correct word
            if best_suggestion == correct_word:
                correct_count += 1
            total_count += 1

    # Calculate and return accuracy
    accuracy = (correct_count / total_count) * 100
    return accuracy

# Main block to run the evaluation
if __name__ == "__main__":
    correct_words_file = "../data/processed_words.txt"  # Path to the dictionary file
    test_data_file = "../data/test_data.csv"  # Path to the test dataset
    
    # Create an instance of SpellChecker
    user_input = ""  # Empty input for evaluation
    spell_checker = SpellChecker(correct_words_file, user_input)
    
    # Evaluate spell checker accuracy
    accuracy = evaluate_spell_checker(spell_checker, test_data_file)
    print(f"Spell Checker Accuracy: {accuracy:.2f}%")
