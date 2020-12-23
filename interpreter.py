import models.__init__ as all_models;string = "";code = []
path = f"C:/Users/maxda/Desktop/HTPY tests/{string.join(all_models.htpy().htmlcheck())}"
lines = open(path).readlines()
for a in lines:
  if a.endswith("\n"):
   code.append(a[:-1:])
  else:
   code.append(a)
print(code)
#for a in code:
  # if a.startswith("echo"):
   #   print(all_models.echo(a))