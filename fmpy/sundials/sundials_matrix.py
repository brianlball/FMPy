from ctypes import *

# #include <sundials/sundials_types.h>
# #include <sundials/sundials_nvector.h>
#
# #ifdef __cplusplus  /* wrapper to enable C++ usage */
# extern "C" {
# #endif
#
#
# /* -----------------------------------------------------------------
#  * Implemented SUNMatrix types
#  * ----------------------------------------------------------------- */
#
# typedef enum {
#   SUNMATRIX_DENSE,
#   SUNMATRIX_BAND,
#   SUNMATRIX_SPARSE,
#   SUNMATRIX_CUSTOM
# } SUNMatrix_ID;
#
#
# /* -----------------------------------------------------------------
#  * Generic definition of SUNMatrix
#  * ----------------------------------------------------------------- */
#
# /* Forward reference for pointer to SUNMatrix_Ops object */
# typedef struct _generic_SUNMatrix_Ops *SUNMatrix_Ops;
#
# /* Forward reference for pointer to SUNMatrix object */
# typedef struct _generic_SUNMatrix *SUNMatrix;
SUNMatrix = c_void_p
#
# /* Structure containing function pointers to matrix operations  */
# struct _generic_SUNMatrix_Ops {
#   SUNMatrix_ID (*getid)(SUNMatrix);
#   SUNMatrix    (*clone)(SUNMatrix);
#   void         (*destroy)(SUNMatrix);
#   int          (*zero)(SUNMatrix);
#   int          (*copy)(SUNMatrix, SUNMatrix);
#   int          (*scaleadd)(realtype, SUNMatrix, SUNMatrix);
#   int          (*scaleaddi)(realtype, SUNMatrix);
#   int          (*matvec)(SUNMatrix, N_Vector, N_Vector);
#   int          (*space)(SUNMatrix, long int*, long int*);
# };
#
# /* A matrix is a structure with an implementation-dependent
#    'content' field, and a pointer to a structure of matrix
#    operations corresponding to that implementation.  */
# struct _generic_SUNMatrix {
#   void *content;
#   struct _generic_SUNMatrix_Ops *ops;
# };
#
#
# /* -----------------------------------------------------------------
#  * Functions exported by SUNMatrix module
#  * ----------------------------------------------------------------- */
#
# SUNDIALS_EXPORT SUNMatrix_ID SUNMatGetID(SUNMatrix A);
# SUNDIALS_EXPORT SUNMatrix SUNMatClone(SUNMatrix A);
# SUNDIALS_EXPORT void SUNMatDestroy(SUNMatrix A);
# SUNDIALS_EXPORT int SUNMatZero(SUNMatrix A);
# SUNDIALS_EXPORT int SUNMatCopy(SUNMatrix A, SUNMatrix B);
# SUNDIALS_EXPORT int SUNMatScaleAdd(realtype c, SUNMatrix A, SUNMatrix B);
# SUNDIALS_EXPORT int SUNMatScaleAddI(realtype c, SUNMatrix A);
# SUNDIALS_EXPORT int SUNMatMatvec(SUNMatrix A, N_Vector x, N_Vector y);
# SUNDIALS_EXPORT int SUNMatSpace(SUNMatrix A, long int *lenrw,
#                                 long int *leniw);