
class QuadraticCongruentialGenerator:

    def __init__(self, seed = 42, a = 1103, b = 12345, c = 23,modulus = 2**13):

        self.seed = seed
        self.modulus = modulus
        self.a = a
        self.b = b
        self.c = c

    def srand(self):

        self.seed = ((self.a * pow(self.seed,2)) + (self.b * self.seed) + self.c) % self.modulus
        return self.seed


if __name__ == "__main__":

    qcg = QuadraticCongruentialGenerator()

    for i in range(10):
        rand = qcg.srand()
        print(rand)
