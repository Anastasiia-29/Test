lst = []
for i in range(11):
    lst.append(i)
tpl = tuple(lst)    
print(lst)
print(type(tpl))

new_tuple = tuple(lst)
print(new_tuple)
print(lst)
