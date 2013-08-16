import os, sys

import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex exp.tex")
    os.system("evince exp.pdf")
    exit()
    
