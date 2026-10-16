dict1={}
print(type(dict1))   #<class 'dict'>
print(dict1)

print()

dict1["virat"]=100
dict1["sachin"]=500   #
print(dict1)    #{'virat': 100}
print()

print(dict1.get("virat"))   #100  get is function
print(dict1.items())   #dict_items([('virat', 100)])
print(dict1.keys())     #dict_keys(['virat'])
print(dict1.values())   #dict_values([100])
