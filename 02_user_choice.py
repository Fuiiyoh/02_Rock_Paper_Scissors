# function goes here
def choice_checker(question, valid_list, error):
  
  valid = False
  while not valid:
    # asks user for choice
    response = input(question).lower()
    # if the amount is too low / too high
    for item in valid_list:
      if response == item[0] or response == item:
        return response
  
    print(error)
    print

# main routine goes here

# list for checking responses
rps_list = ["rock","paper","scissors","xxx"]

# loop
user_choice = ""
while user_choice != "xxx":

  user_choice = choice_checker("Choose rock / paper / scissors (or 'xxx' to quit): ", rps_list,"Choose rock / paper / scissors (or 'xxx' to quit): ")

  print("You chose {}".format(user_choice))