library(R2jags) 
require(arm)

D=scan("coal.txt")

N=length(D)

data=list("N","D")

inits = function() { list(b=c(0,0),changeyear=50) }

parameters <- c("changeyear","b")

#coalmining.sim <- bugs (data, inits, parameters, "coal.bug", n.chains=3, n.iter=1000, codaPkg=TRUE)
coalmining.sim <- jags (data, inits, parameters, "coal.bug", n.chains=3, n.iter=1000)
   
#coalmining.coda = read.bugs(coalmining.sim)
#summary(coalmining.coda)
#xyplot(coalmining.coda)
#acfplot(coalmining.coda)
#densityplot(coalmining.coda,col="black")

print (coalmining.sim)
