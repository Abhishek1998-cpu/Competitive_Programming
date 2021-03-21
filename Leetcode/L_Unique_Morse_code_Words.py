# Unique Morse Code Words
# ord("a") gives the ASCII Code of a

class Solution:
    def uniqueMorseRepresentations(self, words):
        morseCode = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                     "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        transform = []
        for word in words:
            morse = ""
            for char in word:
                # print(j)
                morse += morseCode[ord(char) - 97]
            transform.append(morse)
        return len(list(set(transform)))


X = Solution()
print(X.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
