#-*- coding:utf-8 -*-

def trim(s):
    left = 0
    right = len(s)-1
    while s[left] == ' ' and left <= right:
        left += 1

    while s[right] == ' ' and left <= right:
        right -= 1

    return s[left:right]

s='  hello  '
print(s)
print(trim(s))

print(s.strip())

arr = ["hello", "world"]
print(" ".join(arr))     # "hello world"

s = "hello world"
print(s.split())         # ['hello', 'world']
print(s.split('o'))      # ['hell', ' w', 'rld']

