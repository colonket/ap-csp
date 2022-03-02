# Bogo Sort with Statistics
# Author: Eric Iniguez
# Description:
#   Sorts randomly generated number lists of increasing size using Bogo Sort.
import random
import timeit
import sys
from datetime import datetime

def isOrdered(numList):
    # Returns true if number list is in order, returns false if not in order
    if(all(numList[i] <= numList[i+1] for i in range(len(numList)-1))):
        return True
    else:
        return False

if __name__ == '__main__':
    try:
        minListSize = int(sys.argv[1])
        maxListSize = int(sys.argv[2])+1
    except:
        print("No valid arguments found, using default values from 2 to 15")
        minListSize = 2
        maxListSize = 15

    for i in range(minListSize,maxListSize):
        # Generate a list of random numbers from 1 through 9
        numList = [j for j in range(1,i+1)]
        random.shuffle(numList)

        print(datetime.now().time(),numList)   # Print Start Time
        tries = 0   # Counter to track how many times we shuffle   
        start = timeit.default_timer()  # Keep track of the program start time
        print(datetime.now().time(),numList,end='\r')  # Live updates of number list
        while not isOrdered(numList):
            # Shuffle list until it's sorted!
            tries += 1
            random.shuffle(numList)
            print(datetime.now().time(),numList,end='\r')# Live updates of number list
        stop = timeit.default_timer()   # Keep track of the program stop time
        print()
        seconds = '{0:.10f}'.format(stop-start) # Store the time in seconds it took to sort
        print("Sorted",len(numList),"elements by shuffling",tries,"times in",seconds,"seconds")
        print()

