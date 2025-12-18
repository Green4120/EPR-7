"""
Docstring for blatt7_greedyansatz
this module is used for store the functions such as:
positions, greedy_approach, mode_choice,
and optimal_path.
these will then be used in the main module to create a
concurrent running program
"""

__author__ = "8407548, Winata, 8655943, Quan"
from collections import deque
import doctest

graph = {
    "a": {"ab": [3, 2], "ac": [1, 0]},
    "b": {"ab": [3, 2], "bd": [4, 5], "be": [2, 1]},
    "c": {"ac": [1, 0], "cd": [2, 3]},
    "d": {"bd": [4, 5], "cd": [2, 3], "df": [3, 4]},
    "e": {"be": [2, 1], "ef": [5, 0]},
    "f": {"df": [3, 4], "ef": [5, 0]},
}


def positions():
    # to get the positions of the cat and the house
    cat = input("At which location is the cat [a, b, c, d, e, f]: ").lower()
    while cat not in ["a", "b", "c", "d", "e", "f"]:
        cat = input("Please choose from the box [a, b, c, d, e, f]: ").lower()
    house = input(
        "At which location is the house [a, b, c, d, e, f]: "
    ).lower()
    while house not in ["a", "b", "c", "d", "e", "f"]:
        house = input(
            "Please choose from the box [a, b, c, d, e, f]: "
        ).lower()
    return cat, house


def greedy_approach(graph, cat, house, mode):
    """
    Docstring for greedy_approach
    used to get the maximum amount of distraction or minimum amount
    of effort or combined. the function use four parameters which are graph,
    cat, house, and mode
    :param graph: mapping
    :param cat: starting point
    :param house: destination (for combined mode)
    :param mode: choose what value to be maximize
    :return: ([path], (effort, distraction))
    :rtype: tuple[list, tuple[Any | int, Any | int]] | bool

    Test 1 Normal test distraction:
    >>> print(greedy_approach(graph, "a", "f", "distraction"))
    [(['a', 'b', 'd', 'f'], (10, 11))]

    Test 2 Normal test distraction:
    >>> print(greedy_approach(graph, "b", "f", "distraction"))
    [(['b', 'd', 'f'], (7, 9))]

    Test 3 Negative test distraction:
    >>> print(greedy_approach(graph, "c", "c", "distraction"))
    (['c'], (0, 0))

    Test 1 Normal test effort:
    >>> print(greedy_approach(graph, "a", "f", "effort"))
    [(['a', 'c', 'd', 'f'], (6, 7))]

    Test 2 Normal test effort:
    >>> print(greedy_approach(graph, "c", "f", "effort"))
    [(['c', 'd', 'f'], (5, 7))]

    Test 3 Negative test effort:
    >>> print(greedy_approach(graph, "a", "a", "effort"))
    (['a'], (0, 0))

    Test 1 Normal test combined:
    >>> print(greedy_approach(graph, "d", "f", "combined"))
    [(['d', 'f'], (3, 4)), (['d', 'b', 'a', 'c'], (8, 7))]

    Test 2 Normal test combined:
    >>> print(greedy_approach(graph, "b", "f", "combined"))
    [(['b', 'd', 'f'], (7, 9))]

    Test 3 Negative test combined:
    >>> print(greedy_approach(graph, "b", "b", "combined"))
    (['b'], (0, 0))
    """
    """cur_pos = cat
    visited = []
    key1 = None
    key2 = None
    key3 = None"""
    dis_num = 0
    eff_num = 0
    if cat == house:
        return [cat], (eff_num, dis_num)

    # Queue: (current_node, path, cumulative_cost)
    queue = deque([(cat, [cat], (0, 0))])

    # Store all paths that reach the destination
    all_paths = []

    while queue:
        current, path, cost = queue.popleft()

        # If we reached the destination, save this path
        if current == house:
            all_paths.append((path, cost))
            continue

        # Check ONCE per node, not once per edge
        if current in graph:
            unvisited_neighbors = []

            for edge_name, edge_cost in graph[current].items():
                next_node = edge_name.strip(current)

                if next_node not in path:
                    unvisited_neighbors.append(
                        (next_node, edge_name, edge_cost)
                    )

            # If there are unvisited neighbors, explore them
            if unvisited_neighbors:
                for next_node, edge_name, edge_cost in unvisited_neighbors:
                    new_path = path + [next_node]
                    new_cost = (cost[0] + edge_cost[0], cost[1] + edge_cost[1])
                    queue.append((next_node, new_path, new_cost))
            else:
                # All neighbors visited = dead end
                if house not in path and (path, cost) not in all_paths:
                    all_paths.append((path, cost))

    # Find Paths according to targeted value
    use_paths = []

    for i, (path1, cost1) in enumerate(all_paths):
        is_dominated = False

        # Check if this path is dominated by any other path
        for j, (path2, cost2) in enumerate(all_paths):
            if i != j:
                if mode == "combined":
                    # cost2 dominates cost1 if effort <= and distraction >=
                    if (
                        cost2[0] <= cost1[0]
                        and cost2[1] >= cost1[1]
                        and (
                            cost2[0] < cost1[0]
                            or cost2[1] > cost1[1]
                        )
                    ):
                        is_dominated = True
                        break
                elif mode == "distraction":
                    if cost2[1] >= cost1[1]:
                        if (cost2[1] == cost1[1]) and (cost2[0] < cost1[0]):
                            is_dominated = True
                            break
                        elif cost2[1] > cost1[1]:
                            is_dominated = True
                            break
                elif mode == "effort":
                    if cost2[0] <= cost1[0]:
                        if (cost2[0] == cost1[0]) and (cost2[1] > cost1[1]):
                            is_dominated = True
                            break
                        elif cost2[0] < cost1[0]:
                            is_dominated = True
                            break

        if not is_dominated:
            use_paths.append((path1, cost1))

    return use_paths


def optimal_path(
    graph, start, goal, mode, visited=None, path=None, effort=0, distraction=0
):
    """
    Docstring for optimal_path
    this function is used to get the optimal path based on one of the three
    modes: effort, distraction, or combined. The function uses
    seven parameters which are graph, cat, house, mode, visited, path,
    eff_num, and dis_num.

    :param graph: mapping of nodes and edges with [effort, distraction] values
    :param cat: starting point of the path
    :param house: destination
    :param mode: choose optimization rule ('effort', 'distraction', 'combined')
    :param visited: set of already visited nodes to avoid cycles
    :param path: list of nodes representing the current path
    :param eff_num: number of effort value along the path
    :param dis_num: number of distraction value along the path
    :return: (effort, distraction, [path]) for one optimal path
    :rtype: tuple[int, int, list[str]] | None

    Test 1 Normal test effort:
    >>> print(optimal_path(graph, "a", "f", "effort"))
    (6, 7, ['a', 'c', 'd', 'f'])

    Test 2 Normal test effort:
    >>> print(optimal_path(graph, "c", "f", "effort"))
    (5, 7, ['c', 'd', 'f'])

    Test 3 Negative test effort:
    >>> print(optimal_path(graph, "e", "e", "effort"))
    (0, 0, ['e'])

    Test 1 Normal test distraction:
    >>> print(optimal_path(graph, "a", "f", "distraction"))
    (10, 11, ['a', 'b', 'd', 'f'])

    Test 2 Normal test distraction:
    >>> print(optimal_path(graph, "c", "f", "distraction"))
    (11, 11, ['c', 'a', 'b', 'd', 'f'])

    Test 3 Negative test distraction:
    >>> print(optimal_path(graph, "f", "f", "distraction"))
    (0, 0, ['f'])

    Test 1 Normal test combined:
    >>> print(optimal_path(graph, "a", "f", "combined"))
    (10, 11, ['a', 'b', 'd', 'f'])

    Test 2 Normal test combined:
    >>> print(optimal_path(graph, "b", "a", "combined"))
    (7, 8, ['b', 'd', 'c', 'a'])

    Test 3 Negative test combined:
    >>> print(optimal_path(graph, "b", "b", "combined"))
    (0, 0, ['b'])
    """
    if visited is None:
        visited = set()
    if path is None:
        path = [start]

    # base case: goal reached
    if start == goal:
        return effort, distraction, path

    visited.add(start)
    best_result = None

    # exploring all neighbors
    for edge, values in graph[start].items():
        neighbor = edge.replace(start, "")
        if neighbor not in visited:
            new_effort = effort + values[0]
            new_distraction = distraction + values[1]
            result = optimal_path(
                graph,
                neighbor,
                goal,
                mode,
                visited.copy(),
                path + [neighbor],
                new_effort,
                new_distraction,
            )

            if result is not None:
                if best_result is None:
                    best_result = result
                else:
                    # choose optimization rule
                    if mode == "effort":  # minimize effort
                        if result[0] < best_result[0]:
                            best_result = result
                    elif mode == "distraction":  # maximize distraction
                        if result[1] > best_result[1]:
                            best_result = result
                    elif mode == "combined":  # minimize effort - distraction
                        if (result[0] - result[1]) < (
                            best_result[0] - best_result[1]
                        ):
                            best_result = result

    return best_result


def mode_choice():
    """
    Docstring for mode_choice
    this function is used to define the characteristic of the program
    the choice is either effort, distraction, or combined.
    input from the user other than those three are not accepted
    therefor this function will always return mode in type of string
    with the value of
    'effort' or 'distraction' or 'combined'
    """
    mode = input("Choose mode [effort/distraction/combined]: ").strip().lower()
    while mode not in ("effort", "distraction", "combined"):
        mode = (
            input("Please enter from the box [effort/distraction/combined]: ")
            .strip()
            .lower()
        )
    return mode


if __name__ == "__main__":
    print("Running doctests...\n")
    doctest.testmod(verbose=True)
    print(
        "some functions (positions and mode_choice) have no doctest "
        "because they take inputs"
    )
