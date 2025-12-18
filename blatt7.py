"""
Docstring for blatt7_greedyansatz
this module is used for store the functions such as:
positions, greedy_approach, mode_choice, and optimal_path.
theese will then be used in the main module to create a concurent running programm
"""
__author__ = "8407548, Winata, 8655943, Quan"
from collections import defaultdict, deque

graph = {"a": {"ab": [3, 2], "ac": [1, 0]},
         "b": {"ab": [3, 2], "bd": [4, 5], "be": [2, 1]},
         "c": {"ac": [1, 0], "cd": [2, 3]},
         "d": {"bd": [4, 5], "cd": [2, 3], "df": [3, 4]},
         "e": {"be": [2, 1], "ef": [5, 0]},
         "f": {"df": [3, 4], "ef": [5, 0]}}


def positions():
    """
    Docstring for positions
    this function is used to get the position of the cat and the house
    from the user.
    """
    cat = input("At which location is the cat [a, b, c, d, e, f]: ").lower()
    while cat not in ["a", "b", "c", "d", "e", "f"]:
        cat = input("Please choose from the box [a, b, c, d, e, f]: ").lower()
    house = input(
        "At which location is the house [a, b, c, d, e, f]: ").lower()
    while house not in ["a", "b", "c", "d", "e", "f"]:
        house = input(
            "Please choose from the box [a, b, c, d, e, f]: ").lower()
    return cat, house


def greedy_approach(graph, cat, house, mode):
    """
        Docstring for greedy_approach
        used to get the maximum amount of effort or distraction
        or combined. the function use four parameters which are graph,
        cat, house, and mode

        Example:
        >>> greedy_approach(graph, "a", "f", "effort")
        (['a', 'c', 'd', 'f'], (6, 7))
        >>> greedy_approach(graph, "a", "f", "combined")
        [(['a', 'b', 'd', 'f'], (10, 11)), (['a', 'c', 'd', 'f'], (6, 7))]
        >>> greedy_approach(graph, "c", "f", "distraction")
        (['c', 'd', 'b', 'a'], (9, 10))

        :param graph: mapping
        :param cat: starting point
        :param house: destination (for combined mode)
        :param mode: choose what value to be maximize
        :return: ([path], (effort, distraction))
        :rtype: tuple[list, tuple[Any | int, Any | int]] | bool
        """
    cur_pos = cat
    visited = []
    key1 = None
    key2 = None
    key3 = None
    dis_num = 0
    eff_num = 0

    if mode == "distraction":
        """
        run the function with distraction as the targeted value
        which means the end result will have the most amount 
        of distraction than all other possible paths
        """
        while True:
            diss1 = -1
            eff1 = 0
            diss2 = -1
            eff2 = 0
            diss3 = -1
            eff3 = 0

            count = 0

            for key, worth in graph[cur_pos].items():
                # if cur_pos in key:
                if key.strip(cur_pos) in visited:
                    count += 1
                    continue

                if cat == "b" or cat == "d":
                    if diss1 == -1:
                        key1 = key.strip(cur_pos)
                        diss1 = worth[1]
                        eff1 = worth[0]
                    elif diss2 == -1:
                        key2 = key.strip(cur_pos)
                        diss2 = worth[1]
                        eff2 = worth[0]
                    else:
                        key3 = key.strip(cur_pos)
                        diss3 = worth[1]
                        eff3 = worth[0]

                else:
                    if diss1 == -1:
                        key1 = key.strip(cur_pos)
                        diss1 = worth[1]
                        eff1 = worth[0]

                    else:
                        key2 = key.strip(cur_pos)
                        diss2 = worth[1]
                        eff2 = worth[0]

            if cat == "b" or cat == "d":
                if diss1 >= diss2 and diss1 >= diss3:
                    visited.append(cur_pos)
                    dis_num = dis_num + diss1
                    eff_num = eff_num + eff1
                    cur_pos = key1
                elif diss2 >= diss1 and diss2 >= diss3:
                    visited.append(cur_pos)
                    dis_num = dis_num + diss2
                    eff_num = eff_num + eff2
                    cur_pos = key2
                else:
                    visited.append(cur_pos)
                    dis_num = dis_num + diss3
                    eff_num = eff_num + eff3
                    cur_pos = key3

            else:
                if diss1 < diss2:
                    visited.append(cur_pos)
                    dis_num = dis_num + diss2
                    eff_num = eff_num + eff2
                    cur_pos = key2
                else:
                    visited.append(cur_pos)
                    dis_num = dis_num + diss1
                    eff_num = eff_num + eff1
                    cur_pos = key1

            if cur_pos in ["b", "d"] and count == 3:
                return visited, (eff_num, dis_num)

            elif cur_pos not in ["b", "d"] and count == 2:
                return visited, (eff_num, dis_num + 1)

            elif cur_pos == house:
                visited.append(cur_pos)
                return visited, (eff_num, dis_num)

    elif mode == "effort":
        """
        run the function with effort as the targeted value
        which means the end result will have the least amount of effort
        than all other possible paths
        """
        while True:
            diss1 = 0
            eff1 = 100
            diss2 = 0
            eff2 = 100
            diss3 = 0
            eff3 = 100
            count = 0
            for key, worth in graph[cur_pos].items():
                # if cur_pos in key:
                if key.strip(cur_pos) in visited:
                    count += 1
                    continue

                if cat == "b" or cat == "d":
                    if eff1 == 100:
                        key1 = key.strip(cur_pos)
                        diss1 = worth[1]
                        eff1 = worth[0]
                    elif eff2 == 100:
                        key2 = key.strip(cur_pos)
                        diss2 = worth[1]
                        eff2 = worth[0]
                    else:
                        key3 = key.strip(cur_pos)
                        diss3 = worth[1]
                        eff3 = worth[0]

                else:
                    if eff1 == 100:
                        key1 = key.strip(cur_pos)
                        diss1 = worth[1]
                        eff1 = worth[0]

                    else:
                        key2 = key.strip(cur_pos)
                        diss2 = worth[1]
                        eff2 = worth[0]

            if cat == "b" or cat == "d":
                if eff1 <= eff2 and eff1 <= eff3:
                    visited.append(cur_pos)
                    dis_num = dis_num + diss1
                    eff_num = eff_num + eff1
                    cur_pos = key1
                elif eff2 <= eff1 and eff2 <= eff3:
                    visited.append(cur_pos)
                    dis_num = dis_num + diss2
                    eff_num = eff_num + eff2
                    cur_pos = key2
                else:
                    visited.append(cur_pos)
                    dis_num = dis_num + diss3
                    eff_num = eff_num + eff3
                    cur_pos = key3

            else:
                if eff1 <= eff2:
                    visited.append(cur_pos)
                    dis_num = dis_num + diss1
                    eff_num = eff_num + eff1
                    cur_pos = key1
                else:
                    visited.append(cur_pos)
                    dis_num = dis_num + diss2
                    eff_num = eff_num + eff2
                    cur_pos = key2
            if cur_pos in ["b", "d"] and count == 3:
                return visited, (eff_num, dis_num)

            elif cur_pos not in ["b", "d"] and count == 2:
                return visited, (eff_num + 1, dis_num)

            elif cur_pos == house:
                visited.append(cur_pos)
                return visited, (eff_num, dis_num)

    elif mode == "combined":
        """
        Find all Pareto optimal paths from start to end node.
        Returns paths that minimize effort and maximize distraction values.
        """
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

            # Explore neighbors
            if current in graph:
                for edge_name, edge_cost in graph[current].items():
                    # Determine the next node from edge name
                    # Edge name format: "ab" means from 'a' to 'b'
                    # Find which character in edge_name is NOT the current node
                    next_node = edge_name.strip(current)

                    # Avoid revisiting nodes (prevent cycles)
                    if next_node not in path:
                        new_path = path + [next_node]
                        new_cost = (cost[0] + edge_cost[0],
                                    cost[1] + edge_cost[1])
                        queue.append((next_node, new_path, new_cost))

        # Find Pareto optimal paths (min effort and max distraction)
        pareto_paths = []

        for i, (path1, cost1) in enumerate(all_paths):
            is_dominated = False

            # Check if this path is dominated by any other path
            for j, (path2, cost2) in enumerate(all_paths):
                if i != j:
                    # cost2 dominates cost1 if effort is <= and distraction is >=
                    if (cost2[0] <= cost1[0] and cost2[1] >= cost1[1] and
                            (cost2[0] < cost1[0] or cost2[1] > cost1[1])):
                        is_dominated = True
                        break

            if not is_dominated:
                pareto_paths.append((path1, cost1))

        return pareto_paths


def optimal_path(graph, cat, house, mode, visited=None, path=None, eff_num=0, dis_num=0):
    """
    Docstring for optimal_path
    this function is used to get the optimal path based on one of the three
    modes: effort, distraction, or combined. The function uses
    seven parameters which are graph, cat, house, mode, visited, path,
    eff_num, and dis_num.

    Example:
    >>> optimal_path(graph, "a", "f", "effort")
    (6, 7, ['a', 'c', 'd', 'f'])
    >>> optimal_path(graph, "a", "f", "combined")
    (10, 11, ['a', 'b', 'd', 'f'])
    >>> optimal_path(graph, "c", "f", "distraction")
    (11, 11, ['c', 'a', 'b', 'd', 'f'])

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
    """
    # make sure visited and path are initialized
    if visited is None:
        visited = set()
    if path is None:
        path = [cat]

    # stop condition for recursive function:
    # when the current position is the destination
    if cat == house:
        return eff_num, dis_num, path

    # mark the current node as visited, so we don't visit it again
    visited.add(cat)
    best_result = None

    # exploring all neighbors
    for edge, values in graph[cat].items():
        # get the neighbor node by removing the current node from the edge name
        neighbor = edge.replace(cat, "")

        # make sure to not revisit nodes in the same path
        # update effort and distraction values has been accumulated during the path
        if neighbor not in visited:
            new_eff_num = eff_num + values[0]
            new_dis_num = dis_num + values[1]

            result = optimal_path(graph, neighbor, house, mode, visited.copy(),
                                  path + [neighbor], new_eff_num, new_dis_num)
            """
            call the function again with:
            neighbor as the new current node with updated visited set,
            updated path + updated effort and distraction values
            """
            # if the best path is not found yet, set it using the current result
            if result is not None:
                if best_result is None:
                    best_result = result
                else:
                    # choose optimization rule and compare with the best result accordingly
                    if mode == "effort":  # minimize effort
                        if result[0] < best_result[0]:
                            best_result = result
                    elif mode == "distraction":  # maximize distraction
                        if result[1] > best_result[1]:
                            best_result = result
                    elif mode == "combined":  # minimize effort - distraction
                        if (result[0] - result[1]) < (best_result[0] - best_result[1]):
                            best_result = result

    return best_result


def mode_choice():
    """
    Docstring for mode_choice
    this function is used to ask if user wants to maximize effort,
    distraction, or combined.
    """
    mode = input(
        "Choose mode [effort/distraction/combined]: ").lower()
    while mode not in ("effort", "distraction", "combined"):
        mode = input(
            "Please enter from the box [effort/distraction/combined]: ").lower()
    return mode


if __name__ == "__main__":

    print("Test 1: Greedy Approach")
    print(greedy_approach(graph, "a", "f", "effort"))
    # (['a', 'c', 'd', 'f'], (6, 7))
    print(greedy_approach(graph, "a", "f", "combined"))
    # [(['a', 'b', 'd', 'f'], (10, 11)), (['a', 'c', 'd', 'f'], (6, 7))]
    print(greedy_approach(graph, "c", "f", "distraction"))
    # (['c', 'd', 'b', 'a'], (9, 10))

    print("Test 2: Optimal Path")
    print(optimal_path(graph, "a", "f", "effort"))
    # (6, 7, ['a', 'c', 'd', 'f'])
    print(optimal_path(graph, "a", "f", "combined"))
    # (10, 11, ['a', 'b', 'd', 'f'])
    print(optimal_path(graph, "c", "f", "distraction"))
    # (11, 11, ['c', 'a', 'b', 'd', 'f'])
