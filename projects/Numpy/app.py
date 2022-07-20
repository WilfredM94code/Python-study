import numpy as np

# Numpy allows to build arrays

np_array_a = np.array ([0,1,2,3,4])
print ('np_array_a = ',np_array_a)
print ('type(np_array_a) = ',type(np_array_a))
# This method 'array ()' builds a <class 'numpy.ndarray'> object when recieving a list of
# numbers. These numbers can be integers, float and even strings

np_array_b = np.array (['a','b','c'])
print ('np_array_b = ',np_array_b)
print ('type(np_array_b) = ',type(np_array_b))
# This method 'array ()' builds a <class 'numpy.ndarray'> object

shape_a = np_array_a.shape
print ('shape_a = ',shape_a)
print ('type(shape_a) = ',type(shape_a))
# This attribute retuns a tuple with the shape of the array

# To build multidimensional array 'n x m' there has to be passed a constructor argument in this way

np_array_c = np.array ([['a','b','c'],['d','e','f']])
shape_b = np_array_c.shape
print ('shape_b = ',shape_b)
# This will return a tuple (2, 3), which stands for the shape of a two dimentional array for 
# 2 rows of 3 columns

np_array_d = np.array ([[['a','b','c'],['d','e','f']],[['g','h','i'],['j','k','l']],[['m','n','o'],['p','q','r']]])
shape_c = np_array_d.shape
print ('shape_c = ',shape_c)
# This structure builds a 3 dimensional array which stacks 3 layers of 2 dimentional arrays with 
# 2 rows of 3 columns

# There can be built n dimentional arrays with numpy

# There are several methods useful to work with numpy arrays

shape_d = (8, 6, 4, 2)

np_array_e = np.zeros(shape_d)
print ('np_array_e = ',np_array_e)
print ('type(np_array_e) = ',type(np_array_e))
print ('np_array_e.shape = ',np_array_e.shape)
# The 'zeros()' mwthods recieves a tuple with the wanted shape of an array filled with zeros

np_array_f = np.ones(shape_d,dtype=int)
print ('np_array_f = ',np_array_f)
print ('type(np_array_f) = ',type(np_array_f))
print ('np_array_f.shape = ',np_array_f.shape)
# The 'zeros()' mwthods recieves a tuple with the wanted shape of an array filled with zeros
# It also recieves a data type called 'dtype', which argument is the format wanted for the array

np_array_g = np.ones(shape_d,7,dtype=int)
print ('np_array_g = ',np_array_g)
print ('type(np_array_g) = ',type(np_array_g))
print ('np_array_g.shape = ',np_array_g.shape)
# The 'zeros()' mwthods recieves a tuple with the wanted shape of an array filled with any number
# in this case is '7'.# It also recieves a data type called 'dtype', which argument is the format wanted for the array

np_array_h = np.random.random(size = shape_d)
print ('np_array_h = ',np_array_h)
print ('type(np_array_h) = ',type(np_array_h))
print ('np_array_h.shape = ',np_array_h.shape)
# The 'random.random()' mwthods recieves a tuple with the wanted shape of an array filled with random numbers between
# 0 and 1

# An array value can be acessed providing it's particular index
value_a = np_array_h [0,0,0,0]
print ('value_a = ',value_a)
print ('type(value_a) = ',type(value_a))
# This operation will retunr the 1st value of the whole array

# And array can be sliced
np_array_i = np_array_h [4:7,3:5,0:2,0:2]
np_array_j = np_array_h [2:5,2:4,0:2,0:2]

print ('np_array_i = ',np_array_i)
print ('np_array_j',np_array_j)

print ('np_array_i.shape = ',np_array_i.shape)
print ('np_array_j.shape = ',np_array_j.shape)

# There can be used comparison operators

np_array_k = np_array_i < 0.1
print ('np_array_k = ',np_array_k)
# This statement returns an array same shape as the argument with boolean expresions 
# that replaces the values with the result of the comparison at that particular value

# There can be built an array only with the values that satisfies the conditional statement

np_array_l = np_array_i[np_array_i > 0.3]
print ('np_array_l = ',np_array_l)
# This statement returns an array

# There are several functions related to numpy arrays

np_array_m = np.random.random(shape_d)

value_a = np.sum(np_array_m)
print ('value_a = ',value_a)
# The 'sum()' function returns the sum of every value in the array

np_array_m = np.array([0.15,1.77,2.94,3.45,5.55])

value_b = np.floor(np_array_m)
print ('value_b = ',value_b)
# The 'floor()' returns an array with the integer value of every value within the argument

value_c = np.ceil(np_array_m)
print ('value_c = ',value_c)
# The 'ceil()' returns an array with the decimal value of every value within the argument

value_d = np.round(np_array_m)
print ('value_d = ',value_d)
# The 'round()' rounds every value in the array

# There can be used arithmethic operations on arrays of the same shape or with plain values

np_array_m = np.array([0,1,2,3,4])
np_array_n = np.array([5,6,7,8,9])

np_array_o = np_array_m + np_array_n
print ('np_array_o = ', np_array_o)
# This returns a sum of two arrays

np_array_p = np_array_m + 100
print ('np_array_p = ', np_array_p)
# This returns a sum of an array and a value

np_array_q = np_array_m * 1000
print ('np_array_q = ', np_array_q)