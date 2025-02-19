import random

def guessing_game():
    the_random_number = random.randint(1, 100)
    max_number_attempts = 5
    current_number_attempts = 0

    # Uncomment this line if you want to display the random number:
    # print(the_random_number)

    while current_number_attempts < max_number_attempts:
        if current_number_attempts == 0:
            user_input = input('Pick a number between 1 and 100: ')
        else:
            print('You have', 5 - current_number_attempts, 'attempts left.')
            user_input = input('Try again: ')

        try:
            user_input = int(user_input)
            if user_input < 1 or user_input > 100:
                raise ValueError
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 100.')
            continue

        current_number_attempts += 1

        if user_input == the_random_number:
            print('Congratulations! You guessed the number correctly.')
            return

        print ('Too low' if user_input < the_random_number else 'Too High')

    print('You lose, the number to guess was: ', the_random_number)