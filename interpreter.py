string = "";code = []
import models.stringfuncs as stringfuncs;from models.checkscript import files;
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
  if a.startswith("echo|"):
   #  if stringfuncs.echo(a) != None:
        print(stringfuncs.echo(a))
    # else:
       # return f"   Line {code.index(a)+1} Error\n   |\n   -->[{a}] "
  if a.startswith("var|"):
    # if stringfuncs.var(a) != None:
        stringfuncs.var(a)
     #else:
       # return f"   Line {code.index(a)+1} Error\n   |\n   -->[{a}] "
interpreter()