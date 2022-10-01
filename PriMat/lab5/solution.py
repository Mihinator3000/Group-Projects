import numpy as np

import restriction as r
import statement as st
import simplex_solution_method as ssm

if __name__ == '__main__':
    # CASE 1
    r_1 = r.Restriction(np.array([1, -1]), r.RestrictionType.LESS, 3)
    r_2 = r.Restriction(np.array([3, -4]), r.RestrictionType.GREATER, -12)
    r_3 = r.Restriction(np.array([1, 0]), r.RestrictionType.LESS, 5)
    statement = st.Statement(np.array([-1, 2]), [r_1, r_2, r_3])

    # CASE 2
    # r_1 = r.Restriction(np.array([1, 2]), r.RestrictionType.LESS, 7)
    # r_2 = r.Restriction(np.array([2, 1]), r.RestrictionType.LESS, 8)
    # r_3 = r.Restriction(np.array([0, 1]), r.RestrictionType.LESS, 3)
    # statement = st.Statement(np.array([-3, -2]), [r_1, r_2, r_3])

    # CASE 3
    # r_1 = r.Restriction(np.array([1, 2]), r.RestrictionType.LESS, 4)
    # r_2 = r.Restriction(np.array([1, -1]), r.RestrictionType.GREATER, 1)
    # r_3 = r.Restriction(np.array([1, 1]), r.RestrictionType.LESS, 8)
    # statement = st.Statement(np.array([-1, 3]), [r_1, r_2, r_3])

    # CASE 4
    # r_1 = r.Restriction(np.array([4, 1]), r.RestrictionType.LESS, 8)
    # r_2 = r.Restriction(np.array([1, -1]), r.RestrictionType.GREATER, -3)
    # statement = st.Statement(np.array([3, 4]), [r_1, r_2])

    # TODO: add test cases from statements
    # TODO: implement input from file

    func_vector, b, vectors = statement.create_statement_vectors()
    basis = statement.create_basis()
    basis_content = statement.create_basis_content()

    simplex_solution_method = ssm.SimplexSolutionMethod(
        ssm.SolutionAim.MIN,
        func_vector,
        b,
        vectors,
        basis,
        basis_content)

    v, z = simplex_solution_method.solve()
    print(v, z)
