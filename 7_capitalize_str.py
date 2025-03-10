# def normalize(name):
#     return name.capitalize()

def normalize(name):
    if not name:
        return name
    
    first=name[0].upper()
    last=name[1:].lower()
    return first+last


# 输入的名字列表
names = ['adam', 'LISA', 'barT']
# 使用 map() 函数将 normalize 函数应用到 names 列表的每个元素上
result = list(map(normalize, names))
print(result)