class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return str(complex(self.real, self.imag))

    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.imag * other.real + self.real * other.imag)


a = Complex(3, 1)
b = Complex(2, -3)
print(a + b)
print(a * b)
