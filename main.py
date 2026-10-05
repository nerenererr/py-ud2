import math
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
par = nume % 2 == 0

print(f'El número {nume} es par: {par}')


# ejercicio 5

numer = 6
num_en_rango = numer in range(0, 11)
print(f'El número {numer} está entre 0 y 10: {num_en_rango}')


# ejercicio 6
numb = float(input("Introduce un número: "))
mult3 = numb % 3 == 0
mult5 = numb % 5 == 0
mult7 = numb % 7 == 0

print(f'El número {numb} es múltiplo de 3: {mult3}, múltiplo de 5: {mult5}, múltiplo de 7: {mult7}')


# ejercicio 7

# cuadrado
lado_c = 4
perim_c = lado_c * 4
area_c = lado_c * lado_c


# triángulo
base_t = 2
altura_t = 7
area_t = base_t * altura_t


#círculo
radio_ci = 44
perim_ci = 2 * 3.14 * radio_ci
area_ci = 3.14 * radio_ci**2


#triángulo rectángulo
cat1 = 11
cat2 = 22
hipotenusa = math.sqrt(cat1**2 + cat2**2)


# ejercicio 8

product = "Silla"
precio = 6
ud = 7
subt = precio * ud
imp = 10
precio_t = subt + (subt * imp / 100)

print(f'Producto: {product}')
print(f'Precio unitario: {precio} euros')
print(f'Uniddades: {ud} uds')
print(f'Subtotal: {subt} euros')
print(f'Impuestos: {imp} %')
print(f'Precio total: {precio_t} euros')


# ejercicio 9

seg_total = 3457
horas = seg_total // 3600
rest_sec = seg_total % 3600

min = rest_sec // 60
seg = rest_sec % 60

print(f"{horas} horas, {min} minutos y {seg} segundos")