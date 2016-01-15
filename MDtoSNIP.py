
import textwrap
import glob
import string

def reindent(s, numSpaces):
    s = string.split(s, '\n')
    s = [(numSpaces * ' ') + string.lstrip(line) for line in s]
    s = string.join(s, '\n')
    return s

f = open("snippets_output.txt","w") #opens file with name of "test.txt"
path = "/Users/robsalz/Projects/MDtoSNIP/mdFiles/*.md"
for fname in glob.glob(path):

    myfile = open(fname,"r")
    data = ""
    lines = myfile.read()
    lines.replace("\'","\"")

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

    index.append(len(lines))
    #Create a list with the markdown text in it for that function
    #for k in range(0,len(index)):

    k=0
    while k<len(index)-1:
        functions.append(lines[index[k]:index[k+1]])
        k=k+1


    #print(description)
    #Prepend snippet text
    a = 'nnconvolution'
    #Choose a naming convention
    for k in range(0,n):


        body = reindent(functions[k],8)
        prefix = description[k].replace(".", "")
        f.write("  \'"+description[k]+"""\':
      \'prefix\': \'"""+prefix+"""\'
      \'body\': \"\"\"
"""+body+ """
        \"\"\"

 """)
