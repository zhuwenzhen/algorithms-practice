"""
637. Valid Word Abbreviation
Given a non-empty string word and an abbreviation abbr, return whether the string matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Example
Example 1:

Given s = "internationalization", abbr = "i12iz4n":
Return true.
Example 2:

Given s = "apple", abbr = "a2e":
Return false.

"""
class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """


    def validWordAbbreviation(self, word, abbr):
        import re
        abbr_list = re.split('(\d+)', abbr)

        print(abbr_list)
        for i in range(len(abbr_list)):
            print(i)

            if abbr_list[i].isdigit():
                print(i)
                t = int(abbr[i])
                i = i + t

            else:
                if word[i] == abbr_list[i]: continue
                else: return False

        return True

abbr = "i12iz4n"
word = "internationalization"

s = Solution()
print(s.validWordAbbreviation(word, abbr))

