# Homework Python I

# 1. Да се напише циклус во кој ќе се испринтаат броевите од 50 до 100

print('Prva:\n')
for i in range(50, 101):
    print(f'{i}\n')

# 2. Да се напише циклус со кој ќе се испринтаат само парните броеви од 50 до 100
print('Vtora:\n')
for i in range(50, 101, 2):
    print(f'{i}\n')

# 3. Да се напише циклус со кој ќе се испринтаат само непарните броеви од 50 до 100
print('Tretta:\n')
for i in range(50, 101):
    if i % 2 != 0:
        print(f'{i}\n')

# 4. Да се напише циклус со кој ќе се пресмета сума на елементите од следната листа
# list1 =[10,20,30,40,50,60,70,80,90,100]
print('Cetvrta:\n')
list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
s = 0
for num in list1:
    s = s + num
print(f'Sumata na elementite na listata {list1} e {s}\n')

# 5. Бонус задача: Да се напише еден циклус со кој е потребно да се избрише секој трет
# елемент од листата. list1 =[10,20,30,40,50,60,70,80,90,100] -> 30, 60 и 90 треба да бидат
# избришани со циклус и на крајот да се испринта листата без тие елементи.
print('Petta:\n')
list5 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# indexi=[0 , 1, 2,   3, 4,  5,  6,  7,   8,  9]
print(f'Listata {list5} ima izbrisani elementi \n')
for i in range(2, 8, 2):
    print(list5.pop(i))
print(f'\nI sega ima elementi : {list5} .\n')

# 6. Да се напише циклус вo кој ќе се избришат непарните броеви од дадениот tuple.(Прво
# правиме циклус кој ќе го изминува/итерира дадениот tuple, потоа проверуваме кој број
# е непарен и на крајот правиме remove/pop на тој број)
# aTuple = (333, 444, 555, 666, 777,888)
print("Sesta:\n")
aTuple = (333, 444, 555, 666, 777, 888)
print(f'{aTuple} \n')
aList = list(aTuple)
for t in aList:
    if t % 2 != 0:
        aList.remove(t)
aTuple = tuple(aList)
print(f'{aTuple}\n')

# 7. Да се напише циклус со кој ќе се провери кој елемент од tuple-от е делив со 10.
# bTuple = (100, 10, 11, 8, 350, 9, 6, 14, 620)
bTuple = (100, 10, 11, 8, 350, 9, 6, 14, 620)
del_so_10 = []
for elem in bTuple:
    if elem % 10 == 0:
        del_so_10.append(elem)
print(f'Elementi od {bTuple} koi se dellivi so 10 se {del_so_10}.\n')

# 8. Да се напише циклус со кој ќе се испринта индексот на кој се наоѓа елементот “orange”
# cTuple = (“lemon”, “blueberry”, “strawberry”, “apple”, “orange”)
cTuple = ('lemon', 'blueberry', 'strawberry', 'apple', 'orange')
cList = list(cTuple)
for i in range(len(cList)):
    if cList[i] == 'orange':
        indeks = i
print(f'Indeksot na koj se naogja elementot "orange" od tuple {cTuple} e {indeks}.\n')

# 9. Бонус задача: Да се напише циклус со кој ќе се пресмета и испринта должина на
# првиот елемент од cTuple, односно должина на зборот “lemon”.
prv_el = list(cTuple[0])
print(f'Dolzinata na prviot element vo tuple {cTuple} odnosno elementot {cTuple[0]} e {len(prv_el)}.\n')

# 10. Од следниот dictionary да се испринтаат само вредностите за клучот (so if uslov) city:
# dict = {
# “city”: “New York”,
# “country”: “New York”,
# “population”: “”,
# “coastline”:”east”,
# }

# 11. За дадениот dict од претходната задача да се испринтаат целосните парови клуч-
# вредност.
# 12. За дадениот dict да се испринтаат само вредностите.
# 13. За дадениот dict да се испринтаат само клучевите.
# 14. Бонус задача: Да се пресмета колку пати се појавува вредноста “New York”.

# 15. За дадената листа да се најде вредноста 20 во листата и да се замени со 200.
# list1 = [5, 10, 15, 20, 25, 50, 20]
list15 = [5, 10, 15, 20, 25, 50, 20]
print(f'Vo listata {list15} go zamenuvame elementot 20 so 200 taka sto')
for i in range(len(list15)):
    if list15[i] == int('20'):
        list15[i] = 200
print(f'go imame slednoto resenie: {list15}.\n')

# 16. За дадената листа да се најде и избрише бројот 20 и да се испринта новата листа
# без бројот 20.
# list1 = [5, 20, 15, 20, 25, 50, 20]
list16: list[int] = [5, 20, 15, 20, 25, 50, 20]
print(f'Vo listata {list16} go briseme elementot 20 taka sto')
for i in range(len(list16)-2):
    if list16[i] == int('20'):
        list16.pop(i)
print(f"go imame slednoto resenie: {list16}.\n")

# 17. Бонус задача: Да се провери дали првиот и вториот елемент од оваа листа се
# деливи со 5.
# aTuple = ("orange", [10, 20, 30], (5, 15, 25))
aTuple = ("orange", [10, 20, 5, 20, 23, 1], (5, 15, 555, 25))
aLList = list(aTuple[1])+list(aTuple[2])
# indexi : lista=> (0, 1, 2, ... n-1), n = No. of elements
len1 = len(aTuple[1])
len2 = len(aTuple[2])
# dolzinata na prviot i vtoriot element od aTuple ni treba za resenieto
nova_lista = []
for num in aLList:
    if num % 5 != 0:
        fl = False
        nova_lista.append(fl)
    else:
        fl = True
        nova_lista.append(fl)
fl1 = [i for i in nova_lista[:len1]]
fl2 = [i for i in nova_lista[-len2:]]
print(f'Elementite 1 i 2 od {aTuple} se dellivi so 5:'
      f'\n element No. 1 = {aTuple[1]} : {not(False in fl1)} '
      f'\n element No. 2 = {aTuple[2]} : {not(False in fl2)}.')