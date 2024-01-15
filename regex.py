import re

# Question 1
# NOTE: String means a sentence?

pattern = r"\b[A-Za-z]+\b" 
corpus = "Hola soya b Oscar 788851 Perro TT45$%$^ abe67 "

matches = re.findall(pattern, corpus)
print(matches)

# 2. The set of all lowercase alphabetic strings ending in a b.
# NOTE: I don't know if I have to use + or *
pattern = r"[a-z]+[b$]" 
corpus = "Hola soyab b Oscar 788851 perrob TT45$%$^ abe67b "

matches = re.findall(pattern, corpus)
print(matches)

# 3. The set of all strings from the alphabet a,b such that each a is immediately
# preceded and followed by a b. bab

pattern = r"[ab]*bab[ab]*" 
corpus = "aababaa aabaa bab abaaaba osadbabakj" 

matches = re.findall(pattern, corpus)
print(matches)

# Question 2
# 1. The set of all strings with two consecutive repeated words (e.g., “Humbert
# Humbert” and “the the” but not “the bug” or “the big bug”). You may use \s
# to match a whitespace character to make things clear

pattern = r"\b([A-Za-z]+)\s\1\b" 
corpus = "Hola soyab b Oscarb Oscarb 788851 perrob perrob TT45$%$^ abe67b "

matches = re.findall(pattern, corpus)
print(matches)