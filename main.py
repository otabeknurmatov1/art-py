import colorama
from colorama import Fore
from art import clip
import os
import time

name = input("What is your crushes name: ")
text = f"I love you {name.capitalize()}"
for i in range(len(clip)):
    os.system('clear')
    if i < len(clip):
        print(Fore.RED + clip[i].replace('1', ' ')) 
        time.sleep(0.1)
    if i == len(clip):
        for x in text:
            print(x, end="")
            time.sleep(0.1)

print(text)