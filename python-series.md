## Python code to calculate sum of series

This python function takes a number and creates a specific series, and then returns the sum of the series. The series always follows the pattern: 1, 1/4, 1/7, 1/10, 1/13, etc, and carries on for n number of times I created this function as part of a [CodeWars challenge](https://www.codewars.com/kata/555eded1ad94b00403000071).


~~~

def series_sum(n):
  
  # Start by creating a list for the series
  x = []
  
  # Add the series values to the list
  for i in range(n):
    y = (i * 2 + (i + 1))**-1
    x.append(y)
  
  # Add the series together
  m = round(sum(x), 2)
  
  # Specify the different scenarios
  if n <= 0:
    print("0.00")
  elif n == 1:
    print("1.00")
  else:
    print(str(m))

~~~




Overall the function executes properly however there are a couple of improvements I would like to make to this in the future. Firstly, the function relies on a maths calculation based off of a formula that I made for the function. 
&nbsp;

|  n  |  0  |  1  |  2  |  3  |  4  |  5  |
|  X<sub>n</sub>  |  1  |  4  |  7  |  10  |  13  |  16  |
&nbsp;

From this table the formula included in the code can be deduced: X<sub>n</sub> = 2n + (n + 1). I would like to find a solution that doesn't rely on an external maths calculation, but instead on python code.  

Secondly, I would like to find a solution that doesn't specify three scenarios, but instead applies one method to all arguements, and produces the correct output for it. 


