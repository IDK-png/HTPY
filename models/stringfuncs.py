varaibles = {}
def type(line):
       line = str(line)
       def isfloat(x):
          try:
            x = float(x)
            return "x"
          except:
            return "not float"
       if line.startswith('"') and line.endswith('"') or line.startswith("'") and line.endswith("'"):
           return f"{line}:String"
       if line.isdigit():
           return f"{line}:Integer"
       if line.isdigit() == False and isfloat(line) == "x":return f"{line}:Float"
       if line in varaibles:
           varf = varaibles[line] 
           if varf.startswith('"') and varf.endswith('"'): 
               return f"{varf}:String"
           if varf.isdigit() and varf.startswith(varf[0]) and varf.endswith(varf[len(varf)-1]):
               return f"{varf}:Integer"
           if '.' in varf and varf[0:varf.index(".")].isdigit() and varf[varf.index(".")+1:len(varf)-1].isdigit():return f"{varf}:Float"
def echo(line):
    if line.startswith('"') == False and line.endswith('"') == False and line in varaibles:
        return varaibles[line]
    else:
        return line # да блять так просто но сначала тут был ёбанный -t аля тип того что хотят принтануть но теперь это было перенесено в отдельную функцию под названием type
def var(line): #Функция переменной 
           if "=" not in line:
               varaibles[line] = None
           else: 
             for a in varaibles:
                 if line.startswith(a):
                     varaibles[a] = line[line.index("=")+1:len(line)].strip()
def plus(line):
    if "+" in line:
         return sum([int(a) for a in line if a.isdigit()])
       