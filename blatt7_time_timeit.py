"""
Docstring for time_and_timeit
this module consists of time and timeit function to record the
processing time for both function (greedy_approach and
optimal_path)
to find which of the function (with the same input) run faster
"""

__author__ = "8407548, Winata, 8655943, Quan"
import time
import timeit
from blatt7_greedyansatz import greedy_approach, optimal_path, graph


def time_result():
    """each start and end comprises of the processing time for both functions.
    the time at the line where time.perf_counter() run got saved as a value
    inside start and end therefor to get the end result (running time),
    both Greedy_time and Optimal_time substract the end value with
    the start value.
    """
    start1 = time.perf_counter()
    greedy_approach(graph, "a", "f", "combined")
    # [(['a', 'b', 'd', 'f'], (10, 11)), (['a', 'c', 'd', 'f'], (6, 7))]
    end1 = time.perf_counter()

    start2 = time.perf_counter()
    optimal_path(graph, "a", "f", "combined")
    # [(10, 11, ['a', 'b', 'd', 'f'])]
    end2 = time.perf_counter()

    print("Greedy time: ", end1 - start1)
    print("Optimal time: ", end2 - start2)


def timeit_result():
    """greedy_times and optimal_times store the value of the timeit
    variation they both each take their respective function
    and run it multiple times.
    for each repetition the function is called 1000 times
    and it get repeated 5 times.
    and then the fastest time (using the min() command) is used for
    the end comparison of both function
    """
    greedy_times = timeit.repeat(
        lambda: greedy_approach(graph, "a", "f", "combined"),
        number=1000,
        repeat=5,
    )

    optimal_times = timeit.repeat(
        lambda: optimal_path(graph, "a", "f", "combined"),
        number=1000,
        repeat=5,
    )

    print("Greedy best:", min(greedy_times))
    print("Optimal best:", min(optimal_times))


time_result()
# Greedy time:  7.479999840143137e-05
# Optimal time:  5.500000042957254e-05
timeit_result()
# Greedy best: 0.04030369999964023
# Optimal best: 0.04135060000044177

"""Result :
when comparing each method, the greedy method run faster than
optimal method in both time and timeit function, but if we comparing
the result between time and timeit then time have significantly
faster run time than timeit but because timeit run 1000x per repetition
that means the result should be devided by 1000 to find the run time
of each function which would show that, timeit would actually
be faster than time.
"""
