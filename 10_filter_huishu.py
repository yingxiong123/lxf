'''
    找出回数,2321,909
'''

# def is_palindrome(n):
#     num = str(n)
#     length = len(num)
#     middle = length // 2
#     k = 0
#     for i in range(middle):
#         if num[i] == num[length-i-1]:
#             k = k+1

#     if k == middle:
#         return True
#     else:
#         return False
        
def is_palindrome(n):
    num = str(n)
    return num == num[::-1]  # 直接利用字符串切片判断回文

print(is_palindrome(101))
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
