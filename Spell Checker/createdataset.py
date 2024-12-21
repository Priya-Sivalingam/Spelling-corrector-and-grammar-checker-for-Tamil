import pandas as pd
import re
from pathlib import Path

def load_dataset(file_path):
    """
    Load a CSV dataset from the given file path and ensure it contains a 'Text' column.
    """
    if not Path(file_path).exists():
        raise FileNotFoundError(f"Dataset not found at {file_path}")
    try:
        dataset = pd.read_csv(file_path)
        if 'Text' not in dataset.columns:
            raise ValueError("The dataset does not contain a 'Text' column.")
        return dataset
    except Exception as e:
        raise ValueError(f"Failed to load dataset: {e}")

def extract_words_from_text(text):
    """
    Clean and extract Tamil words from a given text string.
    """
    text = re.sub(r'[0-9.,]', '', text)  # Remove digits and certain punctuation
    text = re.sub(r'[^஀-௿\s]', '', text)  # Remove non-Tamil characters
    words = text.split()  # Split into words
    return words

def extract_words_from_dataset(dataset):
    """
    Extract words from the 'Text' column of the dataset.
    """
    all_words = []
    for idx, text in dataset['Text'].dropna().items():  # Fixed incorrect '()' after 'items'
        words = extract_words_from_text(text)
        all_words.extend(words)
    return all_words

def save_words_to_file(words, output_file):
    """
    Save the extracted words to a specified file, creating directories if necessary.
    """
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)  
    with open(output_file, 'w', encoding='utf-8') as file:
        for word in words:
            file.write(word + '\n')

def main():
    """
    Main function to load the dataset, extract words, and save them to a file.
    """
    dataset_path = "../data/Tamil _wiki-data.csv"  # Corrected file name
    output_file = "../data/processed_words.txt"

    print("Loading dataset...")
    try:
        dataset = load_dataset(dataset_path)
        print("Dataset loaded successfully.")
    except Exception as e:
        print(f"Error: {e}")
        return

    print("Extracting words...")
    try:
        extracted_words = extract_words_from_dataset(dataset)
        print(f"Extracted {len(extracted_words)} words successfully.")
    except Exception as e:
        print(f"Error during word extraction: {e}")
        return

    print(f"Saving words to {output_file}...")
    try:
        save_words_to_file(extracted_words, output_file)
        print(f"Words saved successfully to {output_file}.")
    except Exception as e:
        print(f"Error saving words to file: {e}")

if __name__ == "__main__":
    main()
