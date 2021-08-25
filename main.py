#
# # a flag used in the cycle must be defined INSIDE the cycle !!!
#
# for i in range(1, 50):
#     a1 = False
#     a2 = False
#     if i % 3 == 0:
#         print(f'{i} Fizz')
#         a1 = True
#     if i % 5 == 0:
#         print(f'{i} Buzz')
#         a2 = True
#     if a1 and a2:
#         print(f'{i} fizzbuzz')


# bukvi = ['a', 'b', 'c', 'd', 'e', 'f']
# vowels = ['a', 'e', 'i', 'o', 'u']
# for word in bukvi:
#     if word in vowels:
#         print('Samoglaska')
#     else:
#         print('Soglaska')

# # while => define value of i BEFORE while and INCREASE the value of i inside the cycle
# i = 1
# while i < 11:
#     print(i**2)
#     i += 1

# i = 1
# s = 0
# while i < 11:
#     if i % 2 == 0:
#         # break
#         # continue => going back to the beginning of the while cycle
#         s = s + i
#     i += 1
# print(f'Sumata e {s}\n')

# 1. Да се напише циклус во кој ќе се испринтаат броевите од 50 до 100
for i in range(50, 101):
    print(f'{i}\n')

# 2. Да се напише циклус со кој ќе се испринтаат само парните броеви од 50 до 100
for i in range(50, 101, 2):
    print(f'{i}\n')

# 3. Да се напише циклус со кој ќе се испринтаат само непарните броеви од 50 до 100
for i in range(50, 101):
    if i % 2 != 0:
        print(f'{i}\n')

# 4. Да се напише циклус со кој ќе се пресмета сума на елементите од следната листа
# list1 =[10,20,30,40,50,60,70,80,90,100]
list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
s = 0
for num in list1:
    s = s + num
print(f'Sumata na elementite na listata {list1} e {s}\n')

# 5. Бонус задача: Да се напише еден циклус со кој е потребно да се избрише секој трет
# елемент од листата. list1 =[10,20,30,40,50,60,70,80,90,100] -> 30, 60 и 90 треба да бидат
# избришани со циклус и на крајот да се испринта листата без тие елементи.
list5 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# indexi=[0 , 1, 2,   3, 4,  5,  6,  7,   8,  9]
print(f'Listata {list5} ima izbrisani elementi \n')
for i in range(2, len(list5), 2):
    print(list5.pop(i))

