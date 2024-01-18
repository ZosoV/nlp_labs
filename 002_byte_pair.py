# 1. What is tokenization in the context of natural language processing?
# It's the process of splitting a corpus of text into tokens. A token can be any different
# basic unit for understanding a language such as words, only chars, or stems.
# ------------------------------------

# 2. Explain Byte Pair Encoding with an example.
# Vocabulary: _, d, e, i, l, n, o, r, s, t, w
# 
# 5 l o w _
# 2 l o w e s t _
# 6 n e w e r _
# 3 w i d e r _
# 2 n e w _

# 1. Segment the words in different chars and add the unique chars to a vocabulary
#    Add the additional underscore char
# 2. Look for every pair of characters and count the frequency of unique pairs
# 3. The pair with most frequency is added to the vocabulary (NOTE: there can be some ties)
# 4. All the pairs in the words are grouped together as a single char

# ------------------------------------

# 3. Create a basic Byte Pair Encoding algorithm in Python that will work with a test
# corpus.

import re
from collections import Counter

def byte_pair_encoding(corpus, k):

    # Let's convert everything to lower case
    corpus = corpus.lower()

    # 1. Find the unique char of the vocabulary 
    vocabulary = ["_"] + list(set(re.findall(r'[A-Za-z]', corpus)))

    # 2. Split in words -> count -> split chars -> add underscore
    corpus = re.findall(r'[A-Za-z]+', corpus)
    corpus = Counter(corpus)
    words = [ list(word) + ["_"] for word, freq in corpus.items() ]
    frequencies = [ freq for word, freq in corpus.items() ]
    print(words, frequencies)

    # 3. get most frequent
    def get_most_frequent():
        
        hashmap = {}

        for word_idx, word in enumerate(words):
            for i in range(len(word)-1):
                charL, charR = word[i], word[i+1]

                if (charL, charR) in hashmap:
                    hashmap[(charL, charR)] += frequencies[word_idx]
                else:
                    hashmap[(charL, charR)] = frequencies[word_idx]

        max_freq = 0
        max_pair = None
        for pair, freq in hashmap:

            if freq > max_freq:
                max_freq = freq
                max_pair = pair
        
        return max_pair

    # 4. replace_ocurrances
    # NOTE: checked a better way to do it
    def replace_ocurrances(best_pair, words):

        for word_idx, word in enumerate(words):
            tmp_word = []
            i = 0
            while i < len(word-1):
                charL, charR = word[i], word[i+1]
                if (charL, charR) == best_pair:
                    tmp_word.append(charL + charR)
                    i += 1
                else:
                    tmp_word.append(charL)
                
                i += 1

            tmp_word.append(charR)
            words[word_idx] = tmp_word
        
                


    # k maximum merges
    for i in range(k):
        charL, charR = get_most_frequent()
        new_char = charL + charR
        vocabulary.append(new_char)
        replace_ocurrances(best_pair)

    return vocabulary


corpus = '''First of all, let us understand what all these parameters mean:
pattern: The regular expression you want to search and find inside the given 
string in Python. 
string: The variable that contains the given string on which you want to 
perform the operation.
count: If the pattern occurs multiple times in the string, the number of 
times you want to you want it to be replaced. The default value is 0. It is optional.
flags: The regex flags are optional.
'''

def replace_ocurrances(best_pair, words):

    for word_idx, word in enumerate(words):
        tmp_word = []
        i = 0
        while i < len(word) - 1:
            charL, charR = word[i], word[i+1]
            if (charL, charR) == best_pair:
                tmp_word.append(charL + charR)
                i += 1
            else:
                tmp_word.append(charL)
            
            i += 1

        # TODO: change with a function to don't consider the underscore

        tmp_word.append(charR)
        words[word_idx] = tmp_word

    return words
        

# print(byte_pair_encoding(corpus, k = 1))
words = [["l",'o',"w", "_"], ["l", "o", "w", "e", "s", "t", "_"], ["n", "e", "w", "er", "_"], ["w", "i", "d", "er", "_"],["n","e","w","_"]]
print(words)
print(replace_ocurrances( ("er","_"), words))

# print(re.sub("([A-Z])", lambda x: x.group(1).lower(), corpus))

# ------------------------------------

# 4. What is the minimum edit distance and its significance in NLP?
# 5. Compute the edit distance (using insertion cost 1, deletion cost 1, substitution cost
# 1) of leda to deal. Show your work (using the edit distance grid).
# 6. Figure out whether drive is closer to brief or to divers and what the edit distance is
# to each. Use Levehnstein distance.
# 7. Now implement a minimum edit distance algorithm and use your hand-computed
# results to check your code