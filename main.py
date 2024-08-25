x = y = z = 0
print(x, y, z)

# упрощенный вид переменной

a, b, c = 10, 20, 30

print(a, b, c)

a, b, c = [10, 20, 30]

print(a, b, c)

 # list[1] = 10

a, *b = [10, 20, 30, 52, 1488]
# расширенная распаковка 
print(a, b, c)

a, *b, c = 'hello'
print(a)
print(b)
print(c)



