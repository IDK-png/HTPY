varaibles = {}
def echo(line):
    line = str(line).strip()
    def isfloat(x):
        try:
            x = float(x)
            return "x"
        except:
            return "not float"
    def t(text):
       line = list(text.strip())
       line = str("".join(line))
       if line.startswith('echo|"') and line.endswith('"/-t|'):
           return f"{line[6:len(line)-5]}:String"
       if line.startswith("echo|") and line[5:len(line)-4].isdigit() and line.endswith('/-t|'):
           return f"{line[5:len(line)-4]}:Integer"
       if line[5:len(line)-4] in varaibles:
           varf = varaibles[line[5:len(line)-4]]
           if varf.startswith('"') and varf.endswith('"'): 
               return f"{varf}:String"
           if varf.isdigit() and varf.startswith(varf[0]) and varf.endswith(varf[len(varf)-1]):
               return f"{varf}:Integer"
           if '.' in varf and varf[0:varf.index(".")].isdigit() and varf[varf.index(".")+1:len(varf)-1].isdigit():return f"{varf}:Float"
       if '.' in line[5:len(line)-1] and line.startswith('echo|'):
           test = list(line[5:len(line)-4])
           test.pop(test.index('.'))
           test = ''.join(test)
           if test.isnumeric():
               return f"{line[5:len(line)-4]}:Float"
       if line[5:len(line)-4] == "True" or line[5:len(line)-4] == "False":
               return f"{line[5:len(line)-4]}:Boolean"
          
    line = str(line)
    if "-t" in line[len(line)-4:len(line)]:
        return t(line)
    if line[5:len(line)-1] in varaibles and line.endswith("|"):
           return varaibles[line[5:len(line)-1]]
    if line[5:len(line)-1].startswith('"') and line[5:len(line)-1].endswith('"') or line[5:len(line)-1] == "True" or line[5:len(line)-1] == "False" or isfloat(line[5:len(line)-1]) == "x":
        return f"{line[5:len(line)-1]}"
def var(line): #Функция переменной 
    #if line.startswith("var|") and line.endswith("|"):
        #slashes = [a for a,b in enumerate(path) if b == "/"]
        #path = list(path)
       # for a in range(np.subtract(len(path)-1,int(slashes[len(slashes)-1]))):
       #     path.pop(len(path)-1)
     #  path = "".join(path)
     #   open('vars')
    if line.startswith("var|") and line.endswith("|"):
        varaibles[line[4:line.index(",")]] = line[line.index(",")+1:len(line)-1]
        return('')