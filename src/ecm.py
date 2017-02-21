import math
import random
from point import Point
import math
from montgomery import ladder

class ECM:

    try:
        with open('../primes/primes.csv','r') as csv:
            primes = list(map(int, csv.read().split(',')))
    except:
        print("primes/primes.csv is not a proper primes file. Generate it with ECM.generate(n), which generates a file with all primes up to n.")

    # inspired by "starblue"'s code at http://stackoverflow.com/questions/1042902/most-elegant-way-to-generate-prime-numbers
    def generate(n):
        sieve = [True for i in range(n+1)]
        for i in range(2,int(math.sqrt(n))):
            if(sieve[i]):
                for j in range(i*i,n+1,i):
                    sieve[j] = False
        g = open('../primes/primes.csv','w')
        ECM.primes = [p for p in range(2,n+1) if sieve[p]]
        g.write(','.join([str(p) for p in ECM.primes]))
        g.close()

    def gcd(a,b):
        if(b > a):
            return ECM.gcd(b,a)
        if(b == 0):
            return a
        return ECM.gcd(b,a%b)

    def trial_division(N):
        smallprimes = ECM.primes[:1229]
        out = []
        for p in smallprimes:
            if(p > N//2):
                break
            if(N%p == 0):
                out.append(p)
        return out

    # see https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Computational_complexity
    def is_probable_prime(m,ntrials):
        if(m == 1):
            return False
        if m in ECM.primes:
        	return True
        if(m%2 == 0):
        	return False
        t = m - 1
        s = 0
        while(t%2 == 0):
        	s += 1
        	t = t>>1
        for counter in range(ntrials):
        	a = random.randint(2,m-2)
        	x = pow(a,t,m)
        	if (x == 1) or (x == (m-1)):
        		continue
        	for k in range(s-1):
        		x = pow(x,2,m)
        		if(x == 1):
        			return False
        		if(x == (m-1)):
        			break
        	else:
        		return False
        return True

    def ECMTrial(N,A,bound):
        Point.set(N,A)
        if(ECM.gcd(A*A-4,N) != 1):
            return ECM.gcd(A*A-4,N)
        Q = ECM.base
        for l in ECM.primes:
            if (l>bound):
                break
            Q = ladder(pow(l,math.floor(math.log(bound,l)),N),Q)
        return ECM.gcd(Q.Z,N)

    base = Point(1,0)

    def factorization(N):
        result = {}
        small = ECM.trial_division(N)
        for p in small:
            e = 0
            while((N%p) == 0):
                e += 1
                N //= p
            result[p] = e
        if(N == 1):
            L = []
        else:
            L = [N]
        digits = math.log(N,10)
        ubound = int(15 * math.exp(digits/3.9) * (150/digits + 1)) # this gives a decent approximation of the values given by Zimmermann and Dodson
        print("upper bound: "+str(ubound))
        while(L):
            N = L.pop()
            if ECM.is_probable_prime(N,40):
                if N in result:
                    result[N] += 1
                else:
                    result[N] = 1
                continue
            print("Trying to break "+str(N)+".")
            count = 0
            bound = 1200
            seen = False
            while(True):
                count += 1
                if(bound < ubound):
                    bound *= 5
                    bound //= 3
                if(bound > ubound):
                    bound = ubound
                print("current bound is "+str(bound)+", ~"+str(100*bound//ubound)+"% of upper bound")
                if(bound >= ubound and count > 100):
                    print("Gave up.")
                    if N in result:
                        result[N] += 1
                    else:
                        result[N] = 1
                    break
                sigma = random.randint(5,N-1)
                u = sigma * sigma - 5 % N
                v = 4 * sigma % N
                ECM.base = Point(pow(u,3,N),pow(v,3,N))
                A = pow(v,3,N) * (3*u+v) * pow(4*v*pow(u,3,N),N-2,N) - 2 % N
                d = ECM.ECMTrial(N,A,bound)
                if(d == 1 or d == N):
                    continue
                N //= d
                L.append(N)
                L.append(d)
                print("It worked!")
                break
        return result
