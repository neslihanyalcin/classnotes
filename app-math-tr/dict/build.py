import os, sys

if len(sys.argv) == 1:
    print "choose dict number"
    exit()

if sys.argv[1] == 'tex1':
    os.system("pdflatex dict1.tex")
    os.system("evince dict1.pdf")
    exit()

if sys.argv[1] == 'tex2':
    os.system("pdflatex dict2.tex")
    os.system("evince dict2.pdf")
    exit()

if sys.argv[1] == 'tex3':
    os.system("pdflatex dict3.tex")
    os.system("evince dict3.pdf")
    exit()

