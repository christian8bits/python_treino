kpa = float(input("Pressão de entrada em kilopascais> "))
psi = kpa / 6,89475729
mmhg = kpa * 760 / 101,325
atm = kpa / 101,325
print("A pressão em libras por polegada quadrada: %.2f psi" % (psi))
print("A pressão em milímetros de mercúrio: %.2f mmHg" % (mmhg))
print("Pressão atmosférica: %.2f atm." % (atm))
