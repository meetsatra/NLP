import nltk
from nltk import ngrams, word_tokenize
text = "NLP is my favourite subject"
# nltk.download('punkt')  
def generate_ngrams(text, n):
    tokens = word_tokenize(text)
    ngram_list = list(ngrams(tokens, n))
    return [' '.join(ngram) for ngram in ngram_list]
unigrams = generate_ngrams(text, 1)
bigrams = generate_ngrams(text, 2)
trigrams = generate_ngrams(text, 3)
print("Unigrams:", unigrams)
print("Bigrams:", bigrams)
print("Trigrams:", trigrams)