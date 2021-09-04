# Homework Python I

# 1. Да се напише циклус во кој ќе се испринтаат броевите од 50 до 100
print('\nNo.1: Broevi od 50 do 100:\n')
for i in range(50, 101):
    print(i)

# 2. Да се напише циклус со кој ќе се испринтаат само парните броеви од 50 до 100
print('\nNo.2: Parni broevi od 50 do 100:\n')
for i in range(50, 101, 2):
    print(i)

# 3. Да се напише циклус со кој ќе се испринтаат само непарните броеви од 50 до 100
print('\nNo.3: Neparni broevi od 50 do 100:\n')
for i in range(50, 101):
    if i % 2 != 0:
        print(i)

# 4. Да се напише циклус со кој ќе се пресмета сума на елементите од следната листа
# list1 =[10,20,30,40,50,60,70,80,90,100]
print('\nNo.4:\n')
# list4 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list4 = [i for i in range(10, 110, 10)]
s = 0
for num in list4:
    s = s + num
print(f'Sumata na elementite na listata {list4} e {s}.')

# 5. Бонус задача: Да се напише еден циклус со кој е потребно да се избрише секој трет
# елемент од листата. list1 =[10,20,30,40,50,60,70,80,90,100] -> 30, 60 и 90 треба да бидат
# избришани со циклус и на крајот да се испринта листата без тие елементи.
print('\nNo.5:\n')
# list5 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list5 = [i for i in range(10, 110, 10)]
# indexi=[0 , 1, 2, ... 9] => [0, 1, 2, ... n-1], n = No. elements of a list
print(f'Listata {list5} ima izbrisani elementi \n')
for i in range(2, 8, 2):
    print(list5.pop(i))
print(f'\nI sega ima elementi : {list5}.')

# 6. Да се напише циклус вo кој ќе се избришат непарните броеви од дадениот tuple.(Прво
# правиме циклус кој ќе го изминува/итерира дадениот tuple, потоа проверуваме кој број
# е непарен и на крајот правиме remove/pop на тој број)
# aTuple = (333, 444, 555, 666, 777,888)
print("\nNo.6:\n")
aTuple = (333, 444, 555, 666, 777, 888)
aList = list(aTuple)
for t in aList:
    if t % 2 != 0:
        aList.remove(t)
aTuple1 = tuple(aList)
print(f'Od {aTuple} gi briseme neparnite broevi taka sto go imame noviot tuple {aTuple1}.')

# 7. Да се напише циклус со кој ќе се провери кој елемент од tuple-от е делив со 10.
# bTuple = (100, 10, 11, 8, 350, 9, 6, 14, 620)
print('\nNo.7:\n')
bTuple = (100, 10, 11, 8, 350, 9, 6, 14, 620)
del_so_10 = []
for elem in bTuple:
    if elem % 10 == 0:
        del_so_10.append(elem)
print(f'Elementi od {bTuple} koi se dellivi so 10 se {del_so_10}.')

# 8. Да се напише циклус со кој ќе се испринта индексот на кој се наоѓа елементот “orange”
# cTuple = (“lemon”, “blueberry”, “strawberry”, “apple”, “orange”)
print('\nNo.8:\n')
cTuple = ('lemon', 'blueberry', 'strawberry', 'apple', 'orange')
cList = list(cTuple)
ind = 0
for i in range(len(cList)):
    if cList[i] == 'orange':
        ind = i
print(f'Indeksot na koj se naogja elementot "orange" od tuple {cTuple} e {ind}.')

# 9. Бонус задача: Да се напише циклус со кој ќе се пресмета и испринта должина на
# првиот елемент од cTuple, односно должина на зборот “lemon”.
print('\nNo.9:\n')
prv_el = list(cTuple[1])
print(f'Dolzinata na prviot element vo tuple {cTuple} odnosno elementot {cTuple[1]} e {len(prv_el)}.')

# 10. Од следниот dictionary да се испринтаат само вредностите за клучот (so if uslov) city:
# dict = {
# “city”: “New York”,
# “country”: “New York”,
# “population”: “”,
# “coastline”:”east”,
# }
print('No. 10:\n')
dict = {'city': 'New York', 'country': 'New York', 'population': '', 'coastline': 'east'}
for k in dict.keys():
    if k == 'city':
        print(f"""Vrednosta za klucot "city" vo {dict} e {dict.get('city')}""")

# 11. За дадениот dict од претходната задача да се испринтаат целосните парови клуч-
# вредност.
print(f'\nNo. 11: Celosnite parovi key - value za {dict} se:\n')
for k, v in dict.items():
    print(f'Key: {k}, Value: {v}')

# 12. За дадениот dict да се испринтаат само вредностите.
print(f'\nNo. 12: Vrednostite vo {dict} se:\n')
for val in dict.values():
    print(f'Value: {val}')

# 13. За дадениот dict да се испринтаат само клучевите.
print(f'\nNo. 13: Keys vo {dict} se:\n')
for k in dict.keys():
    print(f"Key: {k}")

# 14. Бонус задача: Да се пресмета колку пати се појавува вредноста “New York”.
print('\nNo. 14:\n')
n = []
for v in dict.values():
    if v == 'New York':
        n.append(v)
print(f'Vrednosta "New York" vo dictionary {dict} se javuva {len(n)} pati.')

# 15. За дадената листа да се најде вредноста 20 во листата и да се замени со 200.
# list1 = [5, 10, 15, 20, 25, 50, 20]
print('\nNo.15:\n')
list15 = [5, 10, 15, 20, 25, 50, 20]
print(f'Vo listata {list15} go zamenuvame elementot 20 so 200 taka sto')
for i in range(len(list15)):
    if list15[i] == int('20'):
        list15[i] = 200
print(f'go imame slednoto resenie: {list15}.')

# 16. За дадената листа да се најде и избрише бројот 20 и да се испринта новата листа
# без бројот 20.
# list1 = [5, 20, 15, 20, 25, 50, 20]
print('\nNo.16:\n')
list16 = [5, 20, 15, 20, 25, 50, 20]
print(f'Vo listata {list16} go briseme elementot 20 taka sto')
for e in list16:
    if e == 20:
        list16.remove(e)
print(f"go imame slednoto resenie: {list16}.")

# 17. Бонус задача: Да се провери дали првиот и вториот елемент од оваа листа се
# деливи со 5.
# aTuple = ("orange", [10, 20, 30], (5, 15, 25))
print('\nNo.17:\n')
aTuple = ("orange", [10, 20, 30], (5, 15, 25))
aLList = list(aTuple[1])+list(aTuple[2])
len1 = len(aTuple[1])
len2 = len(aTuple[2])
nova_lista = []
for num in aLList:
    if num % 5 != 0:
        nova_lista.append(False)
    else:
        nova_lista.append(True)
print(f'Elementite 1 i 2 od {aTuple} se dellivi so 5:'
      f'\n element No. 1 = {aTuple[1]} : {not(False in nova_lista[:len1])} '
      f'\n element No. 2 = {aTuple[2]} : {not(False in nova_lista[-len2:])}.')