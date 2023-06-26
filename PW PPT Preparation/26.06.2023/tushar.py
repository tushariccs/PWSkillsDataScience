# # s = ["h","e","l","l","o"]
# # a = s[::-1]
# # print(a)
# s = "Hello World"
# a = s.split(' ')
# print(a)

# # b = len(a[2])
# # print(b)
# def reverseWords(s: str) -> str:
#         q = s.split()
#         str = ""
#         for i in q:
#             str+=str(s[i]).reverse()
#         return str
# b = "Hello World"
# a = reverseWords(b)
# print(a)

def reverseWords(s: str):
        a = s.split()
        print(a)
        b = str(a.reverse())
        print(b)
        print(' '.join(a))
s = "the sky is blue"
reverseWords(s)
a = ' '