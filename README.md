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

# Tamil Grammar Corrector 🇮🇳

This project is a Tamil grammar correction tool that implements multiple methods to detect and correct grammatical errors. The tool focuses on two types of verb grammatical errors in Tamil:
1. **Gender-based verb grammatical errors** 🚻
2. **Tense-based verb grammatical errors** ⏳

## Methods Implemented 🛠️

### 1. Rule-Based Method 📜
The rule-based method uses predefined linguistic rules to detect and correct grammatical errors in Tamil sentences. This approach works by identifying patterns in the sentence structure and applying the correct rule for error correction.

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
