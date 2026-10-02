#!/usr/bin/env python3
import time
removable = 0 

text = "Роскомнадзор запретил букву"
letter = ['а','б','в','д','е','з','и','к','л','м','н','о','п','р','с','т','у']
print("Подсказка:", letter)
while removable != "у":
    removable= input(f"{text} ")
    text=text.lower()
    text=text.replace(removable ,"*")
    if removable.lower() == "к":
        print("Хэй! Хэй! Хэй! Хэй! \n Хэй! Хэй! Хэй! Хэй! \n (Р-р-роскомнадзор!) \n Хэй! Хэй! Хэй! Хэй! n\ Хэй! Хэй! Воу!")
print("РОСКОМПОЗОР КОНТОРА ПИДОРАСОВ")