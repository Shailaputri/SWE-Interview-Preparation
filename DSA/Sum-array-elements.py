def main(arr):
  res = 0
  for element in arr:
    res += element
  return res

if __name__== "__main__":
  arr = [1,2,3,4,5]
  output = main(arr)
  print(f'The sum of the elements of array is {output}')
  
