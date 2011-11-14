import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex compscieng_1_*.tex")
    os.system("evince compscieng_1_*.pdf")
    exit()
    
if sys.argv[1] == 'zip':    
    cmd = "zip ~/Dropbox/Public/skfiles/compscieng_1/compscieng_1_%d.zip compscieng_1_%d.tex compscieng_1_%d.pdf *.m *.png *.py" % \
        (int(sys.argv[2]), int(sys.argv[2]), int(sys.argv[2]))
    os.system(cmd)
    
