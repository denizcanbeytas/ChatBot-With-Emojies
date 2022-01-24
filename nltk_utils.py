import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()


def tokenize(sentence):
    """
    Array kaliplarina ayirma
    """
    return nltk.word_tokenize(sentence)


def stem(word):
    """
    En yakin kelimeleri bir array icerisine lowercase olarak atar
    """
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, words):
    """
        Bizim yazdigimiz cumledeki kelime gruplarini veri setindeki kelime array i ile karsilastirir.
        Var ise 1 koyar 
    """
    sentence_words = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag
