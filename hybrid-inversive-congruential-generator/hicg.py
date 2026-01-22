from sympy import mod_inverse

class HybridInversiveCongruentialGenerator:

    # <https://faculty.nps.edu/pstanica/research/2021EJPAM_HICG.pdf>
    def __init__(self, w = 64, a = 1886906, b = 706715, c = 807782, y0 = 430227, y1 = 1725239):
        
        # ensure both states lie under odd residues
        if (y1 % 2 == 0) or (y0 % 2 == 0):
            raise ValueError("State not invertible modulo 2^w")

        self.n = pow(2,w)   # modulus
        
        self.a = a          # multiplier
        self.b = b          # multiplier
        
        self.c = c          # constant

        self.y0 = y0        # second-order
        self.y1 = y1        # first-order

    def srand(self):

        w = ((self.a * mod_inverse(self.y1, self.n)) + (self.b * self.y0) + self.c) % self.n
        
        self.y0 = self.y1
        self.y1 = w | 1

        return self.y1
        

if __name__ == "__main__":

    hicg = HybridInversiveCongruentialGenerator()

    for i in range(100):
        rand = hicg.srand()
        print(rand)
