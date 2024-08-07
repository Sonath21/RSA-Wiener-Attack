import sympy
import contfrac


def decrypt(ciphertext, N, d):
    plaintext = [pow(c, d, N) for c in ciphertext]
    message = ''.join(chr(p) for p in plaintext)
    return message

def wiener_attack(e, N):
    cf = contfrac.continued_fraction((e, N))
    cf_list = list(cf)
                                                                            # we use max_grade = len (cf_list)
    convergents = contfrac.convergents((e, N), max_grade=len(cf_list))   # because the default ΜΑΧ length is 10 (according to the documentation of contfrac)
    convergents_list = list(convergents)                                    # which terminates our script prematurely

    for k, d in convergents_list:
        if k == 0:
            continue
        phi = (e * d - 1) // k
        x = sympy.symbols('x')
        roots = sympy.solve(x**2 - (N - phi + 1) * x + N, x)
        if len(roots) == 2 and all(root.is_integer for root in roots):
            return d
    return None


N = 194749497518847283
e = 50736902528669041
ciphertext = [47406263192693509, 51065178201172223, 30260565235128704, 82385963334404268,
              8169156663927929, 47406263192693509, 178275977336696442, 134434295894803806,
              112111571835512307, 119391151761050882, 30260565235128704, 82385963334404268,
              134434295894803806, 47406263192693509, 45815320972560202, 174632229312041248,
              30260565235128704, 47406263192693509, 119391151761050882, 57208077766585306,
              134434295894803806, 47406263192693509, 119391151761050882, 47406263192693509,
              112111571835512307, 52882851026072507, 119391151761050882, 57208077766585306,
              119391151761050882, 112111571835512307, 8169156663927929, 134434295894803806,
              57208077766585306, 47406263192693509, 185582105275050932, 174632229312041248,
              134434295894803806, 82385963334404268, 172565386393443624, 106356501893546401,
              8169156663927929, 47406263192693509, 10361059720610816, 134434295894803806,
              119391151761050882, 172565386393443624, 47406263192693509, 8169156663927929,
              52882851026072507, 119391151761050882, 8169156663927929, 47406263192693509,
              45815320972560202, 174632229312041248, 30260565235128704, 47406263192693509,
              52882851026072507, 119391151761050882, 111523408212481879, 134434295894803806,
              47406263192693509, 112111571835512307, 52882851026072507, 119391151761050882,
              57208077766585306, 119391151761050882, 112111571835512307, 8169156663927929,
              134434295894803806, 57208077766585306]


d = wiener_attack(e, N)
if d is not None:
    print("Found d:", d)
    message = decrypt(ciphertext, N, d)
    print("Decrypted message:", message)
else:
    print("Failed to find d .")
