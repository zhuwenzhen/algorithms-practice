

class Solution:
    def breakInput(self, input):
        if not input:
            return []
        chars = list(input)
        res = []
        word = []

        print(chars)

        for c in chars:
            if c == " ":
                res.append(word)
                word = []
            elif c == "\"":
                word.append(c)
                word = []
            else:
                word.append9`(c)

        return ["".join(r) for r in res]


input = "this is \"three tokens\""

s = Solution()
print(s.breakInput(input))