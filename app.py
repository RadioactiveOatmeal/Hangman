import random

with open('words.txt', 'r') as f:
    f_content = f.readlines()
    word = f_content[random.randint(1, 1001)]

help_list = ['_' for i in range(len(word) - 1)]

print(",".join(help_list).replace(",", " "))

g = 0
win = False

while g <= 7:

    check = ",".join(help_list).replace(",", "")
    guess = str(input("Enter a letter"))

    for i, c in enumerate(word):
        if guess == c:
            del help_list[i]
            help_list.insert(i, c)
        elif guess not in word:
            print("Wrong!")
            break

    if '_' not in help_list:
        win = True
        print("You win!")

    if win is True:
        break

    g += 1

    check = ",".join(help_list).replace(",", "")
    print(",".join(help_list).replace(",", " "))

if win is False:
    print("You lose :c")
