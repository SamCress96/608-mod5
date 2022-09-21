#Displaying a Series
#Pandas displays a Series in two-column format with the indices left aligned in the left column and the values right aligned in the right column. 
#After listing the Series elements, pandas shows the data type (dtype) of the underlying array’s elements:
import pandas as pd
grades = pd.Series([87, 100, 94])
print (grades)

#Accessing a Series’ Elements
#You can access a Series’s elements by via square brackets containing an index:
print ('first grade:', grades[0])

#Producing Descriptive Statistics for a Series
print ('count:', grades.count())
print ('mean:', grades.mean())
print ('min:', grades.min())
print ('max:', grades.max())
print ('std:', grades.std())

#Each of these is a functional-style reduction.
#Calling Series method describe produces all these stats and more:
print (grades.describe())

#Dictionary Initializars
#If you initialize a Series with a dictionary, its keys become the Series’ indices, and its values become the Series’ element values:
grades = pd.Series({'Wally': 87, 'Eva': 100, 'Sam': 94})
print (grades)
print ('Eva:', grades['Eva'])

#Get Wally's score using the easier dot notation: grades.Wally.
print ('Wally:', grades.Wally)

#Series also has built-in attributes. For example, the dtype attribute returns the underlying array’s element type:
print ('Array element type:', grades.dtype)
#and the values attribute returns the underlying array:
print ('values:', grades.values)

#Samantha Cress
