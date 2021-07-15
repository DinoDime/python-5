filename = input("Please enter the name of the file: ")
filehandle = open(filename)
for line in filehandle:
    line = line.strip()
    line = line.upper()
    print(line)
