def parse_sentence(sentence, gender_map, tense_map, conjugation_to_base):
    """
    Parses the sentence to extract the subject, tense, verb, and tense indicator.
    If no tense indicator is found, it defaults to present tense.

    Args:
        sentence (str): The input Tamil sentence.
        gender_map (dict): Mapping of subjects to genders.
        tense_map (dict): Mapping of time indicators to tenses.
        conjugation_to_base (dict): Mapping of conjugated verbs to base verbs.

    Returns:
        tuple: Extracted subject, tense, verb, and tense indicator.
    """
    words = sentence.split()
    subject, tense, verb, tense_indicator = None, None, None, None

    for word in words:
        if word in gender_map:
            subject = word
        elif word in tense_map:
            tense = tense_map[word]
            tense_indicator = word  # Store the tense indicator
        elif word in conjugation_to_base:
            verb = word
    
    # Default to 'present' tense if no tense indicator is found
    if tense is None:
        tense = 'present'

    return subject, tense, verb, tense_indicator
