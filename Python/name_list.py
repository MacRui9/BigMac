namelist = ['yn','yw','lcx','ljw','yjy']
print(namelist)
dont_name = namelist.pop(0)#删除了第一个元素
print(f"don't come my party is {dont_name}.")
namelist.insert(0,'sqw')#替换元素
print(namelist)
namelist.insert(0,'rx')
namelist.insert(3,'cxx')
namelist.append('yq')
print(namelist)
pop_1 = namelist.pop(0)
print(f"i'm sorry don't invite to {pop_1}.")
pop_2 = namelist.pop(0)
print(f"i'm sorry don't invite to {pop_2}.")
pop_3 = namelist.pop(1)
print(f"i'm sorry don't invite to {pop_3}.")
pop_4 = namelist.pop(2)
print(f"i'm sorry don't invite to {pop_4}.")
pop_5 = namelist.pop(2)
print(f"i'm sorry don't invite to {pop_5}.")
pop_6 = namelist.pop(2)
print(f"i'm sorry don't invite to {pop_6}.")
print(f"i invite {namelist[0]} & {namelist[1]} come to my party")#list 需要使用[]来选择排序