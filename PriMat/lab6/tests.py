import unittest
import numpy as np

from lab5.entities.restriction import Restriction, RestrictionType
from lab5.entities.statement import Statement
from lab5.solution_methods.simplex_solution_method import SimplexSolutionMethod, SolutionAim
from lab6.game_solution_methods.minimax_method import MinimaxMethod


class Tests(unittest.TestCase):
    def setUp(self) -> None:
        np.seterr(all="ignore")

    def test_case_1(self):
        matrix = np.array([[90.0, 76.5, 91.5, 91.5],
                           [103.5, 90.0, 91.5, 103.5],
                           [88.5, 88.5, 90.0, 103.5],
                           [88.5, 76.5, 76.5, 90.0]])

        minimax_method = MinimaxMethod(matrix)
        minimax_method.solve()
        print(minimax_method.solution)
        self.assertTrue(minimax_method.has_saddle_point(), True)

    def test_case_2(self):
        r_1 = Restriction(np.array([1, 0, 1, 0]), RestrictionType.EQUAL, 230)
        r_2 = Restriction(np.array([0, 1, 0, 1]), RestrictionType.EQUAL, 68)
        r_3 = Restriction(np.array([1 / 10, 1 / 12, 0, 0]), RestrictionType.LESS, 24)
        r_4 = Restriction(np.array([0, 0, 1 / 13, 1 / 13]), RestrictionType.LESS, 24)
        input_basis = np.ones(4) * 1000
        statement = Statement(np.array([8, 7, 12, 13]), [r_1, r_2, r_3, r_4], 0, input_basis)

        solution_aim = SolutionAim.MIN

        func_extremum, extremum_coordinates = Tests.simplex_solution_method_solve(statement, solution_aim)
        print(func_extremum)
        print(extremum_coordinates)

    def test_case_4(self):
        input_basis = np.ones(2) * 1000
        r_1 = Restriction(np.array([4, 2]), RestrictionType.GREATER, 1)
        r_2 = Restriction(np.array([2, 3]), RestrictionType.GREATER, 1)
        statement_1 = Statement(np.array([1, 1]), [r_1, r_2], 0, input_basis)
        solution_aim_1 = SolutionAim.MIN
        func_extremum_1, extremum_coordinates_1 = Tests.simplex_solution_method_solve(statement_1, solution_aim_1)
        print(func_extremum_1)
        print(extremum_coordinates_1)

        r_3 = Restriction(np.array([4, 2]), RestrictionType.LESS, 1)
        r_4 = Restriction(np.array([2, 3]), RestrictionType.LESS, 1)
        statement_2 = Statement(np.array([1, 1]), [r_3, r_4])
        solution_aim_2 = SolutionAim.MAX
        func_extremum_2, extremum_coordinates_2 = Tests.simplex_solution_method_solve(statement_2, solution_aim_2)
        print(func_extremum_2)
        print(extremum_coordinates_2)

    @staticmethod
    def simplex_solution_method_solve(statement: Statement, solution_aim: SolutionAim) -> (float, np.array):
        func_vector, right_hand_side, vectors, value = statement.create_statement()
        basis = statement.create_basis()
        basis_content = statement.create_basis_content()

        simplex_solution_method = SimplexSolutionMethod(
            solution_aim,
            func_vector,
            right_hand_side,
            vectors,
            basis,
            basis_content)

        func_extremum, extremum_coordinates = simplex_solution_method.solve(value)
        return func_extremum, extremum_coordinates


if __name__ == '__main__':
    unittest.main()
