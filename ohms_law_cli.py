"""
Ohm's Law & Power Calculator with Formula Reference Library
This script allows users to calculate Voltage, Current, Resistance, or Power
based on known values and provides quick access to 20 electrical formulas.
"""

def get_float_input(prompt):
    """
    Prompts the user for numerical input and handles invalid entries.
    Returns a float value.
    """
    while True:
        try:
            val = float(input(prompt))
            return val
        except ValueError:
            print("Error: Invalid input. Please enter a numerical value.")

def ohms_law_calculator():
    """
    Main calculator function for Ohm's Law and Power.
    Asks the user what to calculate and handles the required math.
    """
    print("\n--- Ohm's Law & Power Calculator ---")
    print("What would you like to calculate?")
    print("1. Voltage (V)")
    print("2. Current (I)")
    print("3. Resistance (R)")
    print("4. Power (P)")
    
    choice = input("Enter choice (1-4): ").strip()
    
    # ------------------ Voltage Calculations ------------------
    if choice == '1':
        print("\nChoose known parameters:")
        print("a. Current (I) and Resistance (R)  [V = I * R]")
        print("b. Power (P) and Current (I)     [V = P / I]")
        print("c. Power (P) and Resistance (R)  [V = sqrt(P * R)]")
        sub_choice = input("Select (a/b/c): ").strip().lower()
        
        if sub_choice == 'a':
            i = get_float_input("Enter Current (I in Amperes): ")
            r = get_float_input("Enter Resistance (R in Ohms): ")
            print(f"\nResult: Voltage (V) = {i * r:.4f} V")
        elif sub_choice == 'b':
            p = get_float_input("Enter Power (P in Watts): ")
            i = get_float_input("Enter Current (I in Amperes): ")
            if i == 0:
                print("\nError: Division by zero. Current cannot be 0.")
            else:
                print(f"\nResult: Voltage (V) = {p / i:.4f} V")
        elif sub_choice == 'c':
            p = get_float_input("Enter Power (P in Watts): ")
            r = get_float_input("Enter Resistance (R in Ohms): ")
            if p * r < 0:
                print("\nError: Cannot calculate square root of a negative value.")
            else:
                print(f"\nResult: Voltage (V) = {(p * r)**0.5:.4f} V")
        else:
            print("Invalid selection.")

    # ------------------ Current Calculations ------------------
    elif choice == '2':
        print("\nChoose known parameters:")
        print("a. Voltage (V) and Resistance (R)  [I = V / R]")
        print("b. Power (P) and Voltage (V)     [I = P / V]")
        print("c. Power (P) and Resistance (R)  [I = sqrt(P / R)]")
        sub_choice = input("Select (a/b/c): ").strip().lower()
        
        if sub_choice == 'a':
            v = get_float_input("Enter Voltage (V in Volts): ")
            r = get_float_input("Enter Resistance (R in Ohms): ")
            if r == 0:
                print("\nError: Division by zero. Resistance cannot be 0.")
            else:
                print(f"\nResult: Current (I) = {v / r:.4f} A")
        elif sub_choice == 'b':
            p = get_float_input("Enter Power (P in Watts): ")
            v = get_float_input("Enter Voltage (V in Volts): ")
            if v == 0:
                print("\nError: Division by zero. Voltage cannot be 0.")
            else:
                print(f"\nResult: Current (I) = {p / v:.4f} A")
        elif sub_choice == 'c':
            p = get_float_input("Enter Power (P in Watts): ")
            r = get_float_input("Enter Resistance (R in Ohms): ")
            if r == 0:
                print("\nError: Division by zero. Resistance cannot be 0.")
            elif p / r < 0:
                print("\nError: Cannot calculate square root of a negative value.")
            else:
                print(f"\nResult: Current (I) = {(p / r)**0.5:.4f} A")
        else:
            print("Invalid selection.")

    # ------------------ Resistance Calculations ------------------
    elif choice == '3':
        print("\nChoose known parameters:")
        print("a. Voltage (V) and Current (I)   [R = V / I]")
        print("b. Voltage (V) and Power (P)     [R = V^2 / P]")
        print("c. Power (P) and Current (I)     [R = P / I^2]")
        sub_choice = input("Select (a/b/c): ").strip().lower()
        
        if sub_choice == 'a':
            v = get_float_input("Enter Voltage (V in Volts): ")
            i = get_float_input("Enter Current (I in Amperes): ")
            if i == 0:
                print("\nError: Division by zero. Current cannot be 0.")
            else:
                print(f"\nResult: Resistance (R) = {v / i:.4f} Ω")
        elif sub_choice == 'b':
            v = get_float_input("Enter Voltage (V in Volts): ")
            p = get_float_input("Enter Power (P in Watts): ")
            if p == 0:
                print("\nError: Division by zero. Power cannot be 0.")
            else:
                print(f"\nResult: Resistance (R) = {(v ** 2) / p:.4f} Ω")
        elif sub_choice == 'c':
            p = get_float_input("Enter Power (P in Watts): ")
            i = get_float_input("Enter Current (I in Amperes): ")
            if i == 0:
                print("\nError: Division by zero. Current cannot be 0.")
            else:
                print(f"\nResult: Resistance (R) = {p / (i ** 2):.4f} Ω")
        else:
            print("Invalid selection.")

    # ------------------ Power Calculations ------------------
    elif choice == '4':
        print("\nChoose known parameters:")
        print("a. Voltage (V) and Current (I)     [P = V * I]")
        print("b. Current (I) and Resistance (R)  [P = I^2 * R]")
        print("c. Voltage (V) and Resistance (R)  [P = V^2 / R]")
        sub_choice = input("Select (a/b/c): ").strip().lower()
        
        if sub_choice == 'a':
            v = get_float_input("Enter Voltage (V in Volts): ")
            i = get_float_input("Enter Current (I in Amperes): ")
            print(f"\nResult: Power (P) = {v * i:.4f} W")
        elif sub_choice == 'b':
            i = get_float_input("Enter Current (I in Amperes): ")
            r = get_float_input("Enter Resistance (R in Ohms): ")
            print(f"\nResult: Power (P) = {(i ** 2) * r:.4f} W")
        elif sub_choice == 'c':
            v = get_float_input("Enter Voltage (V in Volts): ")
            r = get_float_input("Enter Resistance (R in Ohms): ")
            if r == 0:
                print("\nError: Division by zero. Resistance cannot be 0.")
            else:
                print(f"\nResult: Power (P) = {(v ** 2) / r:.4f} W")
        else:
            print("Invalid selection.")

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")


def display_20_formulas():
    """
    Displays an extended list of 20 essential electrical formulas
    related to V, I, R, P, Energy, AC circuits, and Resistor Combinations.
    """
    formulas = [
        " 1. V = I * R              (Voltage using Current & Resistance)",
        " 2. V = P / I              (Voltage using Power & Current)",
        " 3. V = sqrt(P * R)        (Voltage using Power & Resistance)",
        " 4. I = V / R              (Current using Voltage & Resistance)",
        " 5. I = P / V              (Current using Power & Voltage)",
        " 6. I = sqrt(P / R)        (Current using Power & Resistance)",
        " 7. R = V / I              (Resistance using Voltage & Current)",
        " 8. R = V^2 / P            (Resistance using Voltage & Power)",
        " 9. R = P / I^2            (Resistance using Power & Current)",
        "10. P = V * I              (Power using Voltage & Current)",
        "11. P = I^2 * R            (Power using Current & Resistance)",
        "12. P = V^2 / R            (Power using Voltage & Resistance)",
        "13. E = P * t              (Electrical Energy = Power * Time)",
        "14. R_total = R1 + R2      (Series Resistance)",
        "15. 1/R_eq = 1/R1 + 1/R2   (Parallel Resistance)",
        "16. V_rms = V_peak / sqrt(2) (RMS Voltage from Peak Voltage)",
        "17. I_rms = I_peak / sqrt(2) (RMS Current from Peak Current)",
        "18. P_real = V * I * PF    (AC Real Power with Power Factor PF)",
        "19. S = V * I              (Apparent Power in AC Circuits - VA)",
        "20. Q = sqrt(S^2 - P^2)    (Reactive Power in AC Circuits - VAR)"
    ]
    
    print("\n================ 20 ELECTRICAL FORMULAS REFERENCE ================")
    for formula in formulas:
        print(formula)
    print("==================================================================")


def main():
    """
    Main loop that keeps running the program until the user chooses to quit.
    """
    while True:
        print("\n=========================================")
        print(" MAIN MENU ")
        print("=========================================")
        print("1. Ohm's Law & Power Calculator")
        print("2. View 20 Related Electrical Formulas")
        print("3. Quit")
        
        user_choice = input("Select an option (1-3): ").strip()
        
        if user_choice == '1':
            ohms_law_calculator()
        elif user_choice == '2':
            display_20_formulas()
        elif user_choice == '3':
            print("\nThank you for using the calculator. Goodbye!")
            break
        else:
            print("Invalid menu option. Please select 1, 2, or 3.")

# Run the program
if __name__ == "__main__":
    main()
