'''
19. Escreva um programa em Python para obter uma nova string 
de uma determinada string onde "Is" foi adicionado à frente. 
Se a string fornecida já começar com "Is", retorne a string inalterada.
'''
def new_string(str):
  if len(str) >= 2 and str[:2] == "Is":
    return str
  return "Is" + str

print(new_string("Array"))
print(new_string("IsEmpty"))
