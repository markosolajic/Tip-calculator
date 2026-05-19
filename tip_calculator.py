# Author: Marko Solajic

total_amount = float(input("Enter the total bill amount (e.g., 50 for $50): "))
tip_percentage = int(input("Enter the tip percentage (e.g., 15 for 15%): "))

tip = total_amount * (tip_percentage / 100)
final_amount = total_amount + tip

print(f"Tip: ${tip}")
print(f"Final amount: ${final_amount}")

input("Press Enter to exit...")