import json

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
    Example:
    'அவள் வந்தான்' -> Incorrect, should be 'அவள் வந்தாள்'
    'அவள் வந்தாள்' -> Correct
    """
    tokens = tokenize_sentence(sentence)
    if len(tokens) > 1 and tokens[0] in subject_verb_rules:
        expected_verb = subject_verb_rules[tokens[0]]
        if tokens[1] != expected_verb:
            corrected_sentence = sentence.replace(tokens[1], expected_verb)
            return f"Incorrect: '{sentence}' -> Corrected: '{corrected_sentence}'"
    return None

def check_tense_agreement(sentence, tense_rules):
    """
    Rule: Check if the verb agrees with the tense (past, present, future).
    Example:
    'அவள் வந்து இருக்கின்றாள்' -> Correct (Present continuous)
    'அவள் வந்தாள்' -> Correct (Past)
    'அவள் வருவாள்' -> Correct (Future)
    """
    tokens = tokenize_sentence(sentence)
    
    if len(tokens) > 1 and tokens[0] in tense_rules:
        # Check for tense agreement
        subject = tokens[0]
        verb = tokens[1]
        
        # Check for tense in the verb
        if verb in tense_rules[subject]["past"]:
            expected_tense = "past"
        elif verb in tense_rules[subject]["present"]:
            expected_tense = "present"
        elif verb in tense_rules[subject]["future"]:
            expected_tense = "future"
        else:
            return f"Error: '{verb}' is not a valid verb form for {subject}."
        
        expected_verb = tense_rules[subject][expected_tense]
        if verb != expected_verb:
            corrected_sentence = sentence.replace(verb, expected_verb)
            return f"Incorrect: '{sentence}' -> Corrected: '{corrected_sentence}'"
    return None

def grammar_corrector(sentence, subject_verb_rules, tense_rules):
    """Check for both subject-verb agreement and tense-based agreement errors."""
    subject_verb_error = check_subject_verb_agreement(sentence, subject_verb_rules)
    tense_error = check_tense_agreement(sentence, tense_rules)
    
    if subject_verb_error:
        return subject_verb_error
    elif tense_error:
        return tense_error
    else:
        return f"Correct sentence: '{sentence}'"

# Load the rules from JSON files
subject_verb_rules = load_rules_from_file('subject_verb_rules.json')
tense_rules = load_rules_from_file('tense_rules.json')

# Test examples
sentence1 = 'அவள் வந்தான்'  # Incorrect: subject-verb mismatch
sentence2 = 'அவள் வந்தாள்'  # Correct
sentence3 = 'அவன் வந்து இருக்கின்றான்'  # Correct (Present continuous)
sentence4 = 'அவன் வருவான்'  # Correct (Future)

print(grammar_corrector(sentence1, subject_verb_rules, tense_rules))
print(grammar_corrector(sentence2, subject_verb_rules, tense_rules))
print(grammar_corrector(sentence3, subject_verb_rules, tense_rules))
print(grammar_corrector(sentence4, subject_verb_rules, tense_rules))
