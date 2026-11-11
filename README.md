# Ohm's Law & Power Calculator

## What it does
This Python program calculates Voltage, Current, Resistance, or Power based on known electrical parameters entered by the user. It features input validation to prevent errors like division by zero or non-numeric inputs, running continuously in an interactive loop until the user chooses to exit.

## How to run it
Install Python 3, then run:
```bash
python ohms_law_cli.py
```

## Sample output
```text
=========================================
 MAIN MENU 
=========================================
1. Ohm's Law & Power Calculator
2. View 20 Related Electrical Formulas
3. Quit
Select an option (1-3): 1

--- Ohm's Law & Power Calculator ---
What would you like to calculate?
1. Voltage (V)
2. Current (I)
3. Resistance (R)
4. Power (P)
Enter choice (1-4): 1

Choose known parameters:
a. Current (I) and Resistance (R)  [V = I * R]
b. Power (P) and Current (I)     [V = P / I]
c. Power (P) and Resistance (R)  [V = sqrt(P * R)]
Select (a/b/c): a
Enter Current (I in Amperes): 2
Enter Resistance (R in Ohms): 10

Result: Voltage (V) = 20.0000 V
```

## My own twist
I included 20 mathematical formulas related to voltage, power, current, and circuits for quick reference.

## What I learned
1. I learnt how to structure program logic, use proper indentation, and correct syntax.
2. The project helped me learn how important accuracy is in coding.