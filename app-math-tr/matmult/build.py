import os

os.system("pdflatex -shell-escape matmult2.tex")
os.system("evince matmult2.pdf")
