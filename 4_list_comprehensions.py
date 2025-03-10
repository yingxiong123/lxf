L = ['Hello', 'World', 18, 'Apple', None]

mylist=[s.lower() for s in L if isinstance(s,str)]
print(mylist)

x = [1,3,5]

list = [x*x if x % 3 ==0 else x for x in x]
print(list)