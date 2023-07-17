##https://github.com/DenisMaximum/module_4

# def is_palindrome(x):
#     p = False
#     y = ""
#
#     for i in range(len(x) - 1, -1, -1):
#         y += x[i]
#
#     if x == y:
#         p = True
#
#     return p
#
# print(is_palindrome('1234321'))

# def palindrome(s):
#      print(s[::-1] == s)
#
# while True:
#     s = input('введите слово: ')
#     palindrome(s)

def isPalindrome(s):
    print(True if s == s[::-1] else False)

isPalindrome('asdsa')
