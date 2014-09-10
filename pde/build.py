import os, sys, glob

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdftk pde*/*.pdf \
    heat/heat.pdf heat-deriv/heat-deriv.pdf level/level.pdf \
    lk/lk.pdf curvature/curvature.pdf wave-deriv/pde_01.pdf \
    output ~/Dropbox/Public/skfiles/pde.pdf"
)
    exit()
    
if sys.argv[1] == 'all':
    for a in sorted(glob.glob("pde*")):
        os.chdir(a)
        os.system("pdflatex -shell-escape pde*.tex")    
        os.chdir("..")
    
    
