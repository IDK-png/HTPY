class echo():
    def model(self,line):
        line = list(line)
        for x,i in enumerate(line):
            if x < line.index("("):
              list(i).pop(x)
        if line.startswith("(") and line.endswith(")"):
            line.pop(0);line.pop(len(line)-1);print(line)
        return line
test = echo().model("echo(hello)")