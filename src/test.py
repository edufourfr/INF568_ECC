from point import Point
from montgomery import ladder
import keyexchange
from ecm import ECM
import datetime

def arith():
    Point.set(101,49)
    P = Point(2,1)
    print("First curve.")
    Q = ladder(2,P)
    Q.normalize()
    print("[2]P = ("+str(Q.X)+":*:1)")
    Q = ladder(3,P)
    Q.normalize()
    print("[3]P = ("+str(Q.X)+":*:1)")
    Q = ladder(77,P)
    Q.normalize()
    print("[77]P = ("+str(Q.X)+":*:1)")

    Point.set(1009,682)
    P = Point(7,1)
    print("Second curve.")
    Q = ladder(2,P)
    Q.normalize()
    print("[2]P = ("+str(Q.X)+":*:1)")
    Q = ladder(3,P)
    Q.normalize()
    print("[3]P = ("+str(Q.X)+":*:1)")
    Q = ladder(5,P)
    Q.normalize()
    print("[5]P = ("+str(Q.X)+":*:1)")
    Q = ladder(34,P)
    Q.normalize()
    print("[34]P = ("+str(Q.X)+":*:1)")
    Q = ladder(104,P)
    Q.normalize()
    print("[104]P = ("+str(Q.X)+":*:1)")
    Q = ladder(947,P)
    Q.normalize()
    print("[947]P = ("+str(Q.X)+":*:1)")

def DH():
    Point.set((1<<255) - 19, 486662)
    k = "0900000000000000000000000000000000000000000000000000000000000000"
    u = "0900000000000000000000000000000000000000000000000000000000000000"
    start = datetime.datetime.now()
    for count in range(1,1000001):
        old = k
        k = keyexchange.X25519(k,u)
        u = old
        if(count==1 or count==1000 or count == 1000000):
            print(k)
    end = datetime.datetime.now()
    print("Total time: "+str((end-start).total_seconds()))
    print("Time per X25519: "+str((end-start).total_seconds()/1000000))

def fact(N):
    start = datetime.datetime.now()
    result = ECM.factorization(N)
    end = datetime.datetime.now()
    out = []
    for key in result:
        out.append((key,result[key]))
    out.sort(key=lambda pair: -pair[0])
    prod = 1
    for t in out:
        prod *= t[0]**t[1]
    if prod!=N:
        print("Error, input and output don't match.")
    s = "Factorization of "+str(prod)+" in "+str((end-start).total_seconds())+" seconds:\n"
    for t in out:
        s += str(t[0])+"**"+str(t[1])+"\n"
    g = open("../out/"+str(N)+".out",'w')
    g.write(s)
    print(s)
    g.close()
