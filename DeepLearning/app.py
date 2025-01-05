import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# Load the trained models and tokenizers
encoder_model = tf.keras.models.load_model('D:/07_Semester/AI/project/Spelling-corrector-and-grammar-checker-for-Tamil/DeepLearning/encoder_model.h5')
decoder_model = tf.keras.models.load_model('D:/07_Semester/AI/project/Spelling-corrector-and-grammar-checker-for-Tamil/DeepLearning/decoder_model.h5')

with open('D:/07_Semester/AI/project/Spelling-corrector-and-grammar-checker-for-Tamil/DeepLearning/input_tokenizer.pkl', 'rb') as f:
    input_tokenizer = pickle.load(f)

with open('D:/07_Semester/AI/project/Spelling-corrector-and-grammar-checker-for-Tamil/DeepLearning/output_tokenizer.pkl', 'rb') as f:
    output_tokenizer = pickle.load(f)

# Define constants
max_input_length = 5  # Adjust this to the max length of input sequences in your training data
max_target_length = 5  # Adjust this to the max length of output sequences in your training data

# Function to decode sequence (similar to the one in your model)
def decode_sequence(input_seq):
    states_value = encoder_model.predict(input_seq)
    target_seq = np.zeros((1, 1))
    target_seq[0, 0] = output_tokenizer.word_index['<start>']
    stop_condition = False
    decoded_sentence = ''
    while not stop_condition:
        output_tokens, h, c = decoder_model.predict([target_seq] + states_value)
        sampled_token_index = np.argmax(output_tokens[0, -1, :])
        sampled_word = None
        for word, index in output_tokenizer.word_index.items():
            if index == sampled_token_index:
                sampled_word = word
                break
        if sampled_word == '<end>' or len(decoded_sentence.split()) > max_target_length:
            stop_condition = True
        else:
            decoded_sentence += ' ' + sampled_word
        target_seq = np.zeros((1, 1))
        target_seq[0, 0] = sampled_token_index
        states_value = [h, c]
    return decoded_sentence.strip()

# Streamlit UI
st.title("Tamil Grammar Corrector")

st.write("""
    This application allows you to input an ungrammatical Tamil sentence and get the corrected version using a Seq2Seq model.
    Simply enter a sentence, and the app will output the corrected version.
""")

input_sentence = st.text_input("Enter Ungrammatical Sentence")

if input_sentence:
    # Tokenize the input sentence
    input_seq = pad_sequences(input_tokenizer.texts_to_sequences([input_sentence]), maxlen=max_input_length, padding='post')
    
    # Get the predicted sentence from the model
    predicted_sentence = decode_sequence(input_seq)
    
    st.write(f"Predicted Correct Sentence: {predicted_sentence}")
