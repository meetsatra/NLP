import nltk
# nltk.download('punkt')
# nltk.download('wordnet')
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

a1= lesk(word_tokenize('This device is used to jam the signal'),'jam')
print(a1,a1.definition())
print("*"*70)
a2 = lesk(word_tokenize('I am stuck in a traffic jam'),'jam')
print(a2,a2.definition())
print("*"*70)

b1= lesk(word_tokenize('Apply spices to the chicken to season it'),'season')
print(b1,b1.definition())
print("*"*70)
b2= lesk(word_tokenize('India receives a lot of rain in the rainy season'),'season')
print(b2,b2.definition())
print("*"*70)