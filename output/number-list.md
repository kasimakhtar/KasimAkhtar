## Python code to increase the number range in a list

This code lets you increase the range of a list of consecutive numbers to whatever desired_range you'd need. You can also change the increase in the sequence by changing n += 1 to some other change in n. This doesn't always work however; if you try n = n*2, and have a desired_range of 200, the last item in the list will be 256 instead of 200.

~~~

list = [1, 2, 3, 4, 5]
n = list[-1]
desired_range = 12
for i in list:
  if n < desired_range:
    n += 1
    list.append(n)
print(list)

~~~

Output:
~~~

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

~~~
