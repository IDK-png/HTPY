import os
def files():
  htpy_files = []
  x = list(os.listdir("C:/Users/maxda/Desktop/HTPY tests"))
  for a in x:
    if a.endswith(".htpy"):
      htpy_files.append(a)
  return htpy_files