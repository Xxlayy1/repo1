import tkinter as tk

def validate_credit_card(card_number: str) -> bool:
    """This function validates a credit card number."""
    # 1. Change datatype to list[int]
    card_number = [int(num) for num in card_number]

    # 2. Remove the last digit:
    checkDigit = card_number.pop(-1)

    # 3. Reverse the remaining digits:
    card_number.reverse()

    # 4. Double digits at even indices
    card_number = [num * 2 if idx % 2 == 0
                   else num for idx, num in enumerate(card_number)]

    # 5. Subtract 9 at even indices if digit is over 9
    # (or you can add the digits)
    card_number = [num - 9 if idx % 2 == 0 and num > 9
                   else num for idx, num in enumerate(card_number)]

    # 6. Add the checkDigit back to the list:
    card_number.append(checkDigit)

    # 7. Sum all digits:
    checkSum = sum(card_number)

    # 8. If checkSum is divisible by 10, it is valid.
    return checkSum % 10 == 0

# Block for user input
def get_credit_card_number() -> str:
    """This function prompts the user to input a credit card number."""
    while True:
        card_number = entry.get()
        # Remove any spaces or dashes from the input
        card_number = card_number.replace(" ", "").replace("-", "")
        if card_number.isdigit() and len(card_number) == 16:
            return card_number
        else:
            result_label.config(text="Invalid input! Please enter a 16-digit credit card number.")

# Function to handle validation and display result
def validate_and_display():
    card_number = get_credit_card_number()
    if validate_credit_card(card_number):
        result_label.config(text="Valid.")
    else:
        result_label.config(text="Invalid.")

# Function to exit the application
def exit_application():
    window.destroy()

# Create a tkinter window
window = tk.Tk()
window.title("Credit Card Validator")

# Set background color to dark
window.configure(bg='#333')

# Set window size
window.geometry("300x140")

# Create input entry
entry = tk.Entry(window, width=30)
entry.pack(pady=10)

# Create validate button
validate_button = tk.Button(window, text="Validate", command=validate_and_display, bg='#666', fg='#fff')
validate_button.pack()

# Create label to display result
result_label = tk.Label(window, text="", bg='#333', fg='#fff')
result_label.pack(pady=10)

# Run the tkinter event loop
window.mainloop()
