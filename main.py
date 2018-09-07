import ctypes 
import numpy as np 

## Create a similar struct 
## as in the .h file
class Points(ctypes.Structure):
	_fields_ = [("m", ctypes.c_float),("t", ctypes.c_float)]

def main():
	## Load the object file using numpy
	lib = np.ctypeslib.load_library('_pointers.dll', '.')
	## Retrieve the function name
	f = lib.frames
	## Initialize input and output 
	f.argtype = [ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.c_int]
	f.restype = ctypes.POINTER(Points)

	## Define inputs
	A = [1.0,2.0,3.0]
	B = [1.0,2.0,3.0]
	
	## Use .cpp function
	array_type = ctypes.c_float * len(A) ## For input pointers
	_result = f(array_type(*A), array_type(*B), ctypes.c_int(len(A)))

	## For pointer outputs in C, use this to convert to list.
	result = _result[:3]

	## Get results
	## Result1: Array of points object
	print(result)
	## Result2: Use each item in list as normal Python object
	for X in result:
		print(X.m,"---", X.t)


if __name__ == "__main__":
	main()