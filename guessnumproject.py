logo = """      _____                              _                                                 _                     _ 
  / ____|                            (_)                                               | |                   | |
 | |  __   _   _    ___   ___   ___   _   _ __     __ _     _ __    _   _   _ __ ___   | |__     ___   _ __  | |
 | | |_ | | | | |  / _ \ / __| / __| | | | '_ \   / _` |   | '_ \  | | | | | '_ ` _ \  | '_ \   / _ \ | '__| | |
 | |__| | | |_| | |  __/ \__ \ \__ \ | | | | | | | (_| |   | | | | | |_| | | | | | | | | |_) | |  __/ | |    |_|
  \_____|  \__,_|  \___| |___/ |___/ |_| |_| |_|  \__, |   |_| |_|  \__,_| |_| |_| |_| |_.__/   \___| |_|    (_)
                                                   __/ |                                                        
                                                  |___/                                                         

"""
print(logo)



from random import randint

# from art import text2art


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
# ascii_logo = text2art("guessing number!")
# print(ascii_logo)



def check_answer(guess, answer, turns):
  """ check answer againt guess. Returns the number of turns remaining.  """
  if guess > answer:
    print("Too High.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You Win ! The answer was {answer}.")

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy or 'hard':")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():


  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  #print(f"pssst, the correct answer is {answer}")

  turns = set_difficulty()

  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))

    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")

game()