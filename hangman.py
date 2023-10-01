from random import choice
from colorama import Fore, Back, Style
                             
def show_keyboard(correct_choices, wrong_choices):
    row1 = ['q','w','e','r','t','y','u','i','o','p']
    row2 = ['a','s','d','f','g','h','j','k','l']
    row3 = ['z','x','c','v','b','n','m']
    for ch in row1:
        if ch in wrong_choices:
            print(Fore.RED + ch + Fore.RESET, end = " ")
        elif ch in correct_choices:
            print(Fore.GREEN + ch + Fore.RESET, end = " ")
        else:
            print(ch, end=" ")
    print()
    for ch in row2:
        if ch in wrong_choices:
            print(Fore.RED + ch + Fore.RESET, end = " ")
        elif ch in correct_choices:
            print(Fore.GREEN + ch + Fore.RESET, end = " ")
        else:
            print(ch, end=" ")
    print()
    for ch in row3:
        if ch in wrong_choices:
            print(Fore.RED + ch + Fore.RESET, end = " ")
        elif ch in correct_choices:
            print(Fore.GREEN + ch + Fore.RESET, end = " ")
        else:
            print(ch, end=" ")
    print()
    print()

# Reading text file
with open("hangman_words.txt", "r") as file: # r - read, w - write, a - append
    words = file.read().splitlines()

wrong_choices = []
correct_choices = []
guesses = 10

word =  choice(words)

l = ['_'] * len(word)

while '_' in l:
    if guesses == 0:
        print(f"you lost,the word was {word}.")
        break
    
    print()
    show_keyboard(correct_choices, wrong_choices)
    inp = input("Guess a letter: ")
    if inp in word:
        correct_choices.append(inp)
        for i in range(len(word)):
            if word[i] == inp:
                l[i] = inp
        print(" ".join(l))
    else:
        wrong_choices.append(inp)
        guesses -= 1
        if guesses != 0:
            print(f"Wrong guesses, you have {guesses} guesses left")
        else:
            print("You have no guesses left.a")
        
        
        print(" ".join(l))

else:
    print()
    print("You won, Congratulations")
