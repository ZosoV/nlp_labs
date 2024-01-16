import re

# NOTE: re.findall() returns all non-overlapping occurrences of the pattern 
# in the input string as a list of strings (or tuples of strings if there are 
# capturing groups), and it continues searching for all matches throughout the entire string

# Question 1: Write regular expressions for the following languages.

# 1. The set of all alphabetic strings
pattern = r"\b[A-Za-z]+\b" # only words
# pattern = r"[A-Za-z]" # chars in general
corpus = "Hola soya b Oscar 788851 Perro TT45$%$^ abe67 "

matches = re.findall(pattern, corpus)
print("Q1.1", matches)
# ------------------------------------------------

# 2. The set of all lowercase alphabetic strings ending in a b.
# NOTE: I don't know if I have to use + or *
pattern = r"\b[a-z]*[b$]\b" # only words
corpus = "Hola soyab b Oscar 788851 perrob TT45$%$^ abe67b "

matches = re.findall(pattern, corpus)
print("Q1.2", matches)
# ------------------------------------------------

# 3. The set of all strings from the alphabet a,b such that each a is immediately
# preceded and followed by a b. bab

pattern = r"[ab]*bab[ab]*" 
corpus = "aababaa aabaa bab abaaaba osadbabakj" 

matches = re.findall(pattern, corpus)
print("Q1.3", matches)
# ------------------------------------------------

# Question 2Write regular expressions for the following languages. By “word”, we mean an 
# alphabetic string separated from other words by whitespace, any relevant punctuation,
# line breaks, and so forth.
# 1. The set of all strings with two consecutive repeated words (e.g., “Humbert
# Humbert” and “the the” but not “the bug” or “the big bug”). You may use \s
# to match a whitespace character to make things clear

pattern = r"\b([A-Za-z]+)\s\1\b" 
corpus = "Hola soyab b Oscarb Oscarb 788851 perrob perrob TT45$%$^ abe67b "

matches = re.findall(pattern, corpus)
print("Q2.1", matches)
# ------------------------------------------------


# 2. All strings that start at the beginning of the line with an integer and that end
# at the end of the line with a word. You may use \b to match the empty string,
# but only when it is not at the beginning or end of a word.

# NOTE: the thing is here I'm trying to find all the matching in a string 
# I think that the problem require me to only check in separate string
pattern = r"[0-9]+\b.*\b[A-Za-z]+\b"
corpus = "Hola soyab b Oscarb Oscarb 788851 perrob perrob TT45$%$^ ab77eb"

matches = re.findall(pattern, corpus)
print("Q2.2", matches)

# Seperate string version

pattern = r"^[0-9]+\b.*\b[A-Za-z]+$"

corpus = "3000 dias de Da Pawn grupo ecuatoriano"
matched = re.match(pattern, corpus)
print("Q2.2", corpus, True if matched else False)

corpus = "3000 dias de Da Pawn grupo ecuato89hh"
matched = re.match(pattern, corpus)
print("Q2.2", corpus, True if matched else False)

# ------------------------------------------------

# 3. All strings that have both the word grotto and the word raven in them (but
# not, e.g., words like grottos that merely contain the word grotto).

# pattern = r".*(=?\bgrotto\b)+.*(=?\braven\b)+.*|.*(=?\braven\b)+.*(=?\bgrotto\b)+.*"
pattern = r'.*\bgrotto\b.*\braven\b.*|.*\braven\b.*\bgrotto\b.*'

corpus = "Hola soy Oscar, grotto es una palabra y raven tambien"
matched = re.match(pattern, corpus)
print("Q2.3", corpus, True if matched else False)

corpus = "Hola soy Oscar, raven es una palabra y grotto tambien"
matched = re.match(pattern, corpus)
print("Q2.3", corpus, True if matched else False)

corpus = "Hola soy Oscar, grotto es una palabra"
matched = re.match(pattern, corpus)
print("Q2.3", corpus, True if matched else False)

corpus = "Hola soy Oscar, raven es una palabra"
matched = re.match(pattern, corpus)
print("Q2.3", corpus, True if matched else False)

corpus = "Hola soy Oscar, grottos no esta permitido una palabra y raven tambien"
matched = re.match(pattern, corpus)
print("Q2.3", corpus, True if matched else False)


# ---------------------------------
# 4. Write a pattern that places the first word of an English sentence in a register.
# Elegantly deal with punctuation
pattern = r'^([A-Za-z]+)\b.*'
corpus = "Hola soy Oscar, grottos no esta permitido una palabra y raven tambien"
matched = re.match(pattern, corpus)
print("Q2.4", corpus, True if matched else False)
if matched:
    first_word = matched.group(1)
    print("First Register:", first_word)
else:
    print("No match found.")


# ----------------------------------
# Implement an ELIZA-like program, using substitutions such as those described on
# page 10. You might want to choose a different domain than a Rogerian psychologist,
# although keep in mind that you would need a domain in which your program can
# legitimately engage in a lot of simple repetition.
