__author__ = "8407548, Winata, 8655943, Quan"

graph = {"a": {"ab": [3, 2], "ac": [1, 0]},
         "b": {"ab": [3, 2], "bd": [4, 5], "be": [2, 1]},
         "c": {"ac": [1, 0], "cd": [2, 3]},
         "d": {"bd": [4, 5], "cd": [2, 3], "df": [3, 4]},
         "e": {"be": [2, 1], "ef": [5, 0]},
         "f": {"df": [3, 4], "ef": [5, 0]}}


def positions():
    # to get the positions of the cat and the house
    cat = input(
        "At which location is the cat [a, b, c, d, e, f]: ").strip().lower()
    while cat not in ["a", "b", "c", "d", "e", "f"]:
        cat = input(
            "Please choose from the box [a, b, c, d, e, f]: ").strip().lower()

    house = input(
        "At which location is the house [a, b, c, d, e, f]: ").strip().lower()
    while house not in ["a", "b", "c", "d", "e", "f"]:
        house = input(
            "Please choose from the box [a, b, c, d, e, f]: ").strip().lower()
    return cat, house


def greedy_ansatz(graph, cat, house):
    # to get the maximal amount of distraction value through comparison of the available path
    cur_pos = cat
    visited = []
    key1 = None
    key2 = None
    dis_num = 0
    while True:
        value1 = -1
        value2 = -1
        count = 0
        # for inhalt in graph.values():
        for key, worth in graph[cur_pos].items():
            # if cur_pos in key:
            if key.strip(cur_pos) in visited:
                count += 1
                continue

            if value1 == -1:
                key1 = key.strip(cur_pos)
                value1 = worth[1]

            else:
                key2 = key.strip(cur_pos)
                value2 = worth[1]

        if value1 < value2:
            visited.append(cur_pos)
            dis_num = dis_num + value2
            cur_pos = key2
        else:
            visited.append(cur_pos)
            dis_num = dis_num + value1
            cur_pos = key1

        if cur_pos in ["b", "d"] and count == 3:
            return cur_pos, dis_num

        elif cur_pos not in ["b", "d"] and count == 2:
            return cur_pos, dis_num

        elif cur_pos == house:
            return cur_pos, dis_num


def mode_choice():
    # to choose the optimization mode
    mode = input(
        "Choose mode [effort/distraction/combined]: ").strip().lower()
    while mode not in ("effort", "distraction", "combined"):
        mode = input(
            "Please enter from the box [effort/distraction/combined]: ").strip().lower()
    return mode


def optimal_path(graph, start, goal, mode, visited=None, path=None, effort=0, distraction=0):
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
            result = optimal_path(graph, neighbor, goal, mode, visited.copy(),
                                  path + [neighbor], new_effort, new_distraction)

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
                        if (result[0] - result[1]) < (best_result[0] - best_result[1]):
                            best_result = result

    return best_result


if __name__ == "__main__":
    print("----- Testing section -----\n")

    print("Test 1: Greedy Approach")
    cat, house = positions()
    cur_pos, dis_num = greedy_ansatz(graph, cat, house)
    print(
        f"Greedy result -> final destination: {cur_pos}, distraction: {dis_num}\n")

    print("Test 2: Optimal Path")
    mode = mode_choice()
    result = optimal_path(graph, cat, house, mode=mode)
    if result is None:
        print("No path found (optimal_path returned None).")
    else:
        effort, distraction, path = result
        print(
            f"Optimal ({mode}) -> effort: {effort}, distraction: {distraction}, path: {path}\n")

    print("----- End of Testing -----")

