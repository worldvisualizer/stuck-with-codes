

## Building and Running the Cpp program with NTL

### Important Variables 

CXX=g++              # The C++ compiler

CXXFLAGS=-g -O2      # C++ complilation flags

NATIVE=on            # Compiles code targeted to the current hardware (see below)
TUNE=generic         # performance-tuning switch (see below)
(or x86 or linux-s390x)

DEF_PREFIX=/usr/local# Default software directory

PREFIX=$(DEF_PREFIX) # Directory in which to install NTL library components
SHARED=off           # Generate a shared library (as well as static -- see below)

NTL_THREADS=on       # compile in thread-safe mode (see below)
NTL_THREAD_BOOST=on  # compile with thread boosting enabled (see below)
NTL_EXCEPTIONS=off   # compile with exceptions enabled (see below)

NTL_GMP_LIP=on       # Switch to enable the use of GMP as primary 
                     #   long integer package

GMP_PREFIX=$(DEF_PREFIX) # Directory in which GMP components are installed

NTL_GF2X_LIB=off     # Switch to enable the use of the gf2x package
                     #   for faster arithmetic GF(2)[X]

GF2X_PREFIX=$(DEF_PREFIX) # Directory in which gf2x components are installed

NTL_STD_CXX11=on     # Build assuming C++11 features

NTL_SAFE_VECTORS=on  # build in "safe vector" mode 

