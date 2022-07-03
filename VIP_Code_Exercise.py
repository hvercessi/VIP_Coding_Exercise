# Vermont Information Processing Technical Exercise 
# Halina Vercessi
# due 7/3/2022 by 8:00am

# =============================================================================
#
# Program that allows for an integer array to be passed in and will then output all of the pairs that sum up to 10.  
# The follwoing solution allows for 
# 1) output all pairs (includes duplicates and the reversed ordered pairs), 
# 2) output unique pairs only once (removes the duplicates but includes the reversed ordered pairs), and 
# 3) output the same combo pair only once (removes the reversed ordered pairs). 
#
# =============================================================================

# Driver code
def main():
    
    # Test function using given example list and outputs
    test = [1, 1, 2, 4, 4, 5, 5, 5, 6, 7, 9]
    num = 10
    
    pairs_sum(test, num)

 # Solution function   
def pairs_sum(int_array, sum_num):
    
    hash_dict = dict()
    sum_to = sum_num
    pairs_array = []
    pairs_array_no_order = []
    size = len(int_array)
    
    if size == 0 or size == 1:
        print("No pairs")
    
    # Go through list and check for possibility of pair using hashing strategy
    for i in range(size):
        remainder = sum_to - int_array[i]
        
        if remainder in hash_dict:
            n = hash_dict[remainder]
            for s in range(n):
                pairs_array.append([int_array[i], remainder])          
                pairs_array.append([remainder, int_array[i]])
                pairs_array_no_order.append([remainder, int_array[i]])
    
        if int_array[i] in hash_dict:
            hash_dict[int_array[i]] = hash_dict[int_array[i]] + 1
        else:
            hash_dict[int_array[i]] = 1
            

    
    # Dislay all pairs
    print("\nAll pairs:\n", sorted(pairs_array))
    
    
    # Display unique pairs (order matters)
    temp_array = []
    j = 0
    while j < len(pairs_array):
        if pairs_array[j] not in temp_array:
            temp_array.append(pairs_array[j])
        j+=1
    print("\nUnique pairs:\n", sorted(temp_array))
    
    
    # Display unique number combos
    temp_array = []
    j = 0
    while j < len(pairs_array_no_order):
        if pairs_array_no_order[j] not in temp_array:
            temp_array.append(pairs_array_no_order[j])
        j+=1
    print("\nUnique number combinations:\n", sorted(temp_array))
            
    
        
main()

