# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = C:/Users/Aaron/AppData/Local/Programs/Python/Python37/Lib/site-packages/cmake/data/bin/cmake.exe

# The command to remove a file.
RM = C:/Users/Aaron/AppData/Local/Programs/Python/Python37/Lib/site-packages/cmake/data/bin/cmake.exe -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = C:/Users/Aaron/Desktop/Nanobiology/MSc/MEP/forecast-indelphi-exploratory-analysis/FORECasT/FORECasT_data/indel_analysis/indelmap

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = C:/Users/Aaron/Desktop/Nanobiology/MSc/MEP/forecast-indelphi-exploratory-analysis/FORECasT/FORECasT_data/indel_analysis/indelmap

# Include any dependencies generated for this target.
include CMakeFiles/indelmap.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/indelmap.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/indelmap.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/indelmap.dir/flags.make

CMakeFiles/indelmap.dir/indel.cpp.obj: CMakeFiles/indelmap.dir/flags.make
CMakeFiles/indelmap.dir/indel.cpp.obj: CMakeFiles/indelmap.dir/includes_CXX.rsp
CMakeFiles/indelmap.dir/indel.cpp.obj: indel.cpp
CMakeFiles/indelmap.dir/indel.cpp.obj: CMakeFiles/indelmap.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:/Users/Aaron/Desktop/Nanobiology/MSc/MEP/forecast-indelphi-exploratory-analysis/FORECasT/FORECasT_data/indel_analysis/indelmap/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/indelmap.dir/indel.cpp.obj"
	C:/msys64/mingw64/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/indelmap.dir/indel.cpp.obj -MF CMakeFiles/indelmap.dir/indel.cpp.obj.d -o CMakeFiles/indelmap.dir/indel.cpp.obj -c C:/Users/Aaron/Desktop/Nanobiology/MSc/MEP/forecast-indelphi-exploratory-analysis/FORECasT/FORECasT_data/indel_analysis/indelmap/indel.cpp

CMakeFiles/indelmap.dir/indel.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/indelmap.dir/indel.cpp.i"
	C:/msys64/mingw64/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E C:/Users/Aaron/Desktop/Nanobiology/MSc/MEP/forecast-indelphi-exploratory-analysis/FORECasT/FORECasT_data/indel_analysis/indelmap/indel.cpp > CMakeFiles/indelmap.dir/indel.cpp.i

CMakeFiles/indelmap.dir/indel.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/indelmap.dir/indel.cpp.s"
	C:/msys64/mingw64/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S C:/Users/Aaron/Desktop/Nanobiology/MSc/MEP/forecast-indelphi-exploratory-analysis/FORECasT/FORECasT_data/indel_analysis/indelmap/indel.cpp -o CMakeFiles/indelmap.dir/indel.cpp.s

CMakeFiles/indelmap.dir/oligo.cpp.obj: CMakeFiles/indelmap.dir/flags.make
CMakeFiles/indelmap.dir/oligo.cpp.obj: CMakeFiles/indelmap.dir/includes_CXX.rsp
CMakeFiles/indelmap.dir/oligo.cpp.obj: oligo.cpp
CMakeFiles/indelmap.dir/oligo.cpp.obj: CMakeFiles/indelmap.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:/Users/Aaron/Desktop/Nanobiology/MSc/MEP/forecast-indelphi-exploratory-analysis/FORECasT/FORECasT_data/indel_analysis/indelmap/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/indelmap.dir/oligo.cpp.obj"
	C:/msys64/mingw64/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/indelmap.dir/oligo.cpp.obj -MF CMakeFiles/indelmap.dir/oligo.cpp.obj.d -o CMakeFiles/indelmap.dir/oligo.cpp.obj -c C:/Users/Aaron/Desktop/Nanobiology/MSc/MEP/forecast-indelphi-exploratory-analysis/FORECasT/FORECasT_data/indel_analysis/indelmap/oligo.cpp

CMakeFiles/indelmap.dir/oligo.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/indelmap.dir/oligo.cpp.i"
	C:/msys64/mingw64/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E C:/Users/Aaron/Desktop/Nanobiology/MSc/MEP/forecast-indelphi-exploratory-analysis/FORECasT/FORECasT_data/indel_analysis/indelmap/oligo.cpp > CMakeFiles/indelmap.dir/oligo.cpp.i

CMakeFiles/indelmap.dir/oligo.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/indelmap.dir/oligo.cpp.s"
	C:/msys64/mingw64/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S C:/Users/Aaron/Desktop/Nanobiology/MSc/MEP/forecast-indelphi-exploratory-analysis/FORECasT/FORECasT_data/indel_analysis/indelmap/oligo.cpp -o CMakeFiles/indelmap.dir/oligo.cpp.s

CMakeFiles/indelmap.dir/readmap.cpp.obj: CMakeFiles/indelmap.dir/flags.make
CMakeFiles/indelmap.dir/readmap.cpp.obj: CMakeFiles/indelmap.dir/includes_CXX.rsp
CMakeFiles/indelmap.dir/readmap.cpp.obj: readmap.cpp
CMakeFiles/indelmap.dir/readmap.cpp.obj: CMakeFiles/indelmap.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:/Users/Aaron/Desktop/Nanobiology/MSc/MEP/forecast-indelphi-exploratory-analysis/FORECasT/FORECasT_data/indel_analysis/indelmap/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object CMakeFiles/indelmap.dir/readmap.cpp.obj"
	C:/msys64/mingw64/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/indelmap.dir/readmap.cpp.obj -MF CMakeFiles/indelmap.dir/readmap.cpp.obj.d -o CMakeFiles/indelmap.dir/readmap.cpp.obj -c C:/Users/Aaron/Desktop/Nanobiology/MSc/MEP/forecast-indelphi-exploratory-analysis/FORECasT/FORECasT_data/indel_analysis/indelmap/readmap.cpp

CMakeFiles/indelmap.dir/readmap.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/indelmap.dir/readmap.cpp.i"
	C:/msys64/mingw64/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E C:/Users/Aaron/Desktop/Nanobiology/MSc/MEP/forecast-indelphi-exploratory-analysis/FORECasT/FORECasT_data/indel_analysis/indelmap/readmap.cpp > CMakeFiles/indelmap.dir/readmap.cpp.i

CMakeFiles/indelmap.dir/readmap.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/indelmap.dir/readmap.cpp.s"
	C:/msys64/mingw64/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S C:/Users/Aaron/Desktop/Nanobiology/MSc/MEP/forecast-indelphi-exploratory-analysis/FORECasT/FORECasT_data/indel_analysis/indelmap/readmap.cpp -o CMakeFiles/indelmap.dir/readmap.cpp.s

CMakeFiles/indelmap.dir/gen.cpp.obj: CMakeFiles/indelmap.dir/flags.make
CMakeFiles/indelmap.dir/gen.cpp.obj: CMakeFiles/indelmap.dir/includes_CXX.rsp
CMakeFiles/indelmap.dir/gen.cpp.obj: gen.cpp
CMakeFiles/indelmap.dir/gen.cpp.obj: CMakeFiles/indelmap.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:/Users/Aaron/Desktop/Nanobiology/MSc/MEP/forecast-indelphi-exploratory-analysis/FORECasT/FORECasT_data/indel_analysis/indelmap/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object CMakeFiles/indelmap.dir/gen.cpp.obj"
	C:/msys64/mingw64/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/indelmap.dir/gen.cpp.obj -MF CMakeFiles/indelmap.dir/gen.cpp.obj.d -o CMakeFiles/indelmap.dir/gen.cpp.obj -c C:/Users/Aaron/Desktop/Nanobiology/MSc/MEP/forecast-indelphi-exploratory-analysis/FORECasT/FORECasT_data/indel_analysis/indelmap/gen.cpp

CMakeFiles/indelmap.dir/gen.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/indelmap.dir/gen.cpp.i"
	C:/msys64/mingw64/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E C:/Users/Aaron/Desktop/Nanobiology/MSc/MEP/forecast-indelphi-exploratory-analysis/FORECasT/FORECasT_data/indel_analysis/indelmap/gen.cpp > CMakeFiles/indelmap.dir/gen.cpp.i

CMakeFiles/indelmap.dir/gen.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/indelmap.dir/gen.cpp.s"
	C:/msys64/mingw64/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S C:/Users/Aaron/Desktop/Nanobiology/MSc/MEP/forecast-indelphi-exploratory-analysis/FORECasT/FORECasT_data/indel_analysis/indelmap/gen.cpp -o CMakeFiles/indelmap.dir/gen.cpp.s

CMakeFiles/indelmap.dir/indelmap.cpp.obj: CMakeFiles/indelmap.dir/flags.make
CMakeFiles/indelmap.dir/indelmap.cpp.obj: CMakeFiles/indelmap.dir/includes_CXX.rsp
CMakeFiles/indelmap.dir/indelmap.cpp.obj: indelmap.cpp
CMakeFiles/indelmap.dir/indelmap.cpp.obj: CMakeFiles/indelmap.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:/Users/Aaron/Desktop/Nanobiology/MSc/MEP/forecast-indelphi-exploratory-analysis/FORECasT/FORECasT_data/indel_analysis/indelmap/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building CXX object CMakeFiles/indelmap.dir/indelmap.cpp.obj"
	C:/msys64/mingw64/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/indelmap.dir/indelmap.cpp.obj -MF CMakeFiles/indelmap.dir/indelmap.cpp.obj.d -o CMakeFiles/indelmap.dir/indelmap.cpp.obj -c C:/Users/Aaron/Desktop/Nanobiology/MSc/MEP/forecast-indelphi-exploratory-analysis/FORECasT/FORECasT_data/indel_analysis/indelmap/indelmap.cpp

CMakeFiles/indelmap.dir/indelmap.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/indelmap.dir/indelmap.cpp.i"
	C:/msys64/mingw64/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E C:/Users/Aaron/Desktop/Nanobiology/MSc/MEP/forecast-indelphi-exploratory-analysis/FORECasT/FORECasT_data/indel_analysis/indelmap/indelmap.cpp > CMakeFiles/indelmap.dir/indelmap.cpp.i

CMakeFiles/indelmap.dir/indelmap.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/indelmap.dir/indelmap.cpp.s"
	C:/msys64/mingw64/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S C:/Users/Aaron/Desktop/Nanobiology/MSc/MEP/forecast-indelphi-exploratory-analysis/FORECasT/FORECasT_data/indel_analysis/indelmap/indelmap.cpp -o CMakeFiles/indelmap.dir/indelmap.cpp.s

# Object files for target indelmap
indelmap_OBJECTS = \
"CMakeFiles/indelmap.dir/indel.cpp.obj" \
"CMakeFiles/indelmap.dir/oligo.cpp.obj" \
"CMakeFiles/indelmap.dir/readmap.cpp.obj" \
"CMakeFiles/indelmap.dir/gen.cpp.obj" \
"CMakeFiles/indelmap.dir/indelmap.cpp.obj"

# External object files for target indelmap
indelmap_EXTERNAL_OBJECTS =

indelmap.exe: CMakeFiles/indelmap.dir/indel.cpp.obj
indelmap.exe: CMakeFiles/indelmap.dir/oligo.cpp.obj
indelmap.exe: CMakeFiles/indelmap.dir/readmap.cpp.obj
indelmap.exe: CMakeFiles/indelmap.dir/gen.cpp.obj
indelmap.exe: CMakeFiles/indelmap.dir/indelmap.cpp.obj
indelmap.exe: CMakeFiles/indelmap.dir/build.make
indelmap.exe: CMakeFiles/indelmap.dir/linklibs.rsp
indelmap.exe: CMakeFiles/indelmap.dir/objects1.rsp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=C:/Users/Aaron/Desktop/Nanobiology/MSc/MEP/forecast-indelphi-exploratory-analysis/FORECasT/FORECasT_data/indel_analysis/indelmap/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Linking CXX executable indelmap.exe"
	C:/Users/Aaron/AppData/Local/Programs/Python/Python37/Lib/site-packages/cmake/data/bin/cmake.exe -E rm -f CMakeFiles/indelmap.dir/objects.a
	C:/msys64/mingw64/bin/ar.exe qc CMakeFiles/indelmap.dir/objects.a @CMakeFiles/indelmap.dir/objects1.rsp
	C:/msys64/mingw64/bin/c++.exe -Wl,--whole-archive CMakeFiles/indelmap.dir/objects.a -Wl,--no-whole-archive -o indelmap.exe -Wl,--out-implib,libindelmap.dll.a -Wl,--major-image-version,0,--minor-image-version,0 @CMakeFiles/indelmap.dir/linklibs.rsp

# Rule to build all files generated by this target.
CMakeFiles/indelmap.dir/build: indelmap.exe
.PHONY : CMakeFiles/indelmap.dir/build

CMakeFiles/indelmap.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/indelmap.dir/cmake_clean.cmake
.PHONY : CMakeFiles/indelmap.dir/clean

CMakeFiles/indelmap.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" C:/Users/Aaron/Desktop/Nanobiology/MSc/MEP/forecast-indelphi-exploratory-analysis/FORECasT/FORECasT_data/indel_analysis/indelmap C:/Users/Aaron/Desktop/Nanobiology/MSc/MEP/forecast-indelphi-exploratory-analysis/FORECasT/FORECasT_data/indel_analysis/indelmap C:/Users/Aaron/Desktop/Nanobiology/MSc/MEP/forecast-indelphi-exploratory-analysis/FORECasT/FORECasT_data/indel_analysis/indelmap C:/Users/Aaron/Desktop/Nanobiology/MSc/MEP/forecast-indelphi-exploratory-analysis/FORECasT/FORECasT_data/indel_analysis/indelmap C:/Users/Aaron/Desktop/Nanobiology/MSc/MEP/forecast-indelphi-exploratory-analysis/FORECasT/FORECasT_data/indel_analysis/indelmap/CMakeFiles/indelmap.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/indelmap.dir/depend
