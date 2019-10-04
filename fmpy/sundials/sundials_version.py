from ctypes import *
from .libraries import sundials_cvode

# #include <sundials/sundials_config.h>
#
# #ifdef __cplusplus  /* wrapper to enable C++ usage */
# extern "C" {
# #endif
#
# /* Fill a string with SUNDIALS version information */
# SUNDIALS_EXPORT int SUNDIALSGetVersion(char *version, int len);
#
# /* Fills integers with the major, minor, and patch release version numbers and a
#    string with the release label.*/
# SUNDIALS_EXPORT int SUNDIALSGetVersionNumber(int *major, int *minor, int *patch,
#                                              char *label, int len);
SUNDIALSGetVersionNumber = getattr(sundials_cvode, 'SUNDIALSGetVersionNumber')
SUNDIALSGetVersionNumber.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int), c_char_p, c_int]
SUNDIALSGetVersionNumber.restype = c_int
