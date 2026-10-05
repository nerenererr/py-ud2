# Ejercicios de programación

## 1. Operaciones básicas

Hacer un programa que haga la suma, resta, multiplicación y división entre dos números. Para cada operación, mostrar por consola un mensaje que diga:

`El resultado de la <operación> es <resultado>`

---

## 2. Conversión de unidades

Hacer un programa que calcule el cambio de una unidad a otra, por ejemplo:

1. De grados Celsius (ºC) a grados Fahrenheit (ºF)
2. De kilómetros (km) a pies (ft), millas (mi), etc.
3. De euros (EUR) a libras esterlinas (GBP), dólares estadounidenses (USD), etc.

Mostrar por consola un mensaje que diga:

`<X> <unidad> es equivalente a <Y> <unidad>`

---

## 3. Media de cuatro notas

Hacer un programa que calcule la media entre 4 notas cualesquiera, y calcule si el alumno ha aprobado o no (si la nota media es mayor o igual a 5).

Mostrar por consola un mensaje que diga:

`La nota media es <X>. El alumno ha aprobado: <True/False>`

---

## 4. Número par

Hacer un programa que muestre si un número es par.

Recuerda que un número es par si al dividirlo por 2 el resto es 0.

Mostrar por consola un mensaje que diga:

`El número <X> es par: <True/False>`

---

## 5. Número dentro de un rango

Hacer un programa que muestre si un número está dentro de un rango de valores, por ejemplo, entre 0 y 10.

Mostrar por consola un mensaje que diga:

`El número <X> está entre <A> y <B>: <True/False>`

---

## 6. Múltiplos de 3, 5 y/o 7

Hacer un programa que determine si un número es múltiplo de 3, 5 y/o 7.

Recuerda que un número A es múltiplo de B si al dividir A entre B el resto es 0.

Mostrar por consola varios mensajes que digan:

`El número <A> es múltiplo de <B>: <True/False>`

---

## 7. Cálculos geométricos

Hacer un programa que haga varios cálculos geométricos, por ejemplo:

### 7.1. Cuadrado

Dado el lado de un cuadrado, calcular su perímetro y área.

### 7.2. Triángulo

Dada la base y la altura de un triángulo, calcular su área.

### 7.3. Círculo

Dado el radio de un círculo, calcular su perímetro y área.

### 7.4. Triángulo rectángulo

Dados los catetos de un triángulo rectángulo, calcular la hipotenusa.

> **Consejo:** la raíz cuadrada se calcula con `math.sqrt(<X>)`. Se debe importar la librería `math`.

---

## 8. Factura de un producto

Hacer un programa que imprima por consola la factura de un producto concreto.

El producto tendrá **un nombre, un precio unitario, un número de unidades y un impuesto**.

El programa debe calcular el subtotal y el precio total.

El resultado debería ser similar al siguiente:

```text
Producto: <Nombre producto>
Precio unitario: <Precio unitario> euros
Unidades: <Unidades> uds.
Subtotal: <Precio total sin impuestos> euros
Impuestos: <Impuestos>%
Precio total: <Precio total con impuestos> euros