import os
class Htmlcheck():
 def __init__(self):
  self._htpy_files = []
  self.cyka = list(os.listdir("C:/Users/maxda/Desktop/HTPY tests"))
  for a in self.cyka:
    if a.endswith(".htpy"):
      self._htpy_files.append(a)
  return None
 def files(self):
   return self._htpy_files