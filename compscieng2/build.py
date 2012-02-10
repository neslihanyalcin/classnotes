import os, sys, glob

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdftk compscieng*/*.pdf output ~/Dropbox/Public/skfiles/compscieng2.pdf")
    exit()
    
if sys.argv[1] == 'all':
    for a in sorted(glob.glob("compscieng*")):
        os.chdir(a)
        os.system("pdflatex compscieng*.tex")    
        os.chdir("..")
        
    
