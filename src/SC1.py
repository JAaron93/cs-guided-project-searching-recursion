'''
Two words are blanagrams if they are anagrams but exactly one letter has been substituted for another.

Given two words, check if they are blanagrams of each other.

Example

For word1 = "tangram" and word2 = "anagram", the output should be
checkBlanagrams(word1, word2) = true;

After changing the first letter 't' to 'a' in the word1, the words become anagrams.

For word1 = "tangram" and word2 = "pangram", the output should be
checkBlanagrams(word1, word2) = true.

Since a word is an anagram of itself (a so-called trivial anagram), we are not obliged to rearrange letters. Only the substitution of a single letter is required for a word to be a blanagram, and here 't' is changed to 'p'.

For word1 = "aba" and word2 = "bab", the output should be
checkBlanagrams(word1, word2) = true.

You can take the first letter 'a' of word1 and change it to 'b', obtaining the word "bba", which is an anagram of word2 = "bab". It is also possible to change the first letter 'b' of word2 to 'a' and obtain "aab", which is an anagram of word1 = "aba".

For word1 = "silent" and word2 = "listen", the output should be
checkBlanagrams(word1, word2) = false.

These two words are anagrams of each other, but no letter substitution was made (the trivial substitution of a letter with itself shouldn't be considered), so they are not blanagrams.
'''


def checkBlanagrams(word1, word2):
    # Tokenizing each letter for both words
    word1_split = []
    for i in word1:
        word1_split.append(i)

    word2_split = []
    for o in word2:
        word2_split.append(o)

    word1_set = len(set(word1_split))
    word2_set = len(set(word2_split))

    word1_ord = []
    word2_ord = []
    for w in word1:
        word1_ord.append(ord(w))

    for z in word2:
        word2_ord.append(ord(z))

    word1_ord_sum = sum(word1_ord)
    word2_ord_sum = sum(word2_ord)

    if (word1_set + 1) == word2_set:
        return True

    elif (word2_set - 1) == word1_set:
        return True

    # If even after the two conditional statements before this aren't satisfied, confirm whether or not the ordinal encodings of the two words are unequal. If so, they must be blanagrams
    if word1_ord_sum != word2_ord_sum:
        return True

    return False

# O(n)


'''
Provide a summary of your solution to this challenge. Describe the process that you went through during 
your attempts to solve it. What specific obstacles or difficulties did you encounter in the process of
 solving it?
'''

# Initially, I was able to solve half of the tests by tokenizing the individual letters of the strings
# before comparing the number of the unique characters of both words. In order to solve for the words
# that had the same number of unique characters, I ordinally encoded the words and set another
# conditional statement after the prior unique character statements to confirm if the encodings of both
# words were not equal. If they weren't, they had to be blanagrams, True was returned.

# I couldn't get the last three hidden tests to pass, struggled quite a bit with them. This is all I
#  could accomplish within the given time limit for this Sprint Challenge.


'''
Explain the time and space complexity of your solution. Is that the most efficient approach? If not, 
how could you improve the time and/or space complexity of your solution?
'''

# I used four for loops and three conditional statements, none of which were nested, thus my algorithm
# has a time/space complexity of O(n). Nothing but constants are present.

# If I could have done this more efficiently, I would have simply used the sorted() function to confirm
# if the two words were sorted the same way or not. This function totally slipped my mind. Regardless,
# I'm glad I was able to solve this problem in a much more complex manner. If this code was in
# production, I would refactor with sorted(). Given that this is a Sprint Challenge that includes
# written tasks asking what challenges I had, I believe the code I wrestled with the most should
# remain.
