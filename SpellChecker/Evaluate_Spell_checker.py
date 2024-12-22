# evaluate.py
def evaluate_spell_checker(test_words, expected_words, corrected_text):
    """
    This function evaluates the spell checker by comparing the corrected words
    against the expected words, calculating metrics like accuracy, precision, recall, etc.
    """
    # Split the corrected text into words
    corrected_words = corrected_text.split()

    # Initialize counts for true positives, false positives, false negatives, and true negatives
    TP = FP = FN = TN = 0

    # Ensure we are comparing the words in test and expected sentences correctly
    for test_word, expected_word, corrected_word in zip(test_words, expected_words, corrected_words):
        # True positive: corrected word matches the expected word
        if corrected_word == expected_word:
            TP += 1
        # False positive: corrected word doesn't match the expected word, but it's not a mistake in the original word
        elif corrected_word != expected_word and corrected_word != test_word:
            FP += 1
        # False negative: the corrected word did not match the expected word, and it should have
        elif corrected_word != expected_word and corrected_word == test_word:
            FN += 1
        # True negative: the word was correct and not corrected
        elif corrected_word == test_word and corrected_word == expected_word:
            TN += 1

    # Calculate metrics
    accuracy = (TP + TN) / (TP + FP + FN + TN) if (TP + FP + FN + TN) != 0 else 0
    precision = TP / (TP + FP) if (TP + FP) != 0 else 0
    recall = TP / (TP + FN) if (TP + FN) != 0 else 0
    specificity = TN / (TN + FP) if (TN + FP) != 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) != 0 else 0

    # Print the evaluation results
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1-Score: {f1_score:.4f}")
