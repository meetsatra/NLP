import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import string

# Read the text
text = '''
    Hello everyone, Myself Meet 505! My contact details are: meetvsatra@gmail.com,
80828 00009. @#!$@%#4 a book is a better friend. U.S. is a country.
'''

# Task 1: Convert text into lower case
text = text.lower()

# Task 2: Remove numbers
text = ''.join([i for i in text if not i.isdigit()])

# Task 3: Perform sentence tokenization using NLTK's punkt tokenizer
sentences = sent_tokenize(text)

# Task 4: Remove punctuation marks
text = text.translate(str.maketrans('', '', string.punctuation))

# Task 5: Remove white space
text = text.strip()

# Task 6: Perform word tokenization
words = word_tokenize(text)

# Task 7: Define a list of stop words using NLTK
stop_words = set(stopwords.words('english'))

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


# Output:
# Text after preprocessing:
# hello everyone myself meet  my contact details are meetvsatragmailcom
#    a book is a better friend us is a country

# Word Tokens:
# ['hello', 'everyone', 'myself', 'meet', 'my', 'contact', 'details', 'are', 'meetvsatragmailcom', 'a', 'book', 'is', 'a', 'better', 'friend', 'us', 'is', 'a', 'country']

# Sentence Tokens:
# ['\n    hello everyone, myself meet !', 'my contact details are: meetvsatra@gmail.com,\n .', '@#!$@%# a book is a better friend.', 'u.s. is a country.']

# Word Tokens after removing stop words:
# ['hello', 'everyone', 'meet', 'contact', 'details', 'meetvsatragmailcom', 'book', 'better', 'friend', 'us', 'country']   