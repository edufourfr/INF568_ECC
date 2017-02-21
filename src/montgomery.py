from point import Point


def ladder(m,P):
    R0,R1 = Point(1,0),P
    d = bin(m)
    for m in d[2:]:
        two0 = Point.xDBL(R0)
        two1 = Point.xDBL(R1)
        addition = Point.xADD(R0,R1,P)
        R0,R1 = (Point.swap(addition,two0,int(m)),Point.swap(two1,addition,int(m)))
    return R0
