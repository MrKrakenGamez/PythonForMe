#una variable permite almacenar informacion de forma temporal
#una variable puede almacenar informacion de tipo cadena(string),numerico(integer), Bolenana(Boolean), etc.
print('variable')

Myname='Miguel' #Myname, es la variable, en este caso almacena un string

print(Myname)

MyAge=23 #MyAge, es la variable, en este caso almacena un int

print(MyAge)

#el valor de la variable puede cambiar, dependiendo del momento en que se ejecute
Myname = 'Angel'
print('aqui se realizo el cambio en la variable',Myname)
print(f'aqui se realizo el cambio en la variable{Myname}') #ante poniendo una f, a lo que se vaya a imprimir, permite concatenar en una funcion

MyNames = input('¿cual es tu nombre?') #input recoje el valor desde lo que se escribe en la terminal
print(f"usando input, ahora el valor almacenado es : {MyNames}")

MyAges = input('¿cual es tu edad?')
print(MyAges)