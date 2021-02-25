#___________.
#переменные |
#___________|
import models.stringfuncs as stringfuncs;from models.checkscript import files;
funcs={"echo":stringfuncs.echo, "var":stringfuncs.var, "plus":stringfuncs.plus, "type":stringfuncs.type}
string = ""
code = []
path = f"C:/Users/maxda/Desktop/New folder (4)/HTPY tests/{string.join(files())}"
lines = open(path).readlines()
#_______.
#Функций|
#_______|
def making_code_list(): #Делание из содержания файла лист
 for a in lines:
  if a.endswith("\n"):
   code.append(a[:-1:])
  else:
   code.append(a)
making_code_list()

def interpreter():
    for v in code:
      if v.count("|")>2:
       test = v.split("|") # Делание удобного списка для работы над ним. например: ['echo', 'type', '2', '', '']
       test = test[::-1]
       for a,c in enumerate(test): # Цикл для удаление пустых элементов "" чтобы было еще удобнее работать
           if c == "": test.pop(a)
       test.pop(0) # удаляю последний пустой элемент
       for a,b in enumerate(test): #Сам интерпретатор 
         if b in funcs and a != len(test)-1: # если этот элемент находится в funcs и он не самый последния(тоесть самый первая) функция
           test[test.index(b)] = funcs[b](test[a-1])
       if test[len(test)-1]=="echo":
        print(test[len(test)-2])
      if v.count("|")==2:
       test = v.split("|") # Делание удобного списка для работы над ним. например: ['echo', 'type', '2', '', '']
       test.pop(len(test)-1)
       if test[0] == "echo": #потому что если это не будет echo тоесть принт то зачемв выводить что получилось в консоль ? зачем тогда надо будет echo
         print(funcs[test[0]](test[1]))
       else:
           funcs[test[0]](test[1])
interpreter()