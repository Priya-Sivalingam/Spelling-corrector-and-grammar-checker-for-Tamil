# Spelling Corrector and Grammar Checker for Tamil  
**Artificial Intelligence Project - EC9640**

## Introduction  
Tamil is a widely spoken language, and ensuring text quality in Tamil on digital platforms is essential. This project aims to develop an AI-based tool for:  
1. **Spelling correction**: Identifying and auto-correcting up to five spelling errors in a paragraph.  
2. **Grammar checking**: Detecting and correcting two types of grammatical errors (e.g., subject-verb agreement, contextual misuse).  

## Collaborators  
- **[member name]**  
  - Developed the spelling correction module.  
  - Conducted testing, integration, and accuracy evaluations.  
- **[member name]**  
  - Designed the grammar checking module.  
  - Researched and evaluated AI approaches for grammar correction.

 
# Tamil Grammar Corrector

This project is a Tamil grammar correction tool that implements multiple methods to detect and correct grammatical errors. The tool focuses on two types of verb grammatical errors in Tamil:
1. **Gender-based verb grammatical errors**
2. **Tense-based verb grammatical errors**

## Methods Implemented

### 1. Rule-Based Method
The rule-based method uses predefined linguistic rules to detect and correct grammatical errors in Tamil sentences. This approach works by identifying patterns in the sentence structure and applying the correct rule for error correction.

### 2. Deep Learning Method: Seq2Seq Model
This method uses an Encoder-Decoder architecture based on LSTM (Long Short-Term Memory) for sequence-to-sequence learning. The Seq2Seq model learns to map input sentences with grammatical errors to corrected output sentences, focusing on gender and tense-based verb errors.

- **Encoder**: Processes the input sentence and encodes it into a fixed-size context vector.
- **Decoder**: Generates the corrected output sentence from the context vector.

### 3. Machine Learning / NLP Method
This method utilizes machine learning techniques and natural language processing (NLP) to detect and correct grammar errors. It uses feature extraction, such as syntactic and semantic features, to classify and correct gender and tense errors.

## Types of Grammar Errors Detected

### 1. Gender-Based Verb Grammatical Errors
In Tamil, verbs change depending on the gender of the subject. This tool identifies and corrects gender-based verb errors, such as using masculine verbs with feminine subjects and vice versa.

### 2. Tense-Based Verb Grammatical Errors
Tamil verbs also change based on the tense (past, present, future). The tool detects errors related to incorrect tense usage, such as using a past tense verb when a present tense verb is needed.

