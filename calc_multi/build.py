import os, sys, glob

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdftk calc_multi*/*.pdf output ~/Dropbox/Public/skfiles/multivar_calculus.pdf")
    exit()
    
if sys.argv[1] == 'all':
    for a in sorted(glob.glob("calc*")):
        os.chdir(a)
        os.system("pdflatex -shell-escape calc_mul*.tex") 
        os.chdir("..")
            
if sys.argv[1] == 'clean':
    os.system("find . -name '_region_*' | xargs rm  -rf")
    os.system("find . -name '*.log' | xargs rm  -rf")
