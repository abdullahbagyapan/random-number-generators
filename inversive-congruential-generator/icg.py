from sympy import isprime, mod_inverse

class InversiveCongruentialGenerator:

    def __init__(self, seed = 1, multiplier = 16807, increment = 1, modulus = 2**31 - 1):

        if not isprime(modulus):
            raise ValueError("modulus must be prime")

        if (self.multiplier == 0):
            raise ValueError("multiplier must be nonzero modulo p")

        self.seed = seed
        self.multiplier = multiplier
        self.increment = increment
        self.modulus = modulus

    def srand(self):
        
        if (self.seed == 0):
            self.seed = self.increment
        else:
            inv = mod_inverse(self.seed, self.modulus)
            self.seed = ((self.multiplier * inv) + self.increment) % self.modulus

        return self.seed
        


if __name__ == "__main__":

    icg = InversiveCongruentialGenerator()

    for i in range(10):
        rand = icg.srand()
        print(rand)
