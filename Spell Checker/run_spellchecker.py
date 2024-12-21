# main.py

from spellchecker import SpellChecker, lev

def main():
    correct_words_file = "../data/processed_words.txt"  # Path to the dictionary file
    user_input = "கபபல"  # User input to be corrected

    # Create an instance of SpellChecker
    spell_checker = SpellChecker(correct_words_file, user_input)

    # Get and print suggestions for each word in the user input
    corrections = spell_checker.correct()

    # Print the final best suggestion for each word
    print("\nFinal Suggestions:")
    for word, suggestions in corrections.items():
        # Remove duplicates by converting the suggestions list to a set
        unique_suggestions = list(set(suggestions))

        # Compute Levenshtein distance for each unique suggestion and pick the best
        lev_scores = [(suggestion, lev(word, suggestion)) for suggestion in unique_suggestions]
        lev_scores.sort(key=lambda x: x[1])  # Sort by Levenshtein score (lower is better)

        # Best suggestion is the one with the lowest Levenshtein score
        best_suggestion = lev_scores[0][0]
        
        # Print suggestions for each word along with the best suggestion
        print(f"\nFor '{word}':")
        print("Suggestions: ", ", ".join([suggestion for suggestion, _ in lev_scores]))
        print(f"Best Suggestion -> {best_suggestion}")

if __name__ == "__main__":
    main()
