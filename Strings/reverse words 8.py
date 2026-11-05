# uch.very.program.this.like.i".
# Input: s = "..geeks..for.geeks."
# Output: "geeks.for.geeks"
# Explanation: After removing extra dots and reversing the whole string, the input string becomes "geeks.for.geeks".
# Input: s = "..home....."
# Output: "home"
# Explanation: The input string contains only one word with extra dots around it. After removing the extra dots, the output is "home".

class Solution:
    def reverseWords(self, s):
        # code here
        words=s.split('.')#splits using dots
        words=[i for i in words if i!='']#removes empty strings from the list of words considering only words
        words.reverse()#reverse all words in the list
        return '.'.join(words)#joins the reversed words with dots and returns the final string
      