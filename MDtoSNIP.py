
myfile = open("test2.md","r")
data = ""
lines = myfile.read()

index = [] #Empty list, to index string location of each function
functions = []
description = []
scripts =[]
n = 0 #Counter for number of functions

#Loop through the .md file
for k in range (0,len(lines)):
    if lines[k:k+8]=='<a name=':
        #Store index for the start/end of each function
        index.append(k)
        #Extract the function prefix
        description.append(lines[k+9:k+10+lines[k+10:].index('\"')])
        n = n + 1 #numer of functions
        #print (lines[k+9:k+20])

#Create a list with the markdown text in it for that function
for k in range(1,len(index)):
    if k<len(index)-1:
        functions.append(lines[index[k]:index[k+1]])


#print(description)
#Prepend snippet text
a = 'nnconvolution'
#Choose a naming convention
f = open("test.txt","w") #opens file with name of "test.txt"
for k in range(1,n-2):
    prefix = description[k].replace(".", "")
    f.write("  \'"+description[k]+"""\':
     \'prefix\': \'"""+prefix+"""\'
     \'body\': \"\"\"
     """
                +functions[k] + """
    \"\"\"

 """)
f.close()

print (len(index))
