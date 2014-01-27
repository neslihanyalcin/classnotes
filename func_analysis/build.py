import os, sys, glob

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdftk func*/*.pdf output ~/Dropbox/Public/skfiles/functional_analysis.pdf")
    exit()
    
if sys.argv[1] == 'all':
    for a in sorted(glob.glob("func*")):
        os.chdir(a)
        os.system("pdflatex -shell-escape func*.tex")    
        os.chdir("..")
        
