# Spelling Corrector and Grammar Checker for Tamil  
**Artificial Intelligence Project - EC9640** 🤖

## Introduction  
Tamil is a widely spoken language, and ensuring text quality in Tamil on digital platforms is essential. This project aims to develop an AI-based tool for:  
1. **Spelling correction** ✍️: Identifying and auto-correcting up to five spelling errors in a paragraph.  
2. **Grammar checking** 🧑‍🏫: Detecting and correcting two types of grammatical errors (e.g., subject-verb agreement, contextual misuse).  

## Collaborators  
- **[member name]** 👨‍💻  
  - Developed the spelling correction module.  
  - Conducted testing, integration, and accuracy evaluations.  
- **[member name]** 👩‍💻  
  - Designed the grammar checking module.  
  - Researched and evaluated AI approaches for grammar correction.

---
# Tamil Spell Checker

This project implements a **spell checker** for Tamil text using Levenshtein distance and prefix/suffix matching. The spell checker suggests the closest matches for a given word based on a dictionary of correct words. The goal is to correct spelling errors in Tamil sentences by comparing the input against a predefined list of correct words.

## Features

- **Levenshtein Distance:** Calculates the similarity between two words based on the number of single-character edits required to change one word into the other (insertions, deletions, or substitutions).
- **Prefix and Suffix Matching:** Scores words based on the similarity of their prefixes and suffixes.
- **Suggestions:** Provides the top N suggestions for each word based on the combined score from the Levenshtein distance and matching prefixes/suffixes.
- **File-based Word List:** The spell checker uses a list of correctly spelled words, loaded from a file.
- **Evaluation:** The performance of the spell checker is evaluated against expected output sentences.
  
## Spell Checker Evaluation

The `evaluate_spell_checker` function evaluates a spell checker's performance by comparing its corrected output with the expected version of a text. It calculates key metrics such as **Accuracy**, **Precision**, **Recall**, and **F1-Score**.

### Inputs
1. `test_words`: Original words from the input text (may contain errors).
2. `expected_words`: The correct version of the words.
3. `corrected_text`: The spell checker’s output as a string.

### How It Works
- Compares the corrected words with both the original and expected words.
- Counts:
  - **True Positives (TP)**: Correct fixes.
  - **False Positives (FP)**: Incorrect fixes.
  - **False Negatives (FN)**: Missed corrections.
  - **True Negatives (TN)**: Correctly untouched words.

### Metrics
1. **Accuracy**: Proportion of words correctly handled.
2. **Precision**: Percentage of fixes that were correct.
3. **Recall**: Percentage of errors correctly fixed.
4. **F1-Score**: Balance between precision and recall.

# Tamil Grammar Corrector

This project is a Tamil grammar correction tool that implements multiple methods to detect and correct grammatical errors. The tool focuses on two types of verb grammatical errors in Tamil:
1. **Gender-based verb grammatical errors** 🚻
2. **Tense-based verb grammatical errors** ⏳

## Methods Implemented 🛠️

### 1. Rule-Based Method 📜
This model uses predefined rules to identify and correct errors in subject-verb agreement and tense agreement in Tamil sentences. It then calculates a BLEU score at the character level to evaluate the effectiveness of the correction by comparing predicted sentences to reference sentences.

### Core Functions:
1. **Grammar Correction:**
   - Corrects subject-verb agreement errors.
   - Corrects verb tense agreement errors.

2. **BLEU Score Calculation:**
   - Uses character-level BLEU score to evaluate the performance of the corrections.

## Features

- **Subject-Verb Agreement**: Corrects errors like mismatches between the subject and verb.
- **Tense Agreement**: Corrects verbs to ensure they match the tense of the subject.
- **BLEU Score Evaluation**: Calculates BLEU score at the character level to evaluate the model's performance.
- **Customizable Rules**: Grammar rules for subject-verb and tense agreement are loaded from external JSON files, making it easy to adapt the model to different languages or contexts.

- 
### 2. Deep Learning Method: Seq2Seq Model 🤖
#### Seq2Seq Model for Ungrammatical to Standard Tamil Sentence Translation

This project implements a **Sequence-to-Sequence (Seq2Seq)** model using LSTM layers to translate ungrammatical Tamil sentences into their standard Tamil counterparts. The model leverages the TensorFlow library for training and evaluation.  
A machine translation approach where the goal is to convert ungrammatical Tamil sentences into grammatically correct standard Tamil sentences. The architecture uses a **Seq2Seq model** with LSTM layers for both encoding and decoding sequences.

## Architecture 🏗️

### Encoder:
- The encoder takes ungrammatical sentences as input.
- It consists of an **Embedding layer** to map words to dense vectors, followed by an **LSTM layer** that processes the input and returns the final hidden and cell states.

### Decoder:
- The decoder generates standard Tamil sentences as output.
- It uses an **Embedding layer** and an **LSTM layer** to predict the next word in the output sequence based on the encoder's final states.
- A **Dense layer** with softmax activation is used to predict the output word at each time step.

### Inference 🔍:
- During inference, a separate encoder and decoder model are used to generate translations.
- The encoder produces initial states, and the decoder generates one word at a time, using the previous word's prediction as the next input.

### Training 📈:
- The model is trained using categorical crossentropy loss and the Adam optimizer.
- The training process is visualized using training and validation accuracy and loss plots.

### Evaluation 📊:
- The model's performance is evaluated using **BLEU scores**, a standard metric for machine translation.

## Requirements ⚙️

To run the code, the following libraries are required:

- **TensorFlow**: For building and training the Seq2Seq model.
- **Pandas**: For data handling and preprocessing.
- **NumPy**: For numerical operations.
- **Scikit-learn**: For data splitting and processing.
- **Matplotlib**: For plotting training/validation metrics.
- **NLTK**: For calculating BLEU scores.

### 3. Machine Learning / NLP Method 🧠

## Types of Grammar Errors Detected

### 1. Gender-Based Verb Grammatical Errors 🚻
In Tamil, verbs change depending on the gender of the subject. This tool identifies and corrects gender-based verb errors, such as using masculine verbs with feminine subjects and vice versa.

### 2. Tense-Based Verb Grammatical Errors ⏳
Tamil verbs also change based on the tense (past, present, future). The tool detects errors related to incorrect tense usage, such as using a past tense verb when a present tense verb is needed.

---

We hope this tool makes a significant contribution to improving the quality of Tamil text across digital platforms! ✨
