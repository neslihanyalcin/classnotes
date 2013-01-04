coal=function(n,x,init,hyper)
{
	nn=length(x)
	theta=init[1]
	lambda=init[2]
	k=init[3]
	z=0
	output=matrix(0, ncol=3, nrow=n)
	for(i in 1:n)
	{
	   if(k > 1) ca=hyper[1]+sum(x[1:k])
	   else ca=hyper[1]	   
	   
	   theta=rgamma(1, ca, k+hyper[3])
	   
	   if(k < nn) ca=hyper[2]+sum(x[(k+1):nn])
	   else ca=hyper[2]
	   lambda=rgamma(1, ca, nn-k+hyper[4])
	   
	   for(j in 1:nn)
	   {
	     z[j]=exp((lambda-theta)*j) * (theta/lambda)**sum(x[1:j])	     
	   }
	   k=sample(nn, size=1, prob=z)
	   output[i,]=c(theta, lambda, k)
	}
	output
}

data = scan("coal.txt")
coal(1100, data, c(1,1,1), c(1,1,1,1))

