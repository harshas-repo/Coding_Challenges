"""
Replace character
Problem Statement

You are given a function,

Void *ReplaceCharacter(Char str[], int n, char ch1, char ch2);

The function accepts a string ‘ str’ of length n and two characters ‘ch1’
and ‘ch2’ as its arguments.
Implement the function to modify and return the string ‘ str’ in such a way
that all occurrences of ‘ch1’ in original string are replaced by ‘ch2’.
and all occurrences of ‘ch2’ in original string are replaced by ‘ch1’.
Assumption: String Contains only lower-case alphabetical letters.

Note:

Return null if string is null.
If both characters are not present in string or both of them are same
, then return the string unchanged.
Example:

Input:
Str: hello
ch1:e
ch2:o
Output:
holle
Explanation:

'e' in original string is replaced with 'o' and 'o' in original string is
replaced with 'e', thus output is holle.


Case 1
Input (stdin)
hello e o

Output (stdout)
holle
Case 2
Input (stdin)
tamil a i

Output (stdout)
timal
"""

i = input().split()
for j in i[0]:
    if(j == i[1]):
        print(i[2], end='')
    elif(j == i[2]):
        print(i[1], end='')
    else:
        print(j, end='')
