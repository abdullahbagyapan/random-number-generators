
class LinearCongruentialGenerator:

    def __init__(self, seed = 42, multiplier = 1103515245, increment = 12345, modulus = 2**31):
        # parameters selected from ISO/IEC 9899:201x

        self.seed = seed
        self.modulus = modulus
        self.increment = increment
        self.multiplier = multiplier

    def srand(self):

        self.seed = ((self.seed * self.multiplier) + self.increment) % self.modulus
        return int(self.seed / 65536)



if __name__ == "__main__":

    lcg = LinearCongruentialGenerator()

    for i in range(10):
        rand = lcg.srand()
        print(rand)
