def correct_grammar(subject, tense, verb, gender_map, verb_forms, conjugation_to_base, tense_indicator):
    """
    Corrects grammatical errors in the input sentence based on gender and tense.

    Args:
        subject (str): The subject of the sentence (e.g., "அவன்", "அவள்").
        tense (str): The tense of the sentence (e.g., "past", "present", "future").
        verb (str): The verb in the sentence (e.g., "கொடுக்கிறான்").
        gender_map (dict): Mapping of subjects to their genders.
        verb_forms (dict): Mapping of base verbs to their conjugated forms.
        conjugation_to_base (dict): Mapping of conjugated verbs to base verbs.
        tense_indicator (str): The tense indicator word (e.g., "இன்று", "நாளை").

    Returns:
        str: The corrected sentence.
    """
    # Check if the subject, tense, or verb is missing
    if not (subject and tense and verb):
        return "Error: Unable to parse the sentence."

    # Identify the gender of the subject
    gender = gender_map.get(subject)
    if not gender:
        return f"Error: Gender not found for subject '{subject}'."

    # Get the base form of the verb
    base_verb = conjugation_to_base.get(verb)
    if not base_verb or base_verb not in verb_forms or tense not in verb_forms[base_verb]:
        return f"Error: Conjugation for verb '{verb}' not found."

    # Get the corrected verb
    corrected_verb = verb_forms[base_verb][tense][gender]

    # Reconstruct the full corrected sentence with the tense indicator
    return f"{subject} {tense_indicator} {corrected_verb}"
