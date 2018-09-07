The program activity demonstrates how C/C++ or even CUDA codes
can be used in Python scripts. 

1. The ```_pointers.cpp``` file is loaded with the corresponding header file named ```_pointers.h```. The header file is very much important here!
Declaration as ```extern "C"``` is needed in order for the function to be read by the Python API. The compilation using ```nvcc``` is as follows:
```
C:> nvcc _pointers.cpp -shared -o <outputfile.dll>
```

2. Run ```main.py``` to load function from the shared library. The function names can be checked by running ```dumpbin``` for Windows or ```nm``` for Unix.
