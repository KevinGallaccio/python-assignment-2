# Assignment 2 - Higher / Lower Guessing Game in Python

## **Overview**
This project is a Python implementation of **Assignment #2** from Coders Campus, which involves creating a Higher/Lower guessing game. The original assignment was written in Java, and I translated it into Python while ensuring it maintained the same behavior.

---

## **Original Java Assignment Instructions**

### **Objective**
Create a game where the player attempts to guess a randomly generated number between 1 and 100.

### **Requirements**
1. **Generate a random number between 1 and 100** (inclusive).
2. **Prompt the player to guess a number**.
3. **Provide feedback**:
   - "Pick a higher number" if the guess is too low.
   - "Pick a lower number" if the guess is too high.
   - "You win!" if they guess correctly.
4. **Handle invalid input**:
   - If the guess is outside 1-100, display an error message and do not count it as an attempt.
   - Ignore non-integer inputs (e.g., decimals, words).
5. **Limit the player to 5 attempts**:
   - If they fail, display "You lose!" and reveal the number.
6. **End the game when the number is guessed or attempts run out.**

### **Example Output**
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

---

## **Translating This to Python**
### **Challenges & Lessons Learned**

### **1️⃣ Java’s `Scanner` vs. Python’s `input()`**
- In Java, we use `Scanner` to read user input.
- In Python, we use `input()`, which always returns a string, so it needs conversion:
  ```python
  user_input = int(input("Pick a number between 1 and 100: "))
  ```

### **2️⃣ Handling Invalid Input More Cleanly**
- In Java, we check if input is within range manually.
- In Python, we can use **try-except** blocks to handle non-integer values:
  ```python
  try:
      user_input = int(input("Pick a number: "))
  except ValueError:
      print("Invalid input. Please enter a number.")
      continue
  ```

### **3️⃣ Looping Structure & Attempt Limits**
- Java uses `for` loops with a counter.
- Python uses `while` loops more naturally:
  ```python
  attempts = 0
  while attempts < 5:
      # Game logic here
      attempts += 1
  ```

---

## **Python Implementation - `guessing_game.py`**
```python
import random

def guessing_game():
    the_random_number = random.randint(1, 100)
    max_attempts = 5
    attempts = 0

    while attempts < max_attempts:
        try:
            user_input = int(input("Pick a number between 1 and 100: "))
            if user_input < 1 or user_input > 100:
                print("Your guess is not between 1 and 100, please try again")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if user_input < the_random_number:
            print("Please pick a higher number")
        elif user_input > the_random_number:
            print("Please pick a lower number")
        else:
            print("You win!")
            return

        attempts += 1
    
    print(f"You lose! The number to guess was: {the_random_number}")

if __name__ == "__main__":
    guessing_game()
```

---

## **Conclusion**
✅ Successfully implemented a **Higher/Lower game in Python** that mimics the Java version.  
✅ Learned key differences between **Java and Python input handling**.  
✅ **Python’s `try-except` is more elegant** than Java’s manual error checking.  

**Next steps:** Improve error handling further and implement a **replay feature**! 🚀🐍

---

**🛠️ Built With:**
- Python 3
- No external libraries (pure Python implementation)

📌 **Author:** Kevin Gallaccio[https://github.com/KevinGallaccio]
📌 **Based On:** Coders Campus[https://coderscampus.com/]

🚀 **Excited for the next assignment!**

