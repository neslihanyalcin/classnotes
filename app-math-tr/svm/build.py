import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex svm.tex")
    os.system("evince svm.pdf")
    exit()
    
if sys.argv[1] == 'en':
    os.system("pdflatex svm-en.tex")
    os.system("evince svm-en.pdf")
    exit()
    
