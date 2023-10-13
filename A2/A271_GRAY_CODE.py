def graycode(n):
  if n==0:
    return ['']
  fh = graycode(n-1)
  sh = fh.copy()

  fh = ['0'+code for code in fh]
  sh = ['1'+code for code in reversed(sh)]

  return fh+sh

code = graycode(4)
#print(*code)

for element in code:
  print(element)
