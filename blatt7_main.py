"""
Docstring for blatt7_main
this module is used to be the connector of the functions with the user.
the user can use this module to try to find a path available using the criteria he choose (greedy/optimal)
"""
__author__ = "8407548, Winata, 8655943, Quan"

from blatt7_greedyansatz import positions, graph, greedy_approach, mode_choice, optimal_path

while True:
    cat, house = positions()
    method = input(
        "Which method do you want to use [greedy approach: 1 or optimal approach: 2]: ")
    while method != "1" and method != "2":
        method = input("Please pick either 1 for greedy or 2 for optimal! : ")
    mode = mode_choice()
    if method == "1":
        if mode == "combined":
            pareto = greedy_approach(graph, cat, house, mode)
            for result in pareto:
                print(result)
        else:
            # effort, distraction, path = greedy_ansatz(graph, cat, house, mode)
            print(greedy_approach(graph, cat, house, mode))
    else:
        result = optimal_path(graph, cat, house, mode=mode)
        if result is None:
            print("No path found (optimal_path returned None).")
        else:
            effort, distraction, path = result
            print(optimal_path(graph, cat, house, mode=mode))

    again = input("Run the code again [y/n]: ").lower()
    while again not in ["y", "n", "no", "yes", "j", "ja", "nein"]:
        again = input(
            "Please pick either 'y' for yes or 'n' for no : ").lower()
    if again in ["nein", "n", "no"]:
        break
