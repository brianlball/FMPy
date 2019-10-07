from .sundials_types import *
from .sundials_matrix import *
import os
from fmpy import sharedLibraryExtension

library_dir, _ = os.path.split(__file__)
sundials_sunmatrixdense = cdll.LoadLibrary(os.path.join(library_dir, 'sundials_sunmatrixdense' + sharedLibraryExtension))


# #include <stdio.h>
# #include <sundials/sundials_matrix.h>
#
# #ifdef __cplusplus  /* wrapper to enable C++ usage */
# extern "C" {
# #endif
#
# /* ----------------------------------
#  * Dense implementation of SUNMatrix
#  * ---------------------------------- */
#
# struct _SUNMatrixContent_Dense {
#   sunindextype M;
#   sunindextype N;
#   realtype *data;
#   sunindextype ldata;
#   realtype **cols;
# };
#
# typedef struct _SUNMatrixContent_Dense *SUNMatrixContent_Dense;
#
# /* ------------------------------------
#  * Macros for access to SUNMATRIX_DENSE
#  * ------------------------------------ */
#
# #define SM_CONTENT_D(A)     ( (SUNMatrixContent_Dense)(A->content) )
#
# #define SM_ROWS_D(A)        ( SM_CONTENT_D(A)->M )
#
# #define SM_COLUMNS_D(A)     ( SM_CONTENT_D(A)->N )
#
# #define SM_LDATA_D(A)       ( SM_CONTENT_D(A)->ldata )
#
# #define SM_DATA_D(A)        ( SM_CONTENT_D(A)->data )
#
# #define SM_COLS_D(A)        ( SM_CONTENT_D(A)->cols )
#
# #define SM_COLUMN_D(A,j)    ( (SM_CONTENT_D(A)->cols)[j] )
#
# #define SM_ELEMENT_D(A,i,j) ( (SM_CONTENT_D(A)->cols)[j][i] )
#
# /* ---------------------------------------
#  * Exported Functions for SUNMATRIX_DENSE
#  * --------------------------------------- */
#
# SUNDIALS_EXPORT SUNMatrix SUNDenseMatrix(sunindextype M, sunindextype N);
SUNDenseMatrix = getattr(sundials_sunmatrixdense, 'SUNDenseMatrix')
SUNDenseMatrix.argtypes = [sunindextype, sunindextype]
SUNDenseMatrix.restype = SUNMatrix
#
# SUNDIALS_EXPORT void SUNDenseMatrix_Print(SUNMatrix A, FILE* outfile);
#
# SUNDIALS_EXPORT sunindextype SUNDenseMatrix_Rows(SUNMatrix A);
# SUNDIALS_EXPORT sunindextype SUNDenseMatrix_Columns(SUNMatrix A);
# SUNDIALS_EXPORT sunindextype SUNDenseMatrix_LData(SUNMatrix A);
# SUNDIALS_EXPORT realtype* SUNDenseMatrix_Data(SUNMatrix A);
# SUNDIALS_EXPORT realtype** SUNDenseMatrix_Cols(SUNMatrix A);
# SUNDIALS_EXPORT realtype* SUNDenseMatrix_Column(SUNMatrix A, sunindextype j);
#
# SUNDIALS_EXPORT SUNMatrix_ID SUNMatGetID_Dense(SUNMatrix A);
# SUNDIALS_EXPORT SUNMatrix SUNMatClone_Dense(SUNMatrix A);
# SUNDIALS_EXPORT void SUNMatDestroy_Dense(SUNMatrix A);
# SUNDIALS_EXPORT int SUNMatZero_Dense(SUNMatrix A);
# SUNDIALS_EXPORT int SUNMatCopy_Dense(SUNMatrix A, SUNMatrix B);
# SUNDIALS_EXPORT int SUNMatScaleAdd_Dense(realtype c, SUNMatrix A, SUNMatrix B);
# SUNDIALS_EXPORT int SUNMatScaleAddI_Dense(realtype c, SUNMatrix A);
# SUNDIALS_EXPORT int SUNMatMatvec_Dense(SUNMatrix A, N_Vector x, N_Vector y);
# SUNDIALS_EXPORT int SUNMatSpace_Dense(SUNMatrix A, long int *lenrw, long int *leniw);
