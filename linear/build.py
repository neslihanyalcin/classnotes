import os, sys, glob

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdftk linear*/*.pdf output ~/Dropbox/Public/skfiles/linear_strang.pdf")
    exit()
    
if sys.argv[1] == 'all':
    for a in sorted(glob.glob("linear*")):
        os.chdir(a)
        os.system("pdflatex -shell-escape linear*.tex")    
        os.chdir("..")
        
if sys.argv[1] == 'clean':
    os.system("find . -name '_region_*' | xargs rm  -rf")
    os.system("find . -name '*.log' | xargs rm  -rf")
