# Elliptic Curve Cryptography (Second project for [INF568 Advanced Cryptology](https://moodle.polytechnique.fr/course/view.php?id=2655) @ Ecole polytechnique)


## File structure

**src** contains the *.py* source files.  
**out** contains some the results obtained by running the algorithm on some of the provided integers. These are *.out* files.
**prime** contains *primes.csv*, which is used to store some (relatively small) primes. You can change the upper bound on the primes that are stored by using *ECM.generate*. For instance typing ~~~~ ECM.generate(500000000) ~~~~ will generate all primes up to 500000000 using a sieve and store them in *primes/primes.csv*.

## Code structure

**point.py** contains a class that is used to represent points on a elliptic curve. Of note is the set function that specifies the parameters (N and A) of the elliptic curve we are currently working on. It also there that are implemented the functions for adding, doubling and normalizing points, as well as the conditional swap.
**montgomery.py** contains one function which implements the montgomery *ladder*.
**keyexchange.py** implements half of a Diffie Hellman protocol with elliptic curves, as well as several functions that are used to interpret the inputs as specified in [RFC7748](https://tools.ietf.org/html/rfc7748).
**ecm.py** contains the *ECMTrial* and *factorization* functions, which allow us to attempt to factorize integers. *factorization* returns a dictionary mapping (presumably) prime numbers to their power in the factoring of the input.
**test.py** let's us test all of this. It has three functions. The first one tests the *ladder* and the operations on points on the provided test vectors. We obtain the expected result. The second runs *X25519* a million times, printing the first, thousandth and last value of the scalar, as well as the total and average runtime. We obtain the expected results. The last one takes an integer as input, attempts to factorize it using ECM, checks that the product of the output factors match the input, then prints the decomposition along with the time it took to stdout and to a file.

## Usage

**Move to the src directory**
~~~~
cd src
python3
~~~~

**Setting up primes numbers** *if you just downloaded the files you might want to generate more prime numbers than you currently have to speed up the process*
~~~~
from ecm import ECM
ECM.generate(500000000)
~~~~

**Running the tests**
~~~~
import test # might take some time as python needs to load the prime numbers
test.arith()
test.DH()
test.fact(10097201491719693192)
~~~~

## Performances

~~~~
>>> import test
>>> test.DH()
422c8e7a6227d7bca1350b3e2bb7279f7897b87bb6854b783c60e80311ae3079
684cf59ba83309552800ef566f2f4d3c1c3887c49360e3875f2eb94d99532c51
7c3911e0ab2586fd864497297e575e6f3bc601c0883c30df5f4dd2d24f665424
Total time: 11065.116004
Time per X25519: 0.011065116004
~~~~

~~~~
upper bound: 80519
109879989044108565385742461
2000 ~2% of upper bound
3333 ~4% of upper bound
5555 ~6% of upper bound
9258 ~11% of upper bound
15430 ~19% of upper bound
25716 ~31% of upper bound
1039892934551
105664713542411
Factorization of 30393886518332590346305456575643623 in 3.890113 seconds:
105664713542411**1
1039892934551**1
3323**1
3083**1
3**3
~~~~
