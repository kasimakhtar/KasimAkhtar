## Python code to increase the number range in a list

This code lets you increase the range of a list of consecutive numbers to whatever desired_range you'd need. You can also change the sequence by changing n += 1. This doesn't always work however; if you try n = n*2, and a desired_range of 200, the last item in the list will be 256 instead of 200.

~~~


list = [1, 2, 3, 4, 5]
n = list[-1]
desired_range = 100
for i in list:
  if n < desired_range:
    n += 1
    list.append(n)
for i in list:
  print(i)

~~~
      
