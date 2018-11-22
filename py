import random    

secret_number = random.randint(0, 100)
guess = -1
counter = 0
while secret_number != guess and counter < 10:
    guess = int(input("Enter a number: "))
    if 0 <= guess <= 100:
      if guess < secret_number:
        print("Your guess is low.")
      elif guess > secret_number:
          print("Your guess is high.")
      else:
          print("You guessed right!")
          break
      counter +=1
    else:
      print("Oops! Use a number between 0 and 100.")

if counter == 10:
  print("You lost. The right answer was", secret_number,". Better luck next time!")
