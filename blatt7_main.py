"""
Docstring for blatt7_main
this module is used to be the connector of the functions with the user.
this module lets the user try to find a path available using the
criteria he choose (greedy/optimal)
"""

__author__ = "8407548, Winata, 8655943, Quan"

from blatt7_greedyansatz import (
    positions,
    graph,
    greedy_approach,
    mode_choice,
    optimal_path,
)
import random

while True:
    cat, house = positions()
    method = input(
        "Which method do you want to use [greedy approach: 1 or optimal "
        "approach: 2]: "
    )
    while method != "1" and method != "2":
        method = input("Please pick either 1 for greedy or 2 for optimal! : ")
    mode = mode_choice()
    if method == "1":
        result = greedy_approach(graph, cat, house, mode)
        # result may be more than 1
        print(random.choice(result))
    else:
        result = optimal_path(graph, cat, house, mode=mode)
        if result is None:
            print("No path found (optimal_path returned None).")
        else:
            effort, distraction, path = result
            print((path, (effort, distraction)))

    again = input("Run the code again [y/n]: ").lower()
    while again not in ["y", "n", "no", "yes", "j", "ja", "nein"]:
        again = input(
            "Please pick either 'y' for yes or 'n' for no : "
        ).lower()
    if again in ["nein", "n", "no"]:
        break
