
print("--- Codetown Public Pool POS ---")
determine_if_sale_called = input("Press q to exit or any key to start a new sale: \n")

prices = {
  "Adult" : 5,
  "Child" : 4,
  "Family Pass A" : 16,
  "Family Pass B" : 16
}
  

def family_pass_a_calculation():
  print("Receipt: ")
  print("FAMILY PASS A \t : $Cost for each one ")
  print("---------------------------")
  print("TOTAL: $ return total float")
  print("\n")

def family_pass_b_calculation():
  print("Receipt:")
  print("FAMILY PASS B \t : $Cost for each one ")
  print("---------------------------")
  print("TOTAL: $ return total")
  print("\n")

def ordinary_ticket_calculation():
  print("Receipt:")
  print("Adult \t : $Cost for each one ")
  print("---------------------------")
  print("TOTAL: $ return total")
  print("\n")

while(determine_if_sale_called != "q"):
  
  try:
    # Basis of our program, need numbers of adults & children for calculations:
    no_of_adults = int(input("Enter number of adults: "))
    no_of_children = int(input("Enter number of chlidren: "))
    print("\n")
  except ValueError:
    # redundant, as python checks itself for int type with int(input()), but task requirements speficially mention:
    # The input must be an integer. If the user enters text or a float, display an error and ask again.
    print("Error: Please enter a valid integer using digits for number of adults & children.")
  
  # input validation; We must have at least one adult for supervision.
  if(no_of_adults<1):
    raise ValueError("Error: At least one adult is required for supervision.")
  if(no_of_children<0):
    raise ValueError("Error: Number of children cannot be negative.")
  
  # run through cases to output final tickets
  # this is wrong, what about when there is e.g. 4 adults and 2 children? we wouldn't return cheapest price with this...
  # instead i think what we can do is use modulo and check for even and odd numbers, if even that means we have to have at least 2 adults and 2 children, only then we give family pass
  # this should handle case where we have like 4 adults and 2 children... but even with this modulo approach I need to check the output e.g. when we have 2 adults and 0 children...
  # maybe the solution is to use the modulo thing, but make sure we have at least 1 children and one adult
  if( no_of_adults == 2 and no_of_children == 2):
    family_pass_a_calculation()
  elif( no_of_adults == 1 and no_of_children == 3):
    family_pass_b_calculation()
  else:
    ordinary_ticket_calculation()
    
  
     
  # print(f'no_of_adults is {no_of_adults}')
  # print(f'no_of_children is {no_of_children}')
  
  determine_if_sale_called = input("Press q to exit or any key to start a new sale: \n")
  


