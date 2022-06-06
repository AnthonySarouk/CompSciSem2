import random
list_words = []
with open('wordle.txt') as f:
    for line in f:
        l = line.strip()
        list_words.append(l)
answer = list_words(random.randrange(2315)
a = 0
r = 6
for i in range(0,r):
    guess = input("Guess a 5 letter word: ")
    if answer == guess:
        print("You Won!")
        break
    for word in list_words:
        
        
        
        if(guess == word):
            a = a + 1
        if(a > 0):
            print("Wrong answer")
        else:
            print("invalid word, guess again")
            r = r + 1
        a = 0
print(answer)
f.close()
      
