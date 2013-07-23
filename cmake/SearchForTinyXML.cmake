find_library(tinyxml_library tinyxml)
if (tinyxml_library)
  message (STATUS "Looking for libtinyxml - found")
  set(tinyxml_LIBRARIES ${tinyxml_library})
endif ()

find_path(tinyxml_INCLUDE_DIRS NAMES tinyxml.h PATH_SUFFIXES tinyxml)
if (NOT tinyxml_INCLUDE_DIRS)
   message (STATUS "Looking for tinyxml/tinyxml.hpp or tinyxml/tinyxml.h - not found.")
endif ()

if (NOT tinyxml_INCLUDE_DIRS OR NOT tinyxml_LIBRARIES)
   include (FindPkgConfig)
   if (PKG_CONFIG_FOUND)
     # Find tinyxml
     pkg_check_modules(tinyxml tinyxml)
   else()
     MESSAGE("Missing: tinyxml")
   endif()
endif ()
