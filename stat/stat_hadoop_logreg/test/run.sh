export MODEL=file:///home/burak/Downloads/logistic-regression-sgd-mapreduce/new/model1
#cat ../train.data | ./train_mapper.py | sort | ./train_reducer.py | ./model_encoder.py > ./model1
#cat ../train.data | ./train_mapper.py
cat ../train.data | python read.py
#cat ../test.data | ./test_mapper.py | sort | ./test_reducer.py > test1
