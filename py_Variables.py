a = 67
print(a,type(a))

b = "Arnab Mitra"
print(b,type(b))

c = 48.187691
print(c,type(c))


d = [65,12,34,90,56,70,100,198,134]
print(d,type(d))
print(d[2])

e = complex(6)
print(e,type(e))

f = complex(10,-8)
print(f,type(f))

complex_re = complex(input("Enter the real part: "))
complex_imag = complex(input("Enter the imaginary part: "))
print(complex(complex_re,complex_imag))

g = (45,98,98,12,54,27,29,67,89,95,100,134,752,154,907,912)
print(g,type(g))

h = {1:"Aakash",2:"Aditya",3:"Akash Mandal",4:"Arkaprava",5:"Arnab",6:"Belal"}
print(h,type(h))
print(h[1])
h = {}
print(h,type(h))

s = set()
print(s,type(s))