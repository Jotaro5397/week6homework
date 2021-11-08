x = ['mix', 'xyz', 'apple', 'xanadu', 'rovio']
#            0      1       2        3         4
myorder = [3, 1, 2, 0, 4]
x = [x[i] for i in myorder]
print(x)

# 2:
words = ["xxx", "aaa", "r5t6yy", "g", "wow"]

counter = 0

for items in words:
    if len(items) >= 2 and items[0] == items[-1]:
        counter += 1

print(counter)

passWord = "Secret"

counter = 3

while counter > 0:
    userGuess = input("Attempt to guess my secret password: ")
    if userGuess == passWord:
        print("Well done, you guessed the password!")
        break
    elif userGuess != passWord and counter > 1:
        print("Try Again")
        counter -= 1
    else:
        print("You Lose")
        break