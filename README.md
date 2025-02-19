# python-assignment-2
Having fun trying to translate my Java Assignments to Python - Part 1


## Assignment #2: Higher / Lower Guessing Game
 
### Requirements:

Your task is to create a game that allows players to try to guess a number that’s randomly chosen between 1 and 100.

When the player starts the game, a random number will be generated. This random number will be the number that the player will try to guess (so don’t tell the player what this number is).

The player will then be prompted to “Pick a number between 1 and 100”. The range from 1 to 100 is inclusive, so the number can be 1, or 100 or any number in-between. Also, you should only generate int values (don’t use floats / doubles)

If the number chosen is outside of this range, then an error message should be displayed saying “Your guess is not between 1 and 100, please try again”. Note: an invalid input should not affect the number of guesses the player has left (so do not remove a guess from the player if they enter a number outside of the 1 - 100 range)

(Don’t worry about trying to validate any input other than int values; ie. Don’t worry about decimals or words)

When the player enters a valid guess (a number between 1 and 100), the game should prompt the player with one of three messages:


1.       “Please pick a higher number” (if the number they chose is lower than the randomly generated number), or


2.       “Please pick a lower number” (if the number they chose is higher than the randomly generated number), or


3.       “You win!” (if they guess the correct number)


The player only gets 5 chances to guess the number.

If they haven’t guessed the correct number after 5 tries, then the game is over and the outputted message should read “You lose, the number to guess was theRandomNumber” (where theRandomNumber is the actual value of the variable generated at the beginning of the game)

Once the user fails to guess the number, or if they correctly guess the number, the game is over and the application ends.

Reminder: When you've completed this assignment you must submit it for review via the assignment submission app (you can use the same credentials to login there as you've used to login here)


Example Output:
```TEXT
Pick a number between 1 and 100 0

Your guess is not between 1 and 100, please try again

Pick a number between 1 and 100 101

Your guess is not between 1 and 100, please try again

Pick a number between 1 and 100 50

Please pick a lower number

Pick a number between 1 and 100 25

Please pick a lower number

Pick a number between 1 and 100 15

Please pick a higher number

Pick a number between 1 and 100 20

Please pick a lower number

Pick a number between 1 and 100 17

Please pick a higher number

You lose!

The number to guess was: 19
```
