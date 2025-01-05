# src/utils/corrector.py
def correct_grammar(subject, tense, verb, gender_map, verb_forms, conjugation_to_base):
    if not (subject and tense and verb):
        return "Error: Unable to parse the sentence."

    gender = gender_map[subject]
    base_verb = conjugation_to_base.get(verb)
    if not base_verb or base_verb not in verb_forms or tense not in verb_forms[base_verb]:
        return f"Error: Conjugation for '{verb}' not found."

    return verb_forms[base_verb][tense][gender]
