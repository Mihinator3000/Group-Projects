import numpy as np

import entities.restriction as r
import entities.statement as s
import solution_methods.simplex_solution_method as ssm


def main():
    r_1 = r.Restriction(np.array([1, 2]), r.RestrictionType.LESS, 7)
    r_2 = r.Restriction(np.array([2, 1]), r.RestrictionType.LESS, 8)
    r_3 = r.Restriction(np.array([0, 1]), r.RestrictionType.LESS, 3)
    statement = s.Statement(np.array([-3, -2]), [r_1, r_2, r_3])
    solution_aim = ssm.SolutionAim.MIN

    func_vector, right_hand_side, vectors, value = statement.create_statement()
    basis = statement.create_basis()
    basis_content = statement.create_basis_content()

    simplex_solution_method = ssm.SimplexSolutionMethod(
        solution_aim,
        func_vector,
        right_hand_side,
        vectors,
        basis,
        basis_content)

    func_extremum, extremum_coordinates = simplex_solution_method.solve(value)

    print(f'Function extremum: {func_extremum:.3f}')
    print(f'Extremum coordinates: {extremum_coordinates.tolist()}')


if __name__ == '__main__':
    main()
