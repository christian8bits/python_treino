def add_numbers(a, b):
   if not (isinstance(a, int) and isinstance(b, int)):
       return "As entradas devem ser inteiros"
   return a + b
print(add_numbers(10, 20))
print(add_numbers(10, 20.23))
print(add_numbers('5', 6))
print(add_numbers('5', '6'))
