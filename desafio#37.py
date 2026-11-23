num = int(input('Digite um número inteiro: '))

print('''-=-=-=-= OPÇÕES -=-=-=-=-
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL''')

opção = int(input('Digite uma das opções: '))

if opção == 1:
    print('O número {} convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O número {} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif opção == 3:
        print('O número {} convertido para HEXADECIMAL é {}'.format(num, hex(num)))
else:
     print('O valor é inválido. Tente novamente')


