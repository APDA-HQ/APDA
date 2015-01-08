#!/usr/bin/env python

'''
    Emoticons README generator
'''

from os import listdir
from os.path import isfile, join


blacklist = ["README.md"]
marks = [ f for f in listdir("./") if isfile(join("./",f)) ]

readme = ''''
     _____                 _   _                     
    | ____|_ __ ___   ___ | |_(_) ___ ___  _ __  ___ 
    |  _| | '_ ` _ \ / _ \| __| |/ __/ _ \| '_ \/ __|
    | |___| | | | | | (_) | |_| | (_| (_) | | | \__ \ 
    |_____|_| |_| |_|\___/ \__|_|\___\___/|_| |_|___/ 
                                                     
#   Markdown Emoticons Cheatsheet


'''

EMOTIC_PER_LINE = 5

print "Generating README.md"

for i in marks:
    if i not in blacklist and ".md" in i.lower():
        print "Appending %s" %i
        f = open(i,"r")
        data = f.read()
        f.close()
        data = data.split("\n")
        readme += "##    %s\n\n" % (i.split(".")[0])
        count = 0
        for line in data:
            readme += "%s (`%s`) - " %(line,line)
            count += 1
            if count == EMOTIC_PER_LINE:
                readme += "\n\n"
                count = 0
        readme += "\n\n\n"

f = open("README.md","w")
f.write(readme)
f.close()