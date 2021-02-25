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
       if line in varaibles:
           varf = varaibles[line] 
           if varf.startswith('"') and varf.endswith('"'): 
               return f"{varf}:String"
           if varf.isdigit() and varf.startswith(varf[0]) and varf.endswith(varf[len(varf)-1]):
               return f"{varf}:Integer"
           if '.' in varf and varf[0:varf.index(".")].isdigit() and varf[varf.index(".")+1:len(varf)-1].isdigit():return f"{varf}:Float"
def echo(line):
    return line # да блять так просто но сначала тут был ёбанный -t аля тип того что хотят принтануть но теперь это было перенесено в отдельную функцию под названием type
def var(line): #Функция переменной 
    if line.startswith("var|"):
        #if line[line.index(",")+1:line.index(".")-1] in funcs:
        #    if line[line.index(",")+1:line.index(".")-1] == "Cstring":
        #        varaibles[line[4:line.index(",")]] = C(line[line.index(",")+1:line.index(".")-1])
       # else:       И ТУТ БАГ ВО ВСЕЙ ЭТОЙ ОБЛАСТИ
           varaibles[line[4:line.index(",")]] = line[line.index(",")+1:len(line)-1]
           return('')
def C(line):
    if line.isdigit():return(f'"{line}"')
    if "Cstring" in line and line.startswith("Cstring."):
      if line[line.index(".")+1:len(line)-1] in varaibles:
        varaibles[line[line.index(".")+1:len(line)-1]] = f'"{varaibles[line[line.index(".")+1:len(line)-1]]}"'
        return f'{varaibles[line[line.index(".")+1:len(line)-1]]}'
      else:
        return f'{line[line.index(".")+1:len(line)-1]}'
    if line.startswith("Cstring."):
        return f'"{line[8:len(line)]}"'
def plus(line):
    if "+" in line:
        line = line.split("+")
        return int(line[0])+int(line[1])