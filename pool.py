"""
pool.py : CodeTown Pubilc Pool text-based P.O.S system.

The purpose of this program is to receive an input for the amount of
adults and children enetring the pool, and output the cheapest cost
for the set amount of adults and children.

Knowing the price for a single adult, single child, Family Pass A & 
Family Pass B, the approach taken was to calculate all possible
combinations for the given input and return the minimum cost as output
in the specified receipt format. Input validation is gracefully handled
with prompts and error messages e.g. requiring at least one adult for
supervision, non-negative counts etc.

Run pool.py to experience the P.O.S system and process sales until user
exits.
"""

# Helper to output purchase receipt:
def purchase_receipt(num_of_pass_a, num_of_pass_b, adults_remaining, children_remaining ) -> None :
  '''
    Output transaction receipt given the cheapest transaction possible from number of adults & children.
    
    Args:
      num_of_pass_a (int): Number of Family Type A passes purchased
      num_of_pass_b (int): Number of Family Type B passes purchased
      adults_remaining (int): Number of Adults remaining (Adults not included in Family Pass calculations)
      children_remaining (int): Number of Children remaining (Children not included in Family Pass calculations) 
      
    Returns:
      (None): Prints complete Transaction Receipt with correct purchase quantities & amounts
  '''
  print("\n")
  print("Receipt:")
  
  cost = float(16*num_of_pass_a + 16*num_of_pass_b + 5*adults_remaining + 4*children_remaining)
  
  if(num_of_pass_a >= 1):
    print(f"{num_of_pass_a}x Family Pass A \t : ${16.00*num_of_pass_a:.2f}")
  if(num_of_pass_b >= 1):
    print(f"{num_of_pass_b}x Family Pass B \t : ${16.00*num_of_pass_b:.2f}")
  if(adults_remaining >= 1):
    print(f"{adults_remaining}x Adult \t\t : ${5.00*adults_remaining:.2f}")
  if(children_remaining >= 1):
    print(f"{children_remaining}x Child \t\t : ${4.00*children_remaining:.2f}")
  print("------------------------------------------")
  print(f"TOTAL : ${cost: .2f}\n")
  

# Helper to get the cheapest cost:
# run through cases to output final price
# i.e. make sure we calculate all possible output prices from all possible combinations and select minimum cost
def get_cheapest_cost(no_of_adults,no_of_children) -> (tuple[int, int, int, int] | None):
  '''
  Outputs cheapest possible transaction cost by scanning all possible combinations of billing with given adults and children arguments.
  
  Args:
    no_of_adults (int): Number of Adults wishing to enter facility
    no_of_children (int): Number of Children wishing to enter facility
    
  Returns:
    tuple[int, int, int, int]: Captured arguments for cheapest case to output to purchase_receipt() function.
  '''
  # setting variables to make final calculations of cheapest cost more inuitive, focusing on core logic/problem at hand and readability rather than few short lines of code:
  min_cost = float('inf')
  all_possible_nums_of_family_a_passes = no_of_adults//2 + 1 # e.g. 8 adults = 8//2 = 4 bundles possible, + 1 is to include max num...
  all_possible_nums_of_family_b_passes = no_of_children//3 + 1 # e.g. 3 children = 3//3 = 0 + 1, 1 bundle possible
  receipt_args_for_min_case = None
  
  for num_of_pass_a in range(all_possible_nums_of_family_a_passes):
    for num_of_pass_b in range(all_possible_nums_of_family_b_passes):
      
      adults_used_for_pass_a = 2 * num_of_pass_a
      children_used_for_pass_a = 2 * num_of_pass_a
      
      adults_used_for_pass_b = 1 * num_of_pass_b
      children_used_for_pass_b = 3 * num_of_pass_b
      
      adults_remaining = int(no_of_adults - adults_used_for_pass_a - adults_used_for_pass_b)
      children_remaining = int(no_of_children - children_used_for_pass_a - children_used_for_pass_b)
      
      # Skipping invalid cases where at least 1 adult dont exist and child is less than 0
      if ( adults_remaining < 0 or children_remaining < 0):
        continue
      
      # total cost calulation for each case:
      ttl_cost = 16*num_of_pass_a + 16*num_of_pass_b + 5*adults_remaining + 4*children_remaining
      
      # only store minimum cost out of all the costs we calulated & output that to receipt:
      if ttl_cost < min_cost :
        min_cost = ttl_cost
        receipt_args_for_min_case = (num_of_pass_a,num_of_pass_b,adults_remaining,children_remaining)
      
  return receipt_args_for_min_case

def main() -> None:
  try:
    print("--- Codetown Public Pool POS ---")
    determine_if_sale_called = input("Press Enter to exit or type any key to start a new sale: ")
  
  # we run our program until the user presses enter to exit, 
  # or raises keyboard interrupt exception, which we handle gracefully using try/except
    while(determine_if_sale_called != ""):
      print("\n")
      # Basis of our program, need numbers of adults & children for calculations:
      while True:
        try:
          no_of_adults = int(input("Enter number of adults: "))
          # input validation; We must have at least one adult for supervision.
          if no_of_adults < 1:
            print("Error: At least one adult is required for supervision.\n")
            continue
          break
        # # The input must be an integer. If the user enters text or a float, display an error and ask again.
        except ValueError:
          print("Error: Please enter a valid integer using digits.\n")
          
          
      print("\n")
        
      while True:
        try:
          no_of_children = int(input("Enter number of children: "))
          # input validation; We must have a positive amount of children
          if no_of_children < 0:
            print("Error: Number of children cannot be negative.\n")
            continue
          break
          # The input must be an integer. If the user enters text or a float, display an error and ask again.
        except ValueError:
          print("Error: Please enter a valid integer using digits.\n")
          
      receipt_args = get_cheapest_cost(no_of_adults,no_of_children)
      
      if(receipt_args):
        purchase_receipt(*receipt_args)
      
      determine_if_sale_called = input("Press Enter to exit or type any key to start a new sale: \n")
        
  except KeyboardInterrupt:
    print("\nCurrent Sale aborted by user. Exiting Codetown Public Pool P.O.S..., Goodbye!")


if __name__ == "__main__":
  main()

