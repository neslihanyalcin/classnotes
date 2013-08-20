import os, sys, glob

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdftk calc_multi*/*.pdf output ~/Dropbox/Public/skfiles/multivar_calculus.pdf")
    exit()
    
if sys.argv[1] == 'all':
    for a in sorted(glob.glob("calc*")):
        os.chdir(a)
        os.system("pdflatex calc_mul*.tex")    
        os.chdir("..")
        
    
