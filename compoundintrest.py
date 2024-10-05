def calculate_compound_interest(principal, rate, time, compounded):
    # Calculate compound interest
    amount = principal * (1 + (rate / (100 * compounded)))**(compounded * time)
    compound_interest = amount - principal
    return amount, compound_interest

# Example usage
if __name__ == "__main__":
    try:
        principal = float(input("Enter the principal amount (initial investment): "))
        rate = float(input("Enter the annual interest rate (in percentage): "))
        time = float(input("Enter the time (in years): "))
        compounded = int(input("Enter the number of times interest is compounded per year: "))

        total_amount, interest = calculate_compound_interest(principal, rate, time, compounded)
        
        print(f"\nTotal amount after {time} years: ${total_amount:.2f}")
        print(f"Total compound interest earned: ${interest:.2f}")
    except ValueError as e:
        print("Invalid input. Please enter numerical values.")
    except Exception as e:
        print("An error occurred:", e)