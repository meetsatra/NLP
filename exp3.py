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
text1 = "car racing quickly better lesser"
text = ['car', 'racing', 'quickly', 'better', 'lesser']

# Porter Stemmer
ps = PorterStemmer()
porter_stemmed_words = [ps.stem(word) for word in text]
print("Porter Stemmer:")
print(porter_stemmed_words)

# Snowball Stemmer (aka Porter2 Stemmer)
snowball_stemmer = SnowballStemmer("english")
snowball_stemmed_words = [snowball_stemmer.stem(word) for word in text]
print("\nSnowball Stemmer:")
print(snowball_stemmed_words)

# Lancaster Stemmer
lancaster_stemmer = LancasterStemmer()
lancaster_stemmed_words = [lancaster_stemmer.stem(word) for word in text]
print("\nLancaster Stemmer:")
print(lancaster_stemmed_words)

# Regex Stemmer
pattern = r"(ing|ed|es|s)$"
regex_stemmer = RegexpStemmer(pattern)
regex_stemmed_words = [regex_stemmer.stem(word) for word in text]
print("\nRegex Stemmer:")
print(regex_stemmed_words)

# Lemmatization
lemmatizer = WordNetLemmatizer()
# lemmatized_words = [lemmatizer.lemmatize(word) for word in nltk.word_tokenize(text)]
lemmatized_words = [lemmatizer.lemmatize(word) for word in text]
print("\nLemmatization:")
print(lemmatized_words)

# upload an excel table for output