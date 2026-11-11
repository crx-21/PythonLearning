import random
from collections import deque

random_integer = random.randint(1,10) # random intre 1-10
random_float = random.random() * 5 # Cuprins intre 0-5 cu float

print(random_integer)
print(random_float)

flip = ""
random_flip = random.randint(1,100)
if random_flip > 50:  
   flip = "tails"
else:
   flip = "heads"

print(flip + " cu random_flip fiind: " + str(random_flip))   

lista = ["Ion", "Ana", "Marcel", "Antonio"]
lista.append("John")

print(lista[0] + " primu elem") 
print(lista[-1] + " indexare cu -1 deci printam ultimul elem") 
print(lista[1] + " al doilea elem din lista")

stringtolist = "Marcel are alune"
lista_string = stringtolist.split()
print(lista_string)

unstring = "Cristian"
print(list(unstring))   

nume = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
marime_lista = len(nume)
print(marime_lista)
random_int = random.randint(0,marime_lista-1)
print(nume[random_int] + " is going to buy the meal today!")

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
map = [row1, row2, row3]

choice = input("Where do you want to put the treasure? ")
numbers = choice.split()

row_index = int(numbers[0]) - 1
col_index = int(numbers[1]) - 1

map[col_index][row_index] = "X"

print(f"{row1}\n{row2}\n{row3}")

import random

lista_alegere = ["Piatra", "Hartie", "Foarfeca"]
print("Bun venit la piatra foarfeca hartie!")

alegere_nr = int(input("Scrie 0 ptr piatra, 1 ptr hartie, 2 ptr foarfeca: "))

if alegere_nr < 0 or alegere_nr > 2:
    print("Numar invalid! Alege 0, 1 sau 2.")
else:
    alegere_cpu = random.randint(0, 2)

    print(f"\nTu ai ales: {lista_alegere[alegere_nr]}")
    print(f"Calculatorul a ales: {lista_alegere[alegere_cpu]}\n")

    if alegere_nr == alegere_cpu:
        print("Egalitate!")
    elif (alegere_nr == 0 and alegere_cpu == 2) or \
         (alegere_nr == 1 and alegere_cpu == 0) or \
         (alegere_nr == 2 and alegere_cpu == 1):
        print("Ai castigat!")
    else:
        print("Ai pierdut!")