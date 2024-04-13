class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        remaining = []
        for char in ransomNote:
            remaining.append(char)
        wordBank = []
        for char in magazine:
            wordBank.append(char)

        for letter in remaining:
            for let in wordBank:
                if letter == let:
                    wordBank.remove(let)
                    remaining.remove(letter)
    
        return len(remaining) == 0
    

ex1_note = "a"
ex1_mag = "b"

ex2_note = "a"
ex2_mag = "ba b"

ex3_note = "aa"
ex3_mag = "ab"

ans1 = Solution().canConstruct(ex1_note, ex1_mag)
ans2 = Solution().canConstruct(ex2_note, ex2_mag)
ans3 = Solution().canConstruct(ex3_note, ex3_mag)

print(ans1)
print(ans2)
print(ans3)