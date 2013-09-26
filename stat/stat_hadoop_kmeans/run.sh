sort --random-sort synthetic.txt > /tmp/synthetic.txt
head -15 /tmp/synthetic.txt > /tmp/centers.csv
python kmeans.py synthetic.txt 
