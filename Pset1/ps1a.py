###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cows_dict = {}
    # Opening the file
    with open(filename, "r") as file:
        # Iterating through every line of the file
        for line in file:
            # Store the name and the weight in cows_dict. Key will be the name and value will be the weight
            element_list = line.split(",")
            cows_dict[element_list[0]] = int(element_list[1])
    return cows_dict        

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # Initialize an unsorted_list 
    unsorted_list = []
    # store each key and value in the cows dictionary as elements in the unsorted_list
    for key in cows:
        unsorted_list.append([key, cows[key]])
    # Sort the unsorted_list by weight in descending order and assign it to sorted_list    
    sorted_list = sorted(unsorted_list, key = lambda list: list[1], reverse = True)
    # Initialize a list with elements as the names of the cows that are on  the spaceship 
    settled_cow_list = []
    # Initialize a list of result to be returned
    result = []
    # Initialize a counter to count the number of cows on the spaceship
    used_counter = 0
    # Initialize a counter to count the number of spaceships required
    spaceship_counter = 0
    # Initialize a counter to keep track of the current weight in the current spaceship
    current_weight = 0
    # Loop until all cows are on the spaceship
    while used_counter < len(sorted_list):
        # Create a new list within the result list to indicate a new spaceship
        result.append([])
        current_weight = 0
        # Loop through every cow to see if they can fit in the current spaceship
        for element in sorted_list:
            # Prevent cloning
            if element[0] not in settled_cow_list:
                # Ensure within constraint, append to current spaceship.
                if current_weight + element[1] <= limit:
                    current_weight += element[1]
                    result[spaceship_counter].append(element[0])
                    used_counter += 1
                    settled_cow_list.append(element[0])
        spaceship_counter += 1  
    return result    



# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # Initialize a list to store the names of cows
    cow_name = []
    for cow in cows:
        cow_name.append(cow)
    # Initialize a list to store all possible ways to divide the cows into trips
    unrefined_possibilites = []
    # Append each way into unrefined_possbilites
    for partition in get_partitions(cow_name):
        unrefined_possibilites.append(partition)  
    # Initialize a list to store all possible ways to divide the cows into trips that are within constraint    
    refined_possibilites = []
    # Alogirthm to check if constraint is met for each possibility
    for set in unrefined_possibilites:
        # Initialize a counter that keeps track of the number of times a spaceship is within constraint for each set
        acceptable_weight_counter = 0
        for spaceship in set:
            acceptable_weight = True
            current_weight = 0
            # If weight > constraint, break loop, else update current weight
            for cow in spaceship:
                if current_weight + cows[cow] > limit:
                    acceptable_weight = False
                    break
                current_weight += cows[cow]
            # Increment acceptable_weight_counter when total weight in a spaceship is < constraint    
            if acceptable_weight == True:
                acceptable_weight_counter += 1
            if acceptable_weight_counter == len(set):
                refined_possibilites.append(set)
    result = []
    spaceship_counter = 1
    found = False
    # Alogorithm to find the least number of trips required
    while True:    
        # Start from one spaceship for trip, increment after looping through every set
        # If len(spaceship) equals to lne(set) break out of loop immediately
        for set in refined_possibilites:
            if len(set) == spaceship_counter:
                result += set
                found = True
                break
        if found == True:
            break
        spaceship_counter += 1
    return result                    


        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # Time both greedy and brute force.
    # Return the time takne and the number of trips for each alogrithm
    cows_dict = load_cows("ps1_cow_data.txt") 
    start_greedy = time.time()
    greedy = greedy_cow_transport(cows_dict, 10)
    end_greedy = time.time()
    start_brute= time.time()
    brute_force = brute_force_cow_transport(cows_dict,10)
    end_brute = time.time()
    print(f"Number of Trips using Greedy: {len(greedy)}")
    print(f"Time taken for Greedy Transport: {end_greedy - start_greedy}")
    print()
    print(f"Number of Trips using Brute force: {len(brute_force)}")
    print(f"Time taken for Brute Force Transpore: {end_brute - start_brute}")
    
compare_cow_transport_algorithms()    
