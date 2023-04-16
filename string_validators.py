"""
Python has built-in string validation methods for basic data.
It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc

Task:
You are given a string S .
Your task is to find out if the string S contains:
alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format:
A single line containing a string S.

Output Format:
In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S has any alphabetical characters. Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.

Sample Input:
qA2

Sample Output:
True
True
True
True
True
"""

if __name__ == '__main__':
    s = input()
    return_dict = {
        'isalnum': False,
        'isalpha': False,
        'isdigit': False,
        'islower': False,
        'isupper': False,
    }
    for i in s:
        if i.isalnum():
            return_dict['isalnum'] = True
        if i.isalpha():
            return_dict['isalpha'] = True
        if i.isdigit():
            return_dict['isdigit'] = True
        if i.islower():
            return_dict['islower'] = True
        if i.isupper():
            return_dict['isupper'] = True

    for k, v in return_dict.items():
        print(f'{v}')
