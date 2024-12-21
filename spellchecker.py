import jellyfish  # For Levenshtein distance

# Load Tamil words dataset
def load_tamil_words(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        tamil_words = [line.strip() for line in file.readlines()]
    return tamil_words

# Function to find the closest match
def suggest_word(word, tamil_words):
    suggestions = {}
    for tamil_word in tamil_words:
        # Calculate Levenshtein distance
        distance = jellyfish.levenshtein_distance(word, tamil_word)
        suggestions[tamil_word] = distance
    # Return the word with the smallest distance
    return sorted(suggestions, key=suggestions.get)[0]

# Tamil Spell Checker
def tamil_spell_checker(paragraph, tamil_words):
    corrected_text = []
    words = paragraph.split()  # Split input into words
    for word in words:
        if word in tamil_words:
            corrected_text.append(word)  # If the word is correct
        else:
            suggestion = suggest_word(word, tamil_words)
            corrected_text.append(suggestion)  # Append the corrected word
    return " ".join(corrected_text)

# Evaluate Accuracy
def evaluate_accuracy(paragraphs, tamil_words):
    correct_count = 0
    total_count = 0
    corrected_paragraphs = []

    for paragraph in paragraphs:
        corrected_text = tamil_spell_checker(paragraph, tamil_words)
        corrected_paragraphs.append(corrected_text)

        # For evaluation, compare each word
        original_words = paragraph.split()
        corrected_words = corrected_text.split()
        for o_word, c_word in zip(original_words, corrected_words):
            if o_word == c_word:
                correct_count += 1
            total_count += 1

    accuracy = (correct_count / total_count) * 100
    return accuracy, corrected_paragraphs

# Load Tamil dataset
tamil_words = load_tamil_words("./tamilwords.txt")

# Test with five paragraphs (example paragraphs with spelling errors)
paragraphs = [
    "அன்பி நன்றி மகிழ்ச்சி புத்தக",
    "கணினி தமிழ் வரலாறு கல்லோரி",
    "மரம் அனம்பு நன்றி மன்ஜளம்",
    "புத்தகதான் மரத பற்களி",
    "அன்பு தமிழ் நன்றின வரலர"
]

# Evaluate
accuracy, corrected_paragraphs = evaluate_accuracy(paragraphs, tamil_words)

# Output results
print("Accuracy: {:.2f}%".format(accuracy))
print("\nCorrected Paragraphs:")
for i, corrected in enumerate(corrected_paragraphs, 1):
    print(f"Paragraph {i}: {corrected}")
