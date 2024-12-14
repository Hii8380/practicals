def deposit(balance, amount):
    """Function to deposit money into the account."""
    balance += amount
    return balance

def withdraw(balance, amount):
    """Function to withdraw money from the account, ensuring no negative balance."""
    if balance >= amount:
        balance -= amount
    else:
        print(f"Error: Insufficient funds to withdraw {amount}.")
    return balance

def process_transactions():
    """Function to process a series of transactions and compute the final balance."""
    balance = 0
    while True:
        try:
            transaction = input("Enter transaction (D/W amount) or 'done' to finish: ").strip()
            if transaction.lower() == "done":
                break

            # Split the transaction into type and amount
            parts = transaction.split()
            if len(parts) != 2:
                print("Invalid input format. Please enter in the format 'D/W amount'.")
                continue

            trans_type = parts[0]
            amount = int(parts[1])

            if trans_type == 'D':  # Deposit
                balance = deposit(balance, amount)
            elif trans_type == 'W':  # Withdrawal
                balance = withdraw(balance, amount)
            else:
                print("Invalid transaction type. Use 'D' for deposit or 'W' for withdrawal.")
                continue

        except ValueError:
            print("Invalid amount entered. Please enter a valid integer.")
            continue

    return balance

if __name__ == "__main__":
    final_balance = process_transactions()
    print(f"The final balance is: {final_balance}")
