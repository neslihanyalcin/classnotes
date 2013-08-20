import os, sys, glob

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdftk linear*/*.pdf output ~/Dropbox/Public/skfiles/linear_strang.pdf")
    exit()
    
if sys.argv[1] == 'all':
    for a in sorted(glob.glob("linear*")):
        os.chdir(a)
        os.system("pdflatex linear*.tex")    
        os.chdir("..")
    
    
