import nltk

# Download the averaged perceptron tagger data
nltk.download('averaged_perceptron_tagger')

# Get the sentence from the user
sentence = input("Enter a sentence: ")

# Tokenize the sentence
words = nltk.word_tokenize(sentence)

# Use NLTK's pos_tag function to tag words
tagged_words = nltk.pos_tag(words)

# Print the tagged words
for word, pos in tagged_words:
    print(f"{word}: {pos}")