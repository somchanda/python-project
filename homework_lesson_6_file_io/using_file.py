# always override file text.txt and write some line
fobj = open('file/text.txt', 'w+')
fobj.write("This is line 1.\n")
fobj.write("This is line 2.\n")
fobj.write("This is line 3.\n")
fobj.write("This is line 4.\n")
fobj.close()

# append a line to text.txt file
fobj2 = open('file/text.txt', 'a+')
fobj2.write("This line is appended\n")
fobj2.close()

# Read data from text.txt file
fobj3 = open('file/text.txt', 'r')
lines = fobj3.readlines()
for line in lines:
    print(line.replace('\n', ''))

# To see pointer in file
print('==================')
print(fobj3.tell())
fobj3.close()