arg_list = argv ();
file_in = arg_list{1};
file_hmm = arg_list{2};

data = load(file_in)';

[nex,T] = size(data)

load(file_hmm,'prior2', 'transmat2', 'obsmat2');

loglik = dhmm_logprob(data, prior2, transmat2, obsmat2)

loglik / nex

