from ctypes import *

# #ifndef _SUNDIALS_CONFIG_H
# #define _SUNDIALS_CONFIG_H
# #include <sundials/sundials_config.h>
# #endif
#
# #include <float.h>
# #include <stdint.h>
#
# #ifdef __cplusplus  /* wrapper to enable C++ usage */
# extern "C" {
# #endif
#
# /*
#  *------------------------------------------------------------------
#  * Type realtype
#  * Macro RCONST
#  * Constants BIG_REAL, SMALL_REAL, and UNIT_ROUNDOFF
#  *------------------------------------------------------------------
#  */
#
# #if defined(SUNDIALS_SINGLE_PRECISION)
#
# typedef float realtype;
realtype = c_double
# # define RCONST(x) x##F
# # define BIG_REAL FLT_MAX
# # define SMALL_REAL FLT_MIN
# # define UNIT_ROUNDOFF FLT_EPSILON
#
# #elif defined(SUNDIALS_DOUBLE_PRECISION)
#
# typedef double realtype;
# # define RCONST(x) x
# # define BIG_REAL DBL_MAX
# # define SMALL_REAL DBL_MIN
# # define UNIT_ROUNDOFF DBL_EPSILON
#
# #elif defined(SUNDIALS_EXTENDED_PRECISION)
#
# typedef long double realtype;
# # define RCONST(x) x##L
# # define BIG_REAL LDBL_MAX
# # define SMALL_REAL LDBL_MIN
# # define UNIT_ROUNDOFF LDBL_EPSILON
#
# #endif
#
#
# /*
#  *------------------------------------------------------------------
#  * Type : sunindextype
#  *------------------------------------------------------------------
#  * Defines integer type to be used for vector and matrix indices.
#  * User can build sundials to use 32- or 64-bit signed integers.
#  * If compiler does not support portable data types, the SUNDIALS
#  * CMake build system tries to find a type of the desired size.
#  *------------------------------------------------------------------
#  */
#
# typedef SUNDIALS_INDEX_TYPE sunindextype;
sunindextype = c_int64
#
# /*
#  *------------------------------------------------------------------
#  * Type : booleantype
#  *------------------------------------------------------------------
#  * Constants : SUNFALSE and SUNTRUE
#  *------------------------------------------------------------------
#  * ANSI C does not have a built-in boolean data type. Below is the
#  * definition for a new type called booleantype. The advantage of
#  * using the name booleantype (instead of int) is an increase in
#  * code readability. It also allows the programmer to make a
#  * distinction between int and boolean data. Variables of type
#  * booleantype are intended to have only the two values SUNFALSE and
#  * SUNTRUE which are defined below to be equal to 0 and 1,
#  * respectively.
#  *------------------------------------------------------------------
#  */
#
# #ifndef booleantype
# #define booleantype int
# #endif
booleantype = c_int
#
#
# #ifndef SUNFALSE
# #define SUNFALSE 0
# #endif
#
# #ifndef SUNTRUE
# #define SUNTRUE 1
# #endif
