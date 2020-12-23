def base(line):
    # Тут все параметры для команды echo АКА print
    def t(text):
       line = list(text)
       for a in range(3):line.pop(len(line)-1);
       line = str("".join(line))
       if line.startswith('echo("') and line.endswith('")'):
           return f"{line[6:len(line)-2]}:String"
       if line[5:len(line)-1].isdigit() and line.endswith(')'):
           return f"{line[5:len(line)-1]}:Integer"
    line = str(line)
    if line.endswith("-t"):
        return t(line)
    else:
        return f"{line[5:len(line)-1]}"