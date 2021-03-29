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
