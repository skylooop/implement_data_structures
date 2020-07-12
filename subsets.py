def subsets(a,index,subset):
  print(*subset)
  for i in range(index,len(a)):
    subset.append(a[i])
    subsets(a,index+1,subset)
    subset.pop(-1)
  return

subset = []
a = [1,2,3]
print(subsets(a,0,subset))
