import os, sys, glob

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdftk ode_mattuck*/*.pdf output ~/Dropbox/Public/skfiles/ode_mattuck.pdf")
    exit()
    
if sys.argv[1] == 'all':
    for a in sorted(glob.glob("ode*")):
        if a == "ode_mattuck_99": continue
        os.chdir(a)
        os.system("pdflatex -shell-escape ode_mattuck*.tex")    
        os.chdir("..")
    
    
