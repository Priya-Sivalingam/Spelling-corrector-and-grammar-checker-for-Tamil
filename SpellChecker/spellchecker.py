import re
from collections import Counter
from typing import List

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

# Suggestions function
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

    candidates = sorted(candidates, key=lambda x: x[1])
    return [candidate[0] for candidate in candidates[:top_n]] if candidates else [user_input]

from Levenshtein import distance as lev  # Import Levenshtein distance function

class SpellChecker:
    def __init__(self, correct_words):
        self.correct_words = correct_words  # Load correct words as a list directly

    def suggestions(self, word):
        """
        This method generates a list of suggestions for the given word based on the Levenshtein distance.
        """
        # Calculate the Levenshtein distance between the input word and the correct words
        suggested_words = sorted(self.correct_words, key=lambda w: lev(word, w))
        return suggested_words[:5]  # Return top 5 closest matches

    def correct(self, sentence):
        """
        This method processes the user input and corrects the words using the closest match from the correct words.
        """
        corrected_words = []
        for word_to_check in sentence.split():  # Split sentence into words
            # Get the top suggestions for the word
            suggested_words = self.suggestions(word_to_check)

            # Select the word with the lowest Levenshtein distance as the best match
            best_match = suggested_words[0]
            corrected_words.append(best_match)

        return " ".join(corrected_words)  # Return the corrected sentence
