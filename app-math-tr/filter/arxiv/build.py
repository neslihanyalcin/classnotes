import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("pdflatex vis_track_filtering.tex")
    os.system("evince vis_track_filtering.pdf")
    exit()

