        
# 1. Илова кардани адад ба охири лист.
# # Пример
# # Ввод: список = [1, 2, 3], число = 4
# # Выход: [1, 2, 3, 4]
# list1 = [1, 2, 3, 4]
# list1.append(5)
# print(list1)




# 3. Сложение двух чисел в списке.
# Пример
# Ввод: список = [1, 2, 3], индексы = 0, 2
# Выход: 4
# a = int(input())
# b = int(input())

# list1 = [1, 2, 3, 4]
# c = list1[a] + list1[b]
# print(c)




# 4. Доступ к значению в словаре с использованием метода get.
# Пример
# Ввод: словарь = {'a': 1, 'b': 2}, ключ = 'b'
# Выход: 2

# dict1 = {
#     "a" : 1,
#     "b" : 2,
#     "c" : 3
# }
# print(dict1.get("b"))




# БО ФУНКСИЯ СОЗЕД!!!!!1

# 2. Тағйир додани ду элементи аввал ва охирини лист.
# Пример
# Ввод: список = [1, 2, 3, 4]
# Выход: [4, 2, 3, 1]

# def rev(a):
#     a[0], a[len(a)-1] = a[len(a)-1], a[0]
#     return a
# res = rev(list(map(int,input().split())))
# print(res)
    

    
    
# БО ФУНКСИЯ СОЗЕД!!!!!1

# 3. Илова кардани калида ва арзиш ба дикт.
# Пример
# Ввод: словарь = {'a': 1, 'b': 2}, ключ = 'c', значение = 3
# Выход: {'a': 1, 'b': 2, 'c': 3}

# dict1 = {
#     "a" : 1,
#     "b" : 2,
#     "c" : 3
# }
# def dob(a,b):
#     dict1[a] = b
#     return dict1

# key = dob(input(),int(input()))
# print(key)




# БО ФУНКСИЯ СОЗЕД!!!!!1

# 4. Ёфтани максимуми лист.
# Пример
# Ввод: список = [1, 2, 3, 4]
# Выход: 4

# def maxx (num):
#     if not num:
#         return None
#     maxx = -999999
#     for i in num:
#         if i > maxx:
#             maxx = i
#     return maxx
# res = maxx(list(map(int,input().split())))
# print(res)





# 2. Объединение двух списков.
# Пример
# Ввод: список1 = [1, 2], список2 = [3, 4]
# Выход: [1, 2, 3, 4]
# list1 = [1, 2]
# list2 = [3, 4]
# list3 = []
# def num(a,b):
#     for i in a:
#         list3.append(i)
#     for j in b:
#         list3.append(j)
#     return list3
# res = num(list1,list2)
# print(res)



# dict1={
#     'a':1,
#     'b':2
# }  
# def filter(dct, num):
#     for key, value in dct.items():
#         if num==key:
#             return value
                
# num=input()
# res=filter(dic1,num)
  
# print(res)
        
    
