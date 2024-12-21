# spell_checker.py

import re
from collections import Counter
from typing import List
from itertools import product

# Levenshtein distance function
def lev(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,  # Deletion
                    dp[i][j - 1] + 1,  # Insertion
                    dp[i - 1][j - 1] + 1  # Substitution
                )
    return dp[m][n]

# Prefix matching function
def prefix_match(string1, string2):
    common_length = 0
    for i in range(min(len(string1), len(string2))):
        if string1[i] == string2[i]:
            common_length += 1
        else:
            break
    return common_length

# Suffix matching function
def suffix_match(string1, string2):
    common_length = 0
    for i in range(1, min(len(string1), len(string2)) + 1):
        if string1[-i] == string2[-i]:
            common_length += 1
        else:
            break
    return common_length

# Prefilter candidates based on length difference
def prefilter_candidates(user_input, correct_words, length_threshold=2):
    return [
        word for word in correct_words
        if abs(len(word) - len(user_input)) <= length_threshold
    ]

# Modified suggestions function to return top N candidates
def suggestions(user_input, correct_words, top_n=5):
    candidates = []
    filtered_correct_words = prefilter_candidates(user_input, correct_words)

    # Weights for each component
    w_lev = 0.7  # Weight for Levenshtein distance (penalty)
    w_prefix = 0.15  # Weight for prefix match (reward)
    w_suffix = 0.15  # Weight for suffix match (reward)

    for word in filtered_correct_words:
        lev_score = lev(user_input, word)
        prefix_score = prefix_match(user_input, word)
        suffix_score = suffix_match(user_input, word)

        # Combined score
        score = w_lev * lev_score - w_prefix * prefix_score - w_suffix * suffix_score

        candidates.append((word, score))

    # Sort by combined score (lower is better)
    candidates = sorted(candidates, key=lambda x: x[1])
    return [candidate[0] for candidate in candidates[:top_n]] if candidates else [user_input]


class SpellChecker:
    def __init__(self, correct_words_file, user_input):
        self.user_input_words = user_input.split()  # Split user input into words
        self.correct_words = self.load_dictionary(correct_words_file)  # Load the dictionary

    def load_dictionary(self, correct_words_file):
        """Load dictionary from file."""
        try:
            with open(correct_words_file, 'r', encoding='utf-8') as file:
                return [word.strip() for word in file.readlines()]  # List of words in the dictionary
        except FileNotFoundError:
            return []

    def correct(self):
        """
        Correct the user input by checking for unseen words and generating suggestions.
        """
        corrected_results = {}
        for word in self.user_input_words:
            # Handle unseen word
            if word not in self.correct_words:
                # Generate suggestions for unseen word
                top_suggestions = suggestions(word, self.correct_words, top_n=5)
                corrected_results[word] = top_suggestions
                print(f"'{word}' -> Suggestions: {', '.join(top_suggestions)}")
            else:
                corrected_results[word] = [word]  # Word is correct
        return corrected_results

    def add_to_dictionary(self, new_words: List[str]):
        """Add unseen words to the dictionary."""
        self.correct_words.extend(new_words)
        self.correct_words = list(set(self.correct_words))  # Remove duplicates if any

