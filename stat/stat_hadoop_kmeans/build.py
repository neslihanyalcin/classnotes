import os, sys

if len(sys.argv) == 1 or sys.argv[1] == 'tex':
    os.system("python /home/burak/Downloads/nbconvert/nbconvert.py kmeans.ipynb -f latex")
    #os.system("cp kmeans-diag.png kmeans_files/kmeans_fig_00.png")
    os.system("pdflatex kmeans.tex")
    os.system("evince kmeans.pdf")
    exit()
