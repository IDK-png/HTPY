import models.__init__ as all_models;string = "";code = []
from models.stringfuncs import base;from models.checkscript import files;
path = f"C:/Users/maxda/Desktop/HTPY tests/{string.join(files())}"
lines = open(path).readlines()
def making_code_list():
 for a in lines:
  if a.endswith("\n"):
   code.append(a[:-1:])
  else:
   code.append(a)
making_code_list()
def interpreter():
 for a in code:
  if a.startswith("echo"):
     print(base(a))
interpreter()