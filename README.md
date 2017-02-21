# Elliptic Curve Cryptography (Second project for [INF568 Advanced Cryptology](https://moodle.polytechnique.fr/course/view.php?id=2655) @ Ecole polytechnique)


## File structure

**src** contains the *.py* source files.  
**out** contains some the results obtained by running the algorithm on some of the provided integers. These are *.out* files.
**prime** contains *primes.csv*, which is used to store some (relatively small) primes. You can change the upper bound on the primes that are stored by using *ECM.generate*. For instance typing ~~~~ ECM.generate(500000000) ~~~~ will generate all primes up to 500000000 using a sieve and store them in *primes/primes.csv*.

## Code structure

**point.py** contains a class that is used to represent points on a elliptic curve. Of note is the set function that specifies the parameters (N and A) of the elliptic curve we are currently working on. It also there that are implemented the functions for adding, doubling and normalizing points, as well as the conditional swap.
**montgomery.py** contains one function which implements the montgomery ladder.
**keyexchange.py** implements half of a Diffie Hellman protocol with elliptic curves, as well as several functions that are used to interpret the inputs as specified in [RFC7748](https://tools.ietf.org/html/rfc7748).
**ecm.py** contains the ECMTrial and factorization functions, which allow us 
**test.py** is the second, more reliable implementation, based on sparse matrices.  

## Usage

**Compiling**
~~~~
javac -d bin src/*.java
~~~~

**Running** (for instance on *input/filtration_A.in*)
~~~~
java -cp bin ReadFiltration filtration_A
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
