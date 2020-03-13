#!/usr/bin/env python3
def conv(a):
  
  b = str()
  k = str()
  h = str()

  cociente = 1

  while cociente != 0:
    residuo = a % 2
    cociente = a//2
    a = cociente
    h = str(residuo) + h

  num_bin = h.rjust(8,'0')
  return(num_bin)

if __name__=='__main__':
  n = int(input('Escriba un entero: \n'))
  m = conv(n)
  print('La representacion binaria es: {}'.format(m))
