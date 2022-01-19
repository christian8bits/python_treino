#leia um valor em metros e converta em centimetros e milimetros
metros = float(input('Digite a quantidade de metros: '))
cm = int(metros * 100)
mm = int(metros * 1000)
print(f'{metros} metros equivale a {cm} centimetros e {mm} milimetros ')
