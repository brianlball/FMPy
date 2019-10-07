from .sundials_nvector import *
from .sundials_types import sunindextype, booleantype, realtype
from .libraries import sundials_nvecserial

# #include <stdio.h>
# #include <sundials/sundials_nvector.h>
#
# #ifdef __cplusplus  /* wrapper to enable C++ usage */
# extern "C" {
# #endif
#
# /*
#  * -----------------------------------------------------------------
#  * SERIAL implementation of N_Vector
#  * -----------------------------------------------------------------
#  */
#
# struct _N_VectorContent_Serial {
#   sunindextype length;   /* vector length       */
#   booleantype own_data;  /* data ownership flag */
#   realtype *data;        /* data array          */
# };
class _N_VectorContent_Serial(Structure):
    _fields_ = [('length',   sunindextype),
                ('own_data', booleantype),
                ('data',     POINTER(realtype))]
#
# typedef struct _N_VectorContent_Serial *N_VectorContent_Serial;
N_VectorContent_Serial = POINTER(_N_VectorContent_Serial)
#
# /*
#  * -----------------------------------------------------------------
#  * Macros NV_CONTENT_S, NV_DATA_S, NV_OWN_DATA_S,
#  *        NV_LENGTH_S, and NV_Ith_S
#  * -----------------------------------------------------------------
#  */
#
# #define NV_CONTENT_S(v)  ( (N_VectorContent_Serial)(v->content) )
def NV_CONTENT_S(v):
    return cast(v.contents.content, N_VectorContent_Serial)
#
# #define NV_LENGTH_S(v)   ( NV_CONTENT_S(v)->length )
#
# #define NV_OWN_DATA_S(v) ( NV_CONTENT_S(v)->own_data )
#
# #define NV_DATA_S(v)     ( NV_CONTENT_S(v)->data )
def NV_DATA_S(v):
    return NV_CONTENT_S(v).contents.data
#
# #define NV_Ith_S(v,i)    ( NV_DATA_S(v)[i] )
#
# /*
#  * -----------------------------------------------------------------
#  * Functions exported by nvector_serial
#  * -----------------------------------------------------------------
#  */
#
# SUNDIALS_EXPORT N_Vector N_VNew_Serial(sunindextype vec_length);
N_VNew_Serial = getattr(sundials_nvecserial, 'N_VNew_Serial')
N_VNew_Serial.argtypes = [c_long]
N_VNew_Serial.restype = N_Vector
#
# SUNDIALS_EXPORT N_Vector N_VNewEmpty_Serial(sunindextype vec_length);
#
# SUNDIALS_EXPORT N_Vector N_VMake_Serial(sunindextype vec_length, realtype *v_data);
#
# SUNDIALS_EXPORT N_Vector *N_VCloneVectorArray_Serial(int count, N_Vector w);
#
# SUNDIALS_EXPORT N_Vector *N_VCloneVectorArrayEmpty_Serial(int count, N_Vector w);
#
# SUNDIALS_EXPORT void N_VDestroyVectorArray_Serial(N_Vector *vs, int count);
#
# SUNDIALS_EXPORT sunindextype N_VGetLength_Serial(N_Vector v);
#
# SUNDIALS_EXPORT void N_VPrint_Serial(N_Vector v);
#
# SUNDIALS_EXPORT void N_VPrintFile_Serial(N_Vector v, FILE *outfile);
#
# SUNDIALS_EXPORT N_Vector_ID N_VGetVectorID_Serial(N_Vector v);
# SUNDIALS_EXPORT N_Vector N_VCloneEmpty_Serial(N_Vector w);
# SUNDIALS_EXPORT N_Vector N_VClone_Serial(N_Vector w);
# SUNDIALS_EXPORT void N_VDestroy_Serial(N_Vector v);
N_VDestroy_Serial = getattr(sundials_nvecserial, 'N_VDestroy_Serial')
N_VDestroy_Serial.argtypes = [N_Vector]
N_VDestroy_Serial.restype = None
# SUNDIALS_EXPORT void N_VSpace_Serial(N_Vector v, sunindextype *lrw, sunindextype *liw);
# SUNDIALS_EXPORT realtype *N_VGetArrayPointer_Serial(N_Vector v);
# SUNDIALS_EXPORT void N_VSetArrayPointer_Serial(realtype *v_data, N_Vector v);
#
# /* standard vector operations */
# SUNDIALS_EXPORT void N_VLinearSum_Serial(realtype a, N_Vector x, realtype b, N_Vector y, N_Vector z);
# SUNDIALS_EXPORT void N_VConst_Serial(realtype c, N_Vector z);
# SUNDIALS_EXPORT void N_VProd_Serial(N_Vector x, N_Vector y, N_Vector z);
# SUNDIALS_EXPORT void N_VDiv_Serial(N_Vector x, N_Vector y, N_Vector z);
# SUNDIALS_EXPORT void N_VScale_Serial(realtype c, N_Vector x, N_Vector z);
# SUNDIALS_EXPORT void N_VAbs_Serial(N_Vector x, N_Vector z);
# SUNDIALS_EXPORT void N_VInv_Serial(N_Vector x, N_Vector z);
# SUNDIALS_EXPORT void N_VAddConst_Serial(N_Vector x, realtype b, N_Vector z);
# SUNDIALS_EXPORT realtype N_VDotProd_Serial(N_Vector x, N_Vector y);
# SUNDIALS_EXPORT realtype N_VMaxNorm_Serial(N_Vector x);
# SUNDIALS_EXPORT realtype N_VWrmsNorm_Serial(N_Vector x, N_Vector w);
# SUNDIALS_EXPORT realtype N_VWrmsNormMask_Serial(N_Vector x, N_Vector w, N_Vector id);
# SUNDIALS_EXPORT realtype N_VMin_Serial(N_Vector x);
# SUNDIALS_EXPORT realtype N_VWL2Norm_Serial(N_Vector x, N_Vector w);
# SUNDIALS_EXPORT realtype N_VL1Norm_Serial(N_Vector x);
# SUNDIALS_EXPORT void N_VCompare_Serial(realtype c, N_Vector x, N_Vector z);
# SUNDIALS_EXPORT booleantype N_VInvTest_Serial(N_Vector x, N_Vector z);
# SUNDIALS_EXPORT booleantype N_VConstrMask_Serial(N_Vector c, N_Vector x, N_Vector m);
# SUNDIALS_EXPORT realtype N_VMinQuotient_Serial(N_Vector num, N_Vector denom);
#
# /* fused vector operations */
# SUNDIALS_EXPORT int N_VLinearCombination_Serial(int nvec, realtype* c, N_Vector* V,
#                                                 N_Vector z);
# SUNDIALS_EXPORT int N_VScaleAddMulti_Serial(int nvec, realtype* a, N_Vector x,
#                                             N_Vector* Y, N_Vector* Z);
# SUNDIALS_EXPORT int N_VDotProdMulti_Serial(int nvec, N_Vector x,
#                                            N_Vector *Y, realtype* dotprods);
#
# /* vector array operations */
# SUNDIALS_EXPORT int N_VLinearSumVectorArray_Serial(int nvec,
#                                                    realtype a, N_Vector* X,
#                                                    realtype b, N_Vector* Y,
#                                                    N_Vector* Z);
# SUNDIALS_EXPORT int N_VScaleVectorArray_Serial(int nvec, realtype* c,
#                                                N_Vector* X, N_Vector* Z);
# SUNDIALS_EXPORT int N_VConstVectorArray_Serial(int nvecs, realtype c,
#                                                N_Vector* Z);
# SUNDIALS_EXPORT int N_VWrmsNormVectorArray_Serial(int nvecs, N_Vector* X,
#                                                   N_Vector* W, realtype* nrm);
# SUNDIALS_EXPORT int N_VWrmsNormMaskVectorArray_Serial(int nvecs, N_Vector* X,
#                                                       N_Vector* W, N_Vector id,
#                                                       realtype* nrm);
# SUNDIALS_EXPORT int N_VScaleAddMultiVectorArray_Serial(int nvec, int nsum,
#                                                        realtype* a,
#                                                        N_Vector* X,
#                                                        N_Vector** Y,
#                                                        N_Vector** Z);
# SUNDIALS_EXPORT int N_VLinearCombinationVectorArray_Serial(int nvec, int nsum,
#                                                            realtype* c,
#                                                            N_Vector** X,
#                                                            N_Vector* Z);
#
# /*
#  * -----------------------------------------------------------------
#  * Enable / disable fused vector operations
#  * -----------------------------------------------------------------
#  */
#
# SUNDIALS_EXPORT int N_VEnableFusedOps_Serial(N_Vector v, booleantype tf);
#
# SUNDIALS_EXPORT int N_VEnableLinearCombination_Serial(N_Vector v, booleantype tf);
# SUNDIALS_EXPORT int N_VEnableScaleAddMulti_Serial(N_Vector v, booleantype tf);
# SUNDIALS_EXPORT int N_VEnableDotProdMulti_Serial(N_Vector v, booleantype tf);
#
# SUNDIALS_EXPORT int N_VEnableLinearSumVectorArray_Serial(N_Vector v, booleantype tf);
# SUNDIALS_EXPORT int N_VEnableScaleVectorArray_Serial(N_Vector v, booleantype tf);
# SUNDIALS_EXPORT int N_VEnableConstVectorArray_Serial(N_Vector v, booleantype tf);
# SUNDIALS_EXPORT int N_VEnableWrmsNormVectorArray_Serial(N_Vector v, booleantype tf);
# SUNDIALS_EXPORT int N_VEnableWrmsNormMaskVectorArray_Serial(N_Vector v, booleantype tf);
# SUNDIALS_EXPORT int N_VEnableScaleAddMultiVectorArray_Serial(N_Vector v, booleantype tf);
# SUNDIALS_EXPORT int N_VEnableLinearCombinationVectorArray_Serial(N_Vector v, booleantype tf);
#
# #ifdef __cplusplus
# }
# #endif
#
# #endif
