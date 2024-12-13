# Define basic grammar rules
def check_subject_verb_agreement(sentence):
    """
    - Singular subjects use singular verbs
    - Plural subjects use plural verbs
    """
    errors = []
    singular_subjects = ["அவன்", "அவள்", "அது"]  
    singular_verbs = ["செல்லும்", "படிக்கும்", "காணும்"] 
    plural_subjects = ["அவர்கள்", "நாங்கள்", "அவை"] 
    plural_verbs = ["செல்கிறார்கள்", "படிக்கிறார்கள்", "காண்கிறார்கள்"]  
    words = sentence.split()
    if len(words) >= 2:
        subject, verb = words[0], words[-1]  # Check subject and the last word as verb
        if subject in singular_subjects and verb not in singular_verbs:
            errors.append(f"Subject-verb agreement error: '{subject}' should match a singular verb.")
        elif subject in plural_subjects and verb not in plural_verbs:
            errors.append(f"Subject-verb agreement error: '{subject}' should match a plural verb.")
    return errors


def check_word_order(sentence):
    """
    Checks basic word order in Tamil.
    Tamil follows SOV (Subject-Object-Verb) structure.
    """
    errors = []
    words = sentence.split()
    tamil_verbs = ["செல்லும்", "படிக்கும்", "காணும்", "வாசிக்கிறேன்"]  # Common Tamil verbs

    # Ensure at least Subject-Verb or Subject-Object-Verb structure exists
    if len(words) >= 2:
        # The last word should be a verb
        if words[-1] not in tamil_verbs:
            errors.append(f"Word order error: The last word '{words[-1]}' is not a valid verb in SOV structure.")
        # If 3 or more words, ensure middle words are not verbs
        if len(words) >= 3:
            for obj in words[1:-1]:
                if obj in tamil_verbs:
                    errors.append(f"Word order error: Word '{obj}' should not be a verb in SOV structure.")
    else:
        errors.append("Word order error: Incomplete sentence structure.")

    return errors


def tamil_grammar_checker(sentence):
    """
    Combines different rule-based checks for Tamil grammar.
    """
    errors = []
    errors.extend(check_subject_verb_agreement(sentence))
    errors.extend(check_word_order(sentence))

    if not errors:
        return "No grammatical errors found."
    else:
        return "\n".join(errors)


if __name__ == "__main__":
    # Input Tamil sentences
    sentence1 = "அவன் செல்லுகிறார்கள்"  
    sentence2 = "செல்லும் அவன்"  
    sentence3 = "அவன் செல்லும்"  

    print("Sentence 1:", tamil_grammar_checker(sentence1))
    print("Sentence 2:", tamil_grammar_checker(sentence2))
    print("Sentence 3:", tamil_grammar_checker(sentence3))
