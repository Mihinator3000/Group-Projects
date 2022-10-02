import numpy as np

import restriction as r
import statement as st
import simplex_solution_method as ssm

if __name__ == '__main__':
    # CASE 1
    # r_1 = r.Restriction(np.array([1, 2]), r.RestrictionType.LESS, 7)
    # r_2 = r.Restriction(np.array([2, 1]), r.RestrictionType.LESS, 8)
    # r_3 = r.Restriction(np.array([0, 1]), r.RestrictionType.LESS, 3)
    # statement = st.Statement(np.array([-3, -2]), [r_1, r_2, r_3])
    # solution_aim = ssm.SolutionAim.MIN

    # CASE 2
    # r_1 = r.Restriction(np.array([1, 1]), r.RestrictionType.GREATER, 1)
    # r_2 = r.Restriction(np.array([2, -1]), r.RestrictionType.GREATER, -1)
    # r_3 = r.Restriction(np.array([1, -2]), r.RestrictionType.LESS, 0)
    # statement = st.Statement(np.array([-1, -2]), [r_1, r_2, r_3])
    # solution_aim = ssm.SolutionAim.MIN

    # CASE 3
    # r_1 = r.Restriction(np.array([3, -1, 0, 2, 1]), r.RestrictionType.EQUAL, 5)
    # r_2 = r.Restriction(np.array([2, -3, 1, 2, 1]), r.RestrictionType.EQUAL, 6)
    # r_3 = r.Restriction(np.array([3, -1, 1, 3, 2]), r.RestrictionType.EQUAL, 9)
    # statement = st.Statement(np.array([-5, 4, -3, -1, -5]), [r_1, r_2, r_3])
    # solution_aim = ssm.SolutionAim.MIN

    # CASE 5
    r_1 = r.Restriction(np.array([3, 1, -1, 1]), r.RestrictionType.EQUAL, 4)
    r_2 = r.Restriction(np.array([5, 1, 1, -1]), r.RestrictionType.EQUAL, 4)
    statement = st.Statement(np.array([-6, -1, -4, 5]), [r_1, r_2])
    solution_aim = ssm.SolutionAim.MIN

    # CASE 6
    # r_1 = r.Restriction(np.array([1, 3]), r.RestrictionType.LESS, 200)
    # r_2 = r.Restriction(np.array([1, 1]), r.RestrictionType.EQUAL, 80)
    # statement = st.Statement(np.array([1, 2]), [r_1, r_2])

    # CASE 7
    # r_1 = r.Restriction(np.array([3, 2, 5]), r.RestrictionType.LESS, 18)
    # r_2 = r.Restriction(np.array([4, 2, 3]), r.RestrictionType.LESS, 16)
    # r_3 = r.Restriction(np.array([2, 1, 1]), r.RestrictionType.GREATER, 4)
    # statement = st.Statement(np.array([3, 2, 4]), [r_1, r_2, r_3])
    # TODO: add test cases from statements
    # TODO: implement input from file

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

    v, z = simplex_solution_method.solve(value)
    print(v, z)
