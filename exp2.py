import re

text = '''
    Hello everyone, Myself Meet 505! My contact details are: meetvsatra@gmail.com,
80828 00009. @#!$@%#4 a book is a better friend. U.S. is a country.
'''
# Convert text into lower case
# Remove numbers
# Remove punctuation marks
# Remove white space

# Task 1: Convert text into lower case
text = text.lower()
print("Text To Lower:")
print(text)


# Task 2: Remove numbers
text = re.sub(r'\d+', '', text) # \d+ means digit sequence, it removes digit sequence at once 5264
print("Removing Numbers:")
print(text)

# Task 3: Remove punctuation marks
text = re.sub(r'[^\w\s.]', '', text) #[^\w\s] matches any character that is not a word character or a whitespace character
print("Remove punctuations:")
print(text)

# Task 4: Remove white space
text = text.strip()
print("Remove white space:")
print(text)

# Task 5: Perform word tokenization
words = re.sub(r'\.', '', text).split()
# words = text.split()

# Task 6: Perform sentence tokenization
# sentences = text.split('.')
sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
# (?<!\w\.\w.) U.S.
# (?<![A-Z][a-z]\.) Dr.

# Task 7: Define a list of stop words
stop_words = set(['a', 'an', 'the', 'is', 'in', 'and', 'to', 'for', 'of'])

# Task 8: Remove stop words
filtered_words = [word for word in words if word not in stop_words]

# Displaying the results
# print("Text after preprocessing:")
# print(text)
print("\nWord Tokens:")
print(words)
print("\nSentence Tokens:")
print(sentences)
print("\nWord Tokens after removing stop words:")
print(filtered_words)


# Output:
# Text To Lower:
#     hello everyone, myself meet 505! my contact details are: meetvsatra@gmail.com,
# 80828 00009. @#!$@%#4 a book is a better friend. u.s. is a country.

# Removing Numbers:
#     hello everyone, myself meet ! my contact details are: meetvsatra@gmail.com,
#  . @#!$@%# a book is a better friend. u.s. is a country.

# Remove punctuations:
#     hello everyone myself meet  my contact details are meetvsatragmail.com
#  .  a book is a better friend. u.s. is a country.

# Remove white space:
# hello everyone myself meet  my contact details are meetvsatragmail.com
#  .  a book is a better friend. u.s. is a country.

# Word Tokens:
# ['hello', 'everyone', 'myself', 'meet', 'my', 'contact', 'details', 'are', 'meetvsatragmailcom', 'a', 'book', 'is', 'a', 'better', 'friend', 'us', 'is', 'a', 'country']

# Sentence Tokens:
# ['hello everyone myself meet  my contact details are meetvsatragmail.com\n .', ' a book is a better friend.', 'u.s. is a country.']

# Word Tokens after removing stop words:
# ['hello', 'everyone', 'myself', 'meet', 'my', 'contact', 'details', 'are', 'meetvsatragmailcom', 'book', 'better', 'friend', 'us', 'country']