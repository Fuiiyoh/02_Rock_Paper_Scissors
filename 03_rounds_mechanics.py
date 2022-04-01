# Functions used to check if input is valid
def check_rounds():
  while True:
    response = input("How many rounds: ")

    round_error = "Please typer either <Enter> or an integer that is more than 0"

    if response != "":
      try:
        response = int(response)
        
        if response <1:
          print(round_error)
          continue

      except ValueError:
        print(round_error)
        continue

    return response

# Main routine goes here...
rounds_played = 0
choose_instruction = "Please choose rock (r), paper (p) or scissors (s): "

# Asks user for # of rounds, <Enter> for infinite rounds
rounds = check_rounds()

end_game = "no"
while end_game == "no":
  
  # Start of the Game Play loop
  # Rounds heading
  print()
  if rounds == "":
    heading = "Continous mode: Round {}".format(rounds_played + 1)
  else:
    heading = "Round {} of {}".format(rounds_played + 1, rounds)

  print(heading)
  choose = input("{} or 'xxx' to end: ".format(choose_instruction))

  # End game if exit code is typed
  if choose == "xxx":
    break

  # Rest of the loop / game
  print("You chose {}".format(choose))

  rounds_played += 1

print("Thank you for playing")