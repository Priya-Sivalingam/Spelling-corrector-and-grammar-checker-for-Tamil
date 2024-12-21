import json
from nltk.translate.bleu_score import sentence_bleu

def load_rules_from_file(file_path):
    """Loads rules from a JSON file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def tokenize_sentence(sentence):
    """Splits the sentence into words."""
    return sentence.split()

def check_subject_verb_agreement(sentence, subject_verb_rules):
    """
    Rule: Check if the subject agrees with the verb.
    """
    tokens = tokenize_sentence(sentence)
    if len(tokens) > 1 and tokens[0] in subject_verb_rules:
        expected_verb = subject_verb_rules[tokens[0]]
        if tokens[1] != expected_verb:
            corrected_sentence = sentence.replace(tokens[1], expected_verb)
            return corrected_sentence
    return sentence

def check_tense_agreement(sentence, tense_rules):
    """
    Rule: Check if the verb agrees with the tense.
    """
    tokens = tokenize_sentence(sentence)
    if len(tokens) > 1 and tokens[0] in tense_rules:
        subject = tokens[0]
        verb = tokens[1]

        # Check tense in the verb
        for tense, correct_verb in tense_rules[subject].items():
            if verb == correct_verb:
                return sentence  # Already correct
        
        # Correct the verb if it doesn't match any tense
        expected_verb = tense_rules[subject]["past"]  # Default to past for correction
        corrected_sentence = sentence.replace(verb, expected_verb)
        return corrected_sentence
    return sentence

def grammar_corrector(sentence, subject_verb_rules, tense_rules):
    """Check for both subject-verb agreement and tense-based agreement errors."""
    corrected_sentence = check_subject_verb_agreement(sentence, subject_verb_rules)
    corrected_sentence = check_tense_agreement(corrected_sentence, tense_rules)
    return corrected_sentence

def calculate_char_bleu_score(predicted_sentence, reference_sentence):
    """
    Calculate BLEU score at the character level.
    Tokenizes sentences into characters instead of words.
    """
    reference = [list(reference_sentence)]  # Reference as list of characters
    predicted = list(predicted_sentence)    # Predicted as list of characters
    return sentence_bleu(reference, predicted)

def evaluate_sentences(test_sentences, reference_sentences, subject_verb_rules, tense_rules):
    """
    Evaluate each test sentence, calculate character-level BLEU, and compute average BLEU.
    """
    total_bleu_score = 0.0
    scores = []
    
    for i, test_sentence in enumerate(test_sentences):
        predicted_sentence = grammar_corrector(test_sentence, subject_verb_rules, tense_rules)
        reference_sentence = reference_sentences[i]
        
        bleu_score = calculate_char_bleu_score(predicted_sentence, reference_sentence)
        scores.append(bleu_score)
        total_bleu_score += bleu_score
        
        print(f"Test Sentence {i + 1}: {test_sentence}")
        print(f"Predicted: {predicted_sentence}")
        print(f"Reference: {reference_sentence}")
        print(f"Character-Level BLEU Score: {bleu_score:.4f}\n")
    
    average_bleu_score = total_bleu_score / len(test_sentences)
    print(f"Average Character-Level BLEU Score: {average_bleu_score:.4f}")
    return scores, average_bleu_score

# Load the rules from JSON files
subject_verb_rules = load_rules_from_file("RuleBased\subject_verb_rules.json")
tense_rules = load_rules_from_file("RuleBased\File_tense_rules.json")

# Test Sentences and References
test_sentences = [
    'அவள் வந்தான்',    # Incorrect
    'அவள் வந்தாள்',    # Correct
    'அவன் வந்து இருக்கின்றான்',  # Correct
    'அவன் வருவான்',    # Correct
    'நான் வந்து இருக்கின்றேன்'  # Correct
]

reference_sentences = [
    'அவள் வந்தாள்',
    'அவள் வந்தாள்',
    'அவன் வந்து இருக்கின்றான்',
    'அவன் வருவான்',
    'நான் வந்து இருக்கின்றேன்'
]

# Evaluate
evaluate_sentences(test_sentences, reference_sentences, subject_verb_rules, tense_rules)
