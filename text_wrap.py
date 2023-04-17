"""
You are given a string and width .
Your task is to wrap the string into a paragraph of width .

Function Description:
Complete the wrap function in the editor below.
wrap has the following parameters:

   1) string string: a long string
   2) int max_width: the width to wrap to

Returns:
-- string: a single string with newline characters ('\n') where the breaks should be

Input Format:
The first line contains a string.
The second line contains the width, max_width.

Constraints:
0 < len(string) < 1000
0 < max_width < len(string)

Sample Input:
string = ABCDEFGHIJKLIMNOQRSTUVWXYZ
max_width = 4

Sample Output:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""
import textwrap


def wrap(string, max_width):
    return textwrap.fill(string, max_width)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
