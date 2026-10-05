# ejercicio 1

num1 = 11
num2 = 22

suma = num1 + num2
print(f'EL resultado de la suma es, {suma}')
rest = num1 - num2
print(f'EL resultado de la resta es, {rest}')
mult = num1 * num2
print(f'EL resultado de la multiplicación es, {mult}')
div = num1 / num2
print(f'EL resultado de la división es, {div}')

# ejercicio 2

celsius = 23
celsius_a_fah = celsius * 1.8 + 32

print(f'{celsius} Celsius es equivalente a {celsius_a_fah} Fahrenheit')

km = 444
km_a_ft = km * 3281
print(f'{km} Km es equivalente a {km_a_ft} pies')

km_a_mi = km // 1,609
print(f'{km} Km es equivalente a {km_a_mi} millas')

eur = 555
print(f'{eur} euros equivalen a {eur * 0.85} libras y a {eur * 1.12} USD')


# ejercicio 3

nota1 = float(input("Introduce tu nota: "))
nota2 = float(input("Introduce tu nota: "))
nota3 = float(input("Introduce tu nota: "))
nota4 = float(input("Introduce tu nota: "))

media = (nota1 + nota2+ nota3+ nota4) / 4

if media >= 5:
    aprobado = True
else:
    aprobado = False

print(f'La nota media es {media}. El alumno ha aprobado: {aprobado}')


# ejercicio 4

nume = float(input("Introduce un número: "))
par_o_no = nume % 2