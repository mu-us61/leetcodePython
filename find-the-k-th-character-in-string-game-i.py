# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i
# 3304

class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        alfabe = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        changed_alfabe = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a']
        
        while len(word) < k:  # Keep growing until the length of the string is at least k
            new_word = ""
            for i in range(len(word)):
                yer = alfabe.index(word[i])
                new_word += changed_alfabe[yer]  # Create the transformed word
            
            word += new_word  # Concatenate the transformed part to the original string
            print(word)  # To see the steps of transformation
        
        return word[k - 1]  # Return the k-th character (0-indexed)
