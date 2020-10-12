# Detecta numeros primos no intervalo

num = input("\nDigite um numero maior ou igual a 2: ")
cont = 0

for x in range(2, num+1):
  flag = 0
  for y in range(2, x/2):
      if x%y==0:
          flag = 1
  if flag == 0:
      print('O numero ' + str(x) + ' eh primo')
      cont = cont + 1
print('\n\nO interalo de 2 ate '+str(num)+' possui '+str(cont)+' numeros primos\n\n')
