def bin(num):
    binario = ''
    while num // 2 != 0:
        binario = str(num % 2) + binario
        num = num // 2
    return str(num) + binario
    num=25
bin(num)
eso=bin(num)
print(eso)
print('En 8 bits:',eso.rjust(8, "0"))
   
