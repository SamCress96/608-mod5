## Section 7.14.12 Samantha Cress

# A DataFrame is an enhanced two-dimensional array. Like Series, DataFrames can have custom row and column indices, and offer additional operations and capabilities that make them more convenient for many data-science oriented tasks.
# DataFrames also support missing data. Each column in a DataFrame is a Series. The Series representing each column may contain different element types.

# Creating a dataframe from a Dictionary
# Create a DataFrame from a dictionary that represents student grades on three exams:
import pandas as pd
grades_dict = {'Wally': [87, 96, 70], 'Eva': [100, 87, 90], 'Sam': [94, 77, 90], 'Katie': [100, 81, 82], 'Bob': [83, 65, 85]}
grades = pd.DataFrame(grades_dict)
print ()
print (grades)
# The dictionary’s keys become the column names and the values associated with each key become the element values in the corresponding column.

# Customizing a DataFrame’s Indices with the index Attribute
# We could have specified custom indices with the index keyword argument when we created the DataFrame, as in:
pd.DataFrame(grades_dict, index=['Test1', 'Test2', 'Test3'])
# Use the index attribute to change the DataFrame’s indices from sequential integers to labels:
grades.index = ['Test1', 'Test2', 'Test3']
print ()
print (grades)
# When specifying the indices, you must provide a one-dimensional collection that has the same number of elements as there are rows in the DataFrame; otherwise, a ValueError occurs.

# Accessing a DataFrame’s Columns
# Getting Eva’s grades by name, which displays her column as a Series:
print ()
print ('Eva grades:')
print (grades['Eva'])
# Let’s get Sam’s grades with the Sam attribute:
print ()
print ('Sam grades:')
print (grades.Sam)

# Selecting Rows via the loc and iloc Attributes
# pandas documentation recommends using the attributes loc, iloc, at and iat, which are optimized to access DataFrames and also provide additional capabilities beyond what you can do only with [].
# The following lists all the grades in the row 'Test1':
print ()
print (grades.loc['Test1'])
# You also can access rows by integer zero-based indices using the iloc attribute 
print ()
print (grades.iloc[1])

# Selecting Rows via Slices and Lists with the loc and iloc Attributes
# The index can be a slice. When using slices containing labels with loc, the range specified includes the high index ('Test3'):
print ()
print (grades.loc['Test1':'Test3'])
# When using slices containing integer indices with iloc, the range you specify excludes the high index (2):
print ()
print(grades.iloc[0:2])
# To select specific rows, use a list rather than slice notation with loc or iloc:
print ()
print (grades.loc[['Test1', 'Test3']])
print ()
print (grades.iloc[[0, 2]])

# Selecting Subsets of the Rows and Columns
# You can focus on small subsets of a DataFrame by selecting rows and columns using two slices, two lists or a combination of slices and lists.
print ()
print (grades.loc['Test1':'Test2', ['Eva', 'Katie']])
# Use iloc with a list and a slice to select the first and third tests and the first three columns for those tests:
print ()
print (grades.iloc[[0, 2], 0:3])

# Boolean Indexing
print ()
print ('Grades =< 90:')
print (grades[grades >= 90])
print ()
print ('Grades >=80 & <90:')
print (grades[(grades >= 80) & (grades < 90)])

# Accessing a Specific DataFrame Cell by Row and Column
# You can use a DataFrame’s at and iat attributes to get a single value from a DataFrame. 
print ()
print ('Eva Test 2 grade:')
print (grades.at['Test2', 'Eva'])
print ()
print ('Wally Test 3 grade:')
print (grades.iat[2, 0])
# Let’s change Eva’s Test2 grade to 100 using at, then change it back to 87 using iat:
print ()
grades.at['Test2', 'Eva'] = 100
print ('Eva 100:')
print (grades.at['Test2', 'Eva'])
print ()
grades.iat[1, 2] = 87
print ('Eva 87:')
print (grades.iat[1, 2])

# Descriptive Statistics
# Both Series and DataFrames have a describe method that calculates basic descriptive statistics for the data and returns them as a DataFrame. 
print ()
print (grades.describe())
print ()
pd.set_option('display.precision', 2) # precision caused pattern matched multiple keys error, display.precision needs to be used instead
print (grades.describe())
# You can calculate mean quickly by calling mean on the data froam
print ()
print ('grade means:')
print (grades.mean())

# Transposing the DataFrame with the T Attribute
# You can quickly transpose the rows and columns—so the rows become the columns, and the columns become the rows—by using the T attribute:
print ()
print ('Transpose:')
print ( grades.T)
print ()
print (grades.T.describe())
print ()
print ('Transposed grade means:')
print (grades.T.mean())

# Sorting by Rows by Their Indices
# Sort the rows by their indices in descending order using sort_index and its keyword argument ascending=False
print ()
print (grades.sort_index(ascending=False))

# Sorting by Column Indices
# Now let’s sort the columns into ascending order (left-to-right) by their column names. Passing the axis=1 keyword argument indicates that we wish to sort the column indices, rather than the row indices—axis=0.
print ()
print (grades.sort_index(axis=1))

# Sorting by Column Values
# see Test1’s grades in descending order so we can see the students’ names in highest-to-lowest grade order. We can call the method sort_values as follows:
print ()
print (grades.sort_values(by='Test1', axis=1, ascending=False))
print ()
print (grades.T.sort_values(by='Test1', ascending=False))
print ()
print (grades.loc['Test1'].sort_values(ascending=False))

# Self Check
temps = {'Mon': [68, 89], 'Tue': [71, 93], 'Wed': [66, 82],'Thu': [75, 97], 'Fri': [62, 79]}
# Convert the dictionary into the DataFrame named temperatures with 'Low' and 'High' as the indices, then display the DataFrame.
import pandas as pd
temps_dict = {'Mon': [68, 89], 'Tue': [71, 93], 'Wed': [66, 82],'Thu': [75, 97], 'Fri': [62, 79]}
temps = pd.DataFrame(temps_dict)
pd.DataFrame(temps_dict, index=['Low', 'high'])
temps.index = ['Low', 'High']
print ()
print ('Self Check Part A:')
print (temps)
# Use the column names to select only the columns for 'Mon' through 'Wed'.
print ()
print ('Self Check Part B:')
print (temps.loc[:, 'Mon':'Wed'])
# Use the row index 'Low' to select only the low temperatures for each day.
print ()
print ('Self Check Part C:')
print (temps.loc['Low'])
# Set the floating-point precision to 2, then calculate the average temperature for each day.
print ()
print ('Self Check Part D:')
pd.set_option('display.precision', 2)
print (temps.describe())
print ()
print (temps.mean())
# Calculate the average low and high temperatures.
print ()
print ('Self Check Part E:')
print ( temps.mean(axis=1))

# Samantha Cress

