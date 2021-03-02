# Generate your questions & answers below:
# what do I know & need?
  # generate a random number
    # [x] import the random library
  # ask the user to guess a number
    # [x] take in a interger input
  # the game should say whether the guess is close or not
    #  first what happens when its correct?
      # display that the user is correct
      # then what happens if the user is close?
        # it displays that the user is close
  # the game repeats until the user enteters the right number
import random
print('Guess a number')
print()
randNum = random.randrange(1,21)
print(randNum)
print()

userGuess = int(input('Guess a number (1-20):  '))

# loop until the right answer is guessed
while userGuess != randNum:
  if (abs(randNum - userGuess) <= 5):
    print('Your close! Keep trying!')
    print()
    userGuess = int(input('Guess a number (1-20):  '))
  elif (abs(randNum - userGuess) == 1):
    print('Your SO close! Keep trying!')
    print()
    userGuess = int(input('Guess a number (1-20):  '))
  elif userGuess == randNum:
    print('You got it dude!')
    break
  else:
    print('Your way off. Try again')
    print()
    userGuess = int(input('Guess a number (1-20):  '))