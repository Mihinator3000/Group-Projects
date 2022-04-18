from solution import Solution, Point

if __name__ == "__main__":

    start_point = Point(4, -8)
    solution = Solution(start_point, 10 ** -6)
    print(solution.constant_learning_rate_method(0.1))
    print(solution.step_fragmentation_method(0.1, 0.95, 3))
    print(solution.golden_ratio_method())
    print(solution.fibonacci_method())
