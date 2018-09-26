"""
1017. Similar RGB Color
In the following, every capital letter represents some hexadecimal digit from 0 to f.

The red-green-blue color "#AABBCC" can be written as "#ABC" in shorthand.
For example, "#15c" is shorthand for the color "#1155cc".

Now, say the similarity between two colors "#ABCDEF" and "#UVWXYZ"
is -(AB - UV)^2 - (CD - WX)^2 - (EF - YZ)^2.

Given the color "#ABCDEF", return a 7 character color that is most similar to #ABCDEF,
and has a shorthand (that is, it can be represented as some "#XYZ")

Example
Input: color = "#09f166"
Output: "#11ee66"
Explanation:
The similarity is -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2 = -64 -9 -0 = -73.
This is the highest among any shorthand color.

"""
