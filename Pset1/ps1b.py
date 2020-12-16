###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # Check if target weight in memo. If it is, return value.
    if target_weight in memo:
        result = memo[target_weight]
    # Base Case, if target weight = 0, return 0    
    elif target_weight == 0:
        result = 0
    # Else, find out the branch with the shortest length        
    else:
        list = []
        for i in range(len(egg_weights)):
            # Explore all branches for those with egg weights <= target weight
            if egg_weights[i] <= target_weight:
                number_eggs = dp_make_weight(egg_weights, target_weight - egg_weights[i], memo)
                list.append(number_eggs)
                print(list)
        # Sort by number of eggs        
        sorted_list = sorted(list)
        # Increment by 1 to include the egg add in the current function call
        increment = sorted_list[0] + 1
        # Store the number of eggs into memo
        memo[target_weight] = increment
        result = increment
    return result    


# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    #egg_weights = (1, 5, 10, 25)
    #n = 99
    #print("Egg weights = (1, 5, 10, 25)")
    #print("n = 99")
    #print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    #print("Actual output:", dp_make_weight(egg_weights, n))
    #print()
    #egg_weights = (1,50,100)
    #n = 100
    #print("Egg weights = (50, 100)")
    #print("n = 100")
    #print("Expected ouput: 2")
    #print("Actual output:", dp_make_weight(egg_weights, n))
    #print()
    egg_weights = (50, 53, 1, 100)
    n = 1900
    print("Egg weights = (50, 53, 100, 1)")
    print("n = 103")
    print("Expected ouput: 2")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()