words = ["Python", "Cobol", "C++", "Java", "Visual Studio", "MySQL"]
print(words)
import random
length = len(words)- 1
a= random.randint(0,length)
while 1:
    guess = input()
    if guess == words[a]:
        print("correct")
        break
    else:
        print("You are wrong")
