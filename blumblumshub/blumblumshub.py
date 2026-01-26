from sympy import isprime, gcd


class BlumBlumShub:

    def __init__(self, seed, p, q):

        assert p % 4 == 3
        assert q % 4 == 3
        assert isprime(p) == 1
        assert isprime(q) == 1
        assert gcd(seed, p*q) == 1

        self.seed = seed
        self.modulus = p*q

    def srand(self):
        
        self.seed = (self.seed**2) % self.modulus

        return self.seed
        

if __name__ == "__main__":

    bbs = BlumBlumShub(seed=131, p=499, q=547)

    for i in range(10):
        rand = bbs.srand()
        print(rand)
