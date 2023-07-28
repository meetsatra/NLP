import re

text = '''
Natural Language Processing (NLP) is a branch of Data Science which deals
with Text data. Apart from numerical data, Text data is available to a great
extent which is used to analyze and solve business problems. But before using
the data for analysis or prediction, processing the data is important. To prepare
the text data for the model building we perform text preprocessing. It is the very
first step of NLP projects. Some of the preprocessing steps are: Removing
punctuations like . , ! $( ) * % @, Removing URLs, Removing Stop words,
Lower casing, Tokenization, Stemming, Lemmatization etc.
'''
# Convert text into lower case
# Remove numbers
# Remove punctuation marks
# Remove white space

# Task 1: Convert text into lower case
text = text.lower()

# Task 2: Remove numbers
text = re.sub(r'\d+', '', text) # \d+ means digit sequence, it removes digit sequence at once

# Task 3: Remove punctuation marks
text = re.sub(r'[^\w\s]', '', text)

# Task 4: Remove white space
text = text.strip()

# Task 5: Perform word tokenization
words = text.split()

# Task 6: Perform sentence tokenization
sentences = text.split('.')

# Task 7: Define a list of stop words
stop_words = set(['a', 'an', 'the', 'is', 'in', 'and', 'to', 'for', 'of'])

# Task 8: Remove stop words
filtered_words = [word for word in words if word not in stop_words]

# Displaying the results
print("Text after preprocessing:")
print(text)
print("\nWord Tokens:")
print(words)
print("\nSentence Tokens:")
print(sentences)
print("\nWord Tokens after removing stop words:")
print(filtered_words)
