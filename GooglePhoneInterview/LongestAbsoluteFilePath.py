"""
643. Longest Absolute File Path
Suppose we abstract our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string

"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
"""

"""
Observe:
dir -> subdir: \n\t + directoryName
subdir -> file: \n\t\t + fileName
"""
class Solution:
    """
    @param input: an abstract file system
    @return: return the length of the longest absolute path to file
    """
    def lengthLongestPath(self, input):
        if not input: return 0

        longest = 0
        hash = {}
        paths = input.split('\n')

        for p in paths:
            level = 0
            is_file = False
            # print(p)
            for c in p:
                if c == '\t':
                    level += 1
                elif c == '.':
                    is_file = True
            # print('level =', level)
            # store the file {level: length} pair
            hash[level] = len(p) - level
            # print(level, ":", hash[level])
            if level > 0:
                hash[level] += hash[level - 1] # accumulate level
            # print("accumulated level = ", level, ':', hash[level])
            if is_file and hash[level] + level > longest:
                longest = hash[level] + level

        return longest




sol = Solution()
dir = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.txt";
print(sol.lengthLongestPath(dir))

