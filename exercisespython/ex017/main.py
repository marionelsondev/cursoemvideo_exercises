cateto_oposto = float(input('Informe o comprimento do cateto oposto:'))
cateto_adjacente = float(input('Informe o comprimento do cateto adjacente:'))

hipotenusa = (cateto_oposto**2 + cateto_adjacente**2)**(1/2)
print(f'O comprimento da hipotenusa é de: {hipotenusa:.2f}')
