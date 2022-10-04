import unittest
import numpy as np

import restriction as r
import statement as st
import simplex_solution_method as ssm
import file_input_parser as fip


class MyTestCase(unittest.TestCase):
    # TODO: add test cases from statements & test_cases.txt
    def test_case_1(self):
        parser = fip.FileInputParser("input.txt")
        statement, solution_aim = parser.create_statement()

        func_vector, b, vectors, value = statement.create_statement()
        basis = statement.create_basis()
        basis_content = statement.create_basis_content()

        simplex_solution_method = ssm.SimplexSolutionMethod(
            solution_aim,
            func_vector,
            b,
            vectors,
            basis,
            basis_content)

        func_extremum, extremum_coordinates = simplex_solution_method.solve(value)
        print(f'Function extremum: {func_extremum:.3f}')
        print(f'Extremum coordinates: {extremum_coordinates}')

        self.assertEqual(-4, func_extremum)
        self.assertTrue(np.array_equal(np.array([0, 4, 0, 0]), extremum_coordinates))

    def test_case_2(self):
        r_1 = r.Restriction(np.array([1, 2]), r.RestrictionType.LESS, 7)
        r_2 = r.Restriction(np.array([2, 1]), r.RestrictionType.LESS, 8)
        r_3 = r.Restriction(np.array([0, 1]), r.RestrictionType.LESS, 3)
        statement = st.Statement(np.array([-3, -2]), [r_1, r_2, r_3])
        solution_aim = ssm.SolutionAim.MIN

        func_vector, b, vectors, value = statement.create_statement()
        basis = statement.create_basis()
        basis_content = statement.create_basis_content()

        simplex_solution_method = ssm.SimplexSolutionMethod(
            solution_aim,
            func_vector,
            b,
            vectors,
            basis,
            basis_content)

        func_extremum, extremum_coordinates = simplex_solution_method.solve(value)
        print(f'Function extremum: {func_extremum:.3f}')
        print(f'Extremum coordinates: {extremum_coordinates}')

        self.assertEqual(-13, func_extremum)
        self.assertTrue(np.array_equal(np.array([3, 2]), extremum_coordinates))

    def test_case_3(self):
        r_1 = r.Restriction(np.array([3, 2, 5]), r.RestrictionType.LESS, 18)
        r_2 = r.Restriction(np.array([4, 2, 3]), r.RestrictionType.LESS, 16)
        r_3 = r.Restriction(np.array([2, 1, 1]), r.RestrictionType.GREATER, 4)
        statement = st.Statement(np.array([3, 2, 4]), [r_1, r_2, r_3])
        solution_aim = ssm.SolutionAim.MAX

        func_vector, b, vectors, value = statement.create_statement()
        basis = statement.create_basis()
        basis_content = statement.create_basis_content()

        simplex_solution_method = ssm.SimplexSolutionMethod(
            solution_aim,
            func_vector,
            b,
            vectors,
            basis,
            basis_content)

        func_extremum, extremum_coordinates = simplex_solution_method.solve(value)
        print(f'Function extremum: {func_extremum:.3f}')
        print(f'Extremum coordinates: {extremum_coordinates}')

        self.assertEqual(17, func_extremum)
        self.assertTrue(np.array_equal([0, 6.5, 1], extremum_coordinates))


if __name__ == '__main__':
    unittest.main()
