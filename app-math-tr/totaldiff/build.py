import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex totaldiff.tex")
    os.system("evince totaldiff.pdf")
    exit()
    
if sys.argv[1] == 'zip':    
    cmd = "zip ~/Dropbox/Public/skfiles/total-diff.zip *.py *.pdf *.tex *.png" 
    os.system(cmd)
    
