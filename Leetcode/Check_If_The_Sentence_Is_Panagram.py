# Check if the sentence is Pangram
# Pangram - A pangram is a sentence where every letter of the English alphabet appears at least once.

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # print(len(sentence))
        # print(set(sentence))
        if(len(sentence) >= 26):
            sentence = set(sentence)
            if(len(sentence) == 26):
                return True
        else:
            return False
