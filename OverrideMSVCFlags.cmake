if (MSVC)
  # link statically against the Visual C runtime
  set(CMAKE_CONFIGURATION_TYPES "Debug;Release" CACHE TYPE INTERNAL FORCE)
  
  string(REPLACE "/MD"  "/MT"  CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE}")
  string(REPLACE "/MDd" "/MTd" CMAKE_C_FLAGS_DEBUG   "${CMAKE_C_FLAGS_DEBUG}")
  message("Updated CMAKE_C_FLAGS_RELEASE:")
  message("${CMAKE_C_FLAGS_RELEASE}")

  string(REPLACE "/MD"  "/MT"  CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE}")
  string(REPLACE "/MDd" "/MTd" CMAKE_CXX_FLAGS_DEBUG   "${CMAKE_CXX_FLAGS_DEBUG}")
  message("Updated CMAKE_CXX_FLAGS_RELEASE:")
  message("${CMAKE_CXX_FLAGS_RELEASE}")
endif ()
