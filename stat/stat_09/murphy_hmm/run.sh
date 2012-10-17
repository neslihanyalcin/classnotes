#octave -f dhmm_em_demo.m
octave -f x_train.m sample_sales out_hmm
octave -f x_lk.m sample_sales out_hmm
octave -f x_lk.m sample_test1 out_hmm
octave -f x_lk.m sample_test2 out_hmm
