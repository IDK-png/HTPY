import os
class Htmlcheck():
 def __init__(self):
  self._htpy_files = []
  self.x = list(os.listdir("C:/Users/maxda/Desktop/HTPY tests"))
  for a in self.x:
    if a.endswith(".htpy"):
      self._htpy_files.append(a)
  return None
 def files(self):
   return self._htpy_files