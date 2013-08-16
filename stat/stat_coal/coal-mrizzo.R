library(boot)     #for coal data
year <- floor(coal)
data(coal)
y <- table(year)
plot(y)  #a time plot

y <- floor(coal[[1]])
y <- tabulate(y)
y <- y[1851:length(y)]

# Gibbs sampler for the coal mining change point

# initialization
n <- length(y)    #length of the data
m <- 1000         #length of the chain
mu <- lambda <- k <- numeric(m)
L <- numeric(n)
k[1] <- sample(1:n, 1)
mu[1] <- 1
lambda[1] <- 1
b1 <- 1
b2 <- 1

# run the Gibbs sampler
for (i in 2:m) {
    kt <- k[i-1]

    #generate mu
    r <- .5 + sum(y[1:kt])
    mu[i] <- rgamma(1, shape = r, rate = kt + b1)

    #generate lambda
    if (kt + 1 > n) r <- .5 + sum(y) else
        r <- .5 + sum(y[(kt+1):n])
    lambda[i] <- rgamma(1, shape = r, rate = n - kt + b2)

    #generate b1 and b2
    b1 <- rgamma(1, shape = .5, rate = mu[i]+1)
    b2 <- rgamma(1, shape = .5, rate = lambda[i]+1)

    for (j in 1:n) {
        L[j] <- exp((lambda[i] - mu[i]) * j) *
                      (mu[i] / lambda[i])^sum(y[1:j])
        }
    L <- L / sum(L)

    #generate k from discrete distribution L on 1:n
    k[i] <- sample(1:n, prob=L, size=1)
}

b <- 201
j <- k[b:m]
print(mean(k[b:m]))
print(mean(lambda[b:m]))
print(mean(mu[b:m]))
