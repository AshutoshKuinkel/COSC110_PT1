# For each sale, the program must:
# Ask for the number of adults. Adults are classified as 16 years or older.
# Ask for the number of children. Children are under 16.
# Validate the input.
# The input must be an integer. If the user enters text or a float, display an error and ask again.
# The number of adults must be positive (at least 1, as children must be accompanied).
# The number of children must be non-negative (0 or higher).
# Calculate the cheapest price. The system must calculate the lowest possible cost for the group based on the following price list:
# Adult: $5.00
# Child: $4.00
# Family Type A (2 Adults, 2 Children): $16.00
# Family Type B (1 Adult, 3 Children): $16.00
# Output the receipt. Display an itemised list of fees and the total price.

print("--- Codetown Public Pool POS ---")
determine_if_sale_called = input("Press Enter to exit or type any key to start a new sale: ")

while(determine_if_sale_called != enter_key_pressed):
  no_of_adults = int(input("Enter number of adults: "))
  no_of_children = int(input("Enter number of chlidren: "))
  
  if(type(no_of_adults) != 'int' and type(no_of_children) != 'int'):
    raise TypeError("Error: Please enter a valid integer using digits.")
  if(no_of_adults<=0):
    raise Exception("Error: At least one adult is required for supervision.")
  if(no_of_children<0):
    raise Exception("Error: Number of children cannot be negative.")
    
    



