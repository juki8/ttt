###########################

from ps1_partition import get_partitions
import time
import operator

#================================
# Part A: Transporting Space Cows
#================================

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

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
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
    # sort dict as list
    cows_sorted = sorted(cows.items(), key=operator.itemgetter(1), reverse=True)
    trips = []
    cows_moved = []
    
    while len(cows_sorted) > len(cows_moved):
        trip = []
        trip_weight = []
        for i in range(len(cows_sorted)):
            if cows_sorted[i][0] not in cows_moved:
                if cows_sorted[i][1] + sum(trip_weight) <= limit:
                    trip.append(cows_sorted[i][0])
                    trip_weight.append(cows_sorted[i][1])
                    cows_moved.append(cows_sorted[i][0])

        trips.append(trip)
    print("Greedy takes " + str(len(trips)) + " trips.")
    return trips

# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
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
    cows_sorted = sorted(cows.items(), key=operator.itemgetter(1), reverse=True)
    l = list(get_partitions(cows_sorted))
#    print(" l = all partitions: ")
#    print(l)
    
    # Check possible trips
    l_pos = []
    
    # checks trips in list
    for trips in l: 
        # checks ships in each trips
        ships = []
        for ship in trips:      
            # accesses individual cow
            ship_weight = []
            for i in ship:
                ship_weight.append(i[1])
            ships.append(sum(ship_weight))
        if all(ship <= limit for ship in ships):
            l_pos.append(trips)

    # Remove potential duplicates
    trips = []
    for trip in l_pos:
        if trip not in trips:
            trips.append(trip)
#    print("trips: ")
#    print(trips)
            
    # Sort trip
    trips.sort(key=len)
#    print("trips sorted: ")
#    print(trips)
    print("Brute Force takes " + str(len(trips[0])) + " trips.")
    
    # Remove tuples and weight
    trips_ = []
    for ship in trips[0]:
        ship_ = []
        for cow in ship:
            ship_.append(cow[0])
        trips_.append(ship_)
        
    return trips_
    
        
# Problem 3
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
    greedy = greedy_cow_transport(cows, limit)
    print("AW: Greedy takes " + str(len(greedy)) + " trips.")
    
    brute = brute_force_cow_transport(cows, limit)
    print("AW: Brute Force takes " + str(len(brute)) + " trips.")
    
    
#    
#    def timing(f):
#    def wrap(*args):
#        time1 = time.time()
#        ret = f(*args)
#        time2 = time.time()
#        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2-time1)*1000.0))
#
#        return ret
#    return wrap
#    
#    


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))