from sys import argv

script, filename = argv

def countInversions(A):
   l = len(A)
   if l > 1:
      mid = l // 2
      C = A[:mid]
      D = A[mid:]
      C, c = countInversions(A[:mid])
      D, d = countInversions(A[mid:])
      B, b = mergeCount(C,D)
      return B, b + c + d
   else:
      return A, 0


def mergeCount(A,B):
   split_count = 0
   M = []
   while A and B:
      if A[0] <= B[0]: 
         M.append(A.pop(0)) 
      else: 
         split_count += len(A)
         M.append(B.pop(0)) 
   M  += A + B     
   return M, split_count 

with open(filename, 'rt') as f:
   lines = f.readlines()
   unsorted_array = map(lambda x: int(x), lines)
   print unsorted_array[: 10]
   sorted_array = countInversions(unsorted_array)
   print "***"
   print sorted_array[0][: 10]
   print "***"
   print sorted_array[1]
