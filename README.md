[ReadMe.txt](https://github.com/user-attachments/files/24222178/ReadMe.txt)
This text will briefly explain what each included files does:

-------------------------------------------------
blatt7.py

First main function: greedy_approach() 

This function is used to implement a greedy algorithm to find different paths based on the given criteria. 

There are total 3 modes for the function to prioritize:

 - "effort" → chooses edges with the lowest effort.

 - "distraction" → chooses edges with the highest distraction.

 - "combined" → explores all paths and returns Pareto-optimal solutions (minimizing effort and maximizing distraction).

Result: return path and its cumulative effort/distraction values.

-------------------------------------------------
blatt7.py

Second main function: optimal_path()

This function implements a recursive depth-first search to find an optimal path.
 
It also works with 3 modes same as greedy_approach() function:

 - "effort" → returns the path with minimum total effort.

 - "distraction" → returns the path with maximum total distraction.

 - "combined" → returns one path that minimizes (effort - distraction) as a simple trade-off. 

Result: return tuple (effort, distraction, path) for one optimal path.

-------------------------------------------------
blatt7.py/blatt7_main.py

Side functions: positions() and mode_choice()

There are built in additional function for gather user's input, but they are not used for the sake of easier testing for particulate results.

These functions are explored further in blatt7_main.py which is used to be the connector of the functions with the user.

-------------------------------------------------
time_and_timeit.py

This file contain module consists of time and timeit functions to record the processing time for both functions (greedy_approach() and optimal_path()) to find which of the functions (with the same input) runs faster.

-------------------------------------------------
How the Functions Work Together:

(blatt7.py)

It serve as the core of the project. Define the graph and implement the pathfinding logic.


(blatt7_main.py)

Imports and uses the algorithms from blatt7.py and provides a way to test them interactively.


(time_and_timeit.py)

Also imports the same algorithms and runs them with fixed input to compare performance.

-------------------------------------------------
Tks for reading XDD
