import models.__init__ as all_models
string = ""
path = f"C:/Users/maxda/Desktop/HTPY tests/{string.join(all_models.htpy().htmlcheck())}"
with open(path, 'r') as file:
   print(file.readline())
 