# Using NLTK library do the following
# 1. Implement porter Stemming algorithm
# 2. Implement Snowball stemmer
# 3. Implement Lancaster stemmer
# 4. Implement Regex stemmer
# 5. Implement Lemmatization


import nltk
# nltk.download('wordnet')
from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer, RegexpStemmer, WordNetLemmatizer

# Sample text for testing
text = "The quick brown foxes are jumping over the lazy dogs. They love to play and played all day."

# Porter Stemmer
porter_stemmer = PorterStemmer()
porter_stemmed_words = [porter_stemmer.stem(word) for word in nltk.word_tokenize(text)]
print("Porter Stemmer:")
print(porter_stemmed_words)

# Snowball Stemmer (also known as Porter2 Stemmer)
snowball_stemmer = SnowballStemmer("english")
snowball_stemmed_words = [snowball_stemmer.stem(word) for word in nltk.word_tokenize(text)]
print("\nSnowball Stemmer:")
print(snowball_stemmed_words)

# Lancaster Stemmer
lancaster_stemmer = LancasterStemmer()
lancaster_stemmed_words = [lancaster_stemmer.stem(word) for word in nltk.word_tokenize(text)]
print("\nLancaster Stemmer:")
print(lancaster_stemmed_words)

# Regex Stemmer
pattern = r"(ing|ed|es|s)$"
regex_stemmer = RegexpStemmer(pattern)
regex_stemmed_words = [regex_stemmer.stem(word) for word in nltk.word_tokenize(text)]
print("\nRegex Stemmer:")
print(regex_stemmed_words)

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in nltk.word_tokenize(text)]
print("\nLemmatization:")
print(lemmatized_words)

# Output:
# Porter Stemmer:
# ['the', 'quick', 'brown', 'fox', 'are', 'jump', 'over', 'the', 'lazi', 'dog', '.', 'they', 'love', 'to', 'play', 'and', 'play', 'all', 'day', '.']
# Snowball Stemmer:
# ['the', 'quick', 'brown', 'fox', 'are', 'jump', 'over', 'the', 'lazi', 'dog', '.', 'they', 'love', 'to', 'play', 'and', 'play', 'all', 'day', '.']
# Lancaster Stemmer:
# ['the', 'quick', 'brown', 'fox', 'ar', 'jump', 'ov', 'the', 'lazy', 'dog', '.', 'they', 'lov', 'to', 'play', 'and', 'play', 'al', 'day', '.']
# Regex Stemmer:
# ['The', 'quick', 'brown', 'fox', 'are', 'jump', 'over', 'the', 'lazy', 'dog', '.', 'They', 'love', 'to', 'play', 'and', 'play', 'all', 'day', '.']
# Lemmatization:
# ['The', 'quick', 'brown', 'fox', 'are', 'jumping', 'over', 'the', 'lazy', 'dog', '.', 'They', 'love', 'to', 'play', 'and', 'played', 'all', 'day', '.']