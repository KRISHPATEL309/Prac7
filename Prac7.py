'''
Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character. If there are odd number of characters in the string, we ignore the middle character and check for lapindrome. For example gaga is a lapindrome, since the two halves ga and ga have the same characters with same frequency. Also, abccab, rotor and xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome. The two halves contain the same characters but their frequencies do not match. Your task is simple. Given a string, you need to tell if it is a lapindrome.
Input:
6
gaga
abcde
rotor
xyzxy
abbaab
ababc
Output:
YES
NO
YES
YES
NO
NO
'''
T = int(input())    # for taking number of inputs

string=[]
for t in range(T):
    string.append(input())

for t in range(T):
    s = str(string[t])
    l = len(s)
    # two empty strings to be concatenated
    s1,s2='',''

# Checking the string length, to divide the string in equal parts
    if(len(s)%2==0):     # IF STRING LENGTH IS EVEN
        s1=s[0:l//2]
        s2=s[l//2:]

    else: # IF THE STRING LENGTH IS ODD (it omits the middlemost character of that string)
        s1=s[:l//2]
        s2=s[(l//2)+1:]

        l1=list(s1)
        l2=list(s2)
        l1.sort()
        l2.sort()

        s1=str(l1)
        s2=str(l2)
# checking the strings and printing the required output
    if(s1==s2):
        print('YES')
    else:
        print('NO')