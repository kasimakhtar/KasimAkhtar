## Python code to calculate sum of a series

This python function takes a number and creates a specific series, and then returns the sum of the series. The series always follows the pattern: 1, 1/4, 1/7, 1/10, 1/13, etc, and carries on for n number of times I created this function as part of a [CodeWars challenge](https://www.codewars.com/kata/555eded1ad94b00403000071).


~~~

def series_sum(n):
  
  x = []
  for i in range(n):
    y = (i * 2 + (i + 1))**-1
    x.append(y)
  m = round(sum(x), 2)
 
  if n <= 0:
    print("0.00")
  elif n == 1:
    print("1.00")
  else:
    print(str(m))

~~~
&nbsp;
&nbsp;

## Python code to check if password is valid

This function is designed for a [CodeWar challenge](https://www.codewars.com/kata/57e35f1bc763b8ccce000038) and checks whether a password is strong enough or not. It takes a string as an arguement and returns either "valid" or "not valid" depending on whether the password is or isn't in line with the following requirements:

* Is between 8-20 characters

* Is made up of only uppercase letters, lowercase letters, numbers, special characters (!@#$%^&*), and contains at least one of each of these categories

~~~

def check_password(s):
  special = ["!", "@", "$", "%", "^", "&", "*"]
  for i in special:
    if i in s:
      if any(char.isdigit() for char in s):
        if any(char.isupper() for char in s):
          if any(char.islower() for char in s):
            if len(s) >= 8 and len(s) <= 20:
              return "valid"
    else:
      return "not valid"

~~~
&nbsp;
&nbsp;
## Python code to increase the number range in a list

This code lets you increase the range of a list of numbers to whatever desired range you'd need. You can also change the increase in the sequence by changing last = last*2 to some other change in the last item.

~~~

list = [1, 2]
*rest, last = list
desired_range = 100
for i in list:
  if last < desired_range:
    last = last*2
    list.append(last)
for i in list:
  if i > desired_range:
    list.remove(i)
print(list)

~~~

Output:
~~~

[1, 2, 4, 8, 16, 32, 64]

~~~






