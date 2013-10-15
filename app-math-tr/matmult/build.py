import os

#os.system("ipython nbconvert --to latex matmult.ipynb")
os.system("python /home/burak/Downloads/nbconvert/nbconvert.py matmult.ipynb -f latex")
os.system("pdflatex matmult.tex")
os.system("evince matmult.pdf")
