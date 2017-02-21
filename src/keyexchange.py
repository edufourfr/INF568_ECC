from point import Point
from montgomery import ladder

Point.set((1<<255) - 19, 486662)
base = Point(9, 14781619447589544791020593568409986887264606134616475288964881837755586237401)

# from RFC 7748 (begin)

def decodeLittleEndian(b):
    return sum([b[i] << 8*i for i in range(32)])

def decodeUCoordinate(u):
    u_list = [ord(b) for b in u]
    u_list[-1] &= (1<<7)-1
    return decodeLittleEndian(u_list)

def encodeUCoordinate(u):
    u = u % Point.N
    return ''.join([chr((u >> 8*i) & 0xff) for i in range(32)])

def decodeScalar25519(k):
    k_list = [ord(b) for b in k]
    k_list[0] &= 248
    k_list[31] &= 127
    k_list[31] |= 64
    return decodeLittleEndian(k_list)

# from RFC 7748 (end)

def hexToString(h):
    return ''.join([chr(int(h[2*i:(2*i+2)],16)) for i in range(32)])

def stringToHex(s):
    return ''.join(["{0:0{1}x}".format(ord(s[i]),2) for i in range(32)])

def X25519(m,x):
    out = ladder(decodeScalar25519(hexToString(m)),Point(decodeUCoordinate(hexToString(x)),1))
    out.normalize()
    return stringToHex(encodeUCoordinate(out.X))
