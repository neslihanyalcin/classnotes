import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex ode_mattuck_*.tex")
    os.system("evince ode_mattuck_*.pdf")
    exit()
    
if sys.argv[1] == 'zip':    
    cmd = "zip ~/Dropbox/Public/skfiles/ode/ode_mattuck_%d.zip *.png *.py ode_mattuck_%d.tex ode_mattuck_%d.pdf" % \
        (int(sys.argv[2]), int(sys.argv[2]), int(sys.argv[2]))
    os.system(cmd)
    
