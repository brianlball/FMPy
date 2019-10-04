from .libraries import sundials_sunlinsoldense
from .sundials_linearsolver import *
from .sundials_matrix import *
from .sundials_nvector import *

# #include <sundials/sundials_linearsolver.h>
# #include <sundials/sundials_matrix.h>
# #include <sundials/sundials_nvector.h>
# #include <sundials/sundials_dense.h>
# #include <sunmatrix/sunmatrix_dense.h>
#
# #ifdef __cplusplus  /* wrapper to enable C++ usage */
# extern "C" {
# #endif
#
# /* ----------------------------------------
#  * Dense Implementation of SUNLinearSolver
#  * ---------------------------------------- */
#
# struct _SUNLinearSolverContent_Dense {
#   sunindextype N;
#   sunindextype *pivots;
#   long int last_flag;
# };
#
# typedef struct _SUNLinearSolverContent_Dense *SUNLinearSolverContent_Dense;
#
# /* ----------------------------------------
#  * Exported Functions for SUNLINSOL_DENSE
#  * ---------------------------------------- */
#
# SUNDIALS_EXPORT SUNLinearSolver SUNLinSol_Dense(N_Vector y, SUNMatrix A);
SUNLinSol_Dense = getattr(sundials_sunlinsoldense, 'SUNLinSol_Dense')
SUNLinSol_Dense.argtypes = [N_Vector, SUNMatrix]
SUNLinSol_Dense.restype = SUNLinearSolver
#
# /* deprecated */
# SUNDIALS_EXPORT SUNLinearSolver SUNDenseLinearSolver(N_Vector y,
#                                                      SUNMatrix A);
#
# SUNDIALS_EXPORT SUNLinearSolver_Type SUNLinSolGetType_Dense(SUNLinearSolver S);
# SUNDIALS_EXPORT int SUNLinSolInitialize_Dense(SUNLinearSolver S);
# SUNDIALS_EXPORT int SUNLinSolSetup_Dense(SUNLinearSolver S, SUNMatrix A);
# SUNDIALS_EXPORT int SUNLinSolSolve_Dense(SUNLinearSolver S, SUNMatrix A,
#                                          N_Vector x, N_Vector b, realtype tol);
# SUNDIALS_EXPORT long int SUNLinSolLastFlag_Dense(SUNLinearSolver S);
# SUNDIALS_EXPORT int SUNLinSolSpace_Dense(SUNLinearSolver S,
#                                          long int *lenrwLS,
#                                          long int *leniwLS);
# SUNDIALS_EXPORT int SUNLinSolFree_Dense(SUNLinearSolver S);
