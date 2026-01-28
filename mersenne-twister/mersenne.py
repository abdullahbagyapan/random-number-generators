

class MT19937:

    w, n, m, r = 32, 624, 397, 31
    a = 0x9908B0DF

    u, d = 11, 0xFFFFFFFF
    s, b = 7, 0x9D2C5680
    t, c = 15, 0xEFC60000
    l = 18

    f = 1812433253

    lower_mask = (1 << r) - 1
    upper_mask = (~lower_mask) & 0xFFFFFFFF

    def __init__(self, seed: int):
        self.mt = [0] * self.n
        self.index = self.n
        self.seed_mt(seed)

    def seed_mt(self, seed: int):
        self.mt[0] = seed & 0xFFFFFFFF
        for i in range(1, self.n):
            self.mt[i] = (
                self.f * (self.mt[i - 1] ^ (self.mt[i - 1] >> (self.w - 2))) + i
            ) & 0xFFFFFFFF

    def extract_number(self) -> int:
        if self.index >= self.n:
            self.twist()

        y = self.mt[self.index]

        # Tempering
        y ^= (y >> self.u) & self.d
        y ^= (y << self.s) & self.b
        y ^= (y << self.t) & self.c
        y ^= y >> self.l

        self.index += 1
        return y & 0xFFFFFFFF

    def twist(self):
        for i in range(self.n):
            x = (self.mt[i] & self.upper_mask) + (
                self.mt[(i + 1) % self.n] & self.lower_mask
            )
            xA = x >> 1
            if x & 1:
                xA ^= self.a

            self.mt[i] = self.mt[(i + self.m) % self.n] ^ xA

        self.index = 0


if __name__ == "__main__":
    rng = MT19937(seed=5489)  # reference seed
    for _ in range(10):
        print(rng.extract_number())


