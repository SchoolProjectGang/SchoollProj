import random


class password_maker():
    def __init__(self, n) -> None:
        self.alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.symbols = ['@', '$', '*', '(', ')', '!', '&', '#', '^']
        self.n = n-1

    def generator(self):
        k = ""
        for i in range(0, self.n):
            x = random.randint(0, 8)
            y = random.randint(0, 8)
            z = random.randint(0, 8)
            j = str(self.alphabets[x] +
                    str(self.numbers[z]) + str(self.symbols[y]))
            k = k + str(j)
        return k
        


j = password_maker(6)
print(j.generator())
