import math

# Helper to output purchase receipt:
def purchase_receipt(num_of_pass_a, num_of_pass_b, adults_remaining, children_remaining ) -> str :
  '''
    Write up docstring for this helper
  '''
  print("Receipt: ")
  
  cost = 16*num_of_pass_a + 16*num_of_pass_b + 5*adults_remaining + 4*children_remaining
  
  print(f"{num_of_pass_a}x Family pass A \t : ${16.00*num_of_pass_a}")
  print(f"{num_of_pass_b}x Family pass B \t : ${16.00*num_of_pass_b}")
  print(f"{adults_remaining}x Adult \t\t : ${5.00*adults_remaining}")
  print(f"{children_remaining}x Child \t\t : ${4.00*children_remaining}")
  print("-------------------------------------------------")
  print(f"TOTAL : ${cost}")
  

# Helper to get the cheapest cost:
# run through cases to output final price
# i.e. make sure we calculate all possible output prices from all possible combinations and select minimum cost
def get_cheapest_cost(no_of_adults,no_of_children) -> (tuple[int, int, int, int] | None):
  '''
  Write up docstring for this helper
  '''
  # setting variables to make final calculations of cheapest cost more inuitive, focusing on core logic/problem at hand and readability rather than few short lines of code:
  min_cost = math.inf
  all_possible_nums_of_family_a_passes = no_of_adults//2 + 1 # e.g. 8 adults = 8//2 = 4 bundles possible, + 1 is to include max num...
  all_possible_nums_of_family_b_passes = no_of_children//3 + 1 # e.g. 3 children = 3//3 = 0 + 1, 1 bundle possible
  
  
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
  print("--- Codetown Public Pool POS ---")
  determine_if_sale_called = input("Press q to exit or any key to start a new sale: \n")
  
  while(determine_if_sale_called != "q"):
    
    try:
      # Basis of our program, need numbers of adults & children for calculations:
      no_of_adults = int(input("Enter number of adults: "))
      no_of_children = int(input("Enter number of chlidren: "))
      print("\n")
    except ValueError:
      # redundant, as python checks itself for int type with int(input()), but task requirements speficially mention:
      # The input must be an integer. If the user enters text or a float, display an error and ask again.
      print("\n")
      print("Error: Please enter a valid integer using digits for number of adults & children.")
      continue
    
    # input validation; We must have at least one adult for supervision.
    if(no_of_adults<1):
      raise ValueError("Error: At least one adult is required for supervision.")
    if(no_of_children<0):
      raise ValueError("Error: Number of children cannot be negative.")
    
    receipt_args = get_cheapest_cost(no_of_adults,no_of_children)
    
    if(receipt_args):
      purchase_receipt(*receipt_args)
    
    determine_if_sale_called = input("Press q to exit or any key to start a new sale: \n")


if __name__ == "__main__":
  main()

