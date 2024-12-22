from spellchecker import SpellChecker
# Example usage of the updated SpellChecker class
def correct_text(test_sentence, correct_words_file):
    # Load the correct words from the provided file
    with open(correct_words_file, 'r', encoding='utf-8') as file:
        correct_words = [line.strip() for line in file]  # Strip newline characters

    # Initialize the SpellChecker object with correct words
    spell_checker = SpellChecker(correct_words)

    # Correct the test sentence
    corrected_text = spell_checker.correct(test_sentence)
    return corrected_text

from Evaluate_Spell_checker import evaluate_spell_checker

# File containing the correct words
correct_words_file = "../Data/processed_words.txt"

# Test paragraphs with some incorrect sentences
test_paragraphs_list = [
    "அத நூற்ற கரடமுடான வலிமையான கயறகத் திரக்கலம்.தொழில் ரீதியாக சணல் இழை கச்சா சணல் என்றழைக்கப்படுகிறது. இழைகள் மங்கிய வெள்ளையிலிருந்து பழுப்பு நிறம் வரையிலும்.சணல இழை ஹெஸ்ஸயன என அழைக்கப்படுகிறது."
]

# Expected sentences for comparison
expected_paragraph = [
    "அதை நூற்று கரடமுரடான வலிமையான கயிறாகத் திரிக்கலாம்.தொழில் ரீதியாக சணல் இழை கச்சா சணல் என்றழைக்கப்படுகிறது. இழைகள் மங்கிய வெள்ளையிலிருந்து பழுப்பு நிறம் வரையிலும்.சணல் இழை ஹெஸ்ஸியன் என அழைக்கப்படுகிறது."
]

# Function to split the text into sentences
def split_into_sentences(paragraphs):
    return [para.rstrip(".").split(".") for para in paragraphs]

# Split the test and expected paragraphs into sentences
test_sentences = split_into_sentences(test_paragraphs_list)
expected_sentences = split_into_sentences(expected_paragraph)

# Loop through test paragraphs and perform spell/grammar correction
for idx, test_sentences_group in enumerate(test_sentences):
    print(f"\n\n--- Testing Paragraph {idx+1} ---\n")

    for i, sentence in enumerate(test_sentences_group):
        print(f"\nTest Sentence {i+1}: {sentence.strip()}")

        # Correct the test sentence using the SpellChecker
        corrected_text = correct_text(sentence.strip(), correct_words_file)

        # Output the corrected text
        print(f"Corrected Text: {corrected_text.strip()}")

        # Evaluate the spell checker against the expected result
        print("\n--- Evaluation Results ---")

        # Pass the individual sentences as arguments for evaluation
        evaluate_spell_checker(
            sentence.strip().split(), 
            expected_sentences[idx][i].strip().split(), 
            corrected_text.strip()
        )