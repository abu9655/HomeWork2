# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
print("Введите  количество монет")
n = int(input())
count=count1 =0
for i in range(1,n+1):
    print(f"Введите с какой стороной лежит монета №{i} : Ели решкой - 0,ели гербом - 1")
    n1 = int(input())    
    if n1==1:
        count+=1
    else:
        count1+=1
print(" ")
if count>count1:
    print(count1)
else:
    print(count)    


