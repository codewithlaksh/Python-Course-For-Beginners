# Syntax: f = open("path" [,mode])

# f = open("demo.txt")
'''
Read function: reads the entire content of a text file.
print(f.read())
'''

'''
Readline function: read only a single sentence from the content of a text file.
print(f.readline())
'''

'''
Readlines function: read all sentences from the content of a text file and returns them as a list of strings.
print(f.readlines())
'''

'''
If we provide bytes to read/readline function, then it reads only upto the specific byte position
print(f.read([bytes]))
print(f.readline([bytes]))
'''

'''
print(f.read(6))
f.readline()
print(f.readline(6))
'''

f = open("demo.txt", "w")

'''
Write function: Overwrites the existing data in the file. Takes a string as a parameter
f.write('I am Lakshyaraj')
f.write('I am a good boy')
'''

'''
Writelines function: Overwrites the existing data in the file. Takes a list of strings as a parameter
'''
f.writelines(['I am Lakshyaraj.\n', 'I am a good boy'])

