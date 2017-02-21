class Point:
    A = 2
    Aprime = 1
    N = 2

    def __init__(self, X, Z):
        self.X = X % Point.N
        self.Z = Z % Point.N


    def __str__(self):
        return "Point in the curve A = "+str(Point.A)+" with modulus "+str(Point.N)+": X = "+str(self.X)+" and Z = "+str(self.Z)

    def set(N,A):
        Point.N = N
        Point.A = A
        Point.Aprime = (A+2)*pow(4,Point.N-2,Point.N) % Point.N

    def xADD(P,Q,diff):
        bloc1 = (P.X-P.Z)*(Q.X+Q.Z)
        bloc2 = (P.X+P.Z)*(Q.X-Q.Z)
        step1 = bloc1 + bloc2
        step2 = bloc1 - bloc2
        return Point(diff.Z*step1*step1 % Point.N,diff.X*step2*step2 % Point.N)

    def xDBL(P):
        bloc1 = P.X + P.Z
        bloc1 *= bloc1
        bloc2 = P.X - P.Z
        bloc2 *= bloc2
        return Point(bloc1*bloc2 % Point.N,(bloc1-bloc2)*(bloc2+Point.Aprime*(bloc1-bloc2)) % Point.N)

    def normalize(self):
        if(self.Z != 0):
            self.X *= pow(self.Z,Point.N-2,Point.N)
            self.X %= Point.N
            self.Z = 1

    def swap(P,Q,m):
        l = max(len(bin(P.X)),len(bin(P.Z)),len(bin(Q.X)),len(bin(Q.Z))) - 2
        d = (m<<(l+2)) - m
        notd = ~d
        px = P.X & d
        pz = P.Z & d
        qx = Q.X & notd
        qz = Q.Z & notd
        return Point(px+qx,pz+qz)
