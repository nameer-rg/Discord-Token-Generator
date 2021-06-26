import random
import string
import os 
from os import system
os.system(f"title Discord Token generator by Zola nhk")
class choice():
        print("\n")
        print("how many token do you want ?")
        ch = input(f">>")
        ch = int(ch)
        
       
        os.system('clear')
        for i in range(ch):
                first = ('').join(random.choices(string.ascii_letters + string.digits, k=24))
                second = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=6))
                end = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=27))
                token = f"{first}.{second}.{end}"
                print(f"{token}")
                f = open("token.txt", "a")
                f.write(f'{token}\n')
                f.close()
        print(f'{ch} token generated !')
        os.system('pause')
