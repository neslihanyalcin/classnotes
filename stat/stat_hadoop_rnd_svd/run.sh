#python tabify.py w1.csv w2.dat
#python mrproj.py w2.dat > w3.dat
#python mrr.py w3.dat  > R.dat
#python mrq.py w3.dat --R=R.dat --file R.dat > Q.dat
#python mr_q_ur.py Q.dat --R=R.dat --file R.dat > U.dat
#python mraq.py w3.dat Q.dat > BT.dat
#python mrr.py BT.dat  > R_BT.dat
#python mr_q_uhat.py Q.dat --R=R_BT.dat --file R_BT.dat > U_final.dat

#python strip.py Q.dat > $HOME/Q.dat
#python strip.py BT.dat > $HOME/BT.dat

# test
python mraq.py A_matrix1 B_matrix1 > AtB_test_out.dat
